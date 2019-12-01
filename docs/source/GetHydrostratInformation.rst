GetHydrostratInformation
^^^^^^^^^^^^^^^^^^^^^^^^^

You can request a single drillhole number (DHNO) (see search queries above for how to obtain this number).

`GetHydrostratInformation?DHNO=28083 <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetHydrostratInformation?DHNO=28083>`__

This returns the hydrostratigraphic log (if available) for this drillhole:

Note that one field present in the bulk download CSV (HYDRO_SUBUNIT_CODE) is not
included in the JSON output.

.. code-block:: json

    [
      {
        "DRILLHOLE_NO": 28083,
        "HYDRO_INT_NO": 52959,
        "STRAT_UNIT_NO": 3642,
        "HYDRO_DEPTH_FROM": 0,
        "HYDRO_DEPTH_TO": 96,
        "MAP_SYMBOL": "Qpah",
        "STRAT_NAME": "Hindmarsh Clay",
        "STRAT_UNIT_DESC": "Consolidated mottled clay and sandy clay with sand and gravel lenses, aeolian sand, gypseous and pelletal clay dunes and calcareous palaeosols. Alluvial and colluvial red-brown sandy clay with sand and gravel beds."
      },
      {
        "DRILLHOLE_NO": 28083,
        "HYDRO_INT_NO": 52960,
        "STRAT_UNIT_NO": 3630,
        "HYDRO_DEPTH_FROM": 96,
        "HYDRO_DEPTH_TO": 166,
        "COMMENTS": "T1a aquifer",
        "MAP_SYMBOL": "Tph",
        "STRAT_NAME": "Hallett Cove Sandstone",
        "STRAT_UNIT_DESC": "Sandstone, calcareous; limestone, sandy, fossiliferous. Transgressive, shallow marginal marine."
      },
    ]

.. GetExtraHydrostratInformation
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


