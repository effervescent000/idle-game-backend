from typing import Literal, Optional, Sequence

from pydantic import BaseModel


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

    def calc_damage(self, *, targets: Sequence["BaseCharacter"]) -> float:
        return self.base_damage * len(targets)


class BaseCharacter(BaseModel):
    name: str
    level: int
    max_health: int
    cur_health: Optional[float] = None
    max_mana: int
    cur_mana: Optional[float] = None
    abilities: list[Ability] = []

    def refresh(self) -> None:
        self.cur_health = self.max_health
        self.cur_mana = self.max_mana

    def action(
        self, *, targets: Sequence["BaseEnemy"], selected_ability: Ability
    ) -> "Action":
        """Should be overwritten in sub-classes"""
        raise NotImplementedError

    def apply_damage(self, amount: float) -> None:
        self.cur_health = (
            self.cur_health - amount
            if self.cur_health is not None
            else self.max_health - amount
        )

    def can_act(self) -> bool:
        """For now just checks HP but will eventually look for things like stuns
        and multi-turn moves in progress."""
        if self.cur_health is not None and self.cur_health > 0:
            return True
        return False


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
    abilities: list[Ability] = []
    hero_class: Literal["dancer"]

    @classmethod
    def create_new(cls) -> "BaseHero":
        """Should be overwritten in sub-classes"""

        raise NotImplementedError

    def upgrade_to_level(self, level: int) -> None:
        """Should be overwritten in sub-classes"""

        raise NotImplementedError


class BaseEnemy(BaseCharacter):
    abilities: list[Ability]


class Action(BaseModel):
    ability: Ability
    actor: BaseCharacter
    targets: Sequence[BaseCharacter]
    damage: Optional[float] = None
    # TODO the next line will deal with buffs/debuffs
    # effects: Optional[list[Effects]]
