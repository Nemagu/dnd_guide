from fastapi import APIRouter
from pydantic import BaseModel

from domain.coin import CoinType

coin_router = APIRouter(prefix="/coins", tags=["coins"])


class CoinTypesResponse(BaseModel):
    copper: str = CoinType.COPPER.value
    silver: str = CoinType.SILVER.value
    gold: str = CoinType.GOLD.value
    electrum: str = CoinType.ELECTRUM.value
    platinum: str = CoinType.PLATINUM.value


@coin_router.get("/types")
async def get_coin_types() -> CoinTypesResponse:
    return CoinTypesResponse()
