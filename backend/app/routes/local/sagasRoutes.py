from fastapi import APIRouter, HTTPException, Depends
from app.db.mongo import mongodb, object_id
from app.models.saga import Saga
from typing import List
from app.utils.populate import translate_json_with_cache

router = APIRouter()
class SagaRoutes:
    translation_cache_all = {}
    translation_cache_id = {}

@router.post("/", response_model=Saga, summary="Create a new saga")
async def create_saga(saga: Saga):
    result = await mongodb.db.sagas.insert_one(saga.model_dump(by_alias=True))
    saga.id = str(result.inserted_id)
    return saga

@router.get("/", summary="Obtener todas las Sagas",
        description="Lista todas las sagas que se encuentran en la BBDD.",
        response_model=List[Saga],
        responses={
        200: {
            "description": "Lista de sagas disponibles.",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "_id": "63f4e16e2b7c9d1b9df5b87f",
                            "title": "East Blue",
                            "saga_number": "1",
                            "saga_chapitre": "1 à 100",
                            "saga_volume": "1 à 12",
                            "saga_episode": "1 à 61"
                        }
                    ]
                }
            }
        },
        404: {"description": "No existen sagas en la base datos."},
    },)
async def get_all_sagas():
    response = await mongodb.db.sagas.find().to_list(100)
    
    # Campos específicos para traducir
    fields_to_translate = ["saga_chapitre", "saga_volume", "saga_episode"]
        # Usamos el cache de la clase para la traducción
    sagas = await translate_json_with_cache(
        response, 
        fields_to_translate=fields_to_translate,
        cache=SagaRoutes.translation_cache_all  # Usamos el cache definido en la clase
    )
    return [Saga(**saga) for saga in sagas]

@router.get("/{id}", response_model=Saga, summary="Get a saga by ID")
async def get_saga(id: str):
    saga = await mongodb.db.sagas.find_one({"_id": object_id(id)})
    if not saga:
        raise HTTPException(status_code=404, detail="Saga not found")
    return saga

@router.put("/{id}", response_model=Saga, summary="Update a saga")
async def update_saga(id: str, saga: Saga):
    result = await mongodb.db.sagas.replace_one({"_id": object_id(id)}, saga.model_dump(by_alias=True))
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Saga not found")
    saga.id = id
    return saga

@router.delete("/{id}", summary="Delete a saga")
async def delete_saga(id: str):
    result = await mongodb.db.sagas.delete_one({"_id": object_id(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Saga not found")
    return {"message": "Saga deleted"}

