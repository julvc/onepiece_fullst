from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
import requests
from app.config import settings
from fastapi.logger import logger
from app.models.sword import Sword

logger.setLevel("DEBUG")

router = APIRouter()
BASE_URL = f"{settings.API_URL}"

@router.get("/en", summary="List all swords")
async def list_swords():
    try:
        response = requests.get(f"{BASE_URL}/swords/en")
        response.raise_for_status()
        valid_data = response.json()
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")
    
@router.get("/en/search", response_model=List[Sword], summary="Search sword by name")
async def search_sword(
    name: Optional[str] = None,
    type: Optional[str] = None):
    try:
        params = {}
        if name:
            params = {"name": name}
        if type:
            params = {"type": type}
        response = requests.get(f"{BASE_URL}/swords/en/search", params=params)
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [Sword(**item) for item in valid_data if item]
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")
    
@router.get("/en/state/count", summary="Get count for Swords for state")
async def count_sword(
    state: Optional[str] = None):
    try:
        params = {}
        if state:
            params = {"state": state}
        response = requests.get(f"{BASE_URL}/swords/en/count", params=params)
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [Sword(**item) for item in valid_data if item]
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")

@router.get("/en/state", response_model=List[Sword], summary="Search sword by name")
async def search_sword(
    state: Optional[str] = None):
    try:
        params = {}
        if state:
            params = {"state": state}
        response = requests.get(f"{BASE_URL}/swords/en/state", params=params)
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [Sword(**item) for item in valid_data if item]
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")
    
@router.get("/en/{sword_id}", response_model=Sword, summary="Get haki by ID")
async def get_haki_by_id(sword_id: int):
    try:
        response = requests.get(f"{BASE_URL}/swords/en/{sword_id}")
        response.raise_for_status()
        return Sword(**response.json())
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")