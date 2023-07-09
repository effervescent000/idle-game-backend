from fastapi.testclient import TestClient
from app.models.combat.log import CombatLog
from app.models.heroes.dancer import Dancer

from app.main import app

client = TestClient(app)


def test_run_encounter() -> None:
    response = client.post("/combat/", json=[Dancer.create_new().dict()])
    assert response.status_code == 200
    log = CombatLog(**response.json()["data"])
    assert log.rounds < 50
