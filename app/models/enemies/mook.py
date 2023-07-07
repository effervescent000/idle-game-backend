from app.models.abilities.ability import Ability
from app.models.base_enemy import BaseEnemy


class Mook(BaseEnemy):
    @classmethod
    def create_new(cls, level: int = 1) -> "Mook":
        return cls(
            name="Generic Mook",
            level=level,
            max_health=5 * level,
            max_mana=5 * level,
            abilities=[Ability.make_standard_attack(base_damage=5 * level)],
        )
