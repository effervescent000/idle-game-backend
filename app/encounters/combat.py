from typing import Sequence

from app.models import BaseEnemy, BaseHero, CombatLog


def run_combat(
    *, heroes: Sequence[BaseHero], enemies: Sequence[BaseEnemy]
) -> CombatLog:
    for x in [*heroes, *enemies]:
        x.refresh()
    log = CombatLog(heroes=heroes, enemies=enemies)

    return log
