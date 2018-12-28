import json
import logging
import pandas
import time

import requests


logger = logging.getLogger(__name__)


class Response(object):
    def __init__(self, response):
        self.response = response

    @property
    def r(self):
        return self.response

    @property
    def json(self):
        if not hasattr(self, "_json"):
            self._json = json.loads(self.response.text)
        return self._json

    @property
    def df(self):
        if not hasattr(self, "_df"):
            if isinstance(self.json, list):
                df = pandas.DataFrame(self.json)
            df.columns = [s.lower() for s in df.columns]
            self._df = df
        return self._df


class Session(requests.Session):
    def __init__(self, *args, sleep=2, verify=True, **kwargs):
        super().__init__(*args, **kwargs)
        self.verify = verify
        self.endpoint = "https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/"
        self.last_request = time.time() - sleep
        self.sleep = sleep
        self.refresh_available_groupings()

    def get(self, path, verify=None, **kwargs):
        """HTTP GET verb.

        Args:
            path (str): final portion of URL path off the end of self.endpoint
            e.g. to GET
            https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetAdvancedListsData
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
        return Response(response)

    def refresh_available_groupings(self):
        '''Load lists data from API.'''
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

    def data_pwa(self, pwa):
        pass
        # SALINITY - can join by  AND
        # GetPWASearchData?PWA=Angas-Bremer&Q=SALSTATUS='C'
        # GetPWASearchData?PWA=Angas-Bremer&Q=SWLSTATUS='C'%20AND%20SALSTATUS='C'
