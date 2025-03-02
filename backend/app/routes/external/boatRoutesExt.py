from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
import httpx
from app.config import settings
from fastapi.logger import logger
from app.models.boat import Boat

logger.setLevel("DEBUG")

router = APIRouter()
BASE_URL = f"{settings.API_URL}"

@router.get("/en", summary="List all boats")
async def get_boats(
    limit: Optional[int] = Query(None, description="Número máximo de registros a devolver"),
    offset: Optional[int] = Query(None, description="Número de registros a saltar")
):
    try:
        params = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
            
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/boats/en", params=params)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Error de estado HTTP: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except httpx.RequestError as e:
        logger.error(f"Error de solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error de conexión con la API externa")
    
@router.get("/en/search", response_model=List[Boat], summary="Search boat by name")
async def search_boats(
    name: Optional[str] = None, 
    type: Optional[str] = None,
    limit: Optional[int] = Query(None, description="Número máximo de registros a devolver"),
    offset: Optional[int] = Query(None, description="Número de registros a saltar")
):
    try:
        params = {}
        if name:
            params["name"] = name
        if type:
            params["type"] = type
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        
        logger.debug(f"Realizando búsqueda en {BASE_URL}/boats/en/search con params: {params}")
        
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/boats/en/search", params=params)
            response.raise_for_status()
            data = response.json()
            
            valid_data = [Boat(**item) for item in data if item]
            return valid_data
    except ValueError as e:
        logger.error(f"Error de validación: {e}")
        raise HTTPException(status_code=422, detail=f"Error de validación: {str(e)}")
    except httpx.HTTPStatusError as e:
        logger.error(f"Error de estado HTTP: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except httpx.RequestError as e:
        logger.error(f"Error de solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error de conexión con la API externa")
    
@router.get("/en/count", summary="Get boat count")
async def get_boats_count():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/boats/en/count")
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Error de estado HTTP: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except httpx.RequestError as e:
        logger.error(f"Error de solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error de conexión con la API externa")
    
@router.get("/en/{boat_id}", response_model=Boat, summary="Get boat by id")
async def get_boat_by_id(boat_id: int):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/boats/en/{boat_id}")
            response.raise_for_status()
            return Boat(**response.json())
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"Barco con ID {boat_id} no encontrado")
        logger.error(f"Error de estado HTTP: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except httpx.RequestError as e:
        logger.error(f"Error de solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error de conexión con la API externa")
    except ValueError as e:
        logger.error(f"Error de validación: {e}")
        raise HTTPException(status_code=422, detail=f"Error en datos recibidos: {str(e)}")

@router.get("/en/crew/{crew_id}", response_model=List[Boat], response_model_exclude_none=True, summary="Get boats by crew")
async def get_boats_by_crew(
    crew_id: int,
    limit: Optional[int] = Query(None, description="Número máximo de registros a devolver"),
    offset: Optional[int] = Query(None, description="Número de registros a saltar")
):
    try:
        params = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
            
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/boats/en/crew/{crew_id}", params=params)
            response.raise_for_status()
            boats_data = response.json()
            
            # Procesar los datos con el modelo Boat
            processed_boats = [Boat(**boat) for boat in boats_data if boat]
            return processed_boats
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"No se encontraron barcos para la tripulación {crew_id}")
        logger.error(f"Error de estado HTTP: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except httpx.RequestError as e:
        logger.error(f"Error de solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error de conexión con la API externa")
    except ValueError as e:
        logger.error(f"Error de validación: {e}")
        raise HTTPException(status_code=422, detail=f"Error en datos recibidos: {str(e)}")

@router.get("/en/count/crew/{crew_id}", summary="Get boat count by crew")
async def get_boats_count_by_crew(crew_id: int):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/boats/en/count/crew/{crew_id}")
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Error de estado HTTP: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except httpx.RequestError as e:
        logger.error(f"Error de solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error de conexión con la API externa")

@router.get("/en/captain/{captain_id}", response_model=List[Boat], response_model_exclude_none=True, summary="Get boats by captain")
async def get_boats_by_captain(
    captain_id: int,
    limit: Optional[int] = Query(None, description="Número máximo de registros a devolver"),
    offset: Optional[int] = Query(None, description="Número de registros a saltar")
):
    try:
        params = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
            
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/boats/en/captain/{captain_id}", params=params)
            response.raise_for_status()
            boats_data = response.json()
            
            # Procesar los datos con el modelo Boat
            processed_boats = [Boat(**boat) for boat in boats_data if boat]
            return processed_boats
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"No se encontraron barcos para el capitán {captain_id}")
        logger.error(f"Error de estado HTTP: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except httpx.RequestError as e:
        logger.error(f"Error de solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error de conexión con la API externa")
    except ValueError as e:
        logger.error(f"Error de validación: {e}")
        raise HTTPException(status_code=422, detail=f"Error en datos recibidos: {str(e)}")

@router.get("/en/count/captain/{captain_id}", summary="Get boat count by captain")
async def get_boats_count_by_captain(captain_id: int):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/boats/en/count/captain/{captain_id}")
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Error de estado HTTP: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except httpx.RequestError as e:
        logger.error(f"Error de solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error de conexión con la API externa")