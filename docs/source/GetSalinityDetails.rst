Salinity measurements
===========================

You can request a single drillhole number (DHNO) (see search queries above for how to obtain this number).

`GetSalinityDetails?DHNO=75383 <https://www.waterconnect.sa.gov.au/_layouts/15/DFW.SharePoint.WDD/WDDDMS.ashx/GetSalinityDetails?DHNO=75383>`__

.. code-block:: json

    [
        {
            "COLLECTED_DATE": "1987-09-01",
            "TDS": 2619,
            "EC": 4691,
            "PH": 9.5,
            "SAMPLE_TYPE": "S",
            "SERIES_TYPE": "T",
            "ANOMALOUS_IND": "N",
            "EXTR_METHOD_CODE": "PUMP",
            "MEASURED_DURING": "M",
            "DATA_SOURCE_CODE": "DEWNR"
        },
        {
            "COLLECTED_DATE": "1987-12-16",
            "TDS": 3058,
            "EC": 5461,
            "PH": 8.1,
            "SAMPLE_TYPE": "S",
            "SERIES_TYPE": "T",
            "ANOMALOUS_IND": "N",
            "EXTR_METHOD_CODE": "PUMP",
            "MEASURED_DURING": "M",
            "DATA_SOURCE_CODE": "DEWNR"
        }
    ]

.. include:: footer.rst