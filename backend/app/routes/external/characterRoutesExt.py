from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
import requests
from app.config import settings
from fastapi.logger import logger
from app.models.character import Character

logger.setLevel("DEBUG")

router = APIRouter()
BASE_URL = f"{settings.API_URL}"

@router.get("/en", summary="List all characters")
async def get_characters():
    try:
        response = requests.get(f"{BASE_URL}/characters/en")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/en/search",response_model=List[Character] ,summary="Search character by name")
async def search_characters(
    name: Optional[str] = None,
    job: Optional[str] = None,
    bounty: Optional[str] = None,
    age: Optional[str] = None,
    size: Optional[str] = None):
    try:
        params = {}
        if name:
            params["name"] = name
        if job:
            params["job"] = job
        if bounty:
            params["bounty"] = bounty
        if age:
            params["age"] = age
        if size:
            params["size"] = size
                        
        response = requests.get(f"{BASE_URL}/characters/en/search", params=params)
        response.raise_for_status()
        data = response.json()
        valid_data = [Character(**item) for item in data if item]
        return valid_data
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/en/crew/{crew_id}", summary="Get characters by crew ID")
async def get_characters_by_crew_id(crew_id: int):
    try:
        response = requests.get(f"{BASE_URL}/characters/en/crew/{crew_id}")
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [Character(**item) for item in valid_data if item]
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/crew/{crew_id}/count", summary="Get character count")
async def get_character_count(crew_id: int):
    try:
        response = requests.get(f"{BASE_URL}/characters/en/crew/{crew_id}/count")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/en/{character_id}", response_model=Character, summary="Get character by id")
async def get_character(character_id: int):
    try:
        response = requests.get(f"{BASE_URL}/characters/en/{character_id}")
        response.raise_for_status()
        return Character(**response.json())
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

