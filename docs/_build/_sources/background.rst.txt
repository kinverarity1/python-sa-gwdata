Background information
========================

Websites providing data
~~~~~~~~~~~~~~~~~~~~~~~~~

Groundwater data in SA is available through a variety of websites but the main and
most important sources are:

1. `Groundwater Data  <https://www.waterconnect.sa.gov.au/Systems/GD/Pages/Default.aspx>`__- this the main interface for accessing groundwater data.
2. `Water Data SA <https://water.data.sa.gov.au>`__ (Aquarius Web Portal) - used for continuous logger data of mostly water levels.
3. `SARIG Drillhole database <https://minerals.sarig.sa.gov.au/QuickSearch.aspx>`__ - for accessing historical scanned documentation.

Drillhole/well identifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~

The Groundwater Data website provides access to a wide variety of information for drillholes
or water wells. The data all originates in SA Geodata, which is an internal government database
shared by the Department of Environment and Water and the Department of Energy and Mining.
The fundamental object to understand when trying to access groundwater information 
is the drillhole, which represents either a mineral or petroleum 
exploration drillhole, petroleum production well, or a water well 
(could be a monitoring well or a production well -- from
a data point of view it doesn't matter much). I'll use the language
"drillhole" and "well" largely interchangeably from here on, as this is focused
only on the data point of view.

.. note::

  The one exception is the **water point**. This is a particular
  type of drillhole which is not a drillhole at all in the common sense
  of the word. It represents things which are not boreholes that nonetheless provide a surface expression
  of groundwater (as compared to surface water). Some are natural, others artifical (but not boreholes). The most common types of 
  are sinkholes and artesian springs. A less common type
  are open-cut mine pit lakes.

.. _drillhole-number:

Drillhole number
----------------

Drillholes are uniquely identified by this. It is 
strictly an integer which ranges from one up to six digits. e.g. 53925. 
Note that it forms part of the unique URL to both Groundwater Data:

https://www.waterconnect.sa.gov.au/Systems/GD/Pages/Details.aspx?DHNO=53925
  
and to the SARIG drillhole database:

https://minerals.sarig.sa.gov.au/Details.aspx?DRILLHOLE_NO=53925

.. warning:: 
  
  It works differently in Water Data SA where the unit number (see below) is in the URL, for example '6829-692' here:

  https://water.data.sa.gov.au/Data/Location/Summary/Location/6829-692/Interval/Latest

.. _unit-number:

Unit number
----------- 

This is a set of two numbers: a four digit 100K mapsheet number
e.g. 6628, and an integer as sequence number, e.g. 6956. The mapsheet and
sequence numbers, when presented together, form a "unit number". It can be 
presented in a variety of different formats e.g. "6628-6956" (the most common),
"662806956" (an integer representation formed by padding the sequence to
five digits) and "6628-06956" (seen in contexts relating to water licensing).
Unit numbers are available for all drillholes visible on Groundwater Data.
Although they are generally used only for water wells, they do exist for 
all drillholes.

.. _obswell-number:  

Observation well ID  
-------------------

Also known as **obswell number** or **obsnumber**, this is a similar concept
to the unit number, but utilises abbreviated observation well "hundreds"
for the mapsheet e.g. "YAT" (referring to the hundred of Yatala), and 
a similar observation well network sequence number e.g. 27. It is then presented,
like the unit number, a variety of ways: "YAT027", "YAT27", "YAT 27", and so on.
This stems from the historical use of a different database for water well
monitoring data, now discontinued. Obswell numbers are manually assigned, and
are not available for all wells, not even all water monitoring wells. The
presence of an obswell number also doesn't mean that a well is a monitoring well.

Clustered piezos
-----------------

A drillhole is one bore, so in situations where there are multiple bores connected
together (e.g. a multi-tail exploration or petroleum well) or located together
(a clustered piezometer), there will be multiple drillholes to represent each
bore. Unfortunately the database doesn't link these together (!) other than 
that they are likely to have exactly the same spatial coordinates.

Spatial groupings
~~~~~~~~~~~~~~~~~~~

Groundwater is managed in SA in a variety of ways, and some of these are
available through Groundwater Data:

- **Landscape region** / **Natural resource management (NRM) region** 
  These are large-scale areas which have responsibility for management of 
  water resources - see `Landscape SA <https://www.landscape.sa.gov.au/>`__ for
  more information.

- **Prescribed well area** (PWA) - these are smaller scale areas which are
  used to manage groundwater resources via a water allocation plans (WAP). 
  You can see all of the PWAs in SA on 
  `Location SA <https://location.sa.gov.au/viewer/?map=hybrid&x=142.06629&y=-31.83374&z=6&uids=156>`__.

- **Prescribed water resource area** (PWRA) - similar to a PWA, but they
  are used for both groundwater and surface water resources. To see all of the
  PWRAs in SA visit `Location SA <https://location.sa.gov.au/viewer/?map=hybrid&x=140.33869&y=-34.35527&z=8&uids=154>`__.

- **Observation well network** - these are not defined spatially. They are
  manually maintained lists of monitoring wells which DEW visits
  each year to measure water level and/or salinity. They generally correspond
  to a geographical area. You can see a list on the Groundwater Data
  website:

.. figure:: figures/obswell_networks.png


.. |br| raw:: html

   <br />