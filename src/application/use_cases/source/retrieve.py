from dataclasses import dataclass
from uuid import UUID

from adapters.store.sql import DBHelper
from application.use_cases.source.model import DetailSource
from application.use_cases.source.repository import SourceRepository


@dataclass
class SourceQuery:
    source_id: UUID


async def retrieve_use_case(db_helper: DBHelper, query: SourceQuery) -> DetailSource:
    repo = SourceRepository()
    async with db_helper.session as session:
        source = await repo.detail(session, query.source_id)
    return source
