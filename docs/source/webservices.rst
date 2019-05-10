WaterConnect web services
~~~~~~~~~~~~~~~~~~~~~~~~~

The `Groundwater Data <https://www.waterconnect.sa.gov.au/Systems/GD/Pages/Default.aspx>`__ section of the WaterConnect website uses a number of straightforward GET calls to obtain groundwater data in JSON format.

The links below detail a variety of GET request URLs and examples of the returned JSON responses.

(The documentation is a work in progress; help would be welcome!)

Searching for wells
===================

Searching by well identifiers
------------------------------------------------------------

These services all take a comma-delimited list and return a list of drillhole numbers (DHNO), together with some summary information:

.. toctree::
    :maxdepth: 5

    GetUnitNumberSearchData
    GetObswellNumberSearchData
    GetPermitNumberSearchData
    
Spatial searches
----------------

These also return a list of drillhole numbers, sometimes with other keys -- check the examples for the exact format.

There are geometric queries:

.. toctree::
    :maxdepth: 5

    GetGridData
    GetCircleData

You can search by general-purpose geographic information:

.. toctree::
    :maxdepth: 5

    GetSuburbFromName
    GetLGAFromName
    GetNRMRegionSearchData
    GetHundredParcelData

Or more groundwater-specific areas:

.. toctree::
    :maxdepth: 5

    GetObswellNetworkData
    GetPWASearchData
    GetPWRASearchData

Lists of valid query values for many of these can be obtained through the metadata requests shown in the :ref:`webservice-metadata` section below.

Data from a drillhole
=======================

Most groundwater information is obtained through these queries. All these requests are for a single drillhole at a time; see the pages for more details.

.. toctree::
    :maxdepth: 5

    GetSummaryDetails
    GetWaterLevelDetails
    GetSalinityDetails
    GetWellYieldDetails
    GetWaterChemistryDetails
    GetElevationDetails

- GetConstructionInformation - returns COMPLETION_NOs
- GetElevationDetails - returns ELEVATION_NOs
- GetDrillersLogInformation - returns LOG_NOs
- GetLithologicalLogInformation
- GetHydrostratInformation - returns HYDRO_INT_NOs
- GetStratigraphicLogsDetails

Query with COMPLETION_NO:

- GetProductionZoneSummary
- GetConstructionSummaryInformation
- GetCasingSummary
- GetDrillingSummary
- GetConstructionWaterCut
- GetExtraSummaryDetails

Query with LOG_NO:

- GetDrillersLogSummary

Query with HIN (equivalent to HYDRO_INT_NO):

- GetExtraHydrostratInformation

.. _webservice-metadata:

Metadata 
========

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
                "T": "Biological / Bacteria"
            },
            {
                "V": "S",
                "T": "Standard Analysis"
            }
        ]
    }

.. include:: footer.rst