GetDrillersLogInformation
^^^^^^^^^^^^^^^^^^^^^^^^^

You can request a single drillhole number (DHNO) (see search queries above for how to obtain this number).

`GetDrillersLogInformation?DHNO=28083 <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetDrillersLogInformation?DHNO=28083>`__

This returns a list of drillers logs (referenced by ``LOG_NO``) with metadata:

.. code-block:: json

    [
      {
        "DRILLHOLE_NO": 28083,
        "LOG_NO": 200958,
        "GEOL_LOGGING_DATE": "1984-08-29",
        "GEOL_LOGGER_NAME": "M. FOSDIKE"
      }
    ]

GetDrillersLogSummary
^^^^^^^^^^^^^^^^^^^^^

Each log can then be retrieved with a query for LOG_NO:

`GetDrillersLogSummary?LOG_NO=200958 <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetDrillersLogSummary?LOG_NO=200958>`__

Only the first and last record are shown in the below example:

.. code-block:: json

    [
      {
        "DRILLHOLE_NO": 28083,
        "LOG_NO": 200958,
        "DRILLER_DEPTH_FROM": 0,
        "DRILLER_DEPTH_TO": 12,
        "LITHO_DRILLER_CODE": "SAND",
        "LITHO_DESC": "sand and decomposed ...."
      },
      {
        "DRILLHOLE_NO": 28083,
        "LOG_NO": 200958,
        "DRILLER_DEPTH_FROM": 196,
        "DRILLER_DEPTH_TO": 197,
        "LITHO_DESC": "hard"
      }
    ]

