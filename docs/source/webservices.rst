WaterConnect web services
=========================

Most of the data that can be accessed through this package comes from HTTP requests to some web services
on the `Groundwater Data <https://www.waterconnect.sa.gov.au/Systems/GD/Pages/Default.aspx>`__ section of the WaterConnect website, which return JSON. Although you do not need to understand these requests to use the sa_gwdata
package, I have included some details of the requests below so you can understand exactly where the data is coming
from, and as a resource for building and expanding the sa_gwdata package (and perhaps others).

Not all of the JSON calls have been documented yet. In particular, the bulk download calls are not listed
below.

.. contents:: :local:

Searching for wells
~~~~~~~~~~~~~~~~~~~

By unit/observation well/permit number
--------------------------------------

These services all take a comma-delimited list and return a list of drillhole numbers (DHNO), together with some summary information:

.. include:: GetUnitNumberSearchData.rst
.. include:: GetObswellNumberSearchData.rst
.. include:: GetPermitNumberSearchData.rst

Spatially (by rectangle or circle)
----------------------------------

These also return a list of drillhole numbers, sometimes with other keys -- check the examples for the exact format.

There are geometric queries:

.. include:: GetGridData.rst
.. include:: GetCircleData.rst

Spatially (by suburb, council, NRM, or hundred)
-----------------------------------------------

You can search by general-purpose geographic information:

.. include:: GetSuburbFromName.rst
.. include:: GetLGAFromName.rst
.. include:: GetNRMRegionSearchData.rst
.. include:: GetHundredParcelData.rst

Spatially (by observation network, PWA, or PWRA)
------------------------------------------------

Or more groundwater-specific areas:

.. include:: GetObswellNetworkData.rst
.. include:: GetPWASearchData.rst
.. include:: GetPWRASearchData.rst

Lists of valid query values for many of these can be obtained through the metadata requests shown in the :ref:`webservice-metadata` section below.

Data for a single well
~~~~~~~~~~~~~~~~~~~~~~

Most groundwater information is obtained through these queries. All these requests are for a single drillhole at a time; see the pages for more details.

Query by drillhole number
-------------------------

.. include:: GetSummaryDetails.rst
.. include:: GetWaterLevelDetails.rst
.. include:: GetSalinityDetails.rst
.. include:: GetWellYieldDetails.rst
.. include:: GetWaterChemistryDetails.rst
.. include:: GetElevationDetails.rst
.. include:: GetLithologicalLogInformation.rst
.. include:: GetStratigraphicLogsDetails.rst
.. include:: GetDrillersLogInformation.rst
.. include:: GetHydrostratInformation.rst
.. include:: GetConstructionInformation.rst

.. _webservice-metadata:

Metadata - GetAdvancedListsData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lists of names and codes to be used in requests can be obtained through the `GetAdvancedListsData <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetAdvancedListsData>`__ GET request. The sample below shows only the first and last entries in each list. Follow the link for all the data.

.. code-block:: json

    {
      "LGA": [
        {
          "V": "ADELAIDE"
        },
        {
          "V": "YORKE PENINSULA"
        }
      ],
      "Purpose": [
        {
          "V": "APN",
          "T": "Anode Protection"
        },
        {
          "V": "HOL",
          "T": "Water Hole"
        }
      ],
      "Status": [
        {
          "V": "ABD",
          "T": "Abandoned"
        },
        {
          "V": "UNW",
          "T": "Unworked"
        }
      ],
      "Aquifer": [
        {
          "V": "A",
          "T": "A: Unnamed GIS Unit"
        },
        {
          "V": "Tyw",
          "T": "Tyw: Winnambool Formation"
        }
      ],
      "PrescribedArea": [
        {
          "V": "Angas-Bremer",
          "G": "South Australian Murray Darling Basin"
        },
        {
          "V": "Tintinara-Coonalpyn",
          "G": "South East"
        }
      ],
      "PrescribedWRArea": [
        {
          "V": "Baroota"
        },
        {
          "V": "Western Mount Lofty Ranges"
        }
      ],
      "NRMRegion": [
        {
          "V": "Adelaide & Mt Lofty Ranges",
          "T": "Adelaide & Mt Lofty Ranges"
        },
        {
          "V": "South East",
          "T": "South East"
        }
      ],
      "Networks": [
        {
          "V": "AW_NP",
          "T": "Alinytjara Wilurara Non-Prescribed Area"
        },
        {
          "V": "WMLR",
          "T": "Western Mount Lofty Ranges PWRA"
        }
      ],
      "Suburb": [
        {
          "V": "ABERFOYLE PARK"
        },
        {
          "V": "ZADOWS LANDING"
        }
      ],
      "Chem_Name": [
        {
          "V": "2_4_5_T",
          "T": "2,4,5 - T: 2_4_5_T",
          "G": "P"
        },
        {
          "V": "ZrO2",
          "T": "Zirconium oxide: ZrO2",
          "G": ""
        }
      ],
      "Analyte_Group": [
        {
          "V": "B",
          "T": "Biological \/ Bacteria"
        },
        {
          "V": "S",
          "T": "Standard Analysis"
        }
      ]
    }


.. include:: footer.rst