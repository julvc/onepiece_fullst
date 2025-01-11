from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional
from bson import ObjectId

from app.models.luffygear import LuffyGear

class LuffyTechnique(BaseModel):
    id: Optional[str] = Field(alias="id")
    name: str
    translation: str
    type: str
    description: str
    after_ellipsis: bool
    # The line `luffy_gear: LuffyGear` in the `LuffyTechnique` class is defining a field named
    # `luffy_gear` of type `LuffyGear`. This field represents a relationship between `LuffyTechnique`
    # and `LuffyGear` models, indicating that a `LuffyTechnique` instance can have a reference to a
    # `LuffyGear` instance. This is a way to establish a one-to-one relationship between the two
    # models in the data structure.
    luffy_gear: LuffyGear

    model_config: ConfigDict = {
        'populate_by_name': True
    }
    
    # Validación adicional para convertir ObjectId a str
    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value