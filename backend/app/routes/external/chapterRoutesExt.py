from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
import requests
from app.config import settings
from fastapi.logger import logger
from app.models.chapter import Chapter

logger.setLevel("DEBUG")

router = APIRouter()
BASE_URL = f"{settings.API_URL}"

@router.get("/en", summary="List all chapters")
async def get_chapters():
    try:
        response = requests.get(f"{BASE_URL}/en/chapters")
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [Chapter(**item) for item in valid_data if item]
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/search",response_model=List[Chapter] ,summary="Search chapter by name")
async def search_chapter(title: Optional[str] = None):
    try:
        params = {}
        if title:
            params["title"] = title
        response = requests.get(f"{BASE_URL}/chapters/en/search", params=params)
        response.raise_for_status()
        data = response.json()
        valid_data = [Chapter(**item) for item in data if item]
        return valid_data
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/en/count", summary="Get chapter count")
async def get_chapter_count():
    try:
        response = requests.get(f"{BASE_URL}/chapters/en/count")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/{chapter_id}", response_model=Chapter, summary="Get chapter by id")
async def get_chapter(chapter_id: int):
    try:
        response = requests.get(f"{BASE_URL}/chapters/en/{chapter_id}")
        response.raise_for_status()
        return Chapter(**response.json())
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/tome/{tome_id}", response_model=List[Chapter], summary="Get chapters by Tome id")
async def get_chapters_by_tome(tome_id: int):
    try:
        response = requests.get(f"{BASE_URL}/en/tome/{tome_id}/chapters")
        response.raise_for_status()
        return [Chapter(**item) for item in response.json() if item]
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/tome/{tome_id}/count", summary="Get chapter count by Tome id")
async def get_chapter_count_by_tome(tome_id: int):
    try:
        response = requests.get(f"{BASE_URL}/en/tome/{tome_id}/chapters")
        response.raise_for_status()
        return len(response.json())
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
