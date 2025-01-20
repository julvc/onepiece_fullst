from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional, Union
from bson import ObjectId

from app.models.saga import Saga

class Bow(BaseModel):
    id: Optional[Union[str, int]] = Field(default=None, alias="_id")
    title: Optional[str] = None
    description: Optional[str] = None
    sagaId: Optional[Union[str, int]] = Field(alias="sagaId", default=None)
    saga: Optional[Saga] = None
    
    model_config: ConfigDict = {
        'populate_by_name': True
    }
    
    # Validación adicional para convertir ObjectId a str
    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId) or isinstance(value, int):
            return str(value)
        return value
    
    def model_dump(self, *args, **kwargs):
        kwargs.setdefault('exclude_none', True)  # Asegúrate de que 'exclude_none' sea True por defecto
        return super().model_dump(*args, **kwargs)