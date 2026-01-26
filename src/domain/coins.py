from enum import StrEnum

from domain.exception import DomainException


class CoinType(StrEnum):
    COPPER = "медные"
    SILVER = "серебряные"
    ELECTRUM = "электрум"
    GOLD = "золотые"
    PLATINUM = "платиновые"

    @classmethod
    def from_str(cls, name: str) -> "CoinType":
        match name.upper():
            case cls.COPPER.name:
                return cls.COPPER
            case cls.SILVER.name:
                return cls.SILVER
            case cls.ELECTRUM.name:
                return cls.ELECTRUM
            case cls.GOLD.name:
                return cls.GOLD
            case cls.PLATINUM.name:
                return cls.PLATINUM
            case _:
                raise DomainException.invalid_data(
                    f"для типа монет с названием {name} не удалось сопоставить внутренний тип"
                )


class Coins:
    def __init__(self, count: float, coin_type: CoinType = CoinType.COPPER) -> None:
        if count < 0:
            raise DomainException.invalid_data(
                "количество монет не может быть отрицательным"
            )
        match coin_type:
            case CoinType.COPPER:
                self._count = count
            case CoinType.SILVER:
                self._count = count * 10
            case CoinType.ELECTRUM:
                self._count = count * 50
            case CoinType.GOLD:
                self._count = count * 100
            case CoinType.PLATINUM:
                self._count = count * 1_000

    def in_copper(self) -> float:
        return self._count

    def in_silver(self) -> float:
        return self._count / 10

    def in_electrum(self) -> float:
        return self._count / 50

    def in_gold(self) -> float:
        return self._count / 100

    def in_platinum(self) -> float:
        return self._count / 1_000

    def __eq__(self, value: object) -> bool:
        if value is None:
            return False
        if isinstance(value, self.__class__):
            return self._count == value._count
        raise ValueError()
