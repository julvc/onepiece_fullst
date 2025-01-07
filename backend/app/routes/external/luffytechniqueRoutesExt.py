from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
import requests
from app.config import settings
from fastapi.logger import logger
from app.models.luffytechnique import LuffyTechnique

logger.setLevel("DEBUG")

router = APIRouter()
BASE_URL = f"{settings.API_URL}"

@router.get("/en", summary="List all Luffy's techniques")
async def get_luffy_techniques():
    try:
        response = requests.get(f"{BASE_URL}/luffy_techniques/en")
        response.raise_for_status()
        valid_data = response.json()
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")

@router.get("/en/search", response_model=List[LuffyTechnique], summary="Search techniques by name or translation")
async def search_luffy_techniques(
    name: Optional[str] = None, 
    translation: Optional[str] = None):
    try:
        params = {}
        if name:
            params["name"] = name
        if translation:
            params["translation"] = translation
        response = requests.get(f"{BASE_URL}/luffy-techniques/en/search", params=params)
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [LuffyTechnique(**item) for item in valid_data if item]
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")
    
@router.get("/en/count", summary="Get count for Luffy's techniques")
async def count_volumes():
    try:
        response = requests.get(f"{BASE_URL}/luffy-techniques/en/count")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")

@router.get("/en/gear/{gear_id}/count", summary="Get count by Gear ID")
async def get_count_by_gear_id(gear_id: int):
    try:
        response = requests.get(f"{BASE_URL}/luffy-techniques/en/gear/{gear_id}/count")
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity") 


@router.get("/en/gear/{gear_id}", response_model=LuffyTechnique, summary="Get techniques by gear ID")
async def get_techniques_by_gear_id(gear_id: int):
    try:
        response = requests.get(f"{BASE_URL}/luffy-techniques/en/gear/{gear_id}")
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [LuffyTechnique(**item) for item in valid_data if item]
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/{gear_id}", response_model=LuffyTechnique, summary="Get film by ID")
async def get_techniques_by_id(gear_id: int):
    try:
        response = requests.get(f"{BASE_URL}/luffy-techniques/en/{gear_id}")
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [LuffyTechnique(**item) for item in valid_data if item]
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
