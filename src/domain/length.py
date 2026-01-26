from enum import StrEnum

from domain.exception import DomainException


class LengthUnit(StrEnum):
    FT = "фут"
    M = "метр"

    @classmethod
    def from_str(cls, name: str) -> "LengthUnit":
        upper_name = name.upper()
        for member_name in cls._member_names_:
            if member_name.upper() == upper_name:
                return cls[member_name]
        raise DomainException.invalid_data(
            f"для единиц {name} не удалось сопоставить значение"
        )


class Length:
    def __init__(self, count: float, length_unit: LengthUnit) -> None:
        if count < 0:
            raise DomainException.invalid_data("мера длины не может быть отрицательной")
        match length_unit:
            case LengthUnit.FT:
                self._count = count
            case LengthUnit.M:
                self._count = count * 3.281

    def in_ft(self) -> float:
        return self._count

    def in_m(self) -> float:
        return self._count / 3.281

    @property
    def count(self) -> float:
        return self._count

    def __eq__(self, value: object) -> bool:
        if value is None:
            return False
        if isinstance(value, self.__class__):
            return self._count == value._count
        raise ValueError()

    def __lt__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return self._count < value._count
        raise ValueError()
