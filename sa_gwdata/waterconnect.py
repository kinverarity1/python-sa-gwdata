import json
import logging
import pandas as pd
import time

import requests


__all__ = ("WaterConnectSession", "Response")


logger = logging.getLogger(__name__)


class Response(object):
    """Groundwater Data HTTP response.

    Args:
        response (requests.Response object): the HTTP response to parse

    """

    def __init__(self, response, **kwargs):
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
        columns converted into the lowercase."""
        if not hasattr(self, "_df"):
            df = pd.DataFrame(self.json)
            df.columns = [s.lower() for s in df.columns]
            self._df = df
        return self._df

    @property
    def df_exists(self):
        """Check if JSON can be converted to a DataFrame. Returns bool."""
        if isinstance(self.json, list):
            return True
        return False


class WaterConnectSession(requests.Session):
    """Wrapper around repeated requests to Groundwater Data.

    Args:
        endpoint (str): url endpoint for API, optional
        sleep (int): minimum interval between requests in seconds. 
            Keep things ethical -- do not reduce it.
        verify (bool): require valid SSL certificate

    Other args and kwargs are passed to request.Session constructor.

    Usage:

        >>> with sa_gwdata.WaterConnectSession() as s:
        ...     df = s.get("GetObswellNetworkData", params={"Network": "CENT_ADEL"})

    """

    well_id_cols = {
        "dhno": "drillhole_no",
        "obsnumber": "obs_no",
        "mapnum": "unit_long",
    }

    def __init__(self, *args, endpoint=None, sleep=2, verify=True, **kwargs):
        super().__init__(*args, **kwargs)
        self.well_cache = pd.DataFrame(columns=set(self.well_id_cols.values()))
        self.verify = verify
        if not endpoint:
            endpoint = (
                "https://www.waterconnect.sa.gov.au"
                "/_layouts/15"
                "/dfw.sharepoint.wdd/WDDDMS.ashx/"
            )
        self.endpoint = endpoint
        self.last_request = time.time() - sleep
        self.sleep = sleep
        self.refresh_available_groupings()

    def get(self, path, verify=None, **kwargs):
        """HTTP GET verb to Groundwater Data.

        Args:
            path (str): final portion of URL path off the end of self.endpoint
                e.g. to GET
                ``https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetAdvancedListsData``
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
        return self._cache_data(Response(response, endpoint=endpoint, name=name))

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

    def refresh_available_groupings(self):
        """Load lists data from API. Stores them in the attributes
        networks, nrm_regions, pwas, pwras.

        """
        response = self.get("GetAdvancedListsData")
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
