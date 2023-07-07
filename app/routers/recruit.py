from fastapi import APIRouter

from app.models.heroes.dancer import Dancer

router = APIRouter(prefix="/recruit")


@router.get("/")
async def generate_recruits():
    heroes = [Dancer.create_new()]
    return heroes
