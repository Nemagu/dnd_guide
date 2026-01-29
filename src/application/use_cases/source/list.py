from dataclasses import dataclass
from uuid import UUID

from adapters.store.sql import DBHelper
from application.use_cases.source.model import SimpleSource
from application.use_cases.source.repository import SourceRepository


@dataclass
class ListSourceQuery:
    source_ids: list[UUID] | None = None
    names: list[str] | None = None
    limit: int | None = None
    offset: int | None = None


async def list_use_case(
    db_helper: DBHelper, query: ListSourceQuery
) -> list[SimpleSource]:
    repo = SourceRepository()
    async with db_helper.session as session:
        result = await repo.filters(session, query)
    return result
