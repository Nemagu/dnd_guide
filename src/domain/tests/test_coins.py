import pytest

from domain.coins import Coins, CoinType
from domain.exception import DomainException


@pytest.mark.parametrize(
    "count,coin_type",
    [
        [1, CoinType.COPPER],
        [1, CoinType.SILVER],
        [1, CoinType.GOLD],
        [1, CoinType.PLATINUM],
        [1, CoinType.ELECTRUM],
    ],
)
def test_coins_ok(count, coin_type):
    Coins(count=count, coin_type=coin_type)


def test_invalid_count():
    with pytest.raises(DomainException):
        Coins(count=-1, coin_type=CoinType.COPPER)


@pytest.mark.parametrize(
    "coin_type",
    [
        CoinType.COPPER,
        CoinType.SILVER,
        CoinType.GOLD,
        CoinType.PLATINUM,
        CoinType.ELECTRUM,
    ],
)
def test_coin_type_ok(coin_type):
    new_coin_type = CoinType.from_str(coin_type.name.lower())
    assert coin_type == new_coin_type
    new_coin_type = CoinType.from_str(coin_type.name.upper())
    assert coin_type == new_coin_type


def test_invalid_coin_type_name():
    with pytest.raises(DomainException):
        CoinType.from_str("invalid")
