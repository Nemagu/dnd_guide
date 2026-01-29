import pytest
import pytest_asyncio
from fastapi.testclient import TestClient

from adapters.store.sql import DBHelper
from adapters.store.sql.base import Base
from ports.http.app import init_app
from ports.http.di import DB_HELPER_KEY
from settings import DatabaseSettings, Settings


class MockDBSettings(DatabaseSettings):
    def url(self) -> str:
        return "sqlite+aiosqlite:///:memory:"


class MockSettings(Settings):
    db_settings: DatabaseSettings = MockDBSettings()


app = init_app(settings=MockSettings())
app_client = TestClient(app)


@pytest.fixture(scope="session")
def db_helper() -> DBHelper:
    return app.state.__getattr__(DB_HELPER_KEY)


@pytest_asyncio.fixture()
async def session(db_helper):
    async with db_helper.session as session:
        yield session


@pytest_asyncio.fixture(autouse=True)
async def create_db(db_helper):
    async with db_helper.async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@pytest_asyncio.fixture(autouse=True)
async def clear_db(db_helper):
    async with db_helper.async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="session")
def client() -> TestClient:
    return app_client
