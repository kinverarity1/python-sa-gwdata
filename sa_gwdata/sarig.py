import re

import requests


SARIG_QUERY = "https://minerals.sarig.sa.gov.au/Details.aspx?DRILLHOLE_NO={drillhole}"
SARIG_IMAGE_URL = "https://minerals.sarig.sa.gov.au/{match}"
IMAGE_NO_RE = re.compile(
    r"DisplayHistoricalDocument\.aspx\?image_no=\d*&is_thumbnail=N"
)

__all__ = ("fetch_dh_doc_image_urls",)


def fetch_dh_doc_image_urls(dh_no):
    """Fetch drillhole document image URLs from SARIG.

    Args:
        dh_no (int): drillhole number.

    Returns: a list of URLs to images.

    """
    query = SARIG_QUERY.format(drillhole="{:.0f}".format(dh_no))
    response = requests.get(query)
    return [SARIG_IMAGE_URL.format(match=m) for m in IMAGE_NO_RE.findall(response.text)]

