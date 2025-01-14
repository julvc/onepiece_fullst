from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
import requests
from app.config import settings
from fastapi.logger import logger
from app.models.bow import Bow
# from app.models.saga import Saga
logger.setLevel("DEBUG")

router = APIRouter()
BASE_URL = f"{settings.API_URL}"

@router.get("/en", summary="List all arcs")
async def get_arcs():
    try:
        response = requests.get(f"{BASE_URL}/arcs/en")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/en/search",response_model=List[Bow] ,summary="Search arc by title")
async def search_arc(title: Optional[str] = None):
    try:
        params = {}
        if title:
            params["title"] = title
        response = requests.get(f"{BASE_URL}/arcs/en/search", params=params)
        response.raise_for_status()
        data = response.json()
        
        valid_data = [Bow(**item) for item in data if item]
        return valid_data
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/en/count", summary="Get arc count")
async def get_arc_count():
    try:
        response = requests.get(f"{BASE_URL}/arcs/en/count")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/en/{bow_id}", response_model=Bow, summary="Get arc by id")
async def get_arc(bow_id: int):
    try:
        response = requests.get(f"{BASE_URL}/arcs/en/{bow_id}")
        response.raise_for_status()
        return Bow(**response.json())
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/en/saga/{saga_id}", response_model=List[Bow], summary="Get arcs by saga")
async def get_arcs_by_saga(saga_id: int):
    try:
        response = requests.get(f"{BASE_URL}/arcs/en/saga/{saga_id}")
        response.raise_for_status()
        data = response.json()
        valid_data = [Bow(**item) for item in data if item]
        return valid_data
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/en/count/saga/{saga_id}", summary="Get arc count by saga")
async def get_arc_count_by_saga(saga_id: int):
    try:
        response = requests.get(f"{BASE_URL}/arcs/en/count/saga/{saga_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))