from enum import StrEnum

from domain.exception import DomainException


class GameTimeUnit(StrEnum):
    ACTION = "действие"
    BONUS_ACTION = "бонусное действие"
    REACTION = "реакция"
    MINUTE = "минута"
    HOUR = "час"

    @classmethod
    def from_str(cls, name: str) -> "GameTimeUnit":
        upper_name = name.upper()
        for member_name in cls._member_names_:
            if member_name.upper() == upper_name:
                return cls[member_name]
        raise DomainException.invalid_data(
            f"для временного промежутка с названием {name} не "
            "удалось сопоставить внутреннее значение"
        )


class GameTime:
    def __init__(self, count: int, game_time_unit: GameTimeUnit) -> None:
        if count < 0:
            raise DomainException.invalid_data(
                "отрицательного количества времени не может быть"
            )
        self._count = count
        self._unit = game_time_unit

    @property
    def count(self) -> int:
        return self._count

    @property
    def unit(self) -> GameTimeUnit:
        return self._unit

    def __eq__(self, value: object) -> bool:
        if value is None:
            return False
        if isinstance(value, self.__class__):
            return self._count == value._count and self._unit == value._unit
        raise ValueError()
