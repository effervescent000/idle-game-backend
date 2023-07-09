from typing import Sequence

from fastapi import APIRouter
from app.encounters.combat import generate_enemies, run_combat

from app.models.base import BaseHero
from app.models.combat.log import CombatLog
from app.models.heroes.dancer import Dancer

from app.utils.utils import wrapData

router = APIRouter(prefix="/combat")

class_map = {"dancer": Dancer}


@router.post("/")
async def run_encounter(team: Sequence[BaseHero]) -> dict[str, CombatLog]:
    try:
        heroes = [class_map[x.hero_class](**x.dict()) for x in team]
    except Exception as e:
        print(e)

    enemies = generate_enemies()
    result = run_combat(heroes=heroes, enemies=enemies)
    return wrapData(result)
