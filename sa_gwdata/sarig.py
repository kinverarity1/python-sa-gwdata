import requests
import lxml.html


SARIG_QUERY = "https://minerals.sarig.sa.gov.au/Details.aspx?DRILLHOLE_NO={drillhole}"


__all__ = ("collect_sarig_images",)


def collect_sarig_images(self):
    query = SARIG_QUERY.format(drillhole=str(int(self.drillhole)))
    response = requests.get(query)
    tree = lxml.html.fromstring(response.content)
    image_urls = [
        "https://minerals.sarig.sa.gov.au" + path[2:]
        for path in tree.xpath(
            '//*[@id="ctl00_formBody_TabContainer_tabHistoricalDocuments_udpHistoricalDocuments"]/div[1]/div[2]/a/@href'
        )
    ]
    self.images = [{"url": path} for path in image_urls]
