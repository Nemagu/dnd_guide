from enum import StrEnum

from domain.exception import DomainException


class CreatureType(StrEnum):
    ABERRATION = "аберрация"
    BEAST = "зверь"
    CELESTIAL = "небожитель"
    CONSTRUCT = "конструкт"
    DRAGON = "дракон"
    ELEMENTAL = "элементаль"
    FEY = "фея"
    FIEND = "исчадие"
    GIANT = "великан"
    HUMANOID = "гуманоид"
    MONSTROSITY = "чудовище"
    OOZE = "слизь"
    PLANT = "растение"
    UNDEAD = "нежить"
    TRANSPORT = "транспорт"
    OBJECT = "объект"

    @classmethod
    def from_str(cls, name: str) -> "CreatureType":
        upper_name = name.upper()
        for member_name in cls._member_names_:
            if member_name.upper() == upper_name:
                return cls[member_name]
        raise DomainException.invalid_data(
            f"для типа существа с названием {name} не удалось сопоставить с внутренним значением"
        )
