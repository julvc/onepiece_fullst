from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
import requests
from app.config import settings
from fastapi.logger import logger
from app.models.episode import Episode

logger.setLevel("DEBUG")

router = APIRouter()
BASE_URL = f"{settings.API_URL}"

@router.get("/en", summary="List all episodes")
async def get_episodes():
    try:
        response = requests.get(f"{BASE_URL}/episodes/en")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/en/search",response_model=List[Episode] ,summary="Search episode by name")
async def search_episodes(
    title: Optional[str] = None):
    try:
        params = {}
        if title:
            params = {"title": title}
        response = requests.get(f"{BASE_URL}/episodes/en/search", params=params)
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [Episode(**item) for item in valid_data if item]
        return valid_data
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/en/count", summary="Get count for episode")
async def get_episodes_count():
    try:
        response = requests.get(f"{BASE_URL}/episodes/en/count")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/en/{episode_id}", response_model=Episode, summary="Get episode by ID")
async def get_episode_by_id(episode_id: int):
    try:
        response = requests.get(f"{BASE_URL}/episodes/en/{episode_id}")
        response.raise_for_status()
        data = response.json()

        # Asegúrate de que '_id' esté presente en los datos
        if "_id" not in data:
            data["_id"] = None  # O cualquier valor predeterminado

        return Episode(**data)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/count/saga/{saga_id}",summary="Get count episodes by saga")
async def get_count_episodes_by_saga(saga_id: int):
    try:
        response = requests.get(f"{BASE_URL}/episodes/en/count/saga/{saga_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/count/arc/{arc_id}",summary="Get count episodes by arc")
async def get_count_episodes_by_arc(arc_id: int):
    try:
        response = requests.get(f"{BASE_URL}/episodes/en/count/arc/{arc_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/search/saga",response_model=List[Episode] ,summary="Search episode by saga")
async def search_episodes_by_saga(
    title: Optional[str] = None):
    try:
        params = {}
        if title:
            params = {"title": title}
        response = requests.get(f"{BASE_URL}/episodes/en/search/saga", params=params)
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [Episode(**item) for item in valid_data if item]
        return valid_data
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/saga/{saga_id}", summary="Get episodes by saga ID")
async def get_episodes_by_sagaid(saga_id: int):
    try:
        response = requests.get(f"{BASE_URL}/episodes/en/saga/{saga_id}")
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [Episode(**item) for item in valid_data if item]
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

#TIENE PROBLEMAS DESDE LA API EXTERNA
# @router.get("/en/search/arc",response_model=List[Episode] ,summary="Search episode by saga")
# async def search_episodes_by_arc(
#     title: Optional[str] = None):
#     try:
#         params = {}
#         if title:
#             params = {"title": title}
#         response = requests.get(f"{BASE_URL}/episodes/en/search/arc", params=params)
#         response.raise_for_status()
#         valid_data = response.json()
#         valid_data = [Episode(**item) for item in valid_data if item]
#         return valid_data
#     except ValidationError as e:
#         logger.error(f"Error: {e}")
#         raise HTTPException(status_code=422, detail="Unprocessable Entity")
#     except requests.exceptions.RequestException as e:
#         logger.error(f"Error: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/arc/{arc_id}", summary="Get episodes by saga ID")
async def get_episodes_by_arcid(arc_id: int):
    try:
        response = requests.get(f"{BASE_URL}/episodes/en/arc/{arc_id}")
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [Episode(**item) for item in valid_data if item]
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
