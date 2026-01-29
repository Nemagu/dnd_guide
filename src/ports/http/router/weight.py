from fastapi import APIRouter
from pydantic import BaseModel

from domain.weight import WeightUnit

weight_router = APIRouter(prefix="/weight", tags=["weight"])


class WeightUnitsResponse(BaseModel):
    lb: str = WeightUnit.LB.value
    kg: str = WeightUnit.KG.value


@weight_router.get("/units")
async def get_weight_units() -> WeightUnitsResponse:
    return WeightUnitsResponse()
