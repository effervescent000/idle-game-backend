from typing import Sequence

from fastapi import APIRouter

from app.models.base_hero import BaseHero
from app.models.heroes.dancer import Dancer

router = APIRouter(prefix="/recruit")


@router.get("/")
async def generate_recruits() -> Sequence[BaseHero]:
    heroes = [Dancer.create_new()]
    return heroes
