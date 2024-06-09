import uuid

from typing import Optional
from sqlmodel import Field, SQLModel

class PredictionBase(SQLModel):
    image_path: str
    context: Optional[str]

class Prediction(PredictionBase, table=True):
    id: str = Field(default_factory= lambda : str(uuid.uuid4()), primary_key=True)
    result: str
    time_to_compute_ms: int
    model: str

class PredictionCreate(PredictionBase):
    pass
