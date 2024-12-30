from pydantic import BaseSettings

class Settings(BaseSettings):
    API_URL: str = "https://api-onepiece.com/v1"
    MONGO_URI: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "onepiece"

settings = Settings()