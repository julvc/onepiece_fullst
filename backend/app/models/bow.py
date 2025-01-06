from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional, Union
from bson import ObjectId

from app.models.saga import Saga

class Bow(BaseModel):
    id: Optional[Union[str, int]] = Field(alias="_id")
    title: Optional[str] = None
    description: Optional[str] = None
    saga: Saga
    
    model_config: ConfigDict = {
        'populate_by_name': True
    }
    
    # Validación adicional para convertir ObjectId a str
    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId) or isinstance(value, int):
            return str(value)
        return value