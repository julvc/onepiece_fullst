from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional
from bson import ObjectId

from app.models.volume import Volume

class Chapter(BaseModel):
    id: Optional[str] = Field(alias="id")
    chapter_number: Optional[str] = None
    title: str
    description: Optional[str] = None
    tome: Volume

    model_config: ConfigDict = {
        'populate_by_name': True
    }

    # Validación adicional para convertir ObjectId a str
    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value