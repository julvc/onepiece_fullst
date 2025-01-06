from fastapi import APIRouter, HTTPException
import requests
from app.config import settings
from fastapi.logger import logger
logger.setLevel("DEBUG")

router = APIRouter()
# BASE_URL = f"{settings.API_URL}/sagas/en"
BASE_URL = f"{settings.API_URL}"

@router.get("/sagas", summary="List all sagas")
async def get_sagas():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

# @router.get("/sagas/search", summary="Search saga by title")
# async def search_saga(title: str):
#     try:
#         response = requests.get(f"{BASE_URL}/sagas/en/search", params={"title": title})
#         print(f"Requesting URL: {BASE_URL}/sagas/en/search?title={title}")
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         raise HTTPException(status_code=500, detail=str(e))

@router.get("/sagas/search", summary="Search saga by title")
async def search_saga(title: str):
    try:
        response = requests.get(f"{BASE_URL}/sagas/en/search", params={"title": title})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")  # Debug
        raise HTTPException(status_code=500, detail=str(e))


# @router.get("/sagas/count", summary="Get saga count")
# async def get_saga_count():
#     try:
#         response = requests.get(f"{BASE_URL}/sagas/en/count")
#         print(f"Requesting URL: {BASE_URL}/sagas/en/count")
#         print("External API Response:", response.text)  # Agrega esto
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         raise HTTPException(status_code=500, detail=str(e))

@router.get("/sagas/count", summary="Get saga count")
async def get_saga_count():
    try:
        response = requests.get(f"{BASE_URL}/sagas/en/count")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")  # Debug
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/sagas/{id}", summary="Get saga by ID")
async def get_saga_by_id(id: int):
    try:
        response = requests.get(f"{BASE_URL}/sagas/en/{id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
