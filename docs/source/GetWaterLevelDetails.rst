Water level observations
===========================

You can request a single drillhole number (DHNO) (see search queries above for how to obtain this number).

`GetWaterLevelDetails?DHNO=75383 <https://www.waterconnect.sa.gov.au/_layouts/15/DFW.SharePoint.WDD/WDDDMS.ashx/GetWaterLevelDetails?DHNO=75383>`__

Only the first and last record are shown in the sample response payload below:

.. code-block:: json

    [
        {
            "OBS_DATE": "1985-05-20",
            "STANDING_WATER_LEVEL": 22.68,
            "RSWL": 33.71,
            "ANOMALOUS_IND": "N",
            "PUMPING_IND": "N",
            "MEASURED_DURING": "D",
            "DATA_SOURCE_CODE": "DEWNR"
        },
        {
            "OBS_DATE": "2017-10-10",
            "STANDING_WATER_LEVEL": 8.26,
            "RSWL": 48.13,
            "ANOMALOUS_IND": "N",
            "PUMPING_IND": "N",
            "MEASURED_DURING": "M",
            "DATA_SOURCE_CODE": "DEWNR"
        }
    ]

.. include:: footer.rst