from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import List, Optional, Union
from bson import ObjectId

from app.models.character import Character
from app.models.crew import Crew

class Boat(BaseModel):
    id: Optional[Union[str, int]] = Field(alias="_id")
    name: str
    job: Optional[str] = None
    size: Optional[str] = None
    birthday: Optional[str] = None
    age: Optional[str] = None
    bounty: Optional[str] = None
    status: Optional[str] = None
    crew: Crew
    # crew: List[Crew]
    character_captain: Character

    model_config: ConfigDict = {
        'populate_by_name': True
    }

    # Validación adicional para convertir ObjectId a str
    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value