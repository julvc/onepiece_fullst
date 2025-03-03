from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
import httpx
from app.config import settings
from fastapi.logger import logger
from app.models.bow import Bow

logger.setLevel("DEBUG")

router = APIRouter()
BASE_URL = f"{settings.API_URL}"
NUM_MAX_REGS = "Número máximo de registros a devolver"
NUM_TO_JUMP = "Número de registros a saltar"
ERROR_API_MSG = "Error de conexión con la API externa"

@router.get("/en", summary="List all arcs")
async def get_arcs(
    limit: Optional[int] = Query(None, description=NUM_MAX_REGS),
    offset: Optional[int] = Query(None, description=NUM_TO_JUMP)
):
    try:
        params = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
            
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/arcs/en", params=params)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Error de estado HTTP: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except httpx.RequestError as e:
        logger.error(f"Error de solicitud: {e}")
        raise HTTPException(status_code=500, detail=ERROR_API_MSG)
    
@router.get("/en/search", response_model=List[Bow], summary="Search arc by title")
async def search_arc(
    title: Optional[str] = None,
    limit: Optional[int] = Query(None, description=NUM_MAX_REGS),
    offset: Optional[int] = Query(None, description=NUM_TO_JUMP)
):
    try:
        params = {}
        if title:
            params["title"] = title
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
            
        logger.debug(f"Realizando búsqueda en {BASE_URL}/arcs/en/search con params: {params}")
        
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/arcs/en/search", params=params)
            response.raise_for_status()
            data = response.json()
            
            valid_data = [Bow(**item) for item in data if item]
            return valid_data
    except ValueError as e:
        logger.error(f"Error de validación: {e}")
        raise HTTPException(status_code=422, detail=f"Error de validación: {str(e)}")
    except httpx.HTTPStatusError as e:
        logger.error(f"Error de estado HTTP: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except httpx.RequestError as e:
        logger.error(f"Error de solicitud: {e}")
        raise HTTPException(status_code=500, detail=ERROR_API_MSG)

@router.get("/en/count", summary="Get arc count")
async def get_arc_count():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/arcs/en/count")
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Error de estado HTTP: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except httpx.RequestError as e:
        logger.error(f"Error de solicitud: {e}")
        raise HTTPException(status_code=500, detail=ERROR_API_MSG)

@router.get("/en/{bow_id}", response_model=Bow, summary="Get arc by id")
async def get_arc(bow_id: int):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/arcs/en/{bow_id}")
            response.raise_for_status()
            return Bow(**response.json())
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"Arco con ID {bow_id} no encontrado")
        logger.error(f"Error de estado HTTP: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except httpx.RequestError as e:
        logger.error(f"Error de solicitud: {e}")
        raise HTTPException(status_code=500, detail=ERROR_API_MSG)
    except ValueError as e:
        logger.error(f"Error de validación: {e}")
        raise HTTPException(status_code=422, detail=f"Error en datos recibidos: {str(e)}")
    
@router.get("/en/saga/{saga_id}", response_model=List[Bow], summary="Get arcs by saga")
async def get_arcs_by_saga(
    saga_id: int,
    limit: Optional[int] = Query(None, description=NUM_MAX_REGS),
    offset: Optional[int] = Query(None, description=NUM_TO_JUMP)
):
    try:
        params = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
            
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/arcs/en/saga/{saga_id}", params=params)
            response.raise_for_status()
            data = response.json()
            valid_data = [Bow(**item) for item in data if item]
            return valid_data
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"No se encontraron arcos para la saga {saga_id}")
        logger.error(f"Error de estado HTTP: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except httpx.RequestError as e:
        logger.error(f"Error de solicitud: {e}")
        raise HTTPException(status_code=500, detail=ERROR_API_MSG)
    except ValueError as e:
        logger.error(f"Error de validación: {e}")
        raise HTTPException(status_code=422, detail=f"Error en datos recibidos: {str(e)}")
    
@router.get("/en/count/saga/{saga_id}", summary="Get arc count by saga")
async def get_arc_count_by_saga(saga_id: int):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/arcs/en/count/saga/{saga_id}")
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Error de estado HTTP: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except httpx.RequestError as e:
        logger.error(f"Error de solicitud: {e}")
        raise HTTPException(status_code=500, detail=ERROR_API_MSG)