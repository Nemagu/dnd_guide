from fastapi import APIRouter
from pydantic import BaseModel

from domain.damage_type import DamageType

damage_type_router = APIRouter(prefix="/damages", tags=["damages"])


class DamageTypesResponse(BaseModel):
    acid: str = DamageType.ACID.value
    bludgeoning: str = DamageType.BLUDGEONING.value
    cold: str = DamageType.COLD.value
    fire: str = DamageType.FIRE.value
    force: str = DamageType.FORCE.value
    lightning: str = DamageType.LIGHTNING.value
    necrotic: str = DamageType.NECROTIC.value
    piercing: str = DamageType.PIERCING.value
    poison: str = DamageType.POISON.value
    psychic: str = DamageType.PSYCHIC.value
    radiant: str = DamageType.RADIANT.value
    slashing: str = DamageType.SLASHING.value
    thunder: str = DamageType.THUNDER.value


@damage_type_router.get("/types")
async def get_damage_types() -> DamageTypesResponse:
    return DamageTypesResponse()
