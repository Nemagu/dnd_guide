from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import exists, select
from sqlalchemy.ext.asyncio import AsyncSession

from adapters.store.sql import SourceModel
from application.exception import AppException
from application.use_cases.source.model import DetailSource, SimpleSource
from domain.source import Source

if TYPE_CHECKING:
    from .list import ListSourceQuery


class SourceRepository:
    async def filters(
        self, session: AsyncSession, filters: ListSourceQuery
    ) -> list[SimpleSource]:
        query = select(SourceModel.id, SourceModel.name, SourceModel.name_in_english)
        if filters.source_ids is not None:
            query = query.where(SourceModel.id.in_(filters.source_ids))
        if filters.names is not None:
            query = query.where(SourceModel.name.in_(filters.names))
        if filters.limit is not None:
            query = query.limit(filters.limit)
        if filters.offset is not None:
            query = query.offset(filters.offset)
        result = await session.execute(query)
        return [
            SimpleSource(
                source_id=row.id, name=row.name, name_in_english=row.name_in_english
            )
            for row in result
        ]

    async def by_id(self, session: AsyncSession, id: UUID) -> Source:
        query = select(SourceModel).where(SourceModel.id == id)
        result = await session.execute(query)
        result = result.scalar()
        if result is None:
            raise AppException.not_found("источник не найден")
        return result.to_domain()

    async def detail(self, session: AsyncSession, id: UUID) -> DetailSource:
        query = select(SourceModel).where(SourceModel.id == id)
        result = await session.execute(query)
        result = result.scalar()
        if result is None:
            raise AppException.not_found("источник не найден")
        return DetailSource(
            source_id=result.id,
            name=result.name,
            name_in_english=result.name_in_english,
            description=result.description,
        )

    async def exists_source_name(self, session: AsyncSession, name: str) -> bool:
        query = select(exists(SourceModel)).where(SourceModel.name == name)
        result = await session.execute(query)
        result = result.scalar()
        return result if result is not None else False

    async def save(self, session: AsyncSession, source: Source) -> None:
        await session.merge(SourceModel.from_domain(source))

    async def delete(self, session: AsyncSession, id: UUID) -> None:
        query = select(SourceModel).where(SourceModel.id == id)
        result = await session.execute(query)
        result = result.scalar()
        if result is None:
            raise AppException.not_found("источник не найден")
        await session.delete(result)
