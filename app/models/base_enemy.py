from pydantic import BaseModel

from app.models.abilities.ability import Ability


class BaseEnemy(BaseModel):
    name: str
    level: int
    max_health: int
    max_mana: int
    abilities: list[Ability]
