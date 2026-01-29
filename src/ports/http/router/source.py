from uuid import UUID

from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel, model_validator

from adapters.store.sql import DBHelper
from application.use_cases import source
from ports.http.di import db_helper

source_router = APIRouter(prefix="/sources", tags=["sources"])


class SimpleSourceResponse(BaseModel):
    source_id: UUID
    name: str
    name_in_english: str

    @staticmethod
    def from_app(source_model: source.SimpleSource) -> "SimpleSourceResponse":
        return SimpleSourceResponse(
            source_id=source_model.source_id,
            name=source_model.name,
            name_in_english=source_model.name_in_english,
        )


class DetailSourceResponse(BaseModel):
    source_id: UUID
    name: str
    description: str
    name_in_english: str

    @staticmethod
    def from_app(source_model: source.DetailSource) -> "DetailSourceResponse":
        return DetailSourceResponse(
            source_id=source_model.source_id,
            name=source_model.name,
            description=source_model.description,
            name_in_english=source_model.name_in_english,
        )


class SourceIDResponse(BaseModel):
    source_id: UUID


class SourceQueryFilter(BaseModel):
    source_id: list[UUID] | None = None
    name: list[str] | None = None
    limit: int | None = None
    offset: int | None = None

    def to_app_query(self) -> source.ListSourceQuery:
        return source.ListSourceQuery(
            source_ids=self.source_id,
            names=self.name,
            limit=self.limit,
            offset=self.offset,
        )


class CreateSourceRequest(BaseModel):
    name: str
    description: str
    name_in_english: str

    def to_app_command(self) -> source.CreateSourceCommand:
        return source.CreateSourceCommand(
            name=self.name,
            description=self.description,
            name_in_english=self.name_in_english,
        )


class UpdateSourceRequest(BaseModel):
    name: str | None = None
    description: str | None = None
    name_in_english: str | None = None

    @model_validator(mode="after")
    def validate_all_fields_are_not_empty(self) -> "UpdateSourceRequest":
        if all(
            [self.name is None, self.description is None, self.name_in_english is None]
        ):
            raise ValueError(
                "Для обновления источника необходимо указать хотя бы одно поле"
            )
        return self

    def to_app_command(self, source_id: UUID) -> source.UpdateSourceCommand:
        return source.UpdateSourceCommand(
            source_id=source_id,
            name=self.name,
            description=self.description,
            name_in_english=self.name_in_english,
        )


@source_router.get("")
async def get_source_list(
    filter_query: SourceQueryFilter = Query(),
    db: DBHelper = Depends(db_helper),
) -> list[SimpleSourceResponse]:
    result = await source.list_use_case(db_helper=db, query=filter_query.to_app_query())
    return [SimpleSourceResponse.from_app(d) for d in result]


@source_router.get("/{source_id}")
async def get_source(
    source_id: UUID, db: DBHelper = Depends(db_helper)
) -> DetailSourceResponse:
    result = await source.retrieve_use_case(
        db_helper=db, query=source.SourceQuery(source_id=source_id)
    )
    return DetailSourceResponse.from_app(result)


@source_router.post("", status_code=201)
async def create_source(
    request: CreateSourceRequest, db: DBHelper = Depends(db_helper)
) -> SourceIDResponse:
    result = await source.create_use_case(
        db_helper=db, command=request.to_app_command()
    )
    return SourceIDResponse(source_id=result)


@source_router.put("/{source_id}")
async def update_source(
    source_id: UUID, request: UpdateSourceRequest, db: DBHelper = Depends(db_helper)
):
    await source.update_use_case(
        db_helper=db, command=request.to_app_command(source_id=source_id)
    )


@source_router.delete("/{source_id}", status_code=204)
async def delete_source(source_id: UUID, db: DBHelper = Depends(db_helper)):
    await source.delete_use_case(
        db_helper=db, command=source.DeleteSourceCommand(source_id=source_id)
    )
