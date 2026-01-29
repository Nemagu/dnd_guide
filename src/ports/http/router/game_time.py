from fastapi import APIRouter
from pydantic import BaseModel

from domain.game_time import GameTimeUnit

game_time_router = APIRouter(prefix="/game-times", tags=["game_times"])


class GameTimeUnitsResponse(BaseModel):
    action: str = GameTimeUnit.ACTION.value
    bonus_action: str = GameTimeUnit.BONUS_ACTION.value
    reaction: str = GameTimeUnit.REACTION.value
    minute: str = GameTimeUnit.MINUTE.value
    hour: str = GameTimeUnit.HOUR.value


@game_time_router.get("/units")
async def get_game_time_units() -> GameTimeUnitsResponse:
    return GameTimeUnitsResponse()
