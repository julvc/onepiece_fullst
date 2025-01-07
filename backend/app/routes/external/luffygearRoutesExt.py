from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
import requests
from app.config import settings
from fastapi.logger import logger
from app.models.luffygear import LuffyGear

logger.setLevel("DEBUG")

router = APIRouter()
BASE_URL = f"{settings.API_URL}"

@router.get("/en", summary="List all LuffyGears")
async def get_luffy_gears():
    try:
        response = requests.get(f"{BASE_URL}/luffy-gears/en")
        response.raise_for_status()
        valid_data = response.json()
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")

@router.get("/en/{luffy_id}", response_model=LuffyGear, summary="Get haki by ID")
async def get_haki_by_id(luffy_id: int):
    try:
        response = requests.get(f"{BASE_URL}/luffy-gears/en/{luffy_id}")
        response.raise_for_status()
        return LuffyGear(**response.json())
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/en/count", summary="Get count for Luffy's gears")
async def count_luffygears():
    try:
        response = requests.get(f"{BASE_URL}/luffy-gears/en/count")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")
