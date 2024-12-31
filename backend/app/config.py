from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    API_URL: str = "https://api.api-onepiece.com/v2"
    MONGO_URI: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "onepiece"

    model_config: ConfigDict = {
        "env_file": ".env"
    }

settings = Settings()