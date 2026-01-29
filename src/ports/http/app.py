from fastapi import FastAPI

from application.exception import AppException
from domain.exception import DomainException
from ports.http.di import init_state
from ports.http.exception_handler import app_exception_handler, domain_exception_handler
from ports.http.router import router
from settings import Settings


def init_app(settings: Settings) -> FastAPI:
    app = FastAPI()

    app.include_router(router)

    state = init_state(settings=settings)
    for key, value in state.items():
        app.state.__setattr__(key, value)

    app.add_exception_handler(DomainException, domain_exception_handler)
    app.add_exception_handler(AppException, app_exception_handler)

    return app
