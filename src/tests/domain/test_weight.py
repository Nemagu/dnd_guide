import pytest

from domain.exception import DomainException
from domain.weight import Weight, WeightUnit


@pytest.mark.parametrize(
    "count,weight_unit",
    [
        [1, WeightUnit.LB],
        [1, WeightUnit.KG],
    ],
)
def test_weight_ok(count, weight_unit):
    Weight(count=count, weight_unit=weight_unit)


def test_invalid_count():
    with pytest.raises(DomainException):
        Weight(count=-1, weight_unit=WeightUnit.LB)


@pytest.mark.parametrize(
    "weight_unit",
    [
        WeightUnit.LB,
        WeightUnit.KG,
    ],
)
def test_weight_unit_ok(weight_unit):
    new_weight_unit = WeightUnit.from_str(weight_unit.name.lower())
    assert weight_unit == new_weight_unit
    new_weight_unit = WeightUnit.from_str(weight_unit.name.upper())
    assert weight_unit == new_weight_unit


def test_invalid_weight_unit_name():
    with pytest.raises(DomainException):
        WeightUnit.from_str("invalid")
