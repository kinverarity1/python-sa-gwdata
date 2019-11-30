import io
import json
import logging
import time

import pandas as pd
import requests

from sa_gwdata.identifiers import parse_well_ids, UnitNo, ObsNo, Well, Wells

__all__ = (
    "WaterConnectSession",
    "Response",
    "find_wells",
    "water_levels",
    "salinities",
    "drillers_logs",
)


logger = logging.getLogger(__name__)


class Response(object):
    def __init__(self, response, **kwargs):
        """Groundwater Data HTTP response.

        Args:
            response (requests.Response object): the HTTP response

        """
        self.response = response
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
            df = pd.DataFrame(self.json).rename(columns=str.lower)
            self._df = df
        return self._df

    @property
    def df_exists(self):
        """Check if JSON can be converted to a DataFrame. Returns bool."""
        if isinstance(self.json, list):
            return True
        return False


def get_global_session(force_new=False):
    if not "__waterconnect_session" in globals():
        global __waterconnect_session
        __waterconnect_session = WaterConnectSession()
    else:
        if force_new:
            del globals()["__waterconnect_session"]
            __waterconnect_session = WaterConnectSession()
    return __waterconnect_session


def find_wells(input_text, **kwargs):
    """Find wells and retrieve some summary information.

    Args:
        input_text (str): any well identifiers to parse. See
            :func:`sa_gwdata.parse_well_ids_plaintext` for details of
            other keyword arguments you can pass here.

    For example:

        >>> import sa_gwdata
        >>> wells = sa_gwdata.find_wells("yat99 5840-46 ULE205")
        ...
        >>> wells
        [<sa_gwdata.Well(6916) 5840-46 / MLC008 / HIGHWAY BORE>, 
         <sa_gwdata.Well(198752) 6028-2319 / ULE205 / US 1>, 
         <sa_gwdata.Well(54354) 6628-7385 / YAT099 / ST MICHAELS COLLEGE>
        ]

    """
    session = get_global_session()
    return session.find_wells(input_text, **kwargs)


def water_levels(wells, session=None, **kwargs):
    """Get table of water level measurements for wells.

    Args:
        wells (list): list of drillhole numbers (ints)
            or :class:`sa_gwdata.Well` objects
    
    Returns: pandas DataFrame.

    """
    session = get_global_session()
    return session.bulk_water_levels(wells, **kwargs)


def salinities(wells, session=None, **kwargs):
    """Get table of salinity samples for wells.

    Args:
        wells (list): list of drillhole numbers (ints)
            or :class:`sa_gwdata.Well` objects
    
    Returns: pandas DataFrame.
    
    """
    if session is None:
        session = get_global_session()
    return session.bulk_salinities(wells, **kwargs)


def drillers_logs(wells, session=None, **kwargs):
    """Get table of lithological intervals from drillers logs for wells.

    Args:
        wells (list): list of drillhole numbers (ints)
            or :class:`sa_gwdata.Well` objects
    
    Returns: pandas DataFrame.
    
    """
    if session is None:
        session = get_global_session()
    return session.bulk_drillers_logs(wells, **kwargs)


class WaterConnectSession(requests.Session):
    """Wrapper around repeated requests to Groundwater Data.

    Args:
        endpoint (str): url endpoint for API, optional
        sleep (int): minimum interval between requests in seconds.
            Be nice, do not reduce it.
        verify (bool): require valid SSL certificate

    Other args and kwargs are passed to request.Session constructor.

    Usage:

        >>> from sa_gwdata import WaterConnectSession
        >>> with WaterConnectSession() as s:
        ...     df = s.get("GetObswellNetworkData", params={"Network": "CENT_ADEL"})

    """

    well_id_cols = {
        "dhno": "drillhole_no",
        "obsnumber": "obs_no",
        "mapnum": "unit_long",
    }

    def __init__(
        self, *args, endpoint=None, sleep=2, verify=True, load_list_data=True, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.well_cache = pd.DataFrame(columns=set(self.well_id_cols.values()))
        self.verify = verify
        if not endpoint:
            endpoint = (
                "https://www.waterconnect.sa.gov.au/_layouts"
                "/15/dfw.sharepoint.wdd/WDDDMS.ashx/"
            )
        self.endpoint = endpoint
        self.last_request = time.time() - sleep
        self.sleep = sleep
        if load_list_data:
            self.refresh_available_groupings()

    def get(self, path, verify=None, **kwargs):
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
        logger.debug("GET {} verify={}".format(path, verify))
        response = super().get(path, verify=verify, **kwargs)
        self.last_request = time.time()
        endpoint, name = path.rsplit("/", 1)
        logger.debug("Response content = {}".format(response.content))
        return self._cache_data(Response(response, endpoint=endpoint, name=name))

    def post(self, path, verify=None, **kwargs):
        # TODO: Implement _cache_data for CSV bulk data formats... ?
        if verify is None:
            verify = self.verify
        t_remain = self.sleep - (time.time() - self.last_request)
        if t_remain > 0:
            logger.debug("Waiting {} sec".format(t_remain))
            time.sleep(t_remain)
        if not path.startswith(self.endpoint):
            path = self.endpoint + path
        logger.debug("POST {} verify={}".format(path, verify))
        response = super().post(path, verify=verify, **kwargs)
        self.last_request = time.time()
        endpoint, name = path.rsplit("/", 1)
        return Response(response, endpoint=endpoint, name=name)

    def bulk_download(self, service, json_data, format="CSV"):
        r = self.post(
            "{service}?bulkOutput={format}".format(service=service, format=format),
            data={"exportdata": json.dumps(json_data)},
        )
        print(r.response.content)
        with io.BytesIO(r.response.content) as buffer:
            df = pd.read_csv(buffer)
        return df

    def bulk_water_levels(self, wells, **kwargs):
        dh_nos = [w for w in wells]
        if len(wells):
            if hasattr(wells[0], "dh_no"):
                dh_nos = [w.dh_no for w in wells]
        df = self.bulk_download("GetWaterLevelDownload", {"DHNOs": dh_nos})
        return df

    def bulk_salinities(self, wells, **kwargs):
        dh_nos = [w for w in wells]
        if len(wells):
            if hasattr(wells[0], "dh_no"):
                dh_nos = [w.dh_no for w in wells]
        df = self.bulk_download("GetSalinityDownload", {"DHNOs": dh_nos})
        return df

    def bulk_drillers_logs(self, wells, **kwargs):
        dh_nos = [w for w in wells]
        if len(wells):
            if hasattr(wells[0], "dh_no"):
                dh_nos = [w.dh_no for w in wells]
        df = self.bulk_download("GetDrillersLogDownload", {"DHNOs": dh_nos})
        return df

    def _cache_data(self, response):
        if response.df_exists:
            rdf = response.df
            cols_present = set(self.well_id_cols.keys()).intersection(set(rdf.columns))
            rdf2 = rdf[cols_present].rename(columns=self.well_id_cols)
            self.well_cache = (
                pd.concat([self.well_cache, rdf2], sort=False)
                .drop_duplicates()
                .sort_values("unit_long")
            )
        return response

    def find_wells(self, input_text, **kwargs):
        """Find wells and retrieve some summary information.

        Args:
            input_text (str): any well identifiers to parse. See
                :func:`sa_gwdata.parse_well_ids_plaintext` for details of
                other keyword arguments you can pass here.

        For example:

            >>> from sa_gwdata import WaterConnectSession
            >>> with WaterConnectSession() as s:
            ...     wells = s.find_wells("yat99 5840-46 ULE205")
            ...
            >>> wells
            [<sa_gwdata.Well(6916) 5840-46 / MLC008 / HIGHWAY BORE>, 
             <sa_gwdata.Well(198752) 6028-2319 / ULE205 / US 1>, 
             <sa_gwdata.Well(54354) 6628-7385 / YAT099 / ST MICHAELS COLLEGE>
            ]

        """
        ids = parse_well_ids(input_text, **kwargs)
        dh_nos = [x for id_type, x in ids if id_type == "dh_no"]
        unit_nos = [x for id_type, x in ids if id_type == "unit_no"]
        obs_nos = [x for id_type, x in ids if id_type == "obs_no"]
        r1 = self.get("GetUnitNumberSearchData", params={"MAPNUM": ",".join(unit_nos)})
        r2 = self.get(
            "GetObswellNumberSearchData", params={"OBSNUMBER": ",".join(obs_nos)}
        )
        df = (
            pd.concat([r1.df, r2.df], sort=False)
            .drop_duplicates()
            .rename(
                columns={"dhno": "dh_no", "mapnum": "unit_no", "obsnumber": "obs_no"}
            )
        )
        return Wells([Well(**r.to_dict()) for _, r in df.iterrows()])

    def refresh_available_groupings(self):
        """Load lists data from API. Stores them in the attributes
        networks, nrm_regions, pwas, pwras.

        """
        response = self.get("GetAdvancedListsData")
        self.aquifers = {
            item["V"]: item["T"].replace((item["V"] + ": "), "")
            for item in response.json["Aquifer"]
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
