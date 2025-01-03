from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional
from bson import ObjectId

from backend.app.models.saga import Saga

class Bow(BaseModel):
    id: Optional[str] = Field(alias="id")
    title: Optional[str] = None
    description: Optional[str] = None
    saga: Saga
    
    model_config: ConfigDict = {
        'populate_by_name': True
    }
    
    # Validación adicional para convertir ObjectId a str
    @field_validator("id", mode="before")
    def validate_id(self, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value