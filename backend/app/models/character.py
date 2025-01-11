from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional, Union
from bson import ObjectId
from app.models.crew import Crew
from app.models.fruit import Fruit

class Character(BaseModel):
    id: Optional[Union[str, int]] = Field(alias="_id")
    name: str
    size: Optional[str] = None
    job: Optional[str] = None
    status: Optional[str] = None
    age: Optional[str] = None
    bounty: Optional[str] = None
    crew: Crew
    fruit: Optional[Fruit]

    model_config: ConfigDict = {
        'populate_by_name': True
    }

    # Validación adicional para convertir ObjectId a str
    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value
