from dataclasses import dataclass
from uuid import UUID

from adapters.store.sql import DBHelper
from application.exception import AppException
from application.use_cases.source.repository import SourceRepository


@dataclass
class UpdateSourceCommand:
    source_id: UUID
    name: str | None
    description: str | None
    name_in_english: str | None


async def update_use_case(db_helper: DBHelper, command: UpdateSourceCommand) -> None:
    repo = SourceRepository()
    async with db_helper.session as session:
        domain_source = await repo.by_id(session, command.source_id)
        if command.name is not None:
            if await repo.exists_source_name(session, command.name):
                raise AppException.invalid_data(
                    f"название источника '{command.name}' уже существует"
                )
            domain_source.new_name(command.name)
        if command.description is not None:
            domain_source.new_description(command.description)
        if command.name_in_english is not None:
            domain_source.new_name_in_english(command.name_in_english)
        await repo.save(session, domain_source)
        await session.commit()
