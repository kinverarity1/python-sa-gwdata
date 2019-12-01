sa_gwdata Python package
========================

The sa_gwdata package currently provides a helpful way to access the
WaterConnect web services (see following page) and provide data as
:class:`pandas.DataFrame` instances. Features under development will allow
easier ways to find and use well IDs across the entire interface, and other
things.

Install
~~~~~~~

You can install sa_gwdata the usual way:

.. code-block:: powershell

    > pip install -U python-sa-gwdata

This will install and/or update the Python package ``sa_gwdata``.

Usage
~~~~~

You can locate any wells by plain-text search for well identifiers:

.. code-block:: python

    >>> import sa_gwdata
    >>> wells = sa_gwdata.find_wells("ADE206 ADE207")
    >>> wells
    [<sa_gwdata.Well(259424) 6628-25427 / ADE206 / DFW T2>, 
     <sa_gwdata.Well(259425) 6628-25428 / ADE207 / DFW T1>
    ]

And then get pandas DataFrames with data in them:

.. code-block:: python

    >>> wls = sa_gwdata.water_levels(wells)
    >>> wls.info()
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 55 entries, 0 to 54
    Data columns (total 21 columns):
    DHNO               55 non-null int64
    network            55 non-null object
    Unit_Number        55 non-null int64
    Aquifer            55 non-null object
    Easting            55 non-null float64
    Northing           55 non-null float64
    Zone               55 non-null int64
    Unit_No            55 non-null object
    Obs_No             55 non-null object
    obs_date           55 non-null object
    dtw                48 non-null float64
    swl                48 non-null float64
    rswl               48 non-null float64
    pressure           8 non-null float64
    temperature        2 non-null float64
    dry_ind            0 non-null float64
    anom_ind           55 non-null object
    pump_ind           55 non-null object
    measured_during    55 non-null object
    data_source        55 non-null object
    Comments           18 non-null object
    dtypes: float64(8), int64(3), object(10)
    memory usage: 9.1+ KB

Access to WaterConnect webservices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create the Groundwater Data session wrapper:

.. code-block:: python

    >>> from sa_gwdata import WaterConnectSession
    >>> session = WaterConnectSession()

Then to access any of the web service calls:

.. code-block:: python

    >>> response = session.get("GetObswellNetworkData", params={"Network": "KAT_FP,PIKE_FP"})
    >>> len(response.df)
    190
    >>> response.df.columns
    Index(['aq_mon', 'chem', 'class', 'dhno', 'drill_date', 'lat',
       'latest_open_date', 'latest_open_depth', 'latest_sal_date',
       'latest_swl_date', 'latest_yield_date', 'litholog', 'logdrill', 'lon',
       'mapnum', 'max_depth', 'name', 'nrm', 'obsnetwork', 'obsnumber',
       'permit_no', 'purp_desc', 'pwa', 'replaceunitnum', 'sal', 'salstatus',
       'stat_desc', 'swl', 'swlstatus', 'tds', 'water', 'yield'],
      dtype='object')
    >>> response.df.obsnumber.unique()
    array(['KTR043', 'KTR023', 'KTR025', 'KTR026', 'PYP008', 'PAG003',
           'KTR065', 'LVD002', 'RMK004', 'RMK010', 'RMK006', 'RMK007',
           'KTR021', 'KTR022', 'RMK074', 'RMK080', 'RMK077', 'RMK055',
           'KTR034', 'RMK214', 'RMK215', 'RMK216', 'RMK229', 'RMK233',
           'GDN044', 'GDN055', 'GDN064', 'RMK355', 'RMK356', 'PAG069',
           'PAG070', 'PAG071', 'PAG077', 'PAG078', 'PAG079', 'PAG080',
           'PAG081', 'PAG082', 'PAG083', 'PAG084', 'PAG085', 'PAG086',
           'PAG038', 'PAG042', 'PAG043', 'PAG044', 'PAG045', 'PAG059',
           'PAG058', 'GDN186', 'RMK361', 'MTH012', 'PAG068', 'GDN128',
           'GDN132', 'GDN187', 'GDN188', 'PAG104', 'PYP055', 'RMK357',
           'RMK363', 'RMK365', 'RMK359', 'RMK362', 'RMK385', 'RMK374',
           'KTR060', 'KTR061', 'RMK368', 'GDN185', 'RMK369', 'RMK375',
           'PAG142', 'PAG162', 'PAG161', 'PAG117', 'RMK379', 'PAG130',
           'PAG129', 'PAG116', 'PAG115', 'MTH021', 'PAG089', 'PAG091',
           'PAG092', 'PAG094', 'PAG097', 'RMK370', 'RMK371', 'KTR067',
           'KTR068', 'RMK367', 'RMK347', 'RMK348', 'RMK349', 'RMK382',
           'RMK380', 'RMK381', 'PAG118', 'PAG114', 'PAG119', 'RMK354',
           'RMK384', 'RMK383', 'RMK364', 'RMK360', 'RMK366', 'KTR066',
           'RMK358', 'RMK373', 'PAG158', 'PAG155', 'PAG152', 'PAG135',
           'PAG134', 'PAG131', 'PAG143', 'PAG146', 'PAG151', 'PAG147',
           'PAG168', 'PAG165', 'RMK376', 'KTR058', 'KTR062', 'RMK372',
           'KTR064', 'KTR063', 'RMK377', 'KTR059', 'PAG139', 'PAG140',
           'PAG169', 'PAG170', 'PAG175', 'PAG153', 'PAG154', 'PAG157',
           'PAG156', 'PAG159', 'PAG160', 'PAG133', 'PAG132', 'PAG136',
           'PAG150', 'PAG149', 'PAG148', 'PAG145', 'PAG144', 'PAG122',
           'PAG174', 'PAG163', 'PAG173', 'PAG164', 'PAG166', 'PAG176',
           'PAG167', 'PAG141', 'PAG171', 'PAG138', 'PAG120', 'PAG137',
           'PAG177', 'PAG172', 'PAG123', 'PAG121', 'RMK386', 'PAG180',
           'PAG182', 'PAG181', 'PAG183', 'PAG179', 'PAG178', 'KTR071',
           'RMK388', 'RMK389', 'PAG184', 'PAG185', 'PAG186', 'PAG187',
           'PAG188', 'PAG189', 'KTR070', 'RMK392', 'KTR069', 'RMK395',
           'RMK394', 'RMK393', 'RMK390', 'RMK391'], dtype=object)

For futher information, check out the `Jupyter Notebook tutorial
<https://github.com/kinverarity1/python-sa-gwdata/blob/master/notebooks/tutorial1.ipynb>`__.

Docstrings
~~~~~~~~~~

Find wells
----------

.. autofunction:: sa_gwdata.find_wells
.. autofunction:: sa_gwdata.parse_well_ids_plaintext
.. autofunction:: sa_gwdata.find_wells_in_lat_lon

Download data
-------------

.. autofunction:: sa_gwdata.wells_summary
.. autofunction:: sa_gwdata.water_levels
.. autofunction:: sa_gwdata.salinities
.. autofunction:: sa_gwdata.water_chem
.. autofunction:: sa_gwdata.elevation_surveys
.. autofunction:: sa_gwdata.construction_events
.. autofunction:: sa_gwdata.construction_details
.. autofunction:: sa_gwdata.drillers_logs
.. autofunction:: sa_gwdata.strat_logs
.. autofunction:: sa_gwdata.hydrostrat_logs
.. autofunction:: sa_gwdata.lith_logs


Well identifiers
----------------

.. autoclass:: sa_gwdata.Well
    :members:
.. autoclass:: sa_gwdata.UnitNo
    :members:
.. autoclass:: sa_gwdata.ObsNo
    :members:

WaterConnect web service utilities
----------------------------------

.. autoclass:: sa_gwdata.WaterConnectSession
    :members:

Any calls to :meth:`sa_gwdata.WaterConnectSession.get` return an
:class:`sa_gwdata.Response` object:

.. autoclass:: sa_gwdata.Response()
    :members:
