import pytest

from domain.exception import DomainException
from domain.length import Length, LengthUnit


@pytest.mark.parametrize(
    "count,length_unit",
    [
        [1, LengthUnit.FT],
        [1, LengthUnit.M],
    ],
)
def test_length_ok(count, length_unit):
    Length(count=count, length_unit=length_unit)


def test_invalid_count():
    with pytest.raises(DomainException):
        Length(count=-1, length_unit=LengthUnit.FT)


@pytest.mark.parametrize(
    "length_unit",
    [
        LengthUnit.FT,
        LengthUnit.M,
    ],
)
def test_length_unit_ok(length_unit):
    new_length_unit = LengthUnit.from_str(length_unit.name.lower())
    assert length_unit == new_length_unit
    new_length_unit = LengthUnit.from_str(length_unit.name.upper())
    assert length_unit == new_length_unit


def test_invalid_length_unit_name():
    with pytest.raises(DomainException):
        LengthUnit.from_str("invalid")
