from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
import requests
from app.config import settings
from fastapi.logger import logger
from app.models.location import Location

logger.setLevel("DEBUG")

router = APIRouter()
BASE_URL = f"{settings.API_URL}"

@router.get("/en", summary="List all locates")
async def get_locates():
    try:
        response = requests.get(f"{BASE_URL}/locates/en")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/en/search",response_model=List[Location] ,summary="Search locate by title")
async def search_locate(
    name: Optional[str] = None, 
    sea: Optional[str] = None, 
    affiliation: Optional[str] = None
    ):
    try:
        # Construir los parámetros dinámicamente
        params = {}
        if name:
            params["name"] = name
        if sea:
            params["sea"] = sea
        if affiliation:
            params["affiliation"] = affiliation
        
        response = requests.get(f"{BASE_URL}/locates/en/search", params=params)
        response.raise_for_status()
        data = response.json()
        
        # Validar y convertir los datos
        valid_data = [Location(**item) for item in data if item]
        return valid_data
    except ValidationError as e:
        print(f"Validation Error: {e}")
        raise HTTPException(status_code=422, detail="Invalid data format in API response")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
        
@router.get("/en/count", summary="Get locate count")
async def get_locate_count():
    try:
        response = requests.get(f"{BASE_URL}/locates/en/count")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/en/{id}", summary="Get locate by ID")
async def get_locate(id: int):
    try:
        response = requests.get(f"{BASE_URL}/locates/en/{id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    