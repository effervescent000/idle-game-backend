from __future__ import annotations

from pydantic import BaseModel


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


class Ability(BaseModel):
    name: str
    rank: int = 1
    execution_time: float = 0
    cooldown: float = 0
    base_damage: int
    damage_coefficient: float
    targets: int = 1

    @classmethod
    def make_standard_attack(cls, *, base_damage: int) -> "Ability":
        return cls(name="Attack", base_damage=base_damage, damage_coefficient=0.25)


class BaseHero(BaseModel):
    name: str
    level: int
    max_health: int
    max_mana: int
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
