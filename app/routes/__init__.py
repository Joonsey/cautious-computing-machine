from fastapi import APIRouter

from app.routes import predictions

apis = APIRouter()

apis.include_router(predictions.router)
