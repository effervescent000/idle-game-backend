from typing import Sequence

from fastapi import APIRouter

from app.models.base import BaseHero
from app.models.combat.log import CombatLog

from app.utils.utils import wrapData

router = APIRouter(prefix="/recruit")


@router.post("/")
async def run_encounter(heroes: Sequence[BaseHero]) -> dict[str, CombatLog]:
    ...
