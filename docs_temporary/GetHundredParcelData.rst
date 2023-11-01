GetHundredParcelData (by hundred name)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`GetHundredParcelData?HUND=ALEXANDRINA <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetHundredParcelData?HUND=ALEXANDRINA>`__

You can retrieve the list of valid hundred names from the query in the :ref:`webservice-metadata` section.

Returns a JSON array of objects - only two are shown below:

.. code-block:: json

    [
      {
        "NAME": "DONNA 1",
        "DHNO": 38423,
        "LAT": -35.4858167,
        "LON": 138.91965,
        "MAPNUM": 662700003,
        "MAX_DEPTH": 701.04,
        "DRILL_DATE": "1964-12-17",
        "PURP_DESC": "EXP",
        "STAT_DESC": "DRY",
        "CLASS": "PW",
        "PWRA": "Eastern Mount Lofty Ranges",
        "NRM": "South Australian Murray-Darling Basin",
        "LOGDRILL": "N",
        "LITHOLOG": "N",
        "CHEM": "N",
        "WATER": "N",
        "SAL": "N",
        "OBSWELL": "N",
        "STRATLOG": "Y",
        "HSTRATLOG": "Y",
        "LATEST_OPEN_DEPTH": 701.04,
        "LATEST_OPEN_DATE": "1964-12-17"
      },
      {
        "NAME": "PS 4D",
        "DHNO": 259078,
        "LAT": -35.493279,
        "LON": 139.0294919,
        "MAPNUM": 672703759,
        "MAX_DEPTH": 1.72,
        "DRILL_DATE": "2009-08-23",
        "PURP_DESC": "MON",
        "CLASS": "WW",
        "NRM": "South Australian Murray-Darling Basin",
        "LOGDRILL": "N",
        "LITHOLOG": "Y",
        "CHEM": "N",
        "WATER": "N",
        "SAL": "N",
        "OBSWELL": "N",
        "STRATLOG": "N",
        "HSTRATLOG": "N",
        "LATEST_OPEN_DEPTH": 1.72,
        "LATEST_OPEN_DATE": "2009-08-23"
      }
    ]
    
GetHundredParcelData (by parcel/plan/title numbers)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For example, search for wells on CT5604/777:

`GetHundredParcelData?HUND=&PARCEL=&PARCELNO=&PLAN=&PLANNO=&TITLE_PREFIX=CT&TITLE_VOLUME=5604&TITLE_FOLIO=777 <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetHundredParcelData?HUND=&PARCEL=&PARCELNO=&PLAN=&PLANNO=&TITLE_PREFIX=CT&TITLE_VOLUME=5604&TITLE_FOLIO=777>`__

Returns a JSON array of objects:

.. code-block:: json

    [
      {
        "NAME": "B 361",
        "DHNO": 28764,
        "LAT": -34.155353,
        "LON": 138.455916,
        "MAPNUM": 652900119,
        "MAX_DEPTH": 27.43,
        "OBSNUMBER": "DAE005",
        "DRILL_DATE": "1949-01-18",
        "PURP_DESC": "STK",
        "SWL": 22.15,
        "YIELD": 0.37,
        "TDS": 3753,
        "STAT_DESC": "OPR",
        "CLASS": "WW",
        "NRM": "Northern & Yorke",
        "LOGDRILL": "N",
        "LITHOLOG": "N",
        "CHEM": "N",
        "WATER": "Y",
        "SAL": "Y",
        "OBSWELL": "Y",
        "STRATLOG": "N",
        "HSTRATLOG": "N",
        "LATEST_SWL_DATE": "2010-03-11",
        "LATEST_SAL_DATE": "1995-09-18",
        "LATEST_YIELD_DATE": "1949-01-01",
        "OBSNETWORK": "NY_NP_STH",
        "SWLSTATUS": "H",
        "SALSTATUS": "H",
        "LATEST_OPEN_DEPTH": 26.4,
        "LATEST_OPEN_DATE": "1995-06-29"
      },
      {
        "NAME": "B 362",
        "DHNO": 29112,
        "LAT": -34.156073,
        "LON": 138.456339,
        "MAPNUM": 652900481,
        "MAX_DEPTH": 39,
        "OBSNUMBER": "DAE006",
        "DRILL_DATE": "1992-06-19",
        "PURP_DESC": "STK",
        "YIELD": 3.15,
        "TDS": 2245,
        "STAT_DESC": "OPR",
        "CLASS": "WW",
        "NRM": "Northern & Yorke",
        "LOGDRILL": "N",
        "LITHOLOG": "N",
        "CHEM": "N",
        "WATER": "Y",
        "SAL": "Y",
        "OBSWELL": "Y",
        "STRATLOG": "N",
        "HSTRATLOG": "N",
        "LATEST_SWL_DATE": "2009-04-28",
        "LATEST_SAL_DATE": "1995-09-18",
        "OBSNETWORK": "NY_NP_STH",
        "SWLSTATUS": "H",
        "SALSTATUS": "H",
        "LATEST_OPEN_DATE": "1993-03-03"
      },
      {
        "DHNO": 166516,
        "LAT": -34.1573313,
        "LON": 138.4576219,
        "MAPNUM": 652901068,
        "MAX_DEPTH": 41,
        "OBSNUMBER": "DAE015",
        "PERMIT_NO": 40438,
        "DRILL_DATE": "1997-03-12",
        "PURP_DESC": "STK",
        "SWL": 19.5,
        "YIELD": 4,
        "TDS": 2234,
        "STAT_DESC": "OPR",
        "CLASS": "WW",
        "NRM": "Northern & Yorke",
        "LOGDRILL": "Y",
        "LITHOLOG": "N",
        "CHEM": "N",
        "WATER": "Y",
        "SAL": "Y",
        "OBSWELL": "N",
        "STRATLOG": "N",
        "HSTRATLOG": "N",
        "LATEST_SWL_DATE": "1997-03-12",
        "LATEST_SAL_DATE": "2003-04-03",
        "LATEST_YIELD_DATE": "1997-03-12",
        "LATEST_OPEN_DEPTH": 41,
        "LATEST_OPEN_DATE": "1997-03-12"
      }
    ]

GetBoundaryFromTitle
^^^^^^^^^^^^^^^^^^^^

A related query is `GetBoundaryFromTitle?PREFIX=CT&VOLUME=5604&FOLIO=777 <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDWFS.ashx/GetBoundaryFromTitle?PREFIX=CT&VOLUME=5604&FOLIO=777>`__, which delivers the geographical polygons that CT 5604/777 represents.

.. include:: polyline-explainer.rst

.. code-block:: json

    [
      {
        "PLAN_T": "H",
        "URL": "http:\/\/sdsi.sa.gov.au\/arcgis\/rest\/services\/DEWNRint\/WaterConnect_WaterConnect\/MapServer\/",
        "Boundary": [
          "lymoEueblYvNr@mQ`d@tAue@"
        ]
      },
      {
        "PLAN_T": "H",
        "URL": "http:\/\/sdsi.sa.gov.au\/arcgis\/rest\/services\/DEWNRint\/WaterConnect_WaterConnect\/MapServer\/",
        "Boundary": [
          "b|noEogclY{Bxw@mHnGoUtExb@_gA"
        ]
      }
    ]
