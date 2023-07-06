from fastapi import FastAPI

from .routers import recruit

app = FastAPI()

app.include_router(recruit.router)
