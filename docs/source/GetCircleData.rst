GetCircleData
^^^^^^^^^^^^^

`GetCircleData?Box=-34.155353,138.455916&Radius=2 <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetCircleData?Box=-34.155353,138.455916&Radius=2>`__

Radius is in kilometres.

It returns an JSON array of objects, for example:

.. code-block:: json

    [
      {
        "NAME": "B408",
        "DHNO": 28757,
        "LAT": -34.1419354,
        "LON": 138.4434028,
        "MAPNUM": 652900112,
        "MAX_DEPTH": 35,
        "OBSNUMBER": "DAE008",
        "PURP_DESC": "DOM",
        "SWL": 18,
        "YIELD": 0.13,
        "TDS": 3241,
        "STAT_DESC": "OPR",
        "CLASS": "WW",
        "NRM": "Northern & Yorke",
        "LOGDRILL": "N",
        "LITHOLOG": "N",
        "CHEM": "Y",
        "WATER": "Y",
        "SAL": "Y",
        "OBSWELL": "Y",
        "STRATLOG": "N",
        "HSTRATLOG": "N",
        "LATEST_SWL_DATE": "1985-06-12",
        "LATEST_SAL_DATE": "1995-09-18",
        "LATEST_YIELD_DATE": "1949-01-01",
        "OBSNETWORK": "NY_NP_STH",
        "SWLSTATUS": "N",
        "SALSTATUS": "H",
        "LATEST_OPEN_DATE": "1974-01-01"
      },
      {
        "NAME": "UWIBAMI 1",
        "DHNO": 239671,
        "LAT": -34.1441968,
        "LON": 138.4561724,
        "MAPNUM": 652901133,
        "MAX_DEPTH": 300.2,
        "DRILL_DATE": "2009-02-15",
        "STAT_DESC": "SUS",
        "CLASS": "PW",
        "NRM": "Northern & Yorke",
        "LOGDRILL": "N",
        "LITHOLOG": "N",
        "CHEM": "N",
        "WATER": "N",
        "SAL": "N",
        "OBSWELL": "N",
        "STRATLOG": "N",
        "HSTRATLOG": "Y",
        "LATEST_OPEN_DEPTH": 300.2,
        "LATEST_OPEN_DATE": "2009-02-15"
      }
    ]

