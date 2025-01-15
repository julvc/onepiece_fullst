from typing import Optional, Union
from bson import ObjectId
from pydantic import BaseModel, ConfigDict, Field, field_validator


class Volume(BaseModel):
    id: Optional[Union[str, int]] = Field(alias="_id")
    tome_number: Optional[str] = None
    title: Optional[str] = None
    tome_japan_date_publish: Optional[str] = None
    tome_french_date_publish: Optional[str] = None
    
    model_config: ConfigDict = {
        'populate_by_name': True
    }

    # Validación adicional para convertir ObjectId a str
    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value