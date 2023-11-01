GetElevationDetails
^^^^^^^^^^^^^^^^^^^

You can request a single drillhole number (DHNO) (see search queries above for how to obtain this number).

`GetElevationDetails?DHNO=27382 <https://www.waterconnect.sa.gov.au/_layouts/15/DFW.SharePoint.WDD/WDDDMS.ashx/GetElevationDetails?DHNO=27382>`__

Returns a JSON array of objects:

.. code-block:: json

    [
      {
        "DRILLHOLE_NO": 27382,
        "ELEVATION_NO": 90767,
        "ELEV_DATE": "1995-02-20",
        "GRND_ELEV": 3.544,
        "REF_ELEV": 4.601,
        "REF_POINT_TYPE": "STP",
        "SVY_METH": "SUR",
        "ELEV_POINT_TYPE_DESC": "Stand Pipe (Top)",
        "APPLIED_DATE": "1992-01-01",
        "COMMENTS": "TOP STAND PIPE COVER"
      },
      {
        "DRILLHOLE_NO": 27382,
        "ELEVATION_NO": 90766,
        "ELEV_DATE": "1980-11-04",
        "GRND_ELEV": 3.432,
        "REF_ELEV": 4.332,
        "REF_POINT_TYPE": "WLC",
        "SVY_METH": "SUR",
        "ELEV_POINT_TYPE_DESC": "Well Cover (Top)",
        "APPLIED_DATE": "1980-11-04",
        "COMMENTS": "COVER PLATE"
      },
      {
        "DRILLHOLE_NO": 27382,
        "ELEVATION_NO": 114527,
        "ELEV_DATE": "1980-04-09",
        "REF_ELEV": 3.53,
        "REF_POINT_TYPE": "REF",
        "SVY_METH": "SUR",
        "ELEV_POINT_TYPE_DESC": "Reference",
        "APPLIED_DATE": "1980-04-09"
      },
      {
        "DRILLHOLE_NO": 27382,
        "ELEVATION_NO": 9531,
        "ELEV_DATE": "1968-03-07",
        "GRND_ELEV": 3.138,
        "REF_ELEV": 3.443,
        "REF_POINT_TYPE": "TOC",
        "SVY_METH": "SUR",
        "ELEV_POINT_TYPE_DESC": "Casing (Top)",
        "APPLIED_DATE": "1968-02-07"
      }
    ]
