from fastapi import APIRouter
from pydantic import BaseModel

from domain.modifier import Modifier

modifier_router = APIRouter(prefix="/modifiers", tags=["modifiers"])


class ModifiersResponse(BaseModel):
    strength: str = Modifier.STRENGTH.value
    dexterity: str = Modifier.DEXTERITY.value
    constitution: str = Modifier.CONSTITUTION.value
    intellect: str = Modifier.INTELLECT.value
    wisdom: str = Modifier.WISDOM.value
    charisma: str = Modifier.CHARISMA.value


@modifier_router.get("")
async def get_modifiers() -> ModifiersResponse:
    return ModifiersResponse()
