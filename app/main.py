from fastapi import FastAPI


from .routers import recruit, combat


app = FastAPI()

app.include_router(recruit.router)
app.include_router(combat.router)
