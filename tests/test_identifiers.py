import os, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pytest

from sa_gwdata.identifiers import ObsNo, UnitNo, Well


def test_accept_empty_unit_no():
    UnitNo()


def test_accept_empty_obs_no():
    ObsNo()


def test_dodgy_unit_no():
    with pytest.raises(ValueError):
        UnitNo("yat", 124)


def test_dodgy_unit_no_1():
    with pytest.raises(ValueError):
        UnitNo(615)


def test_dodgy_obs_no():
    with pytest.raises(ValueError):
        ObsNo(6628, 142)


def test_dodgy_obs_no_2():
    with pytest.raises(TypeError):
        ObsNo(662800142)


def test_dodgy_obs_no_3():
    with pytest.raises(ValueError):
        ObsNo("662800142")


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("YAT17", "YAT017"),
        ("yat17", "YAT017"),
        ("yat 17", "YAT017"),
        ("noa2", "NOA002"),
        ("noa 002", "NOA002"),
        (("noa", 2), "NOA002"),
    ],
)
def test_obs_no_parsing(test_input, expected):
    assert ObsNo(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("662800123", "6628-123"),
        ("6628-00123", "6628-123"),
        ("6628-123", "6628-123"),
        ("G662800123", "6628-123"),
        (("6628", "00123"), "6628-123"),
        ((6628, 123), "6628-123"),
        (662800123, "6628-123"),
    ],
)
def test_unit_no_parsing(test_input, expected):
    assert UnitNo(test_input) == expected


@pytest.mark.parametrize(
    "attr_name,expected_value",
    [("hyphen", ""), ("long", ""), ("long_int", None), ("wilma", ""), ("hydstra", "")],
)
def test_empty_unit_no(attr_name, expected_value):
    assert (
        getattr(UnitNo(), attr_name) == expected_value
    )  # against PEP8 for None but should work


@pytest.mark.parametrize("attr_name,expected_value", [("id", ""), ("egis", "")])
def test_empty_obs_no(attr_name, expected_value):
    assert (
        getattr(ObsNo(), attr_name) == expected_value
    )  # against PEP8 for None but should work


def test_unit_no_long_int():
    unit_no = UnitNo("6628-123")
    assert unit_no.long_int == 662800123


def test_unit_no_iter():
    unit_no = UnitNo("6628-123")
    assert [x for x in unit_no] == [6628, 123]


def test_obs_no_iter():
    obs_no = ObsNo("NOA-2")
    assert [x for x in obs_no] == ["NOA", 2]


def test_well_missing_dh_no():
    with pytest.raises(TypeError):
        well = Well()


def test_well_dh_no():
    well = Well(28255)


@pytest.mark.parametrize(
    "attr_name,expected_value", [("id", "28255"), ("title", "[dh_no=28255]")]
)
def test_well_dh_no_missing_attrs(attr_name, expected_value):
    well = Well(28255)
    assert getattr(well, attr_name) == expected_value


@pytest.mark.parametrize(
    "attr_name,expected_value", [("id", "YAT124"), ("title", "6528-1127 / YAT124")]
)
def test_well_manual(attr_name, expected_value):
    well = Well(28255, unit_no="6528-1127", obs_no="YAT124")
    assert getattr(well, attr_name) == expected_value


def test_well_repr():
    well = Well(28255, unit_no="6528-1127", obs_no="YAT124")
    assert str(well) == "'YAT124'"


def test_well_path_safe_repr():
    well = Well(28255, unit_no="6528-1127", obs_no="YAT124")
    assert well.path_safe_repr() == "'YAT124'"


def test_well_path_safe_repr_keep_prefix():
    well = Well(28255, unit_no="6528-1127", obs_no="YAT124")
    assert (
        well.path_safe_repr(remove_prefix=False)
        == "'YAT124'"
    )


def test_well_name():
    well = Well(207050, unit_no="6627-11246", name="OVAL BORE")
    assert well.name == "OVAL BORE"


def test_well_name_in_title():
    well = Well(207050, unit_no="6627-11246", name="OVAL BORE")
    assert well.title == "6627-11246 / OVAL BORE"


def test_well_unit_no_id():
    well = Well(203536, unit_no="6627-11249")
    assert well.id == "6627-11249"


def test_well_hash():
    well = Well(203536, unit_no="6627-11249")
    assert {well: "value"}[well] == "value"


def test_unit_no_hash():
    unit_no = UnitNo("6628-1527")
    assert {unit_no: "value"}[unit_no] == "value"


def test_obs_no_hash():
    obs_no = ObsNo("NOA 2")
    assert {obs_no: "value"}[obs_no] == "value"


def test_well_equality():
    well1 = Well(203536, unit_no="6627-11249")
    well2 = Well(203536)
    assert well1 == well2


def test_well_equality_2():
    well1 = Well(203536, unit_no="6627-11249")
    well2 = Well(203537)
    assert well1 != well2


def test_well_one_is_not_like_another():
    well1 = Well(203536, unit_no="6627-11249")
    dh_no = 203536
    assert well1 != dh_no


def test_well_bool():
    well = Well(203536, unit_no="6627-11249")
    assert well

def test_well_with_property_kwarg():
    well = Well(203536, unit_no=662711249, unit_hyphen="6627-11249")