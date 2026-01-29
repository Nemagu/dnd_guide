from dataclasses import dataclass
from uuid import UUID

from adapters.store.sql import DBHelper
from application.use_cases.source.repository import SourceRepository


@dataclass
class DeleteSourceCommand:
    source_id: UUID


async def delete_use_case(db_helper: DBHelper, command: DeleteSourceCommand) -> None:
    repo = SourceRepository()
    async with db_helper.session as session:
        await repo.delete(session, command.source_id)
        await session.commit()
