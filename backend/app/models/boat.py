from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import List, Optional, Union
from bson import ObjectId

from app.models.character import Character
from app.models.crew import Crew

class Boat(BaseModel):
    id: Optional[Union[str, int]] = Field(alias="_id")
    name: str
    description: Optional[str] = None
    type: Optional[str] = None
    roman_name: Optional[str] = None
    crew: Optional[Crew] = None
    character_captain: Optional[Character] = None

    model_config: ConfigDict = {
        'populate_by_name': True
    }

    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value

    def model_dump(self, *args, **kwargs):
        kwargs.setdefault('exclude_none', True)  # Asegúrate de que 'exclude_none' sea True por defecto
        return super().model_dump(*args, **kwargs)
