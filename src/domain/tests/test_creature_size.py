import pytest

from domain.creature_size import CreatureSize
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
