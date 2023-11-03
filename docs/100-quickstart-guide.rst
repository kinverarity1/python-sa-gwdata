Introduction (Thirty second pitch)
==================================

The python-sa-gwdata repository hosts a Python package called ``sa_gwdata``
which provides an easy way to use code to access groundwater data in
South Australia which is otherwise available via the websites Groundwater Data
(also known as WaterConnect) and "Water Data SA".

Commonly-used data is available in bulk as pandas DataFrames, and comprehensive
data is available via the web services which run in the background on
Groundwater Data.

Comprehensive documentation is also being worked on which will eventually
provide a data dictionary, tutorials on how to find and access data,
some tutorials on how you might use the data (although that won't be
a long-term focus), and comprehensive documentation for technically-minded
users on the Python functions and underlying web services that are 
implemented here.

Requirements
~~~~~~~~~~~~~

Python >= 3.8

Required: pandas>0.24.1, requests, platformdirs, pyarrow, and pyshp - 
these are installed automatically with ``pip install python-sa-gwdata``.

Recommended but optional dependencies: shapely, contextily, geopandas. 
These are best installed with conda/mamba if you are using that: ``conda/mamba install -c conda-forge geopandas shapely contextily``

Install
~~~~~~~~~~

You can install sa_gwdata the usual way with ``pip install python-sa-gwdata``

This will install and/or update the Python package ``sa_gwdata``.

Usage
~~~~~

You can locate wells by plain-text search for well identifiers:

.. code-block:: python

    >>> import sa_gwdata
    >>> wells = sa_gwdata.find_wells("ADE206, ADE207, 7022-11315")
    >>> wells
    [Well(unit_hyphen='7022-11315'), Well(obs_no='ADE206'), Well(obs_no='ADE207')]

These :class:`sa_gwdata.Well` objects are important because they can be used to
query a variety of other functions that let you obtain data.

For example let's download water levels:

.. code-block:: python

    >>> df = sa_gwdata.water_levels(wells)
    >>> df.info()
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 75 entries, 0 to 74
    Data columns (total 21 columns):
    #   Column           Non-Null Count  Dtype
    ---  ------           --------------  -----
    0   dh_no            75 non-null     int64
    1   network          74 non-null     object
    2   unit_long        75 non-null     int64
    3   aquifer          75 non-null     object
    4   easting          75 non-null     float64
    5   northing         75 non-null     float64
    6   zone             75 non-null     int64
    7   unit_hyphen      75 non-null     object
    8   obs_no           74 non-null     object
    9   obs_date         75 non-null     datetime64[ns]
    10  dtw              68 non-null     float64
    11  swl              66 non-null     float64
    12  rswl             66 non-null     float64
    13  pressure         16 non-null     float64
    14  temperature      2 non-null      float64
    15  dry_ind          0 non-null      float64
    16  anomalous_ind    75 non-null     object
    17  pump_ind         75 non-null     object
    18  measured_during  75 non-null     object
    19  data_source      75 non-null     object
    20  comments         22 non-null     object
    dtypes: datetime64[ns](1), float64(8), int64(3), object(9)
    memory usage: 12.4+ KB
