sa_gwdata developer guide
=========================

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
.. autoclass:: sa_gwdata.UnitNumber
    :members:
.. autoclass:: sa_gwdata.ObsNumber
    :members:

WaterConnect web service utilities
----------------------------------

.. autoclass:: sa_gwdata.WaterConnectSession
    :members:

Any calls to :meth:`sa_gwdata.WaterConnectSession.get` return an
:class:`sa_gwdata.Response` object:

.. autoclass:: sa_gwdata.Response()
    :members:
