from uuid import UUID, uuid4

import pytest

from domain.dice import Dice, DiceType
from domain.exception import DomainException
from domain.length import Length, LengthUnit
from domain.weapon_property import WeaponProperty, WeaponPropertyName

PROPERTY_ID = uuid4()
NAME = WeaponPropertyName.AMMUNITION
DESCRIPTION = "valid_description"
BASE_RANGE = Length(10, LengthUnit.FT)
MAX_RANGE = Length(20, LengthUnit.FT)
SECOND_HAND_DICE = None


def generate_property(
    property_id: UUID = PROPERTY_ID,
    name: WeaponPropertyName = NAME,
    description: str = DESCRIPTION,
    base_range: Length | None = BASE_RANGE,
    max_range: Length | None = MAX_RANGE,
    second_hand_dice: Dice | None = SECOND_HAND_DICE,
) -> WeaponProperty:
    return WeaponProperty(
        property_id=property_id,
        name=name,
        description=description,
        base_range=base_range,
        max_range=max_range,
        second_hand_dice=second_hand_dice,
    )


@pytest.mark.parametrize(
    "data",
    [
        {
            "name": NAME,
            "base_range": BASE_RANGE,
            "max_range": MAX_RANGE,
            "second_hand_dice": SECOND_HAND_DICE,
        },
        {
            "name": WeaponPropertyName.HEAVY,
            "base_range": None,
            "max_range": None,
            "second_hand_dice": None,
        },
        {
            "name": WeaponPropertyName.VERSATILE,
            "base_range": None,
            "max_range": None,
            "second_hand_dice": Dice(count=1, dice_type=DiceType.D4),
        },
    ],
)
def test_create_ok(data: dict):
    weapon_property = generate_property(**data)
    assert weapon_property.property_id == data.get("property_id", PROPERTY_ID)
    assert weapon_property.name == data.get("name", NAME)
    assert weapon_property.description == data.get("description", DESCRIPTION)
    assert weapon_property.base_range == data.get("base_range", BASE_RANGE)
    assert weapon_property.max_range == data.get("max_range", MAX_RANGE)
    assert weapon_property.second_hand_dice == data.get(
        "second_hand_dice", SECOND_HAND_DICE
    )


@pytest.mark.parametrize(
    "data",
    [
        {"description": ""},
        {
            "base_range": MAX_RANGE,
            "max_range": BASE_RANGE,
        },
        {
            "name": NAME,
            "base_range": BASE_RANGE,
            "max_range": MAX_RANGE,
            "second_hand_dice": Dice(count=1, dice_type=DiceType.D4),
        },
        {"name": NAME, "base_range": None},
        {"name": NAME, "max_range": None},
        {
            "name": WeaponPropertyName.VERSATILE,
            "base_range": None,
            "max_range": None,
            "second_hand_dice": None,
        },
        {
            "name": WeaponPropertyName.VERSATILE,
            "base_range": BASE_RANGE,
            "max_range": None,
            "second_hand_dice": None,
        },
        {
            "name": WeaponPropertyName.VERSATILE,
            "base_range": None,
            "max_range": MAX_RANGE,
            "second_hand_dice": None,
        },
        {"name": WeaponPropertyName.HEAVY, "base_range": BASE_RANGE},
        {"name": WeaponPropertyName.HEAVY, "max_range": MAX_RANGE},
        {
            "name": WeaponPropertyName.HEAVY,
            "second_hand_dice": Dice(count=1, dice_type=DiceType.D4),
        },
    ],
    ids=[
        "empty_description",
        "max_range_greater_than_base_range",
        "ammunition_with_second_hand_dice",
        "ammunition_without_base_range",
        "ammunition_without_max_range",
        "versatile_without_second_hand_dice",
        "versatile_with_base_range",
        "versatile_with_max_range",
        "heavy_with_base_range",
        "heavy_with_max_range",
        "heavy_with_second_hand_dice",
    ],
)
def test_create_invalid_data(data: dict):
    with pytest.raises(DomainException):
        generate_property(**data)


@pytest.mark.parametrize(
    "created_data,updated_data",
    [
        [
            {
                "name": WeaponPropertyName.HEAVY,
                "base_range": None,
                "max_range": None,
                "second_hand_dice": None,
            },
            {"name": WeaponPropertyName.SPECIAL},
        ],
        [
            dict(),
            {
                "name": WeaponPropertyName.VERSATILE,
                "base_range": None,
                "max_range": None,
                "second_hand_dice": Dice(count=1, dice_type=DiceType.D4),
            },
        ],
        [
            {
                "name": WeaponPropertyName.VERSATILE,
                "base_range": None,
                "max_range": None,
                "second_hand_dice": Dice(count=1, dice_type=DiceType.D4),
            },
            {
                "name": WeaponPropertyName.AMMUNITION,
                "base_range": BASE_RANGE,
                "max_range": MAX_RANGE,
                "second_hand_dice": None,
            },
        ],
    ],
)
def test_new_name_ok(created_data: dict, updated_data: dict):
    weapon_property = generate_property(**created_data)
    weapon_property.new_name(**updated_data)
    assert weapon_property.name == updated_data["name"]


@pytest.mark.parametrize(
    "created_data,updated_data",
    [
        [
            {
                "name": WeaponPropertyName.HEAVY,
                "base_range": None,
                "max_range": None,
                "second_hand_dice": None,
            },
            {"name": WeaponPropertyName.HEAVY},
        ],
        [
            {
                "name": WeaponPropertyName.HEAVY,
                "base_range": None,
                "max_range": None,
                "second_hand_dice": None,
            },
            {"name": WeaponPropertyName.VERSATILE},
        ],
        [
            dict(),
            {
                "name": WeaponPropertyName.VERSATILE,
                "base_range": BASE_RANGE,
            },
        ],
        [
            {
                "name": WeaponPropertyName.VERSATILE,
                "base_range": None,
                "max_range": None,
                "second_hand_dice": Dice(count=1, dice_type=DiceType.D4),
            },
            {
                "name": WeaponPropertyName.AMMUNITION,
                "base_range": BASE_RANGE,
            },
        ],
    ],
)
def test_new_name_invalid_data(created_data: dict, updated_data: dict):
    weapon_property = generate_property(**created_data)
    with pytest.raises(DomainException):
        weapon_property.new_name(**updated_data)


def test_new_base_range_ok():
    weapon_property = generate_property()
    new_base_range = Length(BASE_RANGE.count - 1, LengthUnit.FT)
    weapon_property.new_base_range(new_base_range)
    assert weapon_property.base_range == new_base_range


@pytest.mark.parametrize(
    "new_base_range",
    [BASE_RANGE, Length(MAX_RANGE.count + 1, LengthUnit.FT)],
    ids=["same_range", "range_greater_than_max_range"],
)
def test_new_base_range_invalid_data(new_base_range: Length):
    weapon_property = generate_property()
    with pytest.raises(DomainException):
        weapon_property.new_base_range(new_base_range)


def test_new_max_range_ok():
    weapon_property = generate_property()
    new_max_range = Length(MAX_RANGE.count + 1, LengthUnit.FT)
    weapon_property.new_max_range(new_max_range)
    assert weapon_property.max_range == new_max_range


@pytest.mark.parametrize(
    "new_max_range",
    [MAX_RANGE, Length(BASE_RANGE.count - 1, LengthUnit.FT)],
    ids=["same_range", "range_less_than_base_range"],
)
def test_new_max_range_invalid_data(new_max_range: Length):
    weapon_property = generate_property()
    with pytest.raises(DomainException):
        weapon_property.new_max_range(new_max_range)


def test_new_second_hand_dice_ok():
    weapon_property = generate_property(
        name=WeaponPropertyName.VERSATILE,
        base_range=None,
        max_range=None,
        second_hand_dice=Dice(count=1, dice_type=DiceType.D4),
    )
    new_second_hand_dice = Dice(count=2, dice_type=DiceType.D6)
    weapon_property.new_second_hand_dice(new_second_hand_dice)
    assert weapon_property.second_hand_dice == new_second_hand_dice


@pytest.mark.parametrize(
    "created_data, new_dice",
    [
        [
            {
                "name": WeaponPropertyName.VERSATILE,
                "base_range": None,
                "max_range": None,
                "second_hand_dice": Dice(count=1, dice_type=DiceType.D4),
            },
            Dice(count=1, dice_type=DiceType.D4),
        ],
        [dict(), Dice(count=2, dice_type=DiceType.D6)],
    ],
    ids=["same_dice", "invalid_property_name"],
)
def test_new_second_hand_dice_invalid_data(created_data: dict, new_dice: Dice):
    weapon_property = generate_property(**created_data)
    with pytest.raises(DomainException):
        weapon_property.new_second_hand_dice(new_dice)
