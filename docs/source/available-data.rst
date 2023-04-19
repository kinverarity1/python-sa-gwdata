Available data types on Groundwater Data (GD)
=============================================

.. toctree::
    :maxdepth: 6
    :caption: Data types:

    data-types-well-summary
    data-types-groundwater-level

Salinity samples
~~~~~~~~~~~~~~~~~~~

These are water samples collected from wells, usually by pumping
deliberately for monitoring (or sampled from an irrigation pump), and
the salinity estimated by measuring the electrical conductivity (EC)

See the :ref:`water monitoring data tutorial <tutorial-water-monitoring-data>`
for more details.

Driller's logs
~~~~~~~~~~~~~~~

Lithological logs
~~~~~~~~~~~~~~~~~~~

Stratigraphic logs
~~~~~~~~~~~~~~~~~~~~

Hydrostratigraphic logs
~~~~~~~~~~~~~~~~~~~~~~~~

Drilled intervals
~~~~~~~~~~~~~~~~~~

Casing intervals and cementing information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Contains details of the casing installed in a well - includes
some limited information about the annular grout. Note that production
zone data is not stored alongside casing data

Production zones
~~~~~~~~~~~~~~~~~~~
Details of the production zone interval of a well e.g. screens, slotted sections, blank sections in screens,
open hole intervals, and riser pipes. The types of intervals that are recorded in this table are:

.. _production-zone-interval:
.. list-table::
   :header-rows: 1
   :widths: 10 90

   * - Type
     - Description
   * - OH
     - Open hole interval. 
   * - S / WS 
     - Screen. Although 'WS' originally indicated wirewound screen, many/most of the entries
       with 'S' are indeed for wirewound screens.
   * - SB
     - Blank section of pipe between screened intervals
   * - SMP
     - Sump
   * - SC
     - Slotted casing interval
   * - PC
     - Perforated casing interval
   * - UKN
     - Unknown interval

.. warning:: Some depth entries in this table may not always be consistent with the :ref:`drilled intervals <drilled-intervals>` table above.

.. _production-zone-fields:

Fields and field names are listed below for: the CSV file obtainable from Groundwater Data; the JSON returned
by :ref:`GetProductionZoneSummary`; and the pandas DataFrame returned under the key ``"prod_zones"`` from
:meth:`sa_gwdata.construction_details`. 

.. csv-table::
  :file: data-types/production-zone.csv
  :header-rows: 1
  :widths: 20 35 15 15 15

Water cuts (groundwater observations during drilling)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Observations of groundwater level, salinity and yield made at the time of drilling; generally historical and
collected during cable tool drilling.

Wellhead elevation surveys
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Generally water monitoring wells are surveyed specifically for their elevation, and the data are kept here.
The data are also arranged by time such that changes in the reference point for groundwater level measurements
can be fully corrected to have a consistent and accurate measurement of groundwater level over the well's
life.

Water chemistry analyses
~~~~~~~~~~~~~~~~~~~~~~~~
