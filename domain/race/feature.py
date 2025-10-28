from domain.mixin import ValueDescription, ValueName


class RaceFeature(ValueName, ValueDescription):
    def __init__(
        self,
        name: str,
        description: str,
    ) -> None:
        ValueName.__init__(self, name)
        ValueDescription.__init__(self, description)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return (
                self.__name == value.__name
                and self.__description == value.__description
            )
        raise NotImplemented
