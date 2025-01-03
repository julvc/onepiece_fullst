from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import List, Optional
from bson import ObjectId

from backend.app.models.character import Character
from backend.app.models.crew import Crew

# class Captain(BaseModel):
#     id: Optional[str] = Field(alias="_id")
#     name: str
#     size: Optional[str] = None
#     job: Optional[str] = None
#     status: Optional[str] = None
#     age: Optional[str] = None
#     bounty: Optional[str] = None

class Boat(BaseModel):
    id: Optional[str] = Field(alias="_id")
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