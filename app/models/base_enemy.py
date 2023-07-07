from app.models.abilities.ability import Ability
from app.models.base_character import BaseCharacter


class BaseEnemy(BaseCharacter):
    abilities: list[Ability]
