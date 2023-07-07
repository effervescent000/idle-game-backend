from pydantic import BaseModel

from app.models.abilities.ability import Ability
from app.models.base_character import BaseCharacter


def get_skills_to_append(
    *, target_level: int, current_level: int, skill_map: dict[int, Ability]
) -> list[Ability]:
    return [
        value
        for [key, value] in skill_map.items()
        if target_level >= key > current_level
    ]


class Stat(BaseModel):
    name: str
    amount: int


class BaseHero(BaseCharacter):
    # XXX eventually we'll get rid of this stats field
    # and derive stats based on gear
    stats: list[Stat] = []
    attacks: list[Ability] = []

    @classmethod
    def create_new(cls) -> "BaseHero":
        """Should be overwritten in sub-classes"""
        raise NotImplementedError

    def upgrade_to_level(self, level: int) -> None:
        """Should be overwritten in sub-classes"""
        raise NotImplementedError
