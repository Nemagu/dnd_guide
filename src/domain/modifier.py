from enum import StrEnum

from domain.exception import DomainException


class Modifier(StrEnum):
    STRENGTH = "сила"
    DEXTERITY = "ловкость"
    CONSTITUTION = "телосложение"
    INTELLECT = "интеллект"
    WISDOM = "мудрость"
    CHARISMA = "харизма"

    @classmethod
    def from_str(cls, name: str) -> "Modifier":
        upper_name = name.upper()
        for member_name in cls._member_names_:
            if member_name.upper() == upper_name:
                return cls[member_name]
        raise DomainException.invalid_data(
            f"для модификатора с названием {name} не удалось сопоставить внутреннее значение"
        )
