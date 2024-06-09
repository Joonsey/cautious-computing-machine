from time import time
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import prediction
from app.common import client

router = APIRouter(prefix="/prediction")

@router.post("/", response_model=prediction.Prediction)
async def create_prediction(prediction_request: prediction.PredictionCreate, session: AsyncSession = Depends(get_session)):
    start_time = time() * 1000
    result = client.predict(prediction_request.image_path)
    total_time = int(time() * 1000 - start_time)

    db_prediction = prediction.Prediction(
        image_path=prediction_request.image_path,
        context=prediction_request.context,
        result=result,
        time_to_compute_ms=total_time,
        model=""
    )
    session.add(db_prediction)
    await session.commit()
    await session.refresh(db_prediction)
    return db_prediction
