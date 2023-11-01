import io
import json
import logging
import time
import zipfile

import pandas as pd
import requests

from sa_gwdata.identifiers import *
from sa_gwdata.waterconnect import *


logger = logging.getLogger(__name__)


def find_wells(input_text, **kwargs):
    """Find wells and retrieve some summary information.

    Args:
        input_text (str): any well identifiers to parse. See
            :func:`sa_gwdata.parse_well_ids_plaintext` for details of
            other keyword arguments you can pass here.

    For example:

        >>> import sa_gwdata
        >>> wells = sa_gwdata.find_wells("yat99 5840-46 ULE205")
        ...
        >>> wells
        ['MLC008', 'ULE205', 'YAT099']

    """
    session = get_global_session()
    return session.find_wells(input_text, **kwargs)


def find_wells_in_lat_lon(lats, lons, **kwargs):
    """Find wells within a geographic area.

    Args:
        lats (tuple): two decimal latitudes
        lons (tuple): two decimal longitudes

    Returns: a list of :class:`sa_gwdata.Well` objects (actually
        a :class:`sa_gwdata.Wells` object which very closely
        resembles a list).

    """
    session = get_global_session()
    return session.find_wells_in_lat_lon(lats, lons, **kwargs)


def get_networks(session=None):
    """Return a list of obswell monitoring networks."""
    if session is None:
        session = get_global_session()
    return session.networks


def wells_summary(wells, session=None, **kwargs):
    """Get table of summary information for wells.

    Args:
        wells (list): list of drillhole numbers (ints)
            or :class:`sa_gwdata.Well` objects

    Returns: pandas DataFrame with these columns:

        - dh_no (int64)
        - unit_hyphen (str)
        - unit_long (int64)
        - dh_name (str)
        - network (str)
        - obs_no (str)
        - drillhole_class (str)
        - aquifer (str)
        - orig_drilled_depth (float64)
        - orig_drilled_date (datetime64[ns])
        - max_drilled_depth (float64)
        - max_drilled_date (datetime64[ns])
        - latest_open_depth (float64)
        - latest_open_date (datetime64[ns])
        - latest_permit_no (float64)
        - cased_to (float64)
        - casing_min_diam (float64)
        - purpose (str)
        - latest_status (str)
        - latest_status_date (datetime64[ns])
        - latest_dtw (float64)
        - latest_swl (float64)
        - latest_rswl (float64)
        - latest_wl_date (datetime64[ns])
        - latest_tds (float64)
        - latest_ec (float64)
        - latest_sal_date (datetime64[ns])
        - latest_ph (float64)
        - latest_ph_date (datetime64[ns])
        - latest_yield (float64)
        - latest_yield_date (datetime64[ns])
        - easting (float64)
        - northing (float64)
        - zone (int64)
        - lon_deg (int64)
        - lon_min (int64)
        - lon_sec (float64)
        - lat_deg (int64)
        - lat_min (int64)
        - lat_sec (float64)
        - longitude (float64)
        - latitude_positive (float64)
        - latitude (float64)
        - hundred (str)
        - plan (str)
        - parcel (str)
        - cert_title (str)
        - map_250k (str)
        - map_100k (int64)
        - map_50k (int64)
        - map_10k (int64)
        - map_2_5k (str)
        - map_1k (int64)
        - water_info_exists (str)
        - salinity_exists (str)
        - water_chem_exists (str)
        - geophys_log_exists (str)
        - drillers_log_exists (str)
        - lith_log_exists (str)

    """
    session = get_global_session()
    return session.bulk_wells_summary(wells, **kwargs)


def water_levels(wells, pumping=False, anomalous=True, session=None, **kwargs):
    """Get table of water level measurements for wells.

    Args:
        wells (list): list of drillhole numbers (ints)
            or :class:`sa_gwdata.Well` objects
        pumping (bool): include measurements flagged as "well being subject
            to the influence of local pumping" - default False
        anomalous (bool): include measurements flagged as being anomalous
            default True, as this can be subjective.

    Returns: pandas DataFrame with these columns:

        - dh_no (int64)
        - network (str)
        - unit_long (int64)
        - aquifer (str)
        - easting (float64)
        - northing (float64)
        - zone (int64)
        - unit_hyphen (str)
        - obs_no (str)
        - obs_date (datetime64[ns])
        - dtw (float64)
        - swl (float64)
        - rswl (float64)
        - pressure (float64)
        - temperature (float64)
        - dry_ind (str)
        - anomalous_ind (str)
        - pump_ind (str)
        - measured_during (str)
        - data_source (str)
        - comments (str)

    """
    session = get_global_session()
    return session.bulk_water_levels(
        wells, pumping=pumping, anomalous=anomalous, **kwargs
    )


def salinities(wells, session=None, **kwargs):
    """Get table of salinity samples for wells.

    Args:
        wells (list): list of drillhole numbers (ints)
            or :class:`sa_gwdata.Well` objects

    Returns: pandas DataFrame with these columns:

        - dh_no (int64)
        - network (str)
        - aquifer (str)
        - unit_hyphen (str)
        - unit_long (int64)
        - obs_no (str)
        - collected_date (datetime64[ns])
        - collected_time (str)
        - tds (int64)
        - ec (int64)
        - ph (float64)
        - sample_type (str)
        - anomalous_ind (str)
        - test_place (str)
        - extract_method (str)
        - measured_during (str)
        - data_source (str)
        - easting (float64)
        - northing (float64)
        - zone (int64)

    """
    if session is None:
        session = get_global_session()
    return session.bulk_salinities(wells, **kwargs)


def water_chem(wells, session=None, **kwargs):
    """Get table of water chemistry sample analyses for wells.

    Args:
        wells (list): list of drillhole numbers (ints)
            or :class:`sa_gwdata.Well` objects

    Returns: pandas DataFrame with these columns:

        - dh_no (int64)
        - unit_hyphen (str)
        - obs_no (str)
        - sample_no (int64)
        - collected_date (datetime64[ns])
        - analysis_code (str)
        - analysis_name (str)
        - value (float64)
        - unit (str)

    """
    if session is None:
        session = get_global_session()
    return session.bulk_water_chem(wells, **kwargs)


def elevation_surveys(wells, session=None, **kwargs):
    """Get table of elevation surveys for wells.

    Args:
        wells (list): list of drillhole numbers (ints)
            or :class:`sa_gwdata.Well` objects

    Returns: pandas DataFrame with these columns:

        - dh_no (int64)
        - unit_hyphen (str)
        - obs_no (str)
        - network (str)
        - elev_date (datetime64[ns])
        - ground_elev (float64)
        - ref_elev (float64)
        - survey_meth (str)
        - vert_accuracy (float64)
        - ref_point_type (str)
        - applied_date (datetime64[ns])
        - comments (str)

    """
    if session is None:
        session = get_global_session()
    return session.bulk_elevation_surveys(wells, **kwargs)


def construction_events(wells, session=None, **kwargs):
    """Get table of construction events (summary data) for wells.

    Args:
        wells (list): list of drillhole numbers (ints)
            or :class:`sa_gwdata.Well` objects

    Returns: pandas DataFrame with these columns:

        - dh_no (int64)
        - unit_hyphen (str)
        - obs_no (str)
        - completion_date (datetime64[ns])
        - total_depth (float64)
        - final_depth (float64)
        - current_depth (float64)
        - permit_no (float64)
        - backfilled (str)
        - casing_from (float64)
        - casing_to (float64)
        - casing_min_diam (float64)
        - casing_material (str)
        - pcemented (str)
        - pcement_from (float64)
        - pcement_to (float64)
        - pzone_from (float64)
        - pzone_to (float64)
        - pzone_min_diam (float64)
        - pzone_type (str)
        - pzone_material (str)
        - pzone_aperture (float64)
        - drill_from (float64)
        - drill_to (float64)
        - drill_diam (float64)
        - drill_method (str)
        - development_method (str)
        - development_duration (float64)
        - comments (str)

    """
    if session is None:
        session = get_global_session()
    return session.bulk_construction_events(wells, **kwargs)


def construction_details(wells, session=None, **kwargs):
    """Get table of detailed information collected at time of construction of wells.

    Args:
        wells (list): list of drillhole numbers (ints)
            or :class:`sa_gwdata.Well` objects

    Returns: dict with four pandas DataFrames. The keys, and the
        columns of the DataFrames are below:

        * "water_cuts":
            - dh_no (int64)
            - unit_hyphen (str)
            - water_cut_date (datetime64[ns])
            - depth_from (float64)
            - depth_to (float64)
            - swl (float64)
            - yield (float64)
            - test_method (str)
            - tds (float64)
            - ec (float64)
            - sample_type (str)

        * "drilling":
            - dh_no (int64)
            - unit_hyphen (str)
            - depth_from (float64)
            - depth_to (float64)
            - hole_diam (float64)
            - drill_method (str)
            - comments (str)

        * "casing":
            - dh_no (int64)
            - unit_hyphen (str)
            - depth_from (float64)
            - depth_to (float64)
            - casing_diam (int64)
            - casing_material (str)
            - cement_method (str)
            - cement_from (float64)
            - cement_to (float64)
            - comments (str)

        * "prod_zones":
            - dh_no (int64)
            - unit_hyphen (str)
            - pzone_type (str)
            - depth_from (float64)
            - depth_to (float64)
            - pzone_diam (float64)
            - pzone_material (str)
            - pzone_aperture (float64)
            - comments (str)


    """
    if session is None:
        session = get_global_session()
    return session.bulk_construction_details(wells, **kwargs)


def drillers_logs(wells, session=None, **kwargs):
    """Get table of lithological intervals from drillers logs for wells.

    Args:
        wells (list): list of drillhole numbers (ints)
            or :class:`sa_gwdata.Well` objects

    Returns: pandas DataFrame with these columns:

        - dh_no (int64)
        - unit_hyphen (str)
        - obs_no (str)
        - log_date (datetime64[ns])
        - logger_name (str)
        - depth_from (float64)
        - depth_to (float64)
        - lith_code (str)
        - description (str)

    """
    if session is None:
        session = get_global_session()
    return session.bulk_drillers_logs(wells, **kwargs)


def strat_logs(wells, session=None, **kwargs):
    """Get table of formations from the stratigraphic logs for wells.

    Args:
        wells (list): list of drillhole numbers (ints)
            or :class:`sa_gwdata.Well` objects

    Returns: pandas DataFrame with these columns:

        - dh_no (int64)
        - unit_hyphen (str)
        - depth_from (float64)
        - depth_to (float64)
        - strat_name (str)
        - gis_code (str)

    """
    if session is None:
        session = get_global_session()
    return session.bulk_strat_logs(wells, **kwargs)


def hydrostrat_logs(wells, session=None, **kwargs):
    """Get table of formations from the hydrostratigraphic logs for wells.

    Args:
        wells (list): list of drillhole numbers (ints)
            or :class:`sa_gwdata.Well` objects

    Returns: pandas DataFrame with these columns:

        - dh_no (int64)
        - unit_hyphen (str)
        - unit_depth_from (float64)
        - unit_depth_to (float64)
        - subunit_depth_from (float64)
        - subunit_depth_to (float64)
        - hydro_type (float64)
        - hydro_depth_to_greater_flag (str)
        - comments (str)
        - map_symbol (str)
        - strat_name (str)
        - subunit_comments (float64)
        - subunit_code (float64)
        - subunit_desc (float64)

    """
    if session is None:
        session = get_global_session()
    return session.bulk_hydrostrat_logs(wells, **kwargs)


def lith_logs(wells, session=None, **kwargs):
    """Get table of lithological logs for wells.

    Args:
        wells (list): list of drillhole numbers (ints)
            or :class:`sa_gwdata.Well` objects

    Returns:
        pandas DataFrame with these columns:

        - dh_no (int64)
        - unit_hyphen (str)
        - obs_no (str)
        - depth_from (float64)
        - depth_to (float64)
        - major_lith_code (str)
        - minor_lith_code (str)
        - descr (str)

    """
    if session is None:
        session = get_global_session()
    return session.bulk_lith_logs(wells, **kwargs)


def search_by_suburb(suburb, session=None, **kwargs):
    """Find wells by suburb name.

    Args:
        suburb (str): case-insensitive suburb name

    Returns:
        pandas DataFrame with these columns:

        - xxx

    """
    suburb = suburb.upper()
    if session is None:
        session = get_global_session()
    return session.search_by_suburb(suburb, **kwargs).gdf()


def search_by_radius(lat, lon, radius, session=None, **kwargs):
    """Find wells by radius around a geographic point.

    Args:
        lat (float): latitude of search point
        longitude (float): longitude of search point
        radius (float): search radius in kilometres

    Returns:
        pandas DataFrame with these columns:

        - xxx

    """
    lat = float(lat)
    lon = float(lon)
    radius = float(radius)
    assert lat < 0
    assert lon > 130
    assert lon < 160
    assert lat > -50
    if session is None:
        session = get_global_session()
    return session.search_by_radius(lat, lon, radius, **kwargs).gdf()


def search_by_rect(sw_corner, ne_corner, session=None, **kwargs):
    """Find wells within a rectangle.

    Args:
        sw_corner (sequence length 2): the latitude and longitude of the
            south-western corner of the rectangle (i.e. minimum latitude
            and minimum longitude)
        ne_corner (sequence length 2): the latitude and longitude of the
            north-eastern corner of the rectangle (i.e. maximum latitude
            and maximum longitude)

    Returns:
        pandas DataFrame with these columns:

        - xxx

    """
    if session is None:
        session = get_global_session()
    return session.search_by_rect(sw_corner, ne_corner, **kwargs).gdf()


def search_by_network(*network_codes, session=None, **kwargs):
    """Find wells within observation well networks (one or more network).

    Args:
        network_codes (str): network codes e.g. KAT_FP, NAP, STHNBASINS, LLC_STH

    Returns:
        pandas DataFrame with these columns:

        - xxx

    Example:

    .. code-block:: python

        >>> import sa_gwdata
        >>> wells = sa_gwdata.search_by_network("WMLR", "MCL_VALE")

    """
    if session is None:
        session = get_global_session()
    return session.search_by_network(*network_codes, **kwargs).gdf()
