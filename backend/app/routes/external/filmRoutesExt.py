from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
import requests
from app.config import settings
from fastapi.logger import logger
from app.models.film import Film

logger.setLevel("DEBUG")

router = APIRouter()
BASE_URL = f"{settings.API_URL}"

@router.get("/en", summary="List all films")
async def get_all_films():
    try:
        response = requests.get(f"{BASE_URL}/movies/en")
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [Film(**item) for item in valid_data if item]
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/search", response_model=List[Film], summary="Search film by title")
async def search_films(
    title: Optional[str] = None):
    try:
        response = requests.get(f"{BASE_URL}/movies/en/search/{title}")
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [Film(**item) for item in valid_data if item]
        return valid_data
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/count", summary="Get count for films")
async def get_count():
    try:
        response = requests.get(f"{BASE_URL}/movies/en/count")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/{film_id}", response_model=Film, summary="Get film by ID")
async def get_film_by_id(film_id: int):
    try:
        response = requests.get(f"{BASE_URL}/movies/en/{film_id}")
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [Film(**item) for item in valid_data if item]
        return valid_data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/en/search/count", response_model=List[Film], summary="Get episodes for film")
async def get_count_movies_by_search(
    title: Optional[str] = None):
    try:
        params = {}
        if title:
            params = {"title": title}
        response = requests.get(f"{BASE_URL}/movies/en/search/count", params=params)
        response.raise_for_status()
        valid_data = response.json()
        valid_data = [Film(**item) for item in valid_data if item]
        return valid_data
    except ValidationError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=422, detail="Unprocessable Entity")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

