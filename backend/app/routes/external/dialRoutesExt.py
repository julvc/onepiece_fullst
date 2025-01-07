from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
import requests
from app.config import settings
from fastapi.logger import logger
from app.models.dial import Dial

logger.setLevel("DEBUG")

router = APIRouter()
BASE_URL = f"{settings.API_URL}"

@router.get("/en", summary="List all dials")
async def get_dials():
    try:
        response = requests.get(f"{BASE_URL}/dials/en")
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [Dial(**item) for item in valid_data if item]
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/en/search",response_model=List[Dial] ,summary="Search dial by name")
async def search_dials(
    name: Optional[str] = None,
    type: Optional[str] = None):
    try:
        params = {}
        if name:
            params["name"] = name
        if type:
            params["type"] = type
        response = requests.get(f"{BASE_URL}/dials/en/search", params=params)
        response.raise_for_status()
        data = response.json()
        valid_data = [Dial(**item) for item in data if item]
        return valid_data
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/en/count", summary="Get count for dial")
async def get_dials_count():
    try:
        response = requests.get(f"{BASE_URL}/dials/en/count")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/en/{dial_id}", response_model=Dial, summary="Get dial by ID")
async def get_dials_en_by_id(dial_id: int):
    try:
        response = requests.get(f"{BASE_URL}/dials/en/{dial_id}")
        response.raise_for_status()
        data = response.json()
        return Dial(**data)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    