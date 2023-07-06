from __future__ import annotations

from typing import Literal

from pydantic import BaseModel

class BaseHero(BaseModel):
    name: str | None
    level: int
    hero_class: Literal["dancer"]
    max_health: int
    max_mana: int

    @classmethod
    def create_new(cls):
        """Should be overwritten in sub-classes"""
        raise NotImplementedError