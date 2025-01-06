from pydantic import BaseModel, Field, ConfigDict,field_validator
from typing import Optional, Union
from bson import ObjectId

class Location(BaseModel):
    id: Optional[Union[str, int]] = Field(alias="_id")
    name: str
    roman_name: Optional[str] = None
    sea_name: Optional[str] = None
    region_name: Optional[str] = None
    affiliation_name: Optional[str] = None

    model_config: ConfigDict = {
        'populate_by_name': True  # Nueva forma de configurar
    }

    # Validador para convertir `id` a `str` si es `ObjectId` o `int`
    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId) or isinstance(value, int):
            return str(value)
        return value