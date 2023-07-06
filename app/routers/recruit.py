from fastapi import APIRouter

router = APIRouter(prefix="/recruit")


@router.get("/")
async def generate_recruits():
    return {"Message": "Hello World"}
