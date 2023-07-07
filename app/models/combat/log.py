from typing import Union, Optional, Any, Sequence

from pydantic import BaseModel

from app.models import BaseEnemy, BaseHero, Ability


class LogEvent(BaseModel):
    actor: Union[BaseEnemy, BaseHero]
    targets: Optional[Union[BaseEnemy, BaseHero]]
    ability: Ability
    round_num: int
    # `damage_amount` is negative for healing
    damage_amount: int


class CombatLog(BaseModel):
    log: list[LogEvent] = []
    rounds: int = 1
    errors: list[dict[str, Any]] = []
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
