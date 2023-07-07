from app.models.base_hero import BaseHero, Ability


class Dancer(BaseHero):
    @classmethod
    def create_new(cls) -> "Dancer":
        return cls(
            name="test",
            level=1,
            max_health=10,
            max_mana=10,
            attacks=[Ability.make_standard_attack(base_damage=5)],
        )

    def upgrade_to_level(self, target_level: int) -> None:
        skill_map = {
            10: Ability(
                name="Cascade", base_damage=10, cooldown=2, damage_coefficient=0.5
            )
        }
        skills_to_append = [
            value
            for [key, value] in skill_map.items()
            if target_level >= key > self.level
        ]

        for skill in skills_to_append:
            self.attacks.append(skill)
