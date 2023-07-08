from typing import Sequence

from app.models.base import (
    Ability,
    Action,
    BaseHero,
    BaseEnemy,
    get_skills_to_append,
)


class Dancer(BaseHero):
    @classmethod
    def create_new(cls) -> "Dancer":
        return cls(
            name="test",
            level=1,
            max_health=10,
            max_mana=10,
            abilities=[Ability.make_standard_attack(base_damage=5)],
        )

    def upgrade_to_level(self, target_level: int) -> None:
        skill_map = {
            10: Ability(
                name="Cascade", base_damage=10, cooldown=2, damage_coefficient=0.5
            ),
            20: Ability(
                name="Fountain", base_damage=12, cooldown=2, damage_coefficient=0.5
            ),
            30: Ability(
                name="Windmill",
                base_damage=4,
                cooldown=2,
                damage_coefficient=0.5,
                targets=4,
            ),
        }

        skills_to_append = get_skills_to_append(
            target_level=target_level, current_level=self.level, skill_map=skill_map
        )

        for skill in skills_to_append:
            self.abilities.append(skill)

    def action(
        self, *, targets: Sequence[BaseEnemy], selected_ability: Ability
    ) -> Action:
        dmg = selected_ability.calc_damage(targets=targets)
        result = Action(
            ability=selected_ability, actor=self, targets=targets, damage=dmg
        )
        return result
