from typing import Sequence

from app.models.combat.log import CombatLog
from app.models.base_hero import BaseHero
from app.models.base_enemy import BaseEnemy


def run_combat(
    *, heroes: Sequence[BaseHero], enemies: Sequence[BaseEnemy]
) -> CombatLog:
    for x in [*heroes, *enemies]:
        x.refresh()
    log = CombatLog(heroes=heroes, enemies=enemies)
    while log.rounds < 50 and (log.heroes_alive is True and log.enemies_alive is True):
        log.rounds += 1

    if log.rounds >= 50:
        log.add_error(f"Combat log timed out ({log.rounds} rounds)")

    return log
