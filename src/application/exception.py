from enum import StrEnum


class AppExceptionStatus(StrEnum):
    NOT_FOUND = "not_found"
    INVALID_DATA = "invalid_data"
    ACCESS = "access"
    IDEMPOTENT = "idempotent"
    POLICY = "policy"
    INTERNAL = "internal"


class AppException(Exception):
    def __init__(self, status: StrEnum, msg: str, *args: object) -> None:
        super().__init__(*args)
        self.status = status
        self.msg = msg

    @classmethod
    def not_found(cls, msg: str) -> "AppException":
        return cls(status=AppExceptionStatus.NOT_FOUND, msg=msg)

    @classmethod
    def invalid_data(cls, msg: str) -> "AppException":
        return cls(status=AppExceptionStatus.INVALID_DATA, msg=msg)

    @classmethod
    def access(cls, msg: str) -> "AppException":
        if len(msg) == 0:
            msg = "у вас недостаточно прав для совершения операции"
        return cls(status=AppExceptionStatus.ACCESS, msg=msg)

    @classmethod
    def policy(cls, msg: str) -> "AppException":
        return cls(status=AppExceptionStatus.POLICY, msg=msg)

    @classmethod
    def internal(cls, msg: str) -> "AppException":
        return cls(status=AppExceptionStatus.INTERNAL, msg=msg)
