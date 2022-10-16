Background information
========================

Drillhole/well identifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~

Groundwater Data provides access to a wide variety of information for drillholes
or water wells, sourced from SA Geodata. The fundamental piece of data to
understand is the drillhole, which represents either a mineral or petroleum 
exploration drillhole, petroleum production well, or a water well 
(could be a monitoring well or a production well -- from
a data point of view it doesn't matter much). I'll use the language
"drillhole" and "well" largely interchangeably from here on, as this is focused
only on the data point of view.

- **Drillhole number**: Drillholes are uniquely identified by this. It is 
  strictly an integer which ranges from one up to six digits. e.g. 53925. 
  Note that it forms part of the unique URL to both Groundwater Data 
  https://www.waterconnect.sa.gov.au/Systems/GD/Pages/Details.aspx?DHNO=53925
  and 
  the SARIG drillhole database
  https://minerals.sarig.sa.gov.au/Details.aspx?DRILLHOLE_NO=53925
- **Unit number**: this is a set of two numbers: a four digit mapsheet number
  e.g. 6628, and an integer as sequence number, e.g. 6956. The mapsheet and
  sequence numbers, when presented together, form a "unit number". It can be 
  presented in a variety of different formats e.g. "6628-6956" (the most common),
  "662806956" (an integer representation formed by padding the sequence to
  five digits) and "6628-06956" (seen in contexts relating to water licensing).
  Unit numbers are available for all drillholes visible on Groundwater Data.
  Although they are generally used only for water wells, they do exist for 
  all wells.
- **Observation well ID** (also known as **obsnumber**): this is a similar 
  concept to the unit number, but utilises abbreviated observation well "hundreds"
  for the mapsheet e.g. "YAT" (referring to the hundred of Yatala), and 
  a similar observation well network sequence number e.g. 27. It is then presented,
  like the unit number, a variety of ways: "YAT027", "YAT27", "YAT 27", and so on.
  This stems from the historical use of a different database for water well
  monitoring data, now discontinued. Obswell numbers are manually assigned, and
  are not available for all wells, not even all water monitoring wells. The
  presence of an obswell number also doesn't mean that a well is a monitoring well.

A drillhole is one bore, so in situations where there are multiple bores connected
together (e.g. a multi-tail exploration or petroleum well) or located together
(a clustered piezometer), there will be multiple drillholes to represent each
bore. Unfortunately the database doesn't link these together (!) other than 
that they are likely to have exactly the same spatial coordinates.

Spatial concepts
~~~~~~~~~~~~~~~~

Groundwater is managed in SA in a variety of ways, and some of these are
available through Groundwater Data:

- **Landscape Regions** / **NRM Regions** (NRM = Natural Resource Management)
  These are large-scale areas which have responsibility for management of 
  water resources. See this page for more info: https://www.landscape.sa.gov.au/
- **Prescribed Wells Areas** (PWAs) - these are smaller scale areas which are
  used to manage groundwater resources via water allocation plans (WAPs) - https://location.sa.gov.au/viewer/?map=hybrid&x=142.06629&y=-31.83374&z=6&uids=156.
- **Prescribed Water Resource Areas** (PWRAs) - very similar to PWAs, but they
  are used for both groundwater and surface water resources - see https://location.sa.gov.au/viewer/?map=hybrid&x=140.33869&y=-34.35527&z=8&uids=154
- **Observation Well Networks** - these are not spatially as such, but they are
  manually maintained groupings of water monitoring wells which DEW visits
  each year to measure water level and/or salinity from, and they are grouped
  into geographical areas. You can see a list on the Groundwater Data
  website:

.. figure:: figures/obswell_networks.png

