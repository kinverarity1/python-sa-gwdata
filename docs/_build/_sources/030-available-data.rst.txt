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

See the :ref:`water monitoring data tutorial <042-tutorial-water-monitoring-data>`
for more details.

Geological logs
~~~~~~~~~~~~~~~

There are fundamentally two types of geological logs:

* Driller's / Lithology: descriptions of the lithology
* Stratigraphic / Hydrostratigraphic: interpretations of the (hydro)stratigraphy

.. note:: 
  
  For older wells, logs may be available in the scanned drillhole document 
  images (e.g. typed or handwritten), but may not have yet been transcribed
  into the relevant part of the database, and therefore won't show up in these
  tables.

Driller's logs
---------------

These are descriptions of the lithology intersected by a drillhole, as
recorded by the licensed water well driller on their DWCR (drillers well completion report).
The units and descriptions are often somewhat colloquial and informal but can
be very useful bearing in mind that drillers generally have a lot of experience
in a given area and can be very familiar with local variations in lithology and
aquifer properties.

A driller's log should be available for the majority of wells.

Lithological logs
------------------

Descriptions of the lithology intersected by a drillhole, as recorded by a
geologist or hydrogeologist. These are usually collected in addition to the 
drillers log, and are more detailed and formal in nature. 

They are not available for most water wells.

Stratigraphic logs
--------------------

A stratigraphic log will provide an interpretation of the stratigraphy
intersected by a drillhole. It is generally something done for historic wells,
and mineral and petroleum wells, rather than water wells.

Hydrostratigraphic logs
------------------------

A hydrostratigraphic log provides an interpretation of the hydrostratigraphy
(i.e. sequence of aquitards and aquifers) that a drillhole intersects. It's 
similar to a stratigraphic log, but usually slightly more detailed and more
relevant to groundwater work: for example, in a well on the Adelaide Plains,
it would detail the depths of the T1 and T2 aquifers, whereas a stratigraphic
log will only show the Port Willunga Formation.

These are not available for the majority of water wells, so you may have to
search a little further afield for a nearby one.

Construction information
~~~~~~~~~~~~~~~~~~~~~~~~

Drilled intervals
-----------------

Casing intervals and cementing information
------------------------------------------

Contains details of the casing installed in a well, such as the depths of installation
and the material. It also contains 
limited information about the annular grout (e.g. a top and bottom depth,
and the grout and water volumes).

Note that production zone data is not stored alongside casing data, and that
some things which might be considered "casing" are actually stored in the
production zone table below (e.g. sumps, screen blanks, and riser pipe).

Production zones
----------------

Details of the production zone interval of a well e.g. screens, slotted sections, blank sections in screens,
open hole intervals, and riser pipes.  Some of these are intervals are what might more generally be known
as "production" zones in the sense that they are likely to provide lateral access to groundwater in the formation.
Others, however, do not (e.g. riser pipe), although they are stored in the same table.

The types of intervals that are recorded in this table are:

.. _production-zone-interval:
.. list-table::
   :header-rows: 1
   :widths: 10 70 20

   * - Type
     - Description
     - Provides access to groundwater at this depth?
   * - OH
     - Open hole interval. 
     - Yes
   * - S / WS 
     - Screen. Although 'WS' originally indicated wirewound screen, many/most of the entries
       with 'S' are indeed for wirewound screens.
     - Yes
   * - SB
     - Blank section of pipe between screened intervals
     - No
   * - SMP
     - Sump
     - No
   * - SC
     - Slotted casing interval
     - Yes
   * - PC
     - Perforated casing interval
     - Yes
   * - UKN
     - Unknown interval
     - Maybe

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
-----------------------------------------------------

Observations of groundwater level, salinity and yield made at the time of drilling. These observations
are much more common for historical wells drilled by cable tool rigs, but they are still occasionally collected.

Wellhead elevation surveys
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generally water monitoring wells are surveyed specifically for their elevation, and the data are kept here.
The data are also arranged by time such that changes in the reference point for groundwater level measurements
can be fully corrected to have a consistent and accurate measurement of groundwater level over the well's
life.

DEW also routinely upload elevations derived from digital elevation models (DEM) for wells which have not been
surveyed. These elevations are included in this dataset, with the "survey method" field providing a way to
discriminate the high-quality survey data from the much lower quality DEM data.

Water chemistry analyses
~~~~~~~~~~~~~~~~~~~~~~~~
