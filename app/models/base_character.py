from typing import Optional

from pydantic import BaseModel

from app.models.abilities.ability import Ability


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
