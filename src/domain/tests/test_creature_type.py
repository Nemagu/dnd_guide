import pytest

from domain.creature_type import CreatureType
from domain.exception import DomainException


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
