import os, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pytest

from sa_gwdata.sarig import *


def test_dh_doc_images():
    assert fetch_dh_doc_image_urls(27384) == [
        "https://minerals.sarig.sa.gov.au/DisplayHistoricalDocument.aspx?image_no=399200&is_thumbnail=N",
        "https://minerals.sarig.sa.gov.au/DisplayHistoricalDocument.aspx?image_no=399201&is_thumbnail=N",
        "https://minerals.sarig.sa.gov.au/DisplayHistoricalDocument.aspx?image_no=399202&is_thumbnail=N",
        "https://minerals.sarig.sa.gov.au/DisplayHistoricalDocument.aspx?image_no=399203&is_thumbnail=N",
        "https://minerals.sarig.sa.gov.au/DisplayHistoricalDocument.aspx?image_no=399204&is_thumbnail=N",
    ]

