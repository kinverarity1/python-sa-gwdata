Well yield
===========================

You can request a single drillhole number (DHNO) (see search queries above for how to obtain this number).

`GetWellYieldDetails?DHNO=72339 <https://www.waterconnect.sa.gov.au/_layouts/15/DFW.SharePoint.WDD/WDDDMS.ashx/GetWellYieldDetails?DHNO=72339>`__

``WELL_YIELD`` is in litres per second.

.. code-block:: json

    [
        {
            "WELL_YIELD_MEAS_NO": 87257,
            "OBS_DATE": "1968-08-09",
            "WELL_YIELD": 5.0512,
            "MEASURED_DURING": "D",
            "DATA_SOURCE_CODE": "DEWNR",
            "COMMENTS": "Hydat Angas Bremer upload"
        }
    ]

.. include:: footer.rst