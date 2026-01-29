import pytest

from domain.damage_type import DamageType
from domain.exception import DomainException


@pytest.mark.parametrize(
    "damage_type",
    [
        DamageType.ACID,
        DamageType.BLUDGEONING,
        DamageType.COLD,
        DamageType.FIRE,
        DamageType.FORCE,
        DamageType.LIGHTNING,
        DamageType.NECROTIC,
        DamageType.PIERCING,
        DamageType.POISON,
        DamageType.PSYCHIC,
        DamageType.RADIANT,
        DamageType.SLASHING,
    ],
)
def test_damage_type_ok(damage_type):
    new_damage_type = DamageType.from_str(damage_type.name.lower())
    assert damage_type == new_damage_type
    new_damage_type = DamageType.from_str(damage_type.name.upper())
    assert damage_type == new_damage_type


def test_invalid_damage_type_name():
    with pytest.raises(DomainException):
        DamageType.from_str("invalid")
