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
        match name.upper():
            case cls.STRENGTH.name:
                return cls.STRENGTH
            case cls.DEXTERITY.name:
                return cls.DEXTERITY
            case cls.CONSTITUTION.name:
                return cls.CONSTITUTION
            case cls.INTELLECT.name:
                return cls.INTELLECT
            case cls.WISDOM.name:
                return cls.WISDOM
            case cls.CHARISMA.name:
                return cls.CHARISMA
            case _:
                raise DomainException.invalid_data(
                    f"для модификатора с названием {name} не удалось сопоставить внутреннее значение"
                )
