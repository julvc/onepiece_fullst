from pydantic import BaseModel, Field, ConfigDict,field_validator
from typing import Optional
from bson import ObjectId

class Sword(BaseModel):
    id: Optional[str] = Field(alias="_id")
    name: str
    roman_name: str
    type: str
    category: str
    description: str
    isDestroy: bool

    model_config: ConfigDict = {
        'populate_by_name': True  # Nueva forma de configurar
    }

    # Validación adicional para convertir ObjectId a str
    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value