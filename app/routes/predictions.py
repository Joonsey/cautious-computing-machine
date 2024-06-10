from time import time
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from sceptile.interface import ComTypes

from app.db import get_session
from app.models import prediction
from app.common import client

router = APIRouter(prefix="/prediction")

def _map_status(sign: str) -> prediction.PredictionStatus:
    if sign == ComTypes.RESULT:
        return prediction.PredictionStatus.SUCCESS
    else:
        return prediction.PredictionStatus.ERROR

@router.post("/", response_model=prediction.Prediction)
async def create_prediction(prediction_request: prediction.PredictionCreate, session: AsyncSession = Depends(get_session)):
    start_time = time() * 1000
    sign, result = client.predict(prediction_request.image_path)
    total_time = int(time() * 1000 - start_time)

    status = _map_status(sign)
    db_prediction = prediction.Prediction(
        image_path=prediction_request.image_path,
        context=prediction_request.context,
        result=result,
        time_to_compute_ms=total_time,
        status=status,
        model=""
    )
    session.add(db_prediction)
    await session.commit()
    await session.refresh(db_prediction)

    if status != prediction.PredictionStatus.SUCCESS:
        # We have to assume that the user-delivered content is breaking the api
        #    therefore it's okay to return 400
        raise HTTPException(400, "something went wrong")

    return db_prediction
