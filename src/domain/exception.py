from enum import StrEnum


class DomainExceptionStatus(StrEnum):
    NOT_FOUND = "not_found"
    INVALID_DATA = "invalid_data"
    ACCESS = "access"
    IDEMPOTENT = "idempotent"
    POLICY = "policy"
    INTERNAL = "internal"


class DomainException(Exception):
    def __init__(self, status: StrEnum, msg: str, *args: object) -> None:
        super().__init__(*args)
        self.status = status
        self.msg = msg

    @classmethod
    def not_found(cls, msg: str) -> "DomainException":
        return cls(status=DomainExceptionStatus.NOT_FOUND, msg=msg)

    @classmethod
    def invalid_data(cls, msg: str) -> "DomainException":
        return cls(status=DomainExceptionStatus.INVALID_DATA, msg=msg)

    @classmethod
    def access(cls, msg: str) -> "DomainException":
        if len(msg) == 0:
            msg = "у вас недостаточно прав для совершения операции"
        return cls(status=DomainExceptionStatus.ACCESS, msg=msg)

    @classmethod
    def idempotent(cls, msg: str) -> "DomainException":
        return cls(status=DomainExceptionStatus.IDEMPOTENT, msg=msg)

    @classmethod
    def policy(cls, msg: str) -> "DomainException":
        return cls(status=DomainExceptionStatus.POLICY, msg=msg)

    @classmethod
    def internal(cls, msg: str) -> "DomainException":
        return cls(status=DomainExceptionStatus.INTERNAL, msg=msg)
