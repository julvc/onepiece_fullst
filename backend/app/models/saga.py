from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class Saga(BaseModel):
    id: Optional[int] = Field(alias="_id")
    title: str
    saga_number: Optional[str] = None
    saga_chapitre: Optional[str] = None
    saga_volume: Optional[str] = None
    saga_episode: Optional[str] = None

    model_config: ConfigDict = {
        'populate_by_name': True  # Nueva forma de configurar
    }