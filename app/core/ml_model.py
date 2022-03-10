from pydantic import BaseModel
from typing import Optional


class ConfusionMatrix(BaseModel):
    labels: list[str]
    values: list[list[float]]


class MLModel(BaseModel):
    name: str
    version: str
    active: bool
    location: str
    remarks: str
    cls: str
    cm:  Optional[ConfusionMatrix] = None
