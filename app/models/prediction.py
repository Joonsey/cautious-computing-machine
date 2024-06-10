from enum import StrEnum, auto
import uuid

from typing import Optional
from sqlmodel import Field, SQLModel


class PredictionStatus(StrEnum):
    SUCCESS = auto()
    ERROR = auto()


class PredictionBase(SQLModel):
    image_path: str


class PredictionCreate(PredictionBase):
    context: Optional[str]


class Prediction(PredictionCreate, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    result: str
    time_to_compute_ms: int
    model: str
    status: PredictionStatus


class PredictionInsertResponse(PredictionBase):
    result: str
