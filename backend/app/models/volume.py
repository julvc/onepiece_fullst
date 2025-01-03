from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, ConfigDict, field_validator


class Volume(BaseModel):
    id: Optional[int]
    tome_number: str
    title: str
    tome_japan_date_publish: str
    tome_french_date_publish: str
    
    model_config: ConfigDict = {
        'populate_by_name': True
    }

    # Validación adicional para convertir ObjectId a str
    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value