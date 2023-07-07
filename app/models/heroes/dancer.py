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
