import json
import logging
import time

import requests


class GroundwaterDataSession(object):

    def __init__(self, *args, sleep=2., **kwargs):
        self.session = requests.Session(*args, **kwargs)
        self.sleep = sleep
        self.refresh_available_groupings()

    def get(self, *args, **kwargs):
        response = self.session.get(*args, **kwargs)
        time.sleep(self.sleep)
        return response

    def refresh_available_groupings(self):
        response = self.get('https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetAdvancedListsData')
        list_data = json.loads(response.text)
        self.networks = {item['V']: item['T'] for item in list_data['Networks']}
        self.nrm_regions = {item['V']: item['T'] + ' NRM Region' for item in list_data['NRMRegion']}
        self.pwas = {item['V']: item['V'] + ' PWA' for item in list_data['PrescribedArea']}
        self.pwras = {item['V']: item['V'] + ' PWRA' for item in list_data['PrescribedWRArea']}

    def data_pwa(self, pwa):
        pass
        # SALINITY - can join by  AND 
        # https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetPWASearchData?PWA=Angas-Bremer&Q=SALSTATUS='C'
        # https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetPWASearchData?PWA=Angas-Bremer&Q=SWLSTATUS='C'%20AND%20SALSTATUS='C'