from typing import Optional, Union
from bson import ObjectId
from pydantic import BaseModel, ConfigDict, Field, field_validator

class Fruit(BaseModel):
    id: Optional[Union[str, int]] = Field(None, alias="_id")  # Hacer que sea None por defecto
    name: str
    description: Optional[str] = None
    roman_name: Optional[str] = None
    type: Optional[str] = None
    filename: Optional[str] = None
    technicalFile: Optional[str] = None

    model_config: ConfigDict = {
        'populate_by_name': True  # Nueva forma de configurar
    }
    
    # Validación adicional para convertir ObjectId a str
    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId) or isinstance(value, int):
            return str(value)
        return value