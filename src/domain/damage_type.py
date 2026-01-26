from enum import StrEnum

from domain.exception import DomainException


class DamageType(StrEnum):
    ACID = "кислота"
    BLUDGEONING = "дробящий"
    COLD = "холод"
    FIRE = "огонь"
    FORCE = "силовое поле"
    LIGHTNING = "электричество"
    NECROTIC = "некротический"
    PIERCING = "колющий"
    POISON = "яд"
    PSYCHIC = "психический"
    RADIANT = "излучение"
    SLASHING = "рубящий"
    THUNDER = "звук"

    @classmethod
    def from_str(cls, name: str) -> "DamageType":
        upper_name = name.upper()
        for member_name in cls._member_names_:
            if member_name.upper() == upper_name:
                return cls[member_name]
        raise DomainException.invalid_data(
            f"для типа урона с названием {name} не удалось сопоставить с внутренним значением"
        )
