GetLBSearchData
^^^^^^^^^^^^^^^^^^^^^^

`GetLBSearchData?LB=Green%20Adelaide <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetLBSearchData?LB=Green%20Adelaide>`__

The :ref:`webservice-metadata` section shows how to retrieve the Landscape Board names which can be used in this request.

Returns a list of a wells as a JSON array of objects - only two are shown below:

.. code-block:: json

    [
        {
            "DHNO": 26527,
            "LAT": -35.3385495,
            "LON": 138.4550502,
            "MAPNUM": 652700531,
            "MAX_DEPTH": 66.14,
            "DRILL_DATE": "1950-07-18",
            "PURP_DESC": "IRR",
            "AQ_MON": "Qpa",
            "SWL": 48.77,
            "TDS": 6655,
            "STAT_DESC": "NL",
            "CLASS": "WW",
            "PWA": "McLaren Vale",
            "PWRA": "Western Mount Lofty Ranges",
            "NRM": "Adelaide & Mt Lofty Ranges",
            "LOGDRILL": "N",
            "LITHOLOG": "N",
            "CHEM": "N",
            "WATER": "Y",
            "SAL": "Y",
            "OBSWELL": "N",
            "STRATLOG": "N",
            "HSTRATLOG": "N",
            "LATEST_SWL_DATE": "1950-07-18",
            "LATEST_SAL_DATE": "1950-07-18",
            "LATEST_OPEN_DEPTH": 66.14,
            "LATEST_OPEN_DATE": "1950-07-18"
        }
    ]

GetLBFromName
^^^^^^^^^^^^^^^^^^^^

There is also the related query `GetLBFromName?NAME=Green%20Adelaide <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDWFS.ashx/GetLBFromName?NAME=Green%20Adelaide>`__

.. include:: polyline-explainer.rst

Returns a JSON array of objects:

.. code-block:: json

    [
        {
            "OBJECTID": 3,
            "REGIONNAME": "Green Adelaide",
            "REGIONID": 3,
            "GROREF": "32/2019",
            "SHAPE.AREA": 5018119817.19687,
            "SHAPE.LEN": 408587.310397432,
            "URL": "https://apps.waterconnect.sa.gov.au/Services-WDD/proxy.ashx?https://location.sa.gov.au/server5/rest/services/WaterConnect_PROD/MapServer/",
            "Boundary": [
            "`rprEm~smYlN{YRc@nIgQpC}F`EoIjNv@??rId@@S@Yez@e[QQgFm"
            ]
        }
    ]
    
