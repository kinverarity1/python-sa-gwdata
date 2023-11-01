.. _data-fields-well-info:

Data fields: general well information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Groundwater Data provides data for all drillholes in the State drillhole database (SA Geodata). This
covers multiple types of drillholes:

Water wells
   Wells which are intended to intersect groundwater, whether for monitoring or for
   extraction or recharge/drainage of groundwater. The data for these type
   of wells derives from well completion reports submitted to DEW as part of the 
   requirements attached to water well permits. Any edits or updates or new data
   should be sent to `groundwater@sa.gov.au <mailto:groundwater@sa.gov.au>`__.

Water points
   Database records to record surface expressions of groundwater such as springs and
   sinkholes.

Mineral exploration wells
   Drilled under an exploration or mining lease. Data for these are added by
   the Department of Energy & Mining.

Petroleum exploration or production wells
   Drilled under a petroleum lease. Incomplete data are available for these 
   drillholes: the main place to retrieve petroleum well data from is 
   `PEPS <https://peps.sa.gov.au/>`__.

Other
   Engineering/geotechnical holes and other types of shallow drillholes may
   also be in the database.

All the data types below can be added and present for all types of drillholes,
but in general it will be most complete for water wells, and for some of the
geological data types, also the case for mineral exploration wells.

Well information is available through:

- the "Well Summary" CSV download
- the :doc:`GetSummaryDetails` JSON call
- the :func:`sa_gwdata.wells_summary` function

.. csv-table::
  :file: data-types/well-summary.csv
  :header-rows: 1
  :widths: 20 35 15 15