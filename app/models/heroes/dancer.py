from app.models.base_hero import BaseHero


class Dancer(BaseHero):
    @classmethod
    def create_new(cls) -> Dancer:
        return cls(name="test", level=1, max_health=100, max_mana=100)
