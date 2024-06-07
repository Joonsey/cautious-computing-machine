from fastapi import FastAPI

from app.db import init_db
from app.models.feature_toggle import FeatureToggle

app = FastAPI()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

