import pytest

from domain.exception import DomainException
from domain.skill import Skill


@pytest.mark.parametrize(
    "skill",
    [
        Skill.ACROBATICS,
        Skill.ATHLETICS,
        Skill.PERCEPTION,
        Skill.SURVIVAL,
        Skill.ANIMAL_HANDLING,
        Skill.INTIMIDATION,
        Skill.PERFORMANCE,
        Skill.HISTORY,
        Skill.SLEIGHT_OF_HAND,
        Skill.ARCANA,
        Skill.MEDICINE,
        Skill.DECEPTION,
        Skill.NATURE,
        Skill.INSIGHT,
        Skill.INVESTIGATION,
        Skill.RELIGION,
        Skill.STEALTH,
        Skill.PERSUASION,
    ],
)
def test_skill_ok(skill):
    new_skill = Skill.from_str(skill.name.lower())
    assert skill == new_skill
    new_skill = Skill.from_str(skill.name.upper())
    assert skill == new_skill


def test_invalid_skill_name():
    with pytest.raises(DomainException):
        Skill.from_str("invalid")
