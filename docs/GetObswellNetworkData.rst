GetObswellNetworkData
^^^^^^^^^^^^^^^^^^^^^

`GetObswellNetworkData?Network=KAT_FP,PIKE_FP <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetObswellNetworkData?Network=KAT_FP,PIKE_FP>`__

Note you can request more than one network at a time.

The :ref:`webservice-metadata` section shows how to retrieve the codes for all the different monitoring networks.

Returns a JSON array of objects (a list of wells) - only 2 are shown below:

.. code-block:: json

      [
        {
          "NAME": "LD 5",
          "DHNO": 174806,
          "LAT": -34.3242717,
          "LON": 140.4949448,
          "MAPNUM": 692900829,
          "MAX_DEPTH": 25.4,
          "OBSNUMBER": "KTR043",
          "PERMIT_NO": 48454,
          "DRILL_DATE": "1999-03-24",
          "PURP_DESC": "OBS",
          "AQ_MON": "Tpl",
          "SWL": 19.01,
          "TDS": 28004,
          "CLASS": "WW",
          "NRM": "South Australian Murray-Darling Basin",
          "LOGDRILL": "N",
          "LITHOLOG": "Y",
          "CHEM": "N",
          "WATER": "Y",
          "SAL": "Y",
          "LATEST_SWL_DATE": "2016-07-11",
          "LATEST_SAL_DATE": "1999-03-24",
          "OBSNETWORK": "KAT_FP",
          "SWLSTATUS": "C",
          "SALSTATUS": "N",
          "LATEST_OPEN_DEPTH": 25.4,
          "LATEST_OPEN_DATE": "2009-06-02"
        },
        {
          "NAME": "PMA 8",
          "DHNO": 132425,
          "LAT": -34.2728022,
          "LON": 140.8203725,
          "MAPNUM": 702901214,
          "MAX_DEPTH": 32.22,
          "OBSNUMBER": "PAG045",
          "PERMIT_NO": 28390,
          "DRILL_DATE": "1992-11-13",
          "PURP_DESC": "OBS",
          "AQ_MON": "Tpl",
          "SWL": 25.9,
          "TDS": 28927,
          "STAT_DESC": "OPR",
          "CLASS": "WW",
          "PWA": "Noora",
          "NRM": "South Australian Murray-Darling Basin",
          "LOGDRILL": "Y",
          "LITHOLOG": "N",
          "CHEM": "N",
          "WATER": "Y",
          "SAL": "Y",
          "LATEST_SWL_DATE": "2016-07-12",
          "LATEST_SAL_DATE": "1992-11-13",
          "OBSNETWORK": "PIKE_FP",
          "SWLSTATUS": "C",
          "SALSTATUS": "N",
          "LATEST_OPEN_DEPTH": 32.22,
          "LATEST_OPEN_DATE": "2009-04-20"
        }
      ]
