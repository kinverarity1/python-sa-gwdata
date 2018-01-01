Water chemistry
===========================

You can request a single drillhole number (DHNO) (see search queries above for how to obtain this number).

`GetWaterChemistryDetails?DHNO=27382 <https://www.waterconnect.sa.gov.au/_layouts/15/DFW.SharePoint.WDD/WDDDMS.ashx/GetWaterChemistryDetails?DHNO=27382>`__

This returns a list of sample numbers (``SAMPLE_NO``) with metadata:

.. code-block:: json

    [
        {
            "DRILLHOLE_NO": 27382,
            "SAMPLE_NO": 86671,
            "COLLECTED_DATE": "1968-01-01",
            "TEST_PLACE_CODE": "L",
            "SAMPLE_SOURCE_CODE": "DH",
            "MEASURED_DURING": "U",
            "DATA_SOURCE_CODE": "DEWNR",
            "COMMENTS": "Loaded from Historical SAS Chem Data: Year=1968 ,Name=200 ,Sample_date_meth=JY"
        },
        {
            "DRILLHOLE_NO": 27382,
            "SAMPLE_NO": 631450,
            "COLLECTED_DATE": "2003-04-07",
            "SAMPLE_DEPTH_FROM": 19,
            "TEST_PLACE_CODE": "L",
            "SAMPLE_SOURCE_CODE": "DH",
            "EXTR_METHOD_CODE": "PUMP",
            "MEASURED_DURING": "M",
            "DATA_SOURCE_CODE": "DEWNR",
            "COMMENTS": "COULD NOT GET PUMP BELOW 19M. SAMPLED AFTER 120M PUMPING."
        },
        {
            "DRILLHOLE_NO": 27382,
            "SAMPLE_NO": 964461,
            "COLLECTED_DATE": "2005-02-11",
            "TEST_PLACE_CODE": "L",
            "SAMPLE_SOURCE_CODE": "DH",
            "EXTR_METHOD_CODE": "PUMP",
            "MEASURED_DURING": "M",
            "DATA_SOURCE_CODE": "DEWNR"
        }
    ]

The actual data can be retrieved with another request for each of these sample records:

`GetExtraWaterChemistryAllData?SAMPLE_NO=964461 <https://www.waterconnect.sa.gov.au/_layouts/15/DFW.SharePoint.WDD/WDDDMS.ashx/GetExtraWaterChemistryAllData?SAMPLE_NO=964461>`__

.. code-block:: json

    [
        {
            "CODE": "Al",
            "NAME": "Aluminium",
            "VALUE": 0.027,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "ALK",
            "NAME": "Alkanity as CaCO3",
            "VALUE": 168,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "As",
            "NAME": "Arsenic",
            "VALUE": 0.003,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "B",
            "NAME": "Boron",
            "VALUE": 0.361,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "Ca",
            "NAME": "Calcium",
            "VALUE": 86.6,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "CARB",
            "NAME": "Carbonate Hardness as CaCO3",
            "VALUE": 168,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "Cd",
            "NAME": "Cadmium",
            "VALUE": 0.0013,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "Cl",
            "NAME": "Chloride",
            "VALUE": 1310,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "Cl_tot(NaCl)",
            "NAME": "Total Chlorides as NaCl",
            "VALUE": 2160,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "CO2",
            "NAME": "Carbon Dioxide: Free Carbon Dioxide (water analysis)",
            "VALUE": 3.4,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "Cr",
            "NAME": "Chromium",
            "VALUE": 0.003,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "Cu",
            "NAME": "Copper",
            "VALUE": 0.001,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "DST",
            "NAME": "Sodium/Total Cations Ratio",
            "VALUE": 73.1,
            "UNIT": "%",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "EC",
            "NAME": "Electroconductivity",
            "VALUE": 5930,
            "UNIT": "us/cm",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "F",
            "NAME": "Fluoride",
            "VALUE": 0.51,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "Fe",
            "NAME": "Iron: Iron Total (water analysis)",
            "VALUE": 0.918,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "HARD",
            "NAME": "Total Hardness as CaCO3",
            "VALUE": 623.5,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "HARD_Ca",
            "NAME": "Calcium Hardness as CaCO3",
            "VALUE": 216,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "HARD_Mg",
            "NAME": "Magnesium Hardness as CaCO3",
            "VALUE": 407,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "HCO3",
            "NAME": "Bicarbonate",
            "VALUE": 205,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "ION",
            "NAME": "Ion Balance",
            "VALUE": 1.61,
            "UNIT": "%",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "K",
            "NAME": "Potassium",
            "VALUE": 33.4,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "LGI",
            "NAME": "Langelier Index",
            "VALUE": 0.52,
            "UNIT": "INDEX",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "Mg",
            "NAME": "Magnesium",
            "VALUE": 98.9,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "Mn",
            "NAME": "Manganese",
            "VALUE": 0.0518,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "Na",
            "NAME": "Sodium",
            "VALUE": 832,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "NH3(N)",
            "NAME": "Ammonia as N",
            "VALUE": 0.194,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "Ni",
            "NAME": "Nickel",
            "VALUE": 0.0044,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "NO2(N)",
            "NAME": "Nitrite as N",
            "VALUE": 0.005,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "NO3(N)",
            "NAME": "Nitrate as N",
            "VALUE": 0,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "NONCARB",
            "NAME": "Non-Carbonate Hardness as CaCO3",
            "VALUE": 455.5,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "NOX(N)",
            "NAME": "Nitrite and nitrate as N",
            "VALUE": 0.005,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "NOX(NO3)",
            "NAME": "Nitrite and Nitrate as NO3",
            "VALUE": 0.02,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "P",
            "NAME": "Phosphorus; Phosphorous Total (water analysis)",
            "VALUE": 0.005,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "Pb",
            "NAME": "Lead",
            "VALUE": 0.0005,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "pH",
            "NAME": "Acidity/Alkalinity",
            "VALUE": 8,
            "UNIT": "pH",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "Preact",
            "NAME": "Filtered Reactive Phosphorous",
            "VALUE": 0.005,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "SAR",
            "NAME": "Sodium Adsorption Ratio",
            "VALUE": 14.5,
            "UNIT": "RATIO",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        },
        {
            "CODE": "SiO2",
            "NAME": "Silicon Dioxide; Silica (reactive) (water analysis)",
            "VALUE": 15,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "SO4",
            "NAME": "Sulphate",
            "VALUE": 367,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "TDS_CALC",
            "NAME": "Total Dissolved Solids - Calculated",
            "VALUE": 2840,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "TDS_EC",
            "NAME": "Total Dissolved Solids - Based on EC",
            "VALUE": 3300,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "TKN(N)",
            "NAME": "Total Kjedahl Nitrogen as N",
            "VALUE": 0.26,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "S",
            "GROUP": "Standard Analysis"
        },
        {
            "CODE": "Zn",
            "NAME": "Zinc",
            "VALUE": 0.095,
            "UNIT": "mg/L",
            "WATER_ORDER_GROUP": "O",
            "GROUP": "Other Elements"
        }
    ]

.. include:: footer.rst