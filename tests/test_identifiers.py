import os, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pytest

from sa_gwdata.identifiers import ObsNo, UnitNo


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

