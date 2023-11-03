from pathlib import Path
import requests
import json
import io
import os
import tempfile
import logging

from platformdirs import user_data_dir

from datetime import datetime
import pandas as pd
import shapefile

logger = logging.getLogger(__name__)

DH_LAYER_URL = (
    "https://www.waterconnect.sa.gov.au/Content/Downloads/DEW/WATER_Drillholes_shp.zip"
)

LOCAL = Path(user_data_dir("sa_gwdata", "sa_gwdata"))
LOCAL.mkdir(parents=True, exist_ok=True)

TEMP_DH_LAYER_FN = LOCAL / "drillholes_shapefiles.zip"

LOCAL_DH_CACHE_MISSING = "Local drillhole cache missing. We strongly recommend you run sa_gwdata.cache.update() once to populate. It will download ~80 MB and take about 10 seconds to complete. Total storage required ~125 MB."


class LocalCache:
    def __init__(self):
        self._dh_layer = None
        self._dh_cache_missing = False
        self._check_dh_layer()

    def _check_dh_layer(self):
        self.dh_layer_path
        if not self._dh_cache_missing:
            age = self._dh_layer_age()
            if age.days > 7:
                logger.info(
                    f"The local drillhole cache is {age.days} days old. You may wish to run sa_gwdata.cache.update() to download a new version."
                )

    @property
    def dh_layer_path(self):
        files = sorted([p for p in LOCAL.glob("drillholes_*.feather")])
        if len(files) == 0:
            logger.warning(LOCAL_DH_CACHE_MISSING)
            self._dh_cache_missing = True
        else:
            most_recent_file = files[-1]
            return most_recent_file

    @dh_layer_path.setter
    def dh_layer_path(self, value):
        raise NotImplementedError("Cannot set dh layer path manually")

    @property
    def dh_layer(self):
        if self._dh_cache_missing:
            logger.error(LOCAL_DH_CACHE_MISSING)
            return None
        if self._dh_layer is None:
            self._reload_dh_layer()
        return self._dh_layer

    @dh_layer.setter
    def dh_layer(self, value):
        raise NotImplementedError("Cannot set dh layer manually")

    def _reload_dh_layer(self):
        self._dh_layer = pd.read_feather(self.dh_layer_path)
        self._dh_cache_missing = False

    def _dh_layer_age(self):
        latest_fn = self.dh_layer_path
        date = pd.Timestamp(latest_fn.stem.split("_")[1])
        delta = datetime.now() - date
        return delta

    def update(self, ndays=30, force=False):
        """Update the local cache if necessary.

        Args:
            ndays (int):

        """
        self.update_dh_cache(ndays=ndays, force=force)

    def update_dh_cache(self, ndays=7, force=False):
        update = False
        remove_file = False
        if self._dh_cache_missing:
            logger.debug("Updating as local cache is missing.")
            update = True
        if not force and not self._dh_cache_missing:
            delta = self._dh_layer_age()
            if delta.days > ndays:
                logger.debug(
                    f"Updating cache as it is {delta.days} days out of date (> {ndays})"
                )
                update = True
                remove_file = self.dh_layer_path
            else:
                logger.debug(
                    f"Not updating cache as it is {delta.days} days out of date (<= {ndays})"
                )
        if not update and force:
            logger.debug("Force-updating")
            update = True
        if update:
            download_dh_layer()
            process_dh_layer_download()
            self._reload_dh_layer()
            if remove_file:
                os.remove(remove_file)
            logger.debug("Updated cache.")


def download_dh_layer(temp_fn=TEMP_DH_LAYER_FN):
    temp_fn = TEMP_DH_LAYER_FN

    logger.info(f"Downloading {DH_LAYER_URL} (~80MB) temporarily to {temp_fn}")
    response = requests.get(DH_LAYER_URL)

    logger.debug("Download finished")
    with open(temp_fn, "wb") as f:
        f.write(response.content)


def process_dh_layer_download(temp_fn=TEMP_DH_LAYER_FN):
    logger.info("Processing ~350K rows drillhole records for local cache...")
    categorical_columns = [
        "PARCEL",
        "STATE",
        "STATUS",
        "STAT_DESC",
        "PURPOSE",
        "PURP_DESC",
        "PURPOSE2",
        "PURP2_DESC",
        "PURPOSE3",
        "PURP3_DESC",
        "ANALFULL",
        "LOGGEOPHYS",
        "LOGDRILL",
        "LOGGEOL",
        "LOGSTRAT",
        "LOGHYDROST",
        "LOGGER_DAT",
        "TELEMETRY_",
        "OBSHUND",
        "CLASS",
        "WW_CLASS",
        "PRIVATE",
        "AQ_MON",
        "PHOTO",
        "OWNER_CODE",
        "STATE_ASSE",
        "AQ_MONDESC",
        "SUBURB",
        "LGA",
        "HUNDRED",
        "LANDSCAPES",
        "NRM_REGION",
        "PRESCRIBED",
        "PRESC_WATE",
        "TITLE_PREF",
    ]

    sf = shapefile.Reader(str(temp_fn) + "/WATER_Drillholes_GDA2020.shp")

    columns = [f[0] for f in sf.fields[1:]]
    records = sf.records()
    df = pd.DataFrame(records, columns=columns)
    for column in categorical_columns:
        df[column] = df[column].astype("category")

    null_9999_cols = [
        "REF_ELEV",
        "GRND_ELEV",
        "GRND_ELEV_",
        "CASE_TO",
        "MIN_DIAM",
        "RSWL",
        "EC",
        "SWL",
        "DTW",
        "WATER_CUT",
        "YIELD",
        "TDS",
        "PH",
        "LAT_DEPTH",
        "ORIG_DEPTH",
        "MAX_DEPTH",
    ]
    for col in null_9999_cols:
        df.loc[df[col] == -9999, col] = pd.NA

    date_columns = [
        "TDSDATE",
        "YIELD_DATE",
        "SWLDATE",
        "DRILL_DATE",
    ]
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], format="%Y-%m-%d")

    df.loc[df.PERMIT_NO == 0, "PERMIT_NO"] = pd.NA

    col_remapper = {
        "LOGHYDROST": "LOGHYDROSTRAT",
        "LOGGER_DAT": "LOGGER_DATA",
        "TELEMETRY_": "TELEMETRY_DATA",
        "STATE_ASSE": "STATE_ASSET",
        "SW_CATCHME": "SW_CATCHMENT",
        "LANDSCAPES": "LANDSCAPESA_CODE",
        "NRM_REGION": "NRM_REGION_CODE",
        "PRESCRIBED": "PRESCRIBED_WELL_AREA",
        "PRESC_WATE": "PRESC_WATER_RES_AREA",
        "TITLE_PREF": "TITLE_PREFIX",
        "TITLE_VOLU": "TITLE_VOLUME",
        "TITLE_FOLI": "TITLE_FOLIO",
        "GRND_ELEV_": "GRND_ELEV_DEM",
        "LATEST_REF": "LATEST_REF_POINT_TYP",
        "LATEST_REF_POINT_TYP": "LATEST_REF_POINT_TYPE",
    }

    df = df.rename(columns=col_remapper)

    timestamp = datetime.now().strftime("%Y-%m-%d")
    fn = LOCAL / f"drillholes_{timestamp}.feather"

    logger.debug(f"Writing data to {fn}")
    df.to_feather(fn)
    return fn
