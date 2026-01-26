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
        match name.upper():
            case cls.ACROBATICS.name:
                return cls.ACROBATICS
            case cls.ATHLETICS.name:
                return cls.ATHLETICS
            case cls.PERCEPTION.name:
                return cls.PERCEPTION
            case cls.SURVIVAL.name:
                return cls.SURVIVAL
            case cls.ANIMAL_HANDLING.name:
                return cls.ANIMAL_HANDLING
            case cls.INTIMIDATION.name:
                return cls.INTIMIDATION
            case cls.PERFORMANCE.name:
                return cls.PERFORMANCE
            case cls.HISTORY.name:
                return cls.HISTORY
            case cls.SLEIGHT_OF_HAND.name:
                return cls.SLEIGHT_OF_HAND
            case cls.ARCANA.name:
                return cls.ARCANA
            case cls.MEDICINE.name:
                return cls.MEDICINE
            case cls.DECEPTION.name:
                return cls.DECEPTION
            case cls.NATURE.name:
                return cls.NATURE
            case cls.INSIGHT.name:
                return cls.INSIGHT
            case cls.INVESTIGATION.name:
                return cls.INVESTIGATION
            case cls.RELIGION.name:
                return cls.RELIGION
            case cls.STEALTH.name:
                return cls.STEALTH
            case cls.PERSUASION.name:
                return cls.PERSUASION
            case _:
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
