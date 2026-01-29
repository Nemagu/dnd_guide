import pytest

from domain.exception import DomainException
from domain.game_time import GameTime, GameTimeUnit


@pytest.mark.parametrize(
    "count,game_time_unit",
    [
        [1, GameTimeUnit.ACTION],
        [1, GameTimeUnit.MINUTE],
        [1, GameTimeUnit.HOUR],
        [1, GameTimeUnit.BONUS_ACTION],
        [1, GameTimeUnit.REACTION],
    ],
)
def test_game_time_ok(count, game_time_unit):
    GameTime(count=count, game_time_unit=game_time_unit)


def test_invalid_count():
    with pytest.raises(DomainException):
        GameTime(count=-1, game_time_unit=GameTimeUnit.ACTION)


@pytest.mark.parametrize(
    "game_time_unit",
    [
        GameTimeUnit.ACTION,
        GameTimeUnit.MINUTE,
        GameTimeUnit.HOUR,
        GameTimeUnit.BONUS_ACTION,
        GameTimeUnit.REACTION,
    ],
)
def test_game_time_unit_ok(game_time_unit):
    new_game_time_unit = GameTimeUnit.from_str(game_time_unit.name.lower())
    assert game_time_unit == new_game_time_unit
    new_game_time_unit = GameTimeUnit.from_str(game_time_unit.name.upper())
    assert game_time_unit == new_game_time_unit


def test_invalid_game_time_unit_name():
    with pytest.raises(DomainException):
        GameTimeUnit.from_str("invalid")
