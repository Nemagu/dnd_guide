import pytest

from domain.creature import CreatureSize, CreatureType
from domain.exception import DomainException


@pytest.mark.parametrize(
    "creature_size",
    [
        CreatureSize.TINY,
        CreatureSize.SMALL,
        CreatureSize.MEDIUM,
        CreatureSize.LARGE,
        CreatureSize.HUGE,
        CreatureSize.GARGANTUAN,
    ],
)
def test_creature_size_ok(creature_size):
    new_creature_size = CreatureSize.from_str(creature_size.name.lower())
    assert creature_size == new_creature_size
    new_creature_size = CreatureSize.from_str(creature_size.name.upper())
    assert creature_size == new_creature_size


def test_invalid_creature_size_name():
    with pytest.raises(DomainException):
        CreatureSize.from_str("invalid")


@pytest.mark.parametrize(
    "creature_type",
    [
        CreatureType.ABERRATION,
        CreatureType.BEAST,
        CreatureType.CELESTIAL,
        CreatureType.CONSTRUCT,
        CreatureType.DRAGON,
        CreatureType.ELEMENTAL,
        CreatureType.FEY,
        CreatureType.FIEND,
        CreatureType.GIANT,
        CreatureType.HUMANOID,
        CreatureType.MONSTROSITY,
        CreatureType.OOZE,
        CreatureType.PLANT,
        CreatureType.UNDEAD,
        CreatureType.TRANSPORT,
    ],
)
def test_creature_type_ok(creature_type):
    new_creature_type = CreatureType.from_str(creature_type.name.lower())
    assert creature_type == new_creature_type
    new_creature_type = CreatureType.from_str(creature_type.name.upper())
    assert creature_type == new_creature_type


def test_invalid_creature_type_name():
    with pytest.raises(DomainException):
        CreatureType.from_str("invalid")
