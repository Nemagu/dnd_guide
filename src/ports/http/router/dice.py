from fastapi import APIRouter
from pydantic import BaseModel

from domain.dice import DiceType

dice_router = APIRouter(prefix="/dices", tags=["dices"])


class DiceTypesResponse(BaseModel):
    d4: int = DiceType.D4.value
    d6: int = DiceType.D6.value
    d8: int = DiceType.D8.value
    d10: int = DiceType.D10.value
    d12: int = DiceType.D12.value
    d20: int = DiceType.D20.value
    d100: int = DiceType.D100.value


@dice_router.get("/types")
async def get_dice_types() -> DiceTypesResponse:
    return DiceTypesResponse()
