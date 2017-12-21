from attrdict import AttrDict
import requests
from lxml import html


SARIG_QUERY = 'https://minerals.sarig.sa.gov.au/Details.aspx?DRILLHOLE_NO={drillhole}'


def collect_sarig_images(self):
    query = SARIG_QUERY.format(drillhole=str(int(self.drillhole)))
    response = requests.get(query)
    tree = html.fromstring(response.content)
    image_urls = ['https://minerals.sarig.sa.gov.au' + path[2:] for path in
        tree.xpath('//*[@id="ctl00_formBody_TabContainer_tabHistoricalDocuments_udpHistoricalDocuments"]/div[1]/div[2]/a/@href')]
    self.images = [
        AttrDict({'url': path}) for path in image_urls]
