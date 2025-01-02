from fastapi import APIRouter, HTTPException, Depends
from app.db.mongo import mongodb, object_id
from app.models.saga import Saga
from typing import List
from deep_translator import GoogleTranslator

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
    response = await mongodb.db.sagas.find().to_list(100)
    
        # Campos específicos para traducir
    fields_to_translate = ["saga_chapitre", "saga_volume", "saga_episode"]
    sagas = translate_json_with_cache(response, fields_to_translate=fields_to_translate)
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


# def translate_json_in_bulk(json_data, fields_to_translate=None, source="fr", target="es"):
#     """
#     Traduce solo campos específicos de un objeto JSON, en bloques.

#     Args:
#         json_data (list): Lista de objetos JSON a traducir.
#         fields_to_translate (list): Lista de nombres de los campos que se deben traducir.
#         source (str): Idioma fuente (por defecto, 'fr').
#         target (str): Idioma destino (por defecto, 'es').

#     Returns:
#         list: Lista de objetos JSON traducidos.
#     """
#     if fields_to_translate is None:
#         fields_to_translate = []

#     translated_data = []
#     translator = GoogleTranslator(source=source, target=target)

#     for item in json_data:
#         # Extraer valores a traducir
#         values_to_translate = [item[key] for key in fields_to_translate if key in item and isinstance(item[key], str)]
        
#         # Traducir en bloque
#         if values_to_translate:
#             translated_values = translator.translate_batch(values_to_translate)
        
#         # Crear nuevo objeto con las traducciones
#         translated_item = {
#             key: translated_values.pop(0) if key in fields_to_translate and isinstance(item[key], str) else item[key]
#             for key in item
#         }
#         translated_data.append(translated_item)

#     return translated_data


translation_cache = {}

def translate_with_cache(text, source="fr", target="es"):
    if text in translation_cache:
        return translation_cache[text]

    translator = GoogleTranslator(source=source, target=target)
    translated_text = translator.translate(text)
    translation_cache[text] = translated_text
    return translated_text


def translate_json_with_cache(json_data, fields_to_translate=None, source="fr", target="es"):
    if fields_to_translate is None:
        fields_to_translate = []

    translated_data = []

    for item in json_data:
        translated_item = {
            key: translate_with_cache(item[key], source, target) if key in fields_to_translate and isinstance(item[key], str) else item[key]
            for key in item
        }
        translated_data.append(translated_item)

    return translated_data
