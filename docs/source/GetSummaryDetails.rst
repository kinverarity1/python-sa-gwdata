Summary of drillhole details
=============================

You can request a single drillhole number (DHNO) (see search queries above for how to obtain this number).

`GetSummaryDetails?DHNO=75383 <https://www.waterconnect.sa.gov.au/_layouts/15/DFW.SharePoint.WDD/WDDDMS.ashx/GetSummaryDetails?DHNO=75383>`__

.. code-block:: json

    [
        {
            "OBSWELL_NO": "ANG013",
            "UnitNumber": "6728-2489",
            "DRILLHOLE_NO": 75383,
            "DrillDate": "1985-05-20T00:00:00",
            "Depth": 86,
            "CasedTo": 64,
            "SWL": 8.26,
            "TDS": 3058,
            "DrillClass": "WW, MW",
            "Aquifer": "Tr",
            "DrillStatus": "CAP",
            "LAT": -34.659407,
            "LON": 139.413824,
            "DB_DRILLERS_LOG": "N",
            "DB_LITHO_LOG": "N",
            "DB_STRAT_LOG": "Y",
            "DB_WATER_CHEM": "N",
            "DB_WATER_INFO": "Y",
            "DB_WATER_SAMPLE": "Y",
            "DB_GEOPHYSICAL_LOG": "Y",
            "DB_HYDRO_STRAT_LOG": "Y",
            "DB_YIELD": "N",
            "DB_ELEVATION": "Y",
            "DB_CONSTRUCTION": "Y",
            "DB_PHOTOS": "Y",
            "HUNDRED_NAME": "ANGAS",
            "LAT_DEGREES": 34,
            "LAT_MINUTES": 39,
            "LAT_SECONDS": 33.865,
            "LONG_DEGREES": 139,
            "LONG_MINUTES": 24,
            "LONG_SECONDS": 49.766,
            "AMG_EASTING": 354655.02,
            "AMG_NORTHING": 6163582.03,
            "AMG_ZONE": 54,
            "DH_NAME": "M146",
            "DH_NAME1": "M146",
            "MAP_100000_NO": 6728,
            "DH_SEQ_NO": 2489,
            "DB_OBS_WELL": "Y",
            "NRM_REGION_CODE": "South Australian Murray-Darling Basin",
            "LATEST_PERMIT_NO": 16054,
            "OBS_WELL_PLAN_CODE": "ANG",
            "OBS_WELL_SEQ_NO": 13,
            "PURPOSE_CODE": "EXP",
            "MAP_250000_CODE": "SI5409",
            "MAP_50K_NO": 1,
            "MAP_10K_NO": 16,
            "MAP_2500_CODE": "a",
            "MAP_1000_CODE": "5",
            "ORIG_DRILLED_DEPTH": 86,
            "ORIG_DRILLED_DATE": "1985-05-20T00:00:00",
            "MAX_DRILLED_DEPTH_DATE": "1985-05-20T00:00:00",
            "LATEST_OPEN_DEPTH": 86,
            "LATEST_OPEN_DEPTH_DATE": "1985-05-20T00:00:00",
            "LATEST_MIN_DIAM": 75,
            "LATEST_RSWL": 48.13,
            "LATEST_SWL_DATE": "2017-10-10T10:40:30",
            "LATEST_EC": 5461,
            "LATEST_SAL_DATE": "1987-12-16T00:00:00",
            "LATEST_REF_ELEVATION": 57.21,
            "LATEST_ELEVATION_DATE": "1985-05-20T00:00:00",
            "MAP_250K": "SI5409 ADELAIDE",
            "MAP_100K": "6728 Mannum",
            "GROUP_CODE": "MARNE",
            "STAND_WATER_LEVEL_STATUS": "C",
            "SALINITY_STATUS": "N",
            "DrillClassTT": "Water Well, Mineral Well",
            "PURPOSE_CODETT": "Exploration",
            "DrillStatusTT": "Capped",
            "AquiferTT": "Renmark Group"
        }
    ]

And some additional keywords with `GetExtraSummaryDetails?DHNO=75383 <https://www.waterconnect.sa.gov.au/_layouts/15/DFW.SharePoint.WDD/WDDDMS.ashx/GetExtraSummaryDetails?DHNO=75383>`__

.. code-block:: json

    [
        {
            "DRILLHOLE_NO": 75383,
            "GROUP_CODE": "MARNE",
            "GROUP_DESC": "Marne River and Saunders Creek PWRA"
        }
    ]

.. include:: footer.rst