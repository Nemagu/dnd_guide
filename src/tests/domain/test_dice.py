import pytest

from domain.dice import Dice, DiceType
from domain.exception import DomainException


@pytest.mark.parametrize(
    "count,dice_type",
    [
        [1, DiceType.D4],
        [1, DiceType.D6],
        [1, DiceType.D8],
        [1, DiceType.D10],
        [1, DiceType.D12],
        [1, DiceType.D20],
        [1, DiceType.D100],
    ],
)
def test_dice_ok(count, dice_type):
    Dice(count=count, dice_type=dice_type)


def test_invalid_count():
    with pytest.raises(DomainException):
        Dice(count=-1, dice_type=DiceType.D4)


@pytest.mark.parametrize(
    "dice_type",
    [
        DiceType.D4,
        DiceType.D6,
        DiceType.D8,
        DiceType.D10,
        DiceType.D12,
        DiceType.D20,
        DiceType.D100,
    ],
)
def test_dice_type_ok(dice_type):
    new_dice_type = DiceType.from_str(dice_type.name.lower())
    assert dice_type == new_dice_type
    new_dice_type = DiceType.from_str(dice_type.name.upper())
    assert dice_type == new_dice_type


def test_invalid_dice_type_name():
    with pytest.raises(DomainException):
        DiceType.from_str("invalid")
