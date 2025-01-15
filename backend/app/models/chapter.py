from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional, Union
from bson import ObjectId

from app.models.volume import Volume

class Chapter(BaseModel):
    id: Optional[Union[str, int]] = Field(alias="_id")
    chapter_number: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    tome: Optional[Volume] = None

    model_config: ConfigDict = {
        'populate_by_name': True
    }

    # Validación adicional para convertir ObjectId a str
    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value