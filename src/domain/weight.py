from enum import StrEnum

from domain.exception import DomainException


class WeightUnit(StrEnum):
    LB = "фунт"
    KG = "килограмм"

    @classmethod
    def from_str(cls, name: str) -> "WeightUnit":
        upper_name = name.upper()
        for member_name in cls._member_names_:
            if member_name.upper() == upper_name:
                return cls[member_name]
        raise DomainException.invalid_data(
            f"для единиц измерения массы с названием {name} не удалось "
            "сопоставить внутренний тип"
        )


class Weight:
    def __init__(self, count: float, weight_unit: WeightUnit) -> None:
        if count < 0:
            raise DomainException.invalid_data("масса не может быть отрицательной")
        match weight_unit:
            case WeightUnit.LB:
                self._count = count
            case WeightUnit.KG:
                self._count = 2.205 * count

    def in_lb(self) -> float:
        return self._count

    def in_kg(self) -> float:
        return self._count / 2.205

    @property
    def count(self) -> float:
        return self._count

    def __eq__(self, value: object) -> bool:
        if value is None:
            return False
        if isinstance(value, self.__class__):
            return self._count == value._count
        raise ValueError()
