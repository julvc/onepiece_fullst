from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
import requests
from app.config import settings
from fastapi.logger import logger
from app.models.crew import Crew

logger.setLevel("DEBUG")

router = APIRouter()
BASE_URL = f"{settings.API_URL}"

@router.get("/en", summary="List all crews")
async def get_crews():
    try:
        response = requests.get(f"{BASE_URL}/crews/en")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/yonko", summary="List all crews")
async def get_crews():
    try:
        response = requests.get(f"{BASE_URL}/crews/en/yonko")
        response.raise_for_status()
        logger.info(f"Respuesta de la API externa: {response.json()}")  # Depuración
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/search",response_model=List[Crew] ,summary="Search crew by name")
async def search_crews(
    name: Optional[str] = None,
    status: Optional[str] = None):
    try:
        params = {}
        if name:
            params["name"] = name
        if status:
            params["status"] = status
        
        response = requests.get(f"{BASE_URL}/crews/en/search", params=params)
        response.raise_for_status()
        data = response.json()
        valid_data = [Crew(**item) for item in data if item]
        return valid_data
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")
    
@router.get("/en/count", summary="Get count for volume")
async def count_crews():
    try:
        response = requests.get(f"{BASE_URL}/tomes/en/count")
        response.raise_for_status()
        count = response.json()  # Suponiendo que esto devuelve un número
        return {"count": count}  # Envuelve el número en un diccionario
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")

@router.get("/en/{crew_id}", response_model=Crew, summary="Get crew by ID")
async def get_crews_by_id(crew_id: int):
    try:
        response = requests.get(f"{BASE_URL}/crews/en/{crew_id}")
        response.raise_for_status()
        data = response.json()
        return Crew(**data)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/yonko/count", summary="Get count for crew")
async def get_crews_count_by_yonko():
    try:
        response = requests.get(f"{BASE_URL}/crews/en/yonko/count")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# @router.get("/en/yonko", summary="List all crews")
# async def get_crews():
#     try:
#         response = requests.get(f"{BASE_URL}/crews/en/yonko")
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         logger.error(f"Error: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

