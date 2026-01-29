from dataclasses import dataclass
from uuid import UUID, uuid4

from adapters.store.sql import DBHelper
from application.exception import AppException
from application.use_cases.source.repository import SourceRepository
from domain.source import Source


@dataclass
class CreateSourceCommand:
    name: str
    description: str
    name_in_english: str


async def create_use_case(db_helper: DBHelper, command: CreateSourceCommand) -> UUID:
    repo = SourceRepository()
    async with db_helper.session as session:
        if await repo.exists_source_name(session, command.name):
            raise AppException.invalid_data(
                f"источник с таким названием '{command.name}' уже существует"
            )
        domain_source = Source(
            source_id=uuid4(),
            name=command.name,
            description=command.description,
            name_in_english=command.name_in_english,
        )
        await repo.save(session, domain_source)
        await session.commit()
    return domain_source.source_id
