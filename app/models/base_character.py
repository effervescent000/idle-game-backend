from typing import Optional

from pydantic import BaseModel


class BaseCharacter(BaseModel):
    name: str
    level: int
    max_health: int
    cur_health: Optional[float]
    max_mana: int
    cur_mana: Optional[float]

    def refresh(self) -> None:
        self.cur_health = self.max_health
        self.cur_mana = self.max_mana
