from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from application.exception import AppException, AppExceptionStatus
from domain.exception import DomainException, DomainExceptionStatus


def domain_exception_handler(request: Request, exc: DomainException) -> JSONResponse:
    match exc.status:
        case DomainExceptionStatus.INTERNAL:
            status = 500
        case AppExceptionStatus.NOT_FOUND:
            status = 404
        case AppExceptionStatus.ACCESS:
            status = 403
        case _:
            status = 400
    return JSONResponse(
        content=jsonable_encoder({"detail": exc.msg}), status_code=status
    )


def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
    match exc.status:
        case AppExceptionStatus.INTERNAL:
            status = 500
        case AppExceptionStatus.NOT_FOUND:
            status = 404
        case AppExceptionStatus.ACCESS:
            status = 403
        case _:
            status = 400
    return JSONResponse(
        content=jsonable_encoder({"detail": exc.msg}), status_code=status
    )
