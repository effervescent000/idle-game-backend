from app.models.heroes.dancer import Dancer
from app.models.enemies.mook import Mook

from ..combat import run_combat


def test_run_combat_basic() -> None:
    heroes = [Dancer.create_new()]
    enemies = [Mook.create_new()]

    result = run_combat(heroes=heroes, enemies=enemies)
    assert len(result.errors) == 0
