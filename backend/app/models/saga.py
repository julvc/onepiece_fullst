from pydantic import BaseModel, Field, ConfigDict,field_validator
from typing import Optional, Union
from bson import ObjectId

class Saga(BaseModel):
    id: Optional[Union[str, int]] = Field(alias="_id")
    title: str
    saga_number: Optional[str] = None
    saga_chapitre: Optional[str] = None
    saga_volume: Optional[str] = None
    saga_episode: Optional[str] = None

    model_config: ConfigDict = {
        'populate_by_name': True  # Nueva forma de configurar
    }

    # Validación adicional para convertir ObjectId a str
    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId) or isinstance(value, int):
            return str(value)
        return value