from typing import Union, Optional, Sequence

from pydantic import BaseModel

from app.models.base import Ability, BaseCharacter, BaseEnemy, BaseHero, Action


class LogError(BaseModel):
    round_num: int
    message: str


class LogEvent(BaseModel):
    actor: Union[BaseEnemy, BaseHero]
    targets: Optional[Sequence[BaseCharacter]]
    ability: Ability
    round_num: int
    # `damage` is negative for healing
    damage: Optional[float] = None


class CombatLog(BaseModel):
    log: list[LogEvent] = []
    rounds: int = 1
    errors: list[LogError] = []
    heroes: Sequence[BaseHero]
    enemies: Sequence[BaseEnemy]

    @property
    def heroes_alive(self) -> bool:
        return any([x.cur_health is not None and x.cur_health > 0 for x in self.heroes])

    @property
    def enemies_alive(self) -> bool:
        return any(
            [x.cur_health is not None and x.cur_health > 0 for x in self.enemies]
        )

    def add_error(self, message: str) -> None:
        self.errors.append(LogError(round_num=self.rounds, message=message))

    def add_event(self, action: Action) -> None:
        self.log.append(
            LogEvent(
                round_num=self.rounds,
                actor=action.actor,
                targets=action.targets,
                damage=action.damage,
                ability=action.ability,
            )
        )
