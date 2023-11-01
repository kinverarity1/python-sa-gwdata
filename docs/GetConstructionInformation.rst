GetConstructionInformation
^^^^^^^^^^^^^^^^^^^^^^^^^^

You can request a single drillhole number (DHNO) (see search queries above for how to obtain this number).

`GetConstructionInformation?DHNO=155787 <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetConstructionInformation?DHNO=155787>`__

This returns a list of events related to the construction of the well. There are
two types denoted by "CONSTRN_FLAG". If this is "C", the event is a
"construction event", i.e. some type of physical work was done on the well:
usually either the initial construction, rehabilitation or re-lining, or
decommissioning and backfilling.

If "CONSTRN_FLAG" is "S", that means a "survey event", typically where the depth
of the hole was measured. Survey events can have some details of the
construction but are not the primary references for that information.

.. code-block:: json

    [
      {
        "COMPLETION_DATE": "2018-03-14",
        "CONSTRN_FLAG": "C",
        "TOTAL_DPTH": 0,
        "FINAL_DPTH": 0,
        "CURRENT_DPTH": 0,
        "PERMIT_NO": 281913,
        "BKF_IND": "Y",
        "COMMENTS": "Decommissioned using 7 metres of crushed rock, 3% bentonite grout seal and backfilled with sand",
        "COMPLETION_NO": 342876
      },
      {
        "COMPLETION_DATE": "2013-10-18",
        "CONSTRN_FLAG": "S",
        "CURRENT_DPTH": 250.5,
        "BKF_IND": "N",
        "COMMENTS": "Geophysical logging job 9167 - camera inspection along with other probes.",
        "COMPLETION_NO": 324023
      },
      {
        "COMPLETION_DATE": "1999-01-01",
        "CONSTRN_FLAG": "C",
        "BKF_IND": "N",
        "COMMENTS": "Stainless section swaged across 8-5\" FRP joint at 178 m. Exact date unknown.",
        "COMPLETION_NO": 324022
      },
      {
        "COMPLETION_DATE": "1996-03-08",
        "CONSTRN_FLAG": "C",
        "TOTAL_DPTH": 253.4,
        "FINAL_DPTH": 253.4,
        "CURRENT_DPTH": 253.4,
        "PERMIT_NO": 34201,
        "BKF_IND": "N",
        "COMPLETION_NO": 70892
      }
    ]

The "COMPLETION_NO" field can be used as a query parameter for the following calls which
return details of the drilled hole, casing, and production zone.

GetConstructionSummaryInformation
"""""""""""""""""""""""""""""""""

This query gets a useful summary of the hole dimensions, although note that it
doesn't contain details of multiple casing strings or multiple drilled hole
diameters. The other queries (following) return all details.

`GetConstructionSummaryInformation?COMPLETION_NO=70892 <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetConstructionSummaryInformation?COMPLETION_NO=70892>`__

.. code-block:: json

    [
      {
        "COMPLETION_NO": 70892,
        "SOURCE_DATA_CHANGE_TIME": "2018-09-24",
        "DENORM_TIME": "2018-09-24",
        "GLOBAL_POP": "N",
        "DRILL_FR": 0,
        "DRILL_TO": 253.4,
        "DRILL_DIAM": 200,
        "DRILL_METH": "RTF+RTM+RTW",
        "CORE_FLAG": "N",
        "CASE_FR": 0,
        "CASE_TO": 237.85,
        "CASE_DIAM": 125,
        "CASE_MTRL": "FRP",
        "PCEM": "Y",
        "PCEM_FR": 0,
        "PCEM_TO": 183,
        "PZONE_FR": 237.85,
        "PZONE_TO": 252.85,
        "PZONE_TYPE": "S+SMP",
        "PZONE_MTRL": "SST",
        "PZONE_DIAM": 140,
        "MIN_DIAM": 125,
        "APERTURE": ".8+1",
        "SCREENED": "Y",
        "DEV": "Y",
        "DEV_METH": "AIRL+JET",
        "DEV_DURATION": 12.5,
        "AQ_SUBAQ": "Twd"
      }
    ]

GetDrillingSummary
""""""""""""""""""

This returns a list of the drilled sections of the well, their diameter, and the
drilling method used.

`GetDrillingSummary?COMPLETION_NO=70892 <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetDrillingSummary?COMPLETION_NO=70892>`__

.. code-block:: json

    [
      {
        "DRILLHOLE_NO": 155787,
        "COMPLETION_NO": 70892,
        "DRILL_FR": 0,
        "DRILL_TO": 6,
        "DIAM": 550,
        "DRILL_METH": "RTF"
      },
      {
        "DRILLHOLE_NO": 155787,
        "COMPLETION_NO": 70892,
        "DRILL_FR": 6,
        "DRILL_TO": 96,
        "DIAM": 400,
        "DRILL_METH": "RTM"
      },
      {
        "DRILLHOLE_NO": 155787,
        "COMPLETION_NO": 70892,
        "DRILL_FR": 184,
        "DRILL_TO": 253.4,
        "DIAM": 200,
        "DRILL_METH": "RTM"
      },
      {
        "DRILLHOLE_NO": 155787,
        "COMPLETION_NO": 70892,
        "DRILL_FR": 96,
        "DRILL_TO": 184,
        "DIAM": 275,
        "DRILL_METH": "RTW"
      }
    ]

GetConstructionWaterCut
"""""""""""""""""""""""

This returns a list of the water cuts taken during drilling. Not all of the
fields in the example will necessarily be present in the returned JSON.

`GetConstructionWaterCut?COMPLETION_NO=65568 <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetConstructionWaterCut?COMPLETION_NO=65568>`__

.. code-block:: json

    [
      {
        "WATER_CUT_MEAS_NO": 3818,
        "WATER_CUT_DATE": "1993-12-12",
        "WATER_CUT_DEPTH_FROM": 108,
        "WATER_CUT_DEPTH_TO": 114,
        "DEPTH_TO_WATER": 100,
        "WELL_YIELD": 1,
        "EXTR_METHOD_CODE": "AIRL",
        "TDS": 699,
        "EC": 1270,
        "SAMPLE_TYPE": "S"
      }
    ]

GetCasingSummary
""""""""""""""""

This returns a list of the cased sections of the well, excluding the parts of
the production zone (see below).

`GetCasingSummary?COMPLETION_NO=70892 <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetCasingSummary?COMPLETION_NO=70892>`__

.. code-block:: json

    [
      {
        "DRILLHOLE_NO": 155787,
        "COMPLETION_NO": 70892,
        "CASE_FR": 0,
        "CASE_TO": 6,
        "CASE_DIAM": 450,
        "CASE_MTRL": "STL",
        "CEM_TYPE": "P",
        "CEM_FR": 0,
        "CEM_TO": 6
    },
      {
        "DRILLHOLE_NO": 155787,
        "COMPLETION_NO": 70892,
        "CASE_FR": 0,
        "CASE_TO": 91.5,
        "CASE_DIAM": 300,
        "CASE_MTRL": "FRP",
        "CEM_TYPE": "P",
        "CEM_FR": 0,
        "CEM_TO": 106
    },
      {
        "DRILLHOLE_NO": 155787,
        "COMPLETION_NO": 70892,
        "CASE_FR": 91.5,
        "CASE_TO": 183,
        "CASE_DIAM": 201,
        "CASE_MTRL": "FRP",
        "CEM_TYPE": "P",
        "CEM_FR": 125,
        "CEM_TO": 183
    },
      {
        "DRILLHOLE_NO": 155787,
        "COMPLETION_NO": 70892,
        "CASE_FR": 177.85,
        "CASE_TO": 237.85,
        "CASE_DIAM": 125,
        "CASE_MTRL": "FRP"
    },
      {
        "DRILLHOLE_NO": 155787,
        "COMPLETION_NO": 70892,
        "CASE_DIAM": 201,
        "CASE_MTRL": "SST"
      }
    ]

.. _GetProductionZoneSummary:

GetProductionZoneSummary
""""""""""""""""""""""""

This query returns the details of any screens ("S"), slotted ("SC") or open
("OH") sections. It also includes any blank sections within the production zone,
and the sump ("SMP"), if there is one.

`GetProductionZoneSummary?COMPLETION_NO=70892 <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetProductionZoneSummary?COMPLETION_NO=70892>`__

.. code-block:: json

    [
      {
        "DRILLHOLE_NO": 155787,
        "COMPLETION_NO": 70892,
        "PZONE_FR": 237.85,
        "PZONE_TO": 239.85,
        "PZONE_DIAM": 140,
        "PZONE_TYPE_CODE": "S",
        "PZONE_MTRL": "SST",
        "APERTURE": 1
      },
      {
        "DRILLHOLE_NO": 155787,
        "COMPLETION_NO": 70892,
        "PZONE_FR": 239.85,
        "PZONE_TO": 249.85,
        "PZONE_DIAM": 140,
        "PZONE_TYPE_CODE": "S",
        "PZONE_MTRL": "SST",
        "APERTURE": 0.8
      },
      {
        "DRILLHOLE_NO": 155787,
        "COMPLETION_NO": 70892,
        "PZONE_FR": 249.85,
        "PZONE_TO": 252.85,
        "PZONE_DIAM": 140,
        "PZONE_TYPE_CODE": "SMP",
        "PZONE_MTRL": "SST"
      }
    ]

GetExtraSummaryDetails
""""""""""""""""""""""

Not sure what this contains. Gravel-pack details? Liner seals?

`GetExtraSummaryDetails?COMPLETION_NO=70892 <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetExtraSummaryDetails?COMPLETION_NO=70892>`__

.. code-block:: json
