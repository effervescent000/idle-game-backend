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
