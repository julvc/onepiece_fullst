from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
import requests
from app.config import settings
from fastapi.logger import logger
from app.models.haki import Haki

logger.setLevel("DEBUG")

router = APIRouter()
BASE_URL = f"{settings.API_URL}"

@router.get("/en", summary="List all hakis")
async def get_hakis():
    try:
        response = requests.get(f"{BASE_URL}/hakis/en")
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [Haki(**item) for item in valid_data if item]
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    
@router.get("/en/search",response_model=List[Haki] ,summary="Search haki by name")
async def search_hakis(
    name: Optional[str] = None,
    roman_name: Optional[str] = None):
    try:
        params = {}
        if name:
            params = {"name": name}
        if roman_name:
            params = {"roman_name": roman_name}
        response = requests.get(f"{BASE_URL}/hakis/en/search", params=params)
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [Haki(**item) for item in valid_data if item]
        return valid_data
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/en/count", summary="Get count for haki")
async def get_hakis_count():
    try:
        response = requests.get(f"{BASE_URL}/hakis/en/count")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/character/{haki_id}/count", response_model=Haki, summary="Get haki by Character ID")
async def get_haki_by_character_id(haki_id: int):
    try:
        response = requests.get(f"{BASE_URL}/hakis/en/character/{haki_id}/count")
        response.raise_for_status()
        return Haki(**response.json())
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/en/{haki_id}", response_model=Haki, summary="Get haki by ID")
async def get_haki_by_id(haki_id: int):
    try:
        response = requests.get(f"{BASE_URL}/hakis/en/{haki_id}")
        response.raise_for_status()
        return Haki(**response.json())
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/en/character/{character_id}", response_model=List[Haki], summary="Get haki by Character ID")
async def get_hakis_by_character_id(character_id: int):
    try:
        response = requests.get(f"{BASE_URL}/hakis/en/character/{character_id}")
        response.raise_for_status()
        valid_data = response.json()
        
        if isinstance(valid_data, int):
            return {"count": valid_data}
        
        valid_data = [Haki(**item) for item in valid_data if item]
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")