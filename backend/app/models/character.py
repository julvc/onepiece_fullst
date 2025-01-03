from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional
from bson import ObjectId
from backend.app.models.crew import Crew
from backend.app.models.fruit import Fruit

class Character(BaseModel):
    id: Optional[str] = Field(alias="_id")
    name: str
    job: Optional[str] = None
    size: Optional[str] = None
    birthday: Optional[str] = None
    age: Optional[str] = None
    bounty: Optional[str] = None
    status: Optional[str] = None
    crew: Crew
    fruit: Fruit

    model_config: ConfigDict = {
        'populate_by_name': True
    }

    # Validación adicional para convertir ObjectId a str
    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value
