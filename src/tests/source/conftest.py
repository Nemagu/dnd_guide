from uuid import uuid4

import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from application.use_cases.source.repository import SourceRepository
from domain.source import Source

source_repository = SourceRepository()


@pytest_asyncio.fixture()
async def create_source(session: AsyncSession, request) -> list[Source]:
    default_param = {
        "name": "source_name",
        "description": "source_description",
        "name_in_english": "source_name_in_english",
    }
    domain_sources = list()
    param = request.param
    if len(param) == 0:
        domain_sources.append(Source(source_id=uuid4(), **default_param))
    else:
        for param in request.param:
            p = default_param.copy()
            p.update(param)
            domain_sources.append(Source(source_id=uuid4(), **p))
    for domain_source in domain_sources:
        await source_repository.save(session, domain_source)
    await session.commit()
    return domain_sources
