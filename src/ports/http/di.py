from typing import Any

from fastapi import Request

from adapters.store.sql import DBHelper
from settings import Settings

DB_HELPER_KEY = "db_helper"


def init_state(settings: Settings) -> dict[str, Any]:
    state = dict()
    state[DB_HELPER_KEY] = DBHelper(db_url=settings.db_settings.url())
    return state


class DBHelperContainer:
    def __init__(self, key_for_state: str) -> None:
        self._key = key_for_state

    def __call__(self, request: Request) -> DBHelper:
        return request.app.state.__getattr__(self._key)


db_helper = DBHelperContainer(key_for_state=DB_HELPER_KEY)
