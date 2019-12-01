Python access to groundwater data in South Australia
====================================================

sa_gwdata is a Python package to ease access to groundwater data in South Australia.
This is an unofficial project, use at your own risk/reward.

`The project's homepage is at GitHub <https://github.com/kinverarity1/python-sa-gwdata>`__.

.. toctree::
    :maxdepth: 6
    :caption: Contents:

    python
    webservices

Changelog
---------

Version 0.7.0
~~~~~~~~~~~~~

- Add ``find_wells``, ``water_levels``, ``salinities`` and `drillers_logs`` functions
- Complete documentation of JSON webservices

Version 0.6.0
~~~~~~~~~~~~~

- Add ``find_wells_in_lat_lon()`` method
- Fix ``"nan"`` bug for ``UnitNo``
- Fix correct ``pandas`` dependency requirement

Version 0.5.4
~~~~~~~~~~~~~

- Implement attribute access on ``Wells`` objects.

Version 0.5.3
~~~~~~~~~~~~~

- Add ``ObsNo.parse()`` class method  which ignores exceptions.
>>>>>>> b7b3ac7ecb3c651b27a76deef61e76841be1feca

Version 0.5.2
~~~~~~~~~~~~~
- Tweak release documentation and links

Version 0.5.1
~~~~~~~~~~~~~
- Add ``Well`` class for ID parsing
- Add ``UnitNo.hydstra`` and ``UnitNo.wilma`` attributes

Version 0.5.0
~~~~~~~~~~~~~
- Add ``parse_well_ids()`` to parse well IDs from plain text
- Add ``ObsNo`` and ``UnitNo`` classes for ID parsing

Version 0.4.1
~~~~~~~~~~~~~
- Initial
