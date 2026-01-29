from enum import Enum
from typing import Any

import pytest
from fastapi.testclient import TestClient

from domain.coin import CoinType
from domain.creature import CreatureSize, CreatureType
from domain.damage_type import DamageType
from domain.dice import DiceType
from domain.game_time import GameTimeUnit
from domain.length import LengthUnit
from domain.modifier import Modifier
from domain.skill import Skill
from domain.weight import WeightUnit


def get_url(path: str) -> str:
    return f"/api/v1/{path}"


def validate_enum(enum: type[Enum], response: dict[str, Any]) -> None:
    for key, value in response.items():
        key = key.upper()
        assert key in enum.__members__.keys()
        assert value == enum[key].value


@pytest.mark.parametrize(
    "path,domain_enum",
    [
        ["coins/types", CoinType],
        ["creatures/sizes", CreatureSize],
        ["creatures/types", CreatureType],
        ["damages/types", DamageType],
        ["dices/types", DiceType],
        ["game-times/units", GameTimeUnit],
        ["length/units", LengthUnit],
        ["modifiers", Modifier],
        ["skills", Skill],
        ["weight/units", WeightUnit],
    ],
    ids=[
        "coin_types",
        "creature_sizes",
        "creature_types",
        "damage_types",
        "dice_types",
        "game_time_units",
        "length_units",
        "modifier_types",
        "skill_types",
        "weight_units",
    ],
)
def test_enums(client: TestClient, path: str, domain_enum: type[Enum]):
    response = client.get(get_url(path))
    assert response.status_code == 200
    validate_enum(domain_enum, response.json())
