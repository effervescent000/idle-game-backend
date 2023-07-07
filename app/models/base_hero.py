from __future__ import annotations

from pydantic import BaseModel


class BaseHero(BaseModel):
    name: str
    level: int
    max_health: int
    max_mana: int

    @classmethod
    def create_new(cls) -> BaseHero:
        """Should be overwritten in sub-classes"""
        raise NotImplementedError
