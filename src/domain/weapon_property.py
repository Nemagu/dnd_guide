from enum import StrEnum
from uuid import UUID

from domain.dice import Dice
from domain.exception import DomainException
from domain.length import Length
from domain.mixins import EntityDescription


class WeaponPropertyName(StrEnum):
    AMMUNITION = "боеприпасы"
    FINESSE = "фехтовальное"
    HEAVY = "тяжелое"
    LIGHT = "легкое"
    REACH = "досягаемость"
    SPECIAL = "особое"
    THROWN = "метательное"
    TWO_HANDED = "двуручное"
    VERSATILE = "универсальное"
    DISTANCE = "дистанция"

    @classmethod
    def from_str(cls, name: str) -> "WeaponPropertyName":
        upper_name = name.upper()
        for member_name in cls._member_names_:
            if member_name.upper() == upper_name:
                return cls[member_name]
        raise DomainException.invalid_data(
            f"для названия свойства оружия с названием {name} не удалось "
            "сопоставить внутреннее значение"
        )


class WeaponProperty(EntityDescription):
    def __init__(
        self,
        property_id: UUID,
        name: WeaponPropertyName,
        description: str,
        base_range: Length | None,
        max_range: Length | None,
        second_hand_dice: Dice | None,
    ) -> None:
        self._validate_stats_by_name(name, base_range, max_range, second_hand_dice)
        EntityDescription.__init__(self, description)
        self._property_id = property_id
        self._name = name
        self._base_range = base_range
        self._max_range = max_range
        self._second_hand_dice = second_hand_dice

    @property
    def property_id(self) -> UUID:
        return self._property_id

    @property
    def name(self) -> WeaponPropertyName:
        return self._name

    @property
    def base_range(self) -> Length | None:
        return self._base_range

    @property
    def max_range(self) -> Length | None:
        return self._max_range

    @property
    def second_hand_dice(self) -> Dice | None:
        return self._second_hand_dice

    def new_name(
        self,
        name: WeaponPropertyName,
        **kwargs,
    ) -> None:
        if self._name == name:
            raise DomainException.idempotent("текущее название равно новому названию")
        base_range = kwargs.get("base_range", self.base_range)
        max_range = kwargs.get("max_range", self.max_range)
        second_hand_dice = kwargs.get("second_hand_dice", self.second_hand_dice)
        self._validate_stats_by_name(name, base_range, max_range, second_hand_dice)
        self._name = name
        self._base_range = base_range
        self._max_range = max_range
        self._second_hand_dice = second_hand_dice

    def new_base_range(self, base_range: Length | None) -> None:
        if self._name != WeaponPropertyName.AMMUNITION:
            raise DomainException.invalid_data(
                "для этого свойства нельзя назначить базовую дистанцию"
            )
        if self._base_range == base_range:
            raise DomainException.idempotent(
                "текущий базовый радиус равен новому базовому радиусу"
            )
        if (
            self._max_range is not None
            and base_range is not None
            and self._max_range < base_range
        ):
            raise DomainException.invalid_data(
                "базовый радиус атаки не может быть больше максимального"
            )
        self._base_range = base_range

    def new_max_range(self, max_range: Length | None) -> None:
        if self._name != WeaponPropertyName.AMMUNITION:
            raise DomainException.invalid_data(
                "для этого свойства нельзя назначить максимальную дистанцию"
            )
        if self._max_range == max_range:
            raise DomainException.idempotent(
                "текущий максимальный радиус равен новому максимальному радиусу"
            )
        if (
            self._base_range is not None
            and max_range is not None
            and self._base_range > max_range
        ):
            raise DomainException.invalid_data(
                "максимальный радиус атаки не может быть меньше базового"
            )
        self._max_range = max_range

    def new_second_hand_dice(self, dice: Dice | None) -> None:
        if self._name != WeaponPropertyName.VERSATILE:
            raise DomainException.invalid_data(
                "для этого свойства нельзя назначить кость для двух рук"
            )
        if self._second_hand_dice == dice:
            raise DomainException.idempotent(
                "текущая кость для второй руки ровна новой кости для второй руки"
            )
        self._second_hand_dice = dice

    def _validate_stats_by_name(
        self,
        name: WeaponPropertyName,
        base_range: Length | None,
        max_range: Length | None,
        second_hand_dice: Dice | None,
    ):
        match name:
            case WeaponPropertyName.AMMUNITION:
                if base_range is None or max_range is None:
                    raise DomainException.invalid_data(
                        "для дистанционного оружия необходимо указать "
                        "базовую и максимальную дистанцию атаки"
                    )
                if second_hand_dice is not None:
                    raise DomainException.invalid_data(
                        "для дистанционного оружия нельзя указать кость для второй руки"
                    )
                if base_range > max_range:
                    raise DomainException.invalid_data(
                        "базовый радиус атаки не может быть больше максимального"
                    )
            case WeaponPropertyName.VERSATILE:
                if base_range is not None or max_range is not None:
                    raise DomainException.invalid_data(
                        "для этого свойства нельзя указать базовый и максимальный "
                        "радиус атаки"
                    )
                if second_hand_dice is None:
                    raise DomainException.invalid_data(
                        "для универсального оружия необходимо указать урон "
                        "при удержании оружия двумя руками"
                    )
            case _:
                if (
                    base_range is not None
                    or max_range is not None
                    or second_hand_dice is not None
                ):
                    raise DomainException.invalid_data(
                        "для этого свойства нельзя указать базовый и "
                        "максимальный радиус атаки, а так же нельзя "
                        "указать урон при удержании оружия в двух руках"
                    )

    def __str__(self) -> str:
        return self._name

    def __eq__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return self._property_id == value._property_id
        if isinstance(value, UUID):
            return self._property_id == value
        raise ValueError()
