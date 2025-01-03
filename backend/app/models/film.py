from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional
from bson import ObjectId

from backend.app.models.saga import Saga

class Film(BaseModel):
    id: Optional[str] = Field(alias="id")
    number: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    release_date: Optional[str] = None
    saga: Saga
    
    model_config: ConfigDict = {
        'populate_by_name': True
    }

    # Validación adicional para convertir ObjectId a str
    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value