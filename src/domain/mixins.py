from uuid import UUID

from domain.exception import DomainException


class PrefixConcatenator:
    def __init__(self, prefix: str) -> None:
        self._prefix = prefix

    def concatenate(self, value: str) -> str:
        if len(self._prefix) == 0:
            return value
        return f"{self._prefix} - {value}"


class ValueName:
    def __init__(self, name: str, error_message_prefix: str = "") -> None:
        self._name_error_message_prefix = PrefixConcatenator(error_message_prefix)
        self._validate_name(name)
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def _validate_name(self, name: str) -> None:
        if len(name) == 0:
            raise DomainException.invalid_data(
                self._name_error_message_prefix.concatenate(
                    "название не может быть пустым"
                )
            )
        if len(name) > 50:
            raise DomainException.invalid_data(
                self._name_error_message_prefix.concatenate(
                    "название не может содержать более 50 символов"
                )
            )


class EntityName(ValueName):
    def new_name(self, name: str) -> None:
        if self._name == name:
            raise DomainException.idempotent(
                self._name_error_message_prefix.concatenate(
                    "текущее название равно новому названию"
                )
            )
        self._validate_name(name)
        self._name = name


class ValueNameInEnglish:
    def __init__(self, name_in_english: str, error_message_prefix: str = "") -> None:
        self._name_in_english_error_message_prefix = PrefixConcatenator(
            error_message_prefix
        )
        self._validate_name_in_english(name_in_english)
        self._name_in_english = name_in_english

    @property
    def name_in_english(self) -> str:
        return self._name_in_english

    def _validate_name_in_english(self, name_in_english: str) -> None:
        if len(name_in_english) > 50:
            raise DomainException.invalid_data(
                self._name_in_english_error_message_prefix.concatenate(
                    "название на английском не может содержать более 50 символов"
                )
            )


class EntityNameInEnglish(ValueNameInEnglish):
    def new_name_in_english(self, name_in_english: str) -> None:
        if self._name_in_english == name_in_english:
            raise DomainException.idempotent(
                self._name_in_english_error_message_prefix.concatenate(
                    "текущее название на английском равно новому названию на английском"
                )
            )
        self._validate_name_in_english(name_in_english)
        self._name_in_english = name_in_english


class ValueDescription:
    def __init__(self, description: str, error_message_prefix: str = "") -> None:
        self.__description_error_message_prefix = PrefixConcatenator(
            error_message_prefix
        )
        self._validate_description(description)
        self._description = description

    @property
    def description(self) -> str:
        return self._description

    def _validate_description(self, description: str) -> None:
        if len(description) == 0:
            raise DomainException.invalid_data(
                self.__description_error_message_prefix.concatenate(
                    "описание не может быть пустым"
                )
            )


class EntityDescription(ValueDescription):
    def new_description(self, description: str) -> None:
        self._validate_description(description)
        self._description = description


class EntitySource:
    def __init__(self, source_id: UUID, error_message_prefix: str = "") -> None:
        self.__error_message_prefix = PrefixConcatenator(error_message_prefix)
        self._source_id = source_id

    @property
    def source_id(self) -> UUID:
        return self._source_id

    def new_source_id(self, source_id: UUID) -> None:
        if self._source_id == source_id:
            raise DomainException.idempotent(
                self.__error_message_prefix.concatenate("текущий источник равен новому")
            )
        self._source_id = source_id
