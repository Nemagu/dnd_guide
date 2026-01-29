from uuid import UUID, uuid4

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from adapters.store.sql import SourceModel
from domain.source import Source


def get_url(source_id: UUID | None = None, **query) -> str:
    url = "/api/v1/sources"
    if source_id is not None:
        url += f"/{source_id}"
    if len(query) > 0:
        query_params = "&".join([f"{key}={value}" for key, value in query.items()])
        url += f"?{query_params}"
    return url


@pytest.mark.parametrize(
    "create_source,count",
    [[[{"name": "source"}, {"name": "source2"}], 2], [[{"name": "source3"}], 1]],
    indirect=["create_source"],
    ids=["two_sources", "one_source"],
)
def test_source_ok(client: TestClient, create_source, count: int):
    response = client.get(get_url())

    assert response.status_code == 200
    assert len(response.json()) == count


@pytest.mark.parametrize(
    "create_source,count,query_filter",
    [
        [[{"name": "source"}, {"name": "source2"}], 1, {"name": "source"}],
        [[{"name": "source3"}, {"name": "source4"}], 1, {"name": "source3"}],
    ],
    indirect=["create_source"],
    ids=["name_is_source", "name_is_source3"],
)
def test_query_filter(client: TestClient, create_source, count, query_filter):
    response = client.get(get_url(**query_filter))

    assert response.status_code == 200
    assert len(response.json()) == count


@pytest.mark.asyncio
async def test_create_ok(client: TestClient, session: AsyncSession):
    payload = {
        "name": "source",
        "description": "description",
        "name_in_english": "source",
    }

    response = client.post(get_url(), json=payload)

    assert response.status_code == 201
    source_id = UUID(response.json()["source_id"])
    source = await session.get(SourceModel, source_id)
    assert source is not None
    assert source.name == payload["name"]
    assert source.description == payload["description"]
    assert source.name_in_english == payload["name_in_english"]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "field",
    ["name", "description", "name_in_english"],
    ids=["name_is_missing", "description_is_missing", "name_in_english_is_missing"],
)
async def test_create_missing_field(
    client: TestClient, field: str, session: AsyncSession
):
    if field == "name":
        payload = {
            "description": "description",
            "name_in_english": "source",
        }
    elif field == "description":
        payload = {
            "name": "source",
            "name_in_english": "source",
        }
    else:
        payload = {
            "name": "source",
            "description": "description",
        }

    response = client.post(get_url(), json=payload)

    assert response.status_code == 422
    query = select(SourceModel)
    source = await session.execute(query)
    source = source.scalars().all()
    assert source == []


@pytest.mark.asyncio
async def test_create_missing_all_fields(client: TestClient, session: AsyncSession):
    payload = dict()

    response = client.post(get_url(), json=payload)

    assert response.status_code == 422
    query = select(SourceModel)
    source = await session.execute(query)
    source = source.scalars().all()
    assert source == []


@pytest.mark.asyncio
@pytest.mark.parametrize("create_source", [[]], indirect=["create_source"])
async def test_update_ok(
    client: TestClient, session: AsyncSession, create_source: list[Source]
):
    existing_source_id = create_source[0].source_id
    payload = {
        "name": "new_name",
        "description": "new_description",
        "name_in_english": "new_name_in_english",
    }

    response = client.put(get_url(source_id=existing_source_id), json=payload)

    assert response.status_code == 200
    query = select(SourceModel).where(SourceModel.id == existing_source_id)
    source = await session.execute(query)
    source = source.scalar_one()
    assert source.name == payload["name"]
    assert source.description == payload["description"]
    assert source.name_in_english == payload["name_in_english"]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "create_source,field",
    [[[], "name"], [[], "description"], [[], "name_in_english"]],
    ids=["name", "description", "name_in_english"],
    indirect=["create_source"],
)
async def test_partial_update_ok(
    client: TestClient, session: AsyncSession, create_source: list[Source], field: str
):
    existing_source_id = create_source[0].source_id
    payload = {field: f"new_{field}"}

    response = client.put(get_url(source_id=existing_source_id), json=payload)

    assert response.status_code == 200
    query = select(SourceModel).where(SourceModel.id == existing_source_id)
    source = await session.execute(query)
    source = source.scalar_one()
    assert getattr(source, field) == payload[field]


def test_update_not_found(client: TestClient):
    payload = {
        "name": "new_name",
        "description": "new_description",
        "name_in_english": "new_name_in_english",
    }

    response = client.put(get_url(source_id=uuid4()), json=payload)

    assert response.status_code == 404


@pytest.mark.parametrize("create_source", [[]], indirect=["create_source"])
def test_update_without_all_fields(client: TestClient, create_source: list[Source]):
    payload = dict()

    response = client.put(get_url(source_id=create_source[0].source_id), json=payload)

    assert response.status_code == 422


@pytest.mark.asyncio
@pytest.mark.parametrize("create_source", [[]], indirect=["create_source"])
async def test_delete_ok(
    client: TestClient, session: AsyncSession, create_source: list[Source]
):
    existing_source_id = create_source[0].source_id

    response = client.delete(get_url(source_id=existing_source_id))

    assert response.status_code == 204
    source = await session.get(SourceModel, existing_source_id)
    assert source is None


@pytest.mark.asyncio
async def test_delete_not_found(client: TestClient):
    response = client.delete(get_url(source_id=uuid4()))

    assert response.status_code == 404
