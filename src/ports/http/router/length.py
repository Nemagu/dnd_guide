from fastapi import APIRouter
from pydantic import BaseModel

from domain.length import LengthUnit

length_router = APIRouter(prefix="/length", tags=["length"])


class LengthUnitsResponse(BaseModel):
    ft: str = LengthUnit.FT.value
    m: str = LengthUnit.M.value


@length_router.get("/units")
async def get_length_units() -> LengthUnitsResponse:
    return LengthUnitsResponse()
