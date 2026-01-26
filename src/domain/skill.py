from enum import StrEnum

from domain.exception import DomainException
from domain.modifier import Modifier


class Skill(StrEnum):
    ACROBATICS = "акробатика"
    ATHLETICS = "атлетика"
    PERCEPTION = "внимание"
    SURVIVAL = "выживание"
    ANIMAL_HANDLING = "дрессировка"
    INTIMIDATION = "запугивание"
    PERFORMANCE = "исполнение"
    HISTORY = "история"
    SLEIGHT_OF_HAND = "ловкость рук"
    ARCANA = "магия"
    MEDICINE = "медицина"
    DECEPTION = "обман"
    NATURE = "природа"
    INSIGHT = "проницательность"
    INVESTIGATION = "расследование"
    RELIGION = "религия"
    STEALTH = "скрытность"
    PERSUASION = "убеждение"

    @classmethod
    def from_str(cls, name: str) -> "Skill":
        upper_name = name.upper()
        for member_name in cls._member_names_:
            if member_name.upper() == upper_name:
                return cls[member_name]
        raise DomainException.invalid_data(
            f"для навыка с названием {name} не удалось сопоставить внутренний навык"
        )

    def modifier(self) -> Modifier:
        cls = self.__class__
        match self:
            case cls.ATHLETICS:
                return Modifier.STRENGTH

            case cls.ACROBATICS | cls.SLEIGHT_OF_HAND | cls.STEALTH:
                return Modifier.DEXTERITY

            case (
                cls.ARCANA | cls.HISTORY | cls.INVESTIGATION | cls.NATURE | cls.RELIGION
            ):
                return Modifier.INTELLECT

            case (
                cls.ANIMAL_HANDLING
                | cls.INSIGHT
                | cls.MEDICINE
                | cls.PERCEPTION
                | cls.SURVIVAL
            ):
                return Modifier.WISDOM

            case cls.DECEPTION | cls.INTIMIDATION | cls.PERFORMANCE | cls.PERSUASION:
                return Modifier.CHARISMA
