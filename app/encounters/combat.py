from typing import Sequence

from app.models.combat.log import CombatLog
from app.models.base import BaseHero, BaseEnemy, Action


def apply_action(action: Action) -> None:
    for x in action.targets:
        if action.damage is not None:
            x.apply_damage(action.damage)


def run_combat(
    *, heroes: Sequence[BaseHero], enemies: Sequence[BaseEnemy]
) -> CombatLog:
    for x in [*heroes, *enemies]:
        x.refresh()
    log = CombatLog(heroes=heroes, enemies=enemies)
    # TODO determine speed stat and order turns. for now it's just set
    while log.rounds < 50 and (log.heroes_alive is True and log.enemies_alive is True):
        for x in heroes:
            if x.can_act() is True:
                target = enemies[0]
                selected_ability = x.abilities[0]
                result = x.action(targets=[target], selected_ability=selected_ability)
                apply_action(result)
                log.add_event(result)
        log.rounds += 1

    if log.rounds >= 50:
        log.add_error(f"Combat log timed out ({log.rounds} rounds)")

    return log
