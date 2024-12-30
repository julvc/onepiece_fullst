from fastapi import APIRouter
import requests
from app.config import settings

router = APIRouter()

@router.get("/sagas")
async def get_sagas():
    response = requests.get(f"{settings.API_URL}/saga")
    return response.json()

@router.get("/characters")
async def get_characters():
    response = requests.get(f"{settings.API_URL}/character")
    return response.json()