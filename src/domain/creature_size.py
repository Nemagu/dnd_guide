from enum import StrEnum

from domain.exception import DomainException


class CreatureSize(StrEnum):
    TINY = "крошечный"
    SMALL = "малый"
    MEDIUM = "средний"
    LARGE = "большой"
    HUGE = "огромный"
    GARGANTUAN = "гигантский"

    @classmethod
    def from_str(cls, name: str) -> "CreatureSize":
        upper_name = name.upper()
        for member_name in cls._member_names_:
            if member_name.upper() == upper_name:
                return cls[member_name]
        raise DomainException.invalid_data(
            f"для размера существа с названием {name} не удалось сопоставить значение"
        )
