from domain.creature import CreatureSize, CreatureType
from fastapi import APIRouter
from pydantic import BaseModel, Field

creature_router = APIRouter(prefix="/creatures", tags=["creatures"])


class CreatureTypesResponse(BaseModel):
    aberration: str = CreatureType.ABERRATION.value
    beast: str = CreatureType.BEAST.value
    celestial: str = CreatureType.CELESTIAL.value
    construct_field: str = Field(
        default=CreatureType.CONSTRUCT.value, alias="construct"
    )
    dragon: str = CreatureType.DRAGON.value
    elemental: str = CreatureType.ELEMENTAL.value
    fey: str = CreatureType.FEY.value
    fiend: str = CreatureType.FIEND.value
    giant: str = CreatureType.GIANT.value
    humanoid: str = CreatureType.HUMANOID.value
    monstrosity: str = CreatureType.MONSTROSITY.value
    ooze: str = CreatureType.OOZE.value
    plant: str = CreatureType.PLANT.value
    undead: str = CreatureType.UNDEAD.value
    transport: str = CreatureType.TRANSPORT.value
    object: str = CreatureType.OBJECT.value


class CreatureSizesResponse(BaseModel):
    tiny: str = CreatureSize.TINY.value
    small: str = CreatureSize.SMALL.value
    medium: str = CreatureSize.MEDIUM.value
    large: str = CreatureSize.LARGE.value
    huge: str = CreatureSize.HUGE.value
    gargantuan: str = CreatureSize.GARGANTUAN.value


@creature_router.get("/types")
async def get_creature_types() -> CreatureTypesResponse:
    return CreatureTypesResponse()


@creature_router.get("/sizes")
async def get_creature_sizes() -> CreatureSizesResponse:
    return CreatureSizesResponse()
