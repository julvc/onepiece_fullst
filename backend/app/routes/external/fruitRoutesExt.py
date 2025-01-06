from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
import requests
from app.config import settings
from fastapi.logger import logger
from app.models.fruit import Fruit
logger.setLevel("DEBUG")

router = APIRouter()
BASE_URL = f"{settings.API_URL}"

@router.get("/en", summary="List all fruits")
async def get_fruits():
    try:
        response = requests.get(f"{BASE_URL}/fruits/en")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/en/search",response_model=List[Fruit] ,summary="Search fruit by name")
async def search_fruit(
    name: Optional[str] = None, 
    type: Optional[str] = None 
    ):
    try:
        # Construir los parámetros dinámicamente
        params = {}
        if name:
            params["name"] = name
        if type:
            params["type"] = type
        
        response = requests.get(f"{BASE_URL}/fruits/en/search", params=params)
        response.raise_for_status()
        data = response.json()
        
        # Validar y convertir los datos
        valid_data = [Fruit(**item) for item in data if item]
        return valid_data
    except ValidationError as e:
        print(f"Validation Error: {e}")
        raise HTTPException(status_code=422, detail="Invalid data format in API response")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/en/count", summary="Get fruit count")
async def get_fruit_count():
    try:
        response = requests.get(f"{BASE_URL}/fruits/en/count")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/en/{fruit_id}", response_model=Fruit, summary="Get fruit by id")
async def get_fruit(fruit_id: int):
    try:
        response = requests.get(f"{BASE_URL}/fruits/en/{fruit_id}")
        response.raise_for_status()
        return Fruit(**response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/en/search/count", summary="Get fruit count by search")
async def get_fruit_count_by_search(
    name: Optional[str] = None, 
    type: Optional[str] = None, 
    ):
    try:
        params = {}
        if name:
            params["name"] = name
        if type:
            params["type"] = type
        response = requests.get(f"{BASE_URL}/fruits/en/search/count", params=params)
        response.raise_for_status()
        data = response.json()
        
        # Validar y convertir los datos
        valid_data = [Fruit(**item) for item in data if item]
        return valid_data
    except ValidationError as e:
        print(f"Validation Error: {e}")
        raise HTTPException(status_code=422, detail="Invalid data format in API response")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))