from typing import TYPE_CHECKING

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

if TYPE_CHECKING:
    from sqlalchemy import Engine
    from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession


class DBHelper:
    def __init__(self, db_url: str, echo: bool = False) -> None:
        self._async_engine = create_async_engine(url=db_url, echo=echo)
        self._sync_engine = create_engine(db_url, echo=echo)
        self._session_factory = async_sessionmaker(
            bind=self._async_engine, autoflush=False, expire_on_commit=False
        )

    @property
    def async_engine(self) -> "AsyncEngine":
        return self._async_engine

    @property
    def sync_engine(self) -> "Engine":
        return self._sync_engine

    @property
    def session(self) -> "AsyncSession":
        return self._session_factory()
