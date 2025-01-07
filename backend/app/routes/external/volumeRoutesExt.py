from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
import requests
from app.config import settings
from fastapi.logger import logger
from app.models.volume import Volume

logger.setLevel("DEBUG")

router = APIRouter()
BASE_URL = f"{settings.API_URL}"

@router.get("/en", summary="List all volumes")
async def list_volumes():
    try:
        response = requests.get(f"{BASE_URL}/tomes/en")
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [Volume(**item) for item in valid_data if item]
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")

@router.get("/en/search", response_model=List[Volume], summary="Search volume by name")
async def search_volumes(title: Optional[str] = None):
    try:
        params = {}
        if title:
            params = {"title": title}
        response = requests.get(f"{BASE_URL}/tomes/en/search", params=params)
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [Volume(**item) for item in valid_data if item]
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")

@router.get("/en/count", summary="Get count for volume")
async def count_volumes():
    try:
        response = requests.get(f"{BASE_URL}/tomes/en/count")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")

@router.get("/en/{volume_id}", response_model=Volume, summary="Get volume by ID")
async def get_volume(volume_id: int):
    try:
        response = requests.get(f"{BASE_URL}/tomes/en/{volume_id}")
        response.raise_for_status()
        return Volume(**response.json())
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")
    