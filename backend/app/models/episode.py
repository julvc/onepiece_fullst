from datetime import date
from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional
from bson import ObjectId

from app.models.bow import Bow
from app.models.saga import Saga

class Episode(BaseModel):
    id: Optional[str] = Field(alias="id")
    number: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    chapter: Optional[str] = None
    release_date: Optional[date] = None
    arcId: Optional[int] = None
    sagaId: Optional[int] = None
    saga: Saga
    arc: Bow

    model_config: ConfigDict = {
        'populate_by_name': True
    }

    # Validación adicional para convertir ObjectId a str
    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value