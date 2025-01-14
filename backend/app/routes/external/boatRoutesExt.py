from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
import requests
from app.config import settings
from fastapi.logger import logger
from app.models.boat import Boat
logger.setLevel("DEBUG")

router = APIRouter()
BASE_URL = f"{settings.API_URL}"

@router.get("/en", summary="List all boats")
async def get_boats():
    try:
        response = requests.get(f"{BASE_URL}/boats/en")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/en/search",response_model=List[Boat] ,summary="Search boat by name")
async def search_boats(
    name: Optional[str] = None, 
    type: Optional[str] = None ):
    try:

        params = {}
        if name:
            params["name"] = name
        if type:
            params["type"] = type
        
        print("PAGINA SEARCH")
        print(f"{BASE_URL}/fruits/en/search",params)
        response = requests.get(f"{BASE_URL}/boats/en/search", params=params)
        response.raise_for_status()
        data = response.json()
        
        valid_data = [Boat(**item) for item in data if item]
        return valid_data
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/en/count", summary="Get boat count")
async def get_boats_count():
    try:
        response = requests.get(f"{BASE_URL}/boats/en/count")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/en/{boat_id}", response_model=Boat, summary="Get boat by id")
async def get_boat_by_id(boat_id: int):
    try:
        response = requests.get(f"{BASE_URL}/boats/en/{boat_id}")
        response.raise_for_status()
        return Boat(**response.json())
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

# @router.get("/en/crew/{crew_id}", response_model=List[Boat], summary="Get boats by crew")
# async def get_boats_by_crew(crew_id: int):
#     try:
#         # Solicitar los datos desde la API externa
#         response = requests.get(f"{BASE_URL}/boats/en/crew/{crew_id}")
#         response.raise_for_status()
#         boats_data = response.json()

#         # Depuración inicial: revisa los datos antes de procesarlos con el modelo
#         print("Datos originales:", boats_data)

#         # Procesar los datos con el modelo Boat
#         # processed_boats = [Boat(**boat).model_dump() for boat in boats_data]
#         processed_boats = [Boat(**boat).model_dump(exclude_none=True) for boat in boats_data]

#         # Depuración final: revisa los datos procesados
#         print("Datos procesados:", processed_boats)

#         return processed_boats

#     except requests.exceptions.RequestException as e:
#         raise HTTPException(status_code=500, detail=str(e))

@router.get(
    "/en/crew/{crew_id}",
    response_model=List[Boat],
    response_model_exclude_none=True,
    summary="Get boats by crew",
)
async def get_boats_by_crew(crew_id: int):
    try:
        # Solicitar los datos desde la API externa
        response = requests.get(f"{BASE_URL}/boats/en/crew/{crew_id}")
        response.raise_for_status()
        boats_data = response.json()

        # Procesar los datos con el modelo Boat
        processed_boats = [Boat(**boat) for boat in boats_data]

        return processed_boats

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/en/count/crew/{crew_id}", summary="Get boat count by saga")
async def get_boats_count_by_crew(crew_id: int):
    try:
        response = requests.get(f"{BASE_URL}/boats/en/count/crew/{crew_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/en/captain/{captain_id}", response_model=List[Boat], summary="Get boats by type")
async def get_boats_by_captain(captain_id: int):
    try:
        response = requests.get(f"{BASE_URL}/boats/en/captain/{captain_id}")
        response.raise_for_status()
        return [Boat(**item) for item in response.json()]
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/en/count/captain/{captain_id}", summary="Get boat count by type")
async def get_boats_count_by_captain(captain_id: int):
    try:
        response = requests.get(f"{BASE_URL}/boats/en/count/captain/{captain_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
