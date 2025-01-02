from fastapi import APIRouter, HTTPException, Depends
from app.db.mongo import mongodb, object_id
from app.models.saga import Saga
from typing import List


router = APIRouter()

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
    sagas = await mongodb.db.sagas.find().to_list(100)
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


#region CODIGO COMENTADO PARA PROBAR TODOS LOS ENDPOINTS DE SAGAS
# @router.post("/sagas", response_model=Saga, summary="Create a new saga")
# async def create_saga(saga: Saga):
#     result = await mongodb.db.sagas.insert_one(saga.model_dump(by_alias=True))
#     saga.id = str(result.inserted_id)
#     return saga

# @router.get("/sagas", summary="Get all sagas")
# async def get_all_sagas():
#     sagas = await mongodb.db.sagas.find().to_list(100)
#     return sagas

# @router.get("/sagas/{id}", response_model=Saga, summary="Get a saga by ID")
# async def get_saga(id: str):
#     saga = await mongodb.db.sagas.find_one({"_id": object_id(id)})
#     if not saga:
#         raise HTTPException(status_code=404, detail="Saga not found")
#     return saga

# @router.put("/sagas/{id}", response_model=Saga, summary="Update a saga")
# async def update_saga(id: str, saga: Saga):
#     result = await mongodb.db.sagas.replace_one({"_id": object_id(id)}, saga.model_dump(by_alias=True))
#     if result.matched_count == 0:
#         raise HTTPException(status_code=404, detail="Saga not found")
#     saga.id = id
#     return saga

# @router.delete("/sagas/{id}", summary="Delete a saga")
# async def delete_saga(id: str):
#     result = await mongodb.db.sagas.delete_one({"_id": object_id(id)})
#     if result.deleted_count == 0:
#         raise HTTPException(status_code=404, detail="Saga not found")
#     return {"message": "Saga deleted"}

#endregion