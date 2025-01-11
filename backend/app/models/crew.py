from pydantic import BaseModel, Field, ConfigDict,field_validator
from typing import Optional
from bson import ObjectId

class Crew(BaseModel):
    id: Optional[int] = Field(alias="id")
    name: str
    description: Optional[str] = None
    status: Optional[str] = None
    number: Optional[str] = None
    roman_name: Optional[str] = None
    total_prime: Optional[str] = None
    is_yonko: Optional[str] = None

    model_config: ConfigDict = {
        'populate_by_name': True  # Nueva forma de configurar
    }
    
    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value
    
    @field_validator("is_yonko", mode="before")
    def validate_is_yonko(cls, value):
        if isinstance(value, bool):
            return str(value)  # Convierte True/False a 'True'/'False'
        return value