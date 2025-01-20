from pydantic import BaseModel, Field, ConfigDict,field_validator
from typing import Optional, Union
from bson import ObjectId

class Dial(BaseModel):
    id: Optional[Union[str, int]] = Field(default=None, alias="_id")
    name: Optional[str] = None
    type: Optional[str] = None
    translation: Optional[str] = None
    description: Optional[str] = None

    model_config: ConfigDict = {
        'populate_by_name': True  # Nueva forma de configurar
    }

    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId) or isinstance(value, int):
            return str(value)
        return value
