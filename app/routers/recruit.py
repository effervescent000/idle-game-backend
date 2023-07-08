from typing import Sequence

from fastapi import APIRouter

from app.models.base import BaseHero
from app.models.heroes.dancer import Dancer

from app.utils.utils import wrapData

router = APIRouter(prefix="/recruit")


@router.get("/")
async def generate_recruits() -> dict[str, Sequence[BaseHero]]:
    heroes = [Dancer.create_new()]
    return wrapData(heroes)
