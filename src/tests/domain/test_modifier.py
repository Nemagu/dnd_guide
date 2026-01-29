import pytest

from domain.exception import DomainException
from domain.modifier import Modifier


@pytest.mark.parametrize(
    "modifier",
    [
        Modifier.STRENGTH,
        Modifier.DEXTERITY,
        Modifier.CONSTITUTION,
        Modifier.INTELLECT,
        Modifier.WISDOM,
        Modifier.CHARISMA,
    ],
)
def test_modifier_ok(modifier):
    new_modifier = Modifier.from_str(modifier.name.lower())
    assert modifier == new_modifier
    new_modifier = Modifier.from_str(modifier.name.upper())
    assert modifier == new_modifier


def test_invalid_modifier_name():
    with pytest.raises(DomainException):
        Modifier.from_str("invalid")
