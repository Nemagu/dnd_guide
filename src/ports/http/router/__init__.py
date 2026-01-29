from fastapi import APIRouter

from .coin import coin_router
from .creature import creature_router
from .damage import damage_type_router
from .dice import dice_router
from .game_time import game_time_router
from .length import length_router
from .modifier import modifier_router
from .skill import skill_router
from .source import source_router
from .weight import weight_router

router_v1 = APIRouter(prefix="/v1", tags=["v1"])
router_v1.include_router(coin_router)
router_v1.include_router(creature_router)
router_v1.include_router(damage_type_router)
router_v1.include_router(dice_router)
router_v1.include_router(game_time_router)
router_v1.include_router(length_router)
router_v1.include_router(modifier_router)
router_v1.include_router(skill_router)
router_v1.include_router(source_router)
router_v1.include_router(weight_router)

router = APIRouter(prefix="/api")
router.include_router(router_v1)
