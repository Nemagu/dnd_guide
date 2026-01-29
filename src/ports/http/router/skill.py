from fastapi import APIRouter
from pydantic import BaseModel

from domain.skill import Skill

skill_router = APIRouter(prefix="/skills", tags=["skills"])


class SkillsResponse(BaseModel):
    acrobatics: str = Skill.ACROBATICS.value
    athletics: str = Skill.ATHLETICS.value
    perception: str = Skill.PERCEPTION.value
    survival: str = Skill.SURVIVAL.value
    animal_handling: str = Skill.ANIMAL_HANDLING.value
    intimidation: str = Skill.INTIMIDATION.value
    performance: str = Skill.PERFORMANCE.value
    history: str = Skill.HISTORY.value
    sleight_of_hand: str = Skill.SLEIGHT_OF_HAND.value
    arcana: str = Skill.ARCANA.value
    medicine: str = Skill.MEDICINE.value
    deception: str = Skill.DECEPTION.value
    nature: str = Skill.NATURE.value
    insight: str = Skill.INSIGHT.value
    investigation: str = Skill.INVESTIGATION.value
    religion: str = Skill.RELIGION.value
    stealth: str = Skill.STEALTH.value
    persuasion: str = Skill.PERSUASION.value


@skill_router.get("")
async def get_skills() -> SkillsResponse:
    return SkillsResponse()
