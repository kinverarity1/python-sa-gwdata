import io
import json
import logging
import time
import zipfile

import pandas as pd
import requests

from sa_gwdata.identifiers import *


logger = logging.getLogger(__name__)


class Response(object):
    def __init__(self, response, working_crs="EPSG:4326", **kwargs):
        """Groundwater Data HTTP response.

        Args:
            response (requests.Response object): the HTTP response

        """
        self.response = response
        self.working_crs = working_crs
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def r(self):
        """Return the HTTP requests.Response object."""
        return self.response

    @property
    def json(self):
        """Convert the response to JSON. Returns a dict/list."""
        if not hasattr(self, "_json"):
            self._json = json.loads(self.response.text)
        return self._json

    @property
    def df(self):
        """If the response is a list, convert to a pandas DataFrame with
        columns converted into lowercase."""
        if not hasattr(self, "_df"):
            if len(self.json) > 0:
                if "DHNO" in self.json[0]:
                    if isinstance(self.json[0]["DHNO"], list):
                        # e.g. GetSuburbFromName
                        convert_object = self.json[0]["DHNO"]
                    else:
                        convert_object = self.json
                else:
                    # e.g. GetPWASearchData
                    convert_object = self.json

                df = pd.DataFrame(convert_object).rename(columns=str.lower)
                self._df = df
                logger.debug(f"Response has length={len(df)}")
            else:
                logger.debug("Response is empty")
        return self._df

    @property
    def df_exists(self):
        """Check if JSON can be converted to a DataFrame. Returns bool."""
        if isinstance(self.json, list):
            if len(self.json) > 0:
                return True
        return False

    def gdf(self, x_col="lon", y_col="lat"):
        from shapely.geometry import Point
        import geopandas as gpd

        df = self.df
        return gpd.GeoDataFrame(
            df, geometry=gpd.points_from_xy(df[x_col], df[y_col]), crs="EPSG:4326"
        ).to_crs(self.working_crs)


def get_global_session(working_crs="EPSG:4326", force_new=False):
    if not "__waterconnect_session" in globals():
        global __waterconnect_session
        __waterconnect_session = WaterConnectSession()
    else:
        if force_new:
            del globals()["__waterconnect_session"]
            __waterconnect_session = WaterConnectSession()
    return __waterconnect_session


class WaterConnectSession:
    """Wrapper around repeated requests to Groundwater Data.

    Args:
        endpoint (str): url endpoint for API, optional
        sleep (int): minimum interval between requests in seconds.
            Be nice, do not reduce it.
        verify (bool): require valid SSL certificate

    Other args and kwargs are passed to request.Session constructor.

    Usage:

        >>> from sa_gwdata import WaterConnectSession
        >>> s = WaterConnectSession()
        >>> df = s.get("GetObswellNetworkData", params={"Network": "CENT_ADEL"})

    """

    well_id_cols = {
        "dhno": "drillhole_no",
        "obsnumber": "obs_no",
        "mapnum": "unit_long",
    }

    def __init__(
        self,
        *args,
        endpoint=None,
        sleep=2,
        verify=True,
        load_list_data=True,
        working_crs="EPSG:4326",
        **kwargs
    ):
        self.well_cache = pd.DataFrame(columns=list(set(self.well_id_cols.values())))
        self.working_crs = working_crs
        self.verify = verify
        if not endpoint:
            endpoint = "https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/{app}.ashx/"
        self.endpoint = endpoint
        self.last_request = time.time() - sleep
        self.sleep = sleep
        if load_list_data:
            self.refresh_available_groupings()

    def get(self, path, app="WDDDMS", verify=None, **kwargs):
        """HTTP GET verb to Groundwater Data.

        Args:
            path (str): final portion of URL path off the end of self.endpoint
                e.g. to GET
                ``https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd
                /WDDDMS.ashx/GetAdvancedListsData``
                then you would use ``path="GetAdvancedListsData"``.

        """
        if verify is None:
            verify = self.verify
        t_remain = self.sleep - (time.time() - self.last_request)
        if t_remain > 0:
            logger.debug("Waiting {} sec".format(t_remain))
            time.sleep(t_remain)
        if not path.startswith(self.endpoint):
            path = self.endpoint + path
        path = path.format(app=app)
        logger.debug("GET {} verify={}".format(path, verify))
        response = requests.get(path, verify=verify, **kwargs)
        self.last_request = time.time()
        endpoint, name = path.rsplit("/", 1)
        logger.debug("Response content = {}".format(response.content))
        return self._cache_data(
            Response(
                response, working_crs=self.working_crs, endpoint=endpoint, name=name
            )
        )

    def post(self, path, app="WDDDMS", verify=None, **kwargs):
        if verify is None:
            verify = self.verify
        t_remain = self.sleep - (time.time() - self.last_request)
        if t_remain > 0:
            logger.debug("Waiting {} sec".format(t_remain))
            time.sleep(t_remain)
        if not path.startswith(self.endpoint):
            path = self.endpoint + path
        path = path.format(app=app)
        logger.debug("POST {} verify={}".format(path, verify))
        response = requests.post(path, verify=verify, **kwargs)
        self.last_request = time.time()
        endpoint, name = path.rsplit("/", 1)
        return Response(
            response, working_crs=self.working_crs, endpoint=endpoint, name=name
        )

    def bulk_download_wells(self, service, wells, **kwargs):
        return bulk_download(service, {"DHNOs": wells.dh_no}, **kwargs)

    def bulk_download(self, service, json_data, format="CSV"):
        r = self.post(
            "{service}?bulkOutput={format}".format(service=service, format=format),
            data={"exportdata": json.dumps(json_data)},
        )
        with io.BytesIO(r.response.content) as buffer:
            df = pd.read_csv(buffer)
        return df

    def bulk_wells_summary(self, wells, **kwargs):
        dh_nos = [w for w in wells]
        if len(wells):
            if hasattr(wells[0], "dh_no"):
                dh_nos = [w.dh_no for w in wells]
        df = self.bulk_download("GetSummaryDownload", {"DHNOs": dh_nos})
        for date_col in (
            "Orig_drilled_date",
            "max_drill_date",
            "late_open_date",
            "latest_status_date",
            "water_level_date",
            "salinity_date",
            "pH_date",
            "yield_date",
        ):
            df[date_col] = pd.to_datetime(df[date_col], format="%d/%m/%Y")
        df = df.rename(
            columns={
                "DHNO": "dh_no",
                "Unit_Number": "unit_long",
                "Aquifer": "aquifer",
                "mga_easting": "easting",
                "mga_northing": "northing",
                "mga_zone": "zone",
                "Unit_No": "unit_hyphen",
                "Obs_No": "obs_no",
                "Orig_drilled_depth": "orig_drilled_depth",
                "Orig_drilled_date": "orig_drilled_date",
                "max_drill_depth": "max_drilled_depth",
                "max_drill_date": "max_drilled_date",
                "late_open_depth": "latest_open_depth",
                "late_open_date": "latest_open_date",
                "late_permit_no": "latest_permit_no",
                "case_min_diam": "casing_min_diam",
                "dtw": "latest_dtw",
                "swl": "latest_swl",
                "rswl": "latest_rswl",
                "water_level_date": "latest_wl_date",
                "TDS": "latest_tds",
                "EC": "latest_ec",
                "salinity_date": "latest_sal_date",
                "pH": "latest_ph",
                "pH_date": "latest_ph_date",
                "yield": "latest_yield",
                "yield_date": "latest_yield_date",
                "long_degrees": "lon_deg",
                "long_minutes": "lon_min",
                "long_seconds": "lon_sec",
                "lat_degrees": "lat_deg",
                "lat_minutes": "lat_min",
                "lat_seconds": "lat_sec",
                "decimal_long": "longitude",
                "neg_decimal_lat": "latitude",
                "decimal_lat": "latitude_positive",
                "Title": "cert_title",
                "water_info": "water_info_exists",
                "salinity": "salinity_exists",
                "water_chemistry": "water_chem_exists",
                "geophys_log": "geophys_log_exists",
                "drill_log": "drillers_log_exists",
                "lith_log": "lith_log_exists",
            },
            errors="ignore",
        )
        return df

    def bulk_water_levels(self, wells, pumping=True, anomalous=True, **kwargs):
        dh_nos = [w for w in wells]
        if len(wells):
            if hasattr(wells[0], "dh_no"):
                dh_nos = [w.dh_no for w in wells]
        df = self.bulk_download("GetWaterLevelDownload", {"DHNOs": dh_nos, "Pumping": pumping, "Anomalous": anomalous})
        df["obs_date"] = pd.to_datetime(df.obs_date, format="%d/%m/%Y")
        df = df.rename(
            columns={
                "DHNO": "dh_no",
                "Unit_Number": "unit_long",
                "Aquifer": "aquifer",
                "Easting": "easting",
                "Northing": "northing",
                "Zone": "zone",
                "Unit_No": "unit_hyphen",
                "Obs_No": "obs_no",
                "anom_ind": "anomalous_ind",
                "Comments": "comments",
            },
            errors="ignore",
        )
        return df

    def bulk_salinities(self, wells, **kwargs):
        dh_nos = [w for w in wells]
        if len(wells):
            if hasattr(wells[0], "dh_no"):
                dh_nos = [w.dh_no for w in wells]
        df = self.bulk_download("GetSalinityDownload", {"DHNOs": dh_nos})
        df["Collected_date"] = pd.to_datetime(df["Collected_date"], format="%d/%m/%Y")
        df = df.rename(
            columns={
                "DHNO": "dh_no",
                "Unit_Number": "unit_long",
                "Aquifer": "aquifer",
                "Easting": "easting",
                "Northing": "northing",
                "Zone": "zone",
                "Unit_No": "unit_hyphen",
                "Obs_No": "obs_no",
                "Collected_date": "collected_date",
                "Collected_time": "collected_time",
                "Anomalous_ind": "anomalous_ind",
                "TDS": "tds",
                "EC": "ec",
                "pH": "ph",
                "Test_Place": "test_place",
                "Measured_during": "measured_during",
                "Sample_type": "sample_type",
            },
            errors="ignore",
        )
        return df

    def bulk_water_chem(self, wells, **kwargs):
        dh_nos = [w for w in wells]
        if len(wells):
            if hasattr(wells[0], "dh_no"):
                dh_nos = [w.dh_no for w in wells]
        df = self.bulk_download("GetWaterChemistryDownloadAllData", {"DHNOs": dh_nos})
        df["collected_date"] = pd.to_datetime(df["collected_date"], format="%d/%m/%Y")
        df = df.rename(
            columns={
                "DHNO": "dh_no",
                "SAMPLE_NO": "sample_no",
                "Unit_No": "unit_hyphen",
                "Obs_No": "obs_no",
                "Collected_date": "collected_date",
                "Chem_Code": "analysis_code",
                "Chem_Name": "analysis_name",
                "Chem_Value": "value",
                "Chem_Unit_Code": "unit",
            },
            errors="ignore",
        )
        return df

    def bulk_elevation_surveys(self, wells, **kwargs):
        dh_nos = [w for w in wells]
        if len(wells):
            if hasattr(wells[0], "dh_no"):
                dh_nos = [w.dh_no for w in wells]
        df = self.bulk_download("GetElevationDownload", {"DHNOs": dh_nos})
        for date_col in ("ElevationDate", "AppliedDate"):
            df[date_col] = pd.to_datetime(df[date_col], format="%Y-%m-%d")
        df = df.rename(
            columns={
                "DHNO": "dh_no",
                "UnitNumber": "unit_hyphen",
                "Network": "network",
                "ObsNo": "obs_no",
                "ElevationDate": "elev_date",
                "AppliedDate": "applied_date",
                "GroundElevation": "ground_elev",
                "ReferenceElevation": "ref_elev",
                "SurveyMethod": "survey_meth",
                "VerticalAccuracy": "vert_accuracy",
                "ReferencePointType": "ref_point_type",
                "Comments": "comments",
            },
            errors="ignore",
        )
        return df

    def bulk_construction_events(self, wells, **kwargs):
        dh_nos = [w for w in wells]
        if len(wells):
            if hasattr(wells[0], "dh_no"):
                dh_nos = [w.dh_no for w in wells]
        df = self.bulk_download("GetConstructionDownload", {"DHNOs": dh_nos})
        for date_col in ("completion_date",):
            df[date_col] = pd.to_datetime(df[date_col], format="%d/%m/%Y")
        df = df.rename(
            columns={
                "DHNO": "dh_no",
                "Unit_No": "unit_hyphen",
                "Obs_No": "obs_no",
                "Bkf_ind": "backfilled",
                "case_from": "casing_from",
                "case_to": "casing_to",
                "case_min_diameter": "casing_min_diam",
                "case_material": "casing_material",
                "pcem": "pcemented",
                "pcem_from": "pcement_from",
                "pcem_to": "pcement_to",
                "pz_from": "pzone_from",
                "pz_to": "pzone_to",
                "pz_min_diameter": "pzone_min_diam",
                "pz_type": "pzone_type",
                "pz_material": "pzone_material",
                "pz_aperture": "pzone_aperture",
                "drill_meth": "drill_method",
                "well_dev_method": "development_method",
                "well_dev_duration": "development_duration",
                "Comments": "comments",
            },
            errors="ignore",
        )
        return df

    def bulk_construction_details(self, wells, **kwargs):
        dh_nos = [w for w in wells]
        if len(wells):
            if hasattr(wells[0], "dh_no"):
                dh_nos = [w.dh_no for w in wells]
        resp = self.post(
            "GetConstructionDetailsDownload?bulkOutput=CSV",
            data={"exportdata": json.dumps({"DHNOs": [w.dh_no for w in wells]})},
            **kwargs
        )
        dfs = {}
        name_map = {
            "WaterCut.csv": "water_cuts",
            "Drilling.csv": "drilling",
            "Casing.csv": "casing",
            "ProductionZone.csv": "prod_zones",
        }
        with zipfile.ZipFile(io.BytesIO(resp.r.content)) as zip_file:
            for n in zip_file.namelist():
                with zip_file.open(n, "r") as contained_file:
                    new_name = name_map[n]
                    dfs[new_name] = pd.read_csv(contained_file)

        # water_cuts
        if "water_cuts" in dfs:
            for date_col in ("WaterCutDate",):
                dfs["water_cuts"][date_col] = pd.to_datetime(
                    dfs["water_cuts"][date_col], format="%Y-%m-%d"
                )
            dfs["water_cuts"] = dfs["water_cuts"].rename(
                columns={
                    "DHNO": "dh_no",
                    "UnitNumber": "unit_hyphen",
                    "WaterCutDate": "water_cut_date",
                    "DepthFrom_m": "depth_from",
                    "DepthTo_m": "depth_to",
                    "WaterLevel_m": "swl",
                    "EstYeld_L_Sec": "yield",
                    "TestMethod": "test_method",
                    "TDS_mg_L": "tds",
                    "EC_us_cm": "ec",
                    "SampleType": "sample_type",
                },
                errors="ignore",
            )

        # drilling
        if "drilling" in dfs:
            dfs["drilling"] = dfs["drilling"].rename(
                columns={
                    "DHNO": "dh_no",
                    "UnitNumber": "unit_hyphen",
                    "From_m": "depth_from",
                    "To_m": "depth_to",
                    "Diammeter_mm": "hole_diam",
                    "Method": "drill_method",
                    "COMMENTS": "comments",
                },
                errors="ignore",
            )

        # casing
        if "casing" in dfs:
            dfs["casing"] = dfs["casing"].rename(
                columns={
                    "DHNO": "dh_no",
                    "UnitNumber": "unit_hyphen",
                    "DepthFrom_m": "depth_from",
                    "DepthTo_m": "depth_to",
                    "Diameter_mm": "casing_diam",
                    "Material": "casing_material",
                    "CementType": "cement_method",
                    "CementFrom_m": "cement_from",
                    "CementTo_m": "cement_to",
                    "COMMENTS": "comments",
                }
            )

        # prod_zones
        if "prod_zones" in dfs:
            dfs["prod_zones"] = dfs["prod_zones"].rename(
                columns={
                    "DHNO": "dh_no",
                    "UnitNumber": "unit_hyphen",
                    "Type": "pzone_type",
                    "DepthFrom_m": "depth_from",
                    "DepthTo_m": "depth_to",
                    "Diameter_mm": "pzone_diam",
                    "Material": "pzone_material",
                    "Aperture_mm": "pzone_aperture",
                    "COMMENTS": "comments",
                }
            )
        return dfs

    def bulk_drillers_logs(self, wells, **kwargs):
        dh_nos = [w for w in wells]
        if len(wells):
            if hasattr(wells[0], "dh_no"):
                dh_nos = [w.dh_no for w in wells]
        df = self.bulk_download("GetDrillersLogDownload", {"DHNOs": dh_nos})
        df["log_date"] = pd.to_datetime(df["log_date"], format="%d/%m/%Y")
        df = df.rename(
            columns={"DHNO": "dh_no", "Unit_No": "unit_hyphen", "Obs_No": "obs_no"},
            errors="ignore",
        )
        return df

    def bulk_strat_logs(self, wells, **kwargs):
        dh_nos = [w for w in wells]
        if len(wells):
            if hasattr(wells[0], "dh_no"):
                dh_nos = [w.dh_no for w in wells]
        df = self.bulk_download("GetStratLogDownload", {"DHNOs": dh_nos})
        df = df.rename(
            columns={
                "DHNO": "dh_no",
                "UNITNUMBER": "unit_hyphen",
                "STRAT_DEPTH_FROM": "depth_from",
                "STRAT_DEPTH_TO": "depth_to",
                "STRAT_NAME": "strat_name",
                "GIS_CODE": "gis_code",
            },
            errors="ignore",
        )
        return df

    def bulk_hydrostrat_logs(self, wells, **kwargs):
        dh_nos = [w for w in wells]
        if len(wells):
            if hasattr(wells[0], "dh_no"):
                dh_nos = [w.dh_no for w in wells]
        df = self.bulk_download("GetHydroStratLogDownload", {"DHNOs": dh_nos})
        df = df.rename(
            columns={
                "DHNO": "dh_no",
                "UNITNUMBER": "unit_hyphen",
                "HYDRO_DEPTH_FROM": "unit_depth_from",
                "HYDRO_DEPTH_TO": "unit_depth_to",
                "HYDRO_SUBUNIT_DEPTH_FROM": "subunit_depth_from",
                "HYDRO_SUBUNIT_DEPTH_TO": "subunit_depth_to",
                "HYDRO_TYPE": "hydro_type",
                "HYDRO_DEPTH_TO_GREATER_FLAG": "hydro_depth_to_greater_flag",
                "COMMENTS": "comments",
                "MAP_SYMBOL": "map_symbol",
                "STRAT_NAME": "strat_name",
                "GIS_CODE": "gis_code",
                "HYDRO_SUBUNIT_COMMENTS": "subunit_comments",
                "HYDRO_SUBUNIT_CODE": "subunit_code",
                "HYDRO_SUBUNIT_DESC": "subunit_desc",
            },
            errors="ignore",
        )
        return df

    def bulk_lith_logs(self, wells, **kwargs):
        dh_nos = [w for w in wells]
        if len(wells):
            if hasattr(wells[0], "dh_no"):
                dh_nos = [w.dh_no for w in wells]
        df = self.bulk_download("GetLithologicalLogDownload", {"DHNOs": dh_nos})
        df = df.rename(
            columns={
                "DHNO": "dh_no",
                "Unit_No": "unit_hyphen",
                "Obs_No": "obs_no",
                "Description": "descr",
            },
            errors="ignore",
        )
        return df

    def _cache_data(self, response):
        if response.df_exists:
            rdf = response.df
            cols_present = list(
                set(self.well_id_cols.keys()).intersection(set(rdf.columns))
            )
            rdf2 = rdf[cols_present].rename(columns=self.well_id_cols)
            self.well_cache = (
                pd.concat([self.well_cache, rdf2], sort=True)
                .drop_duplicates()
                .sort_values("unit_long")
            )
        return response

    def find_wells(self, input_text, **kwargs):
        ids = parse_well_ids(input_text, **kwargs)
        dh_nos = [x for id_type, x in ids if id_type == "dh_no"]
        unit_nos = [x for id_type, x in ids if id_type == "unit_no"]
        obs_nos = [x for id_type, x in ids if id_type == "obs_no"]
        r1 = self.get("GetUnitNumberSearchData", params={"MAPNUM": ",".join(unit_nos)})
        r2 = self.get(
            "GetObswellNumberSearchData", params={"OBSNUMBER": ",".join(obs_nos)}
        )
        dfs = [r.df for r in [r1, r2] if r.df_exists]
        df = (
            pd.concat(dfs, sort=False)
            .drop_duplicates()
            .rename(
                columns={"dhno": "dh_no", "mapnum": "unit_no", "obsnumber": "obs_no"}
            )
        )
        for key in ["obs_no", "name"]:
            if not key in df:
                df[key] = ""
            df.loc[df[key].isnull(), key] = ""
        return Wells([Well(**r.to_dict()) for _, r in df.iterrows()])

    def find_wells_in_lat_lon(self, lats, lons):
        lons = sorted(lons)
        lats = sorted(lats)
        dfs = []

        coords = [lats[0], lons[0], lats[1], lons[1]]
        box = ",".join(["{:.4f}".format(c) for c in coords])
        r = self.get("GetGridData?Box={box}".format(box=box))
        df = r.df.drop_duplicates().rename(
            columns={"dhno": "dh_no", "mapnum": "unit_no", "obsnumber": "obs_no"}
        )
        for key in ["obs_no", "name", "unit_no"]:
            if not key in df:
                df[key] = ""
            df.loc[df[key].isnull(), key] = ""
        return Wells([Well(**r.to_dict()) for _, r in df.iterrows()])

    def refresh_available_groupings(self):
        """Load lists data from API. Stores them in the attributes
        aquifers, networks, nrm_regions, pwas, pwras.

        """
        response = self.get("GetAdvancedListsData")
        self.aquifers = {
            item["V"]: item["T"].replace((item["V"] + ": "), "")
            for item in response.json["Aquifer"]
            if "V" in item
        }
        self.networks = {item["V"]: item["T"] for item in response.json["Networks"]}
        self.nrm_regions = {
            item["V"]: item["T"] + " NRM Region" for item in response.json["NRMRegion"]
        }
        self.pwas = {
            item["V"]: item["V"] + " PWA" for item in response.json["PrescribedArea"]
        }
        self.pwras = {
            item["V"]: item["V"] + " PWRA" for item in response.json["PrescribedWRArea"]
        }

    def data_pwa(self, pwa, swl_status=None, tds_status=None):
        q = []
        if not swl_status is None:
            q.append("SWLSTATUS='{}'".format("C" if swl_status else "H"))
        if not tds_status is None:
            q.append("SALSTATUS='{}'".format("H" if tds_status else "H"))
        return self.get(
            "GetPWASearchData?PWA={pwa}&Q={q}".format(pwa=pwa, q="%20AND%20".join(q))
        )
        # SALINITY - can join by  AND
        # GetPWASearchData?PWA=Angas-Bremer&Q=SALSTATUS='C'
        # GetPWASearchData?PWA=Angas-Bremer&Q=SWLSTATUS='C'%20AND%20SALSTATUS='C'

    def search_by_suburb(self, suburb):
        suburb = suburb.upper()
        return self.get("GetSuburbFromName", app="WDDWFS", params={"Suburb": suburb})

    def search_by_radius(self, lat, lon, radius):
        # GetCircleData?Box=-34.155353,138.455916&Radius=2
        lat = float(lat)
        lon = float(lon)
        radius = float(radius)
        return self.get("GetCircleData", params={"Box": [lat, lon], "Radius": radius})

    def search_by_rect(self, sw_corner, ne_corner):
        lat0, lon0 = sw_corner
        lat1, lon1 = ne_corner
        return self.get(
            "GetGridData",
            params="Box=" + ",".join([str(c) for c in [lat1, lon0, lat0, lon1]]),
        )

    def search_by_network(self, *network):
        network_codes = [n for n in network if n in self.networks.keys()]
        networks_inverted = {v: k for k, v in self.networks.items()}
        network_codes += [networks_inverted[n] for n in network if n in self.networks.values()]
        logger.debug(f"Querying for validated network codes: {network_codes}")
        return self.get("GetObswellNetworkData", params="Network=" + ",".join(network_codes))

