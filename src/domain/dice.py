from enum import IntEnum

from domain.exception import DomainException


class DiceType(IntEnum):
    D4 = 4
    D6 = 6
    D8 = 8
    D10 = 10
    D12 = 12
    D20 = 20
    D100 = 100

    @classmethod
    def from_str(cls, name: str) -> "DiceType":
        upper_name = name.upper()
        for member_name in cls._member_names_:
            if member_name.upper() == upper_name:
                return cls[member_name]
        raise DomainException.invalid_data(
            f"для кости с названием {name} не удалось сопоставить значение"
        )


class Dice:
    def __init__(self, count: int, dice_type: DiceType) -> None:
        if count < 1:
            raise DomainException.invalid_data(
                "количество костей не может быть меньше 1"
            )
        self._count = count
        self._dice_type = dice_type

    @property
    def count(self) -> int:
        return self._count

    @property
    def dice_type(self) -> DiceType:
        return self._dice_type

    def __str__(self) -> str:
        return f"{self._count}{self._dice_type.name.lower()}"

    def __eq__(self, value: object) -> bool:
        if value is None:
            return False
        if isinstance(value, self.__class__):
            return self._count == value._count and self._dice_type == value._dice_type
        raise ValueError()
