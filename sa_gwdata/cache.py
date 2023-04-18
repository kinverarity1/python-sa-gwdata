from pathlib import Path
import requests
import json
import io
import tempfile

from platformdirs import user_data_dir

from datetime import datetime
import pandas as pd
import shapefile

SPATIAL_DATA_DRILLHOLES_URL = "https://www.waterconnect.sa.gov.au/Content/Downloads/DEW/WATER_Drillholes_geojson.zip"

LOCAL = Path(user_data_dir("sa_gwdata", "sa_gwdata")).mkdir(parents=True, exist_ok=True)


def download_spatial_data_drillholes():
    response = requests.get(SPATIAL_DATA_DRILLHOLES_URL)
    temp_fn = LOCAL / "drillholes_shapefiles.zip"
    with open(temp_fn, "wb") as f:
        f.write(response.content)

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

    sf = shapefile.Reader(temp_fn + "/WATER_Drillholes_GDA2020.shp")

    columns = [f[0] for f in sf.fields[1:]]
    records = sf.records()
    df = pd.DataFrame(records, columns=columns)
    for column in categorical_columns:
        df[column] = df[column].astype("category")
    timestamp = datetime.now().strftime("%Y-%m-%d")
    fn = LOCAL / f"drillholes_{timestamp}.feather"
    df.to_feather(fn)
    return fn
