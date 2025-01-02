import requests
from app.db.mongo import mongodb
from deep_translator import GoogleTranslator

async def populate_sagas():
    response = requests.get("https://api.api-onepiece.com/v2/sagas/en")
    if response.status_code == 200:
        sagas = response.json()
        await mongodb.db.sagas.insert_many(sagas)
        
        
# translation_cache = {}

# async def translate_with_cache(text, source="fr", target="es"):
#     if text in translation_cache:
#         return translation_cache[text]

#     translator = GoogleTranslator(source=source, target=target)
#     translated_text = translator.translate(text)
#     translation_cache[text] = translated_text
#     return translated_text


# async def translate_json_with_cache(json_data, fields_to_translate=None, source="fr", target="es"):
#     if fields_to_translate is None:
#         fields_to_translate = []

#     translated_data = []

#     for item in json_data:
#         translated_item = {
#             key: translate_with_cache(item[key], source, target) if key in fields_to_translate and isinstance(item[key], str) else item[key]
#             for key in item
#         }
#         translated_data.append(translated_item)

#     return translated_data


translation_cache = {}

async def translate_with_cache(text, source="fr", target="es", cache=None):
    if cache is None:
        cache = translation_cache  # Si no se pasa un caché, usa el caché global

    if text in cache:
        return cache[text]

    translator = GoogleTranslator(source=source, target=target)
    translated_text = translator.translate(text)
    cache[text] = translated_text
    return translated_text


async def translate_json_with_cache(json_data, fields_to_translate=None, source="fr", target="es", cache=None):
    if fields_to_translate is None:
        fields_to_translate = []

    translated_data = []

    for item in json_data:
        translated_item = {
            key: await translate_with_cache(item[key], source, target, cache)
            if key in fields_to_translate and isinstance(item[key], str)
            else item[key]
            for key in item
        }
        translated_data.append(translated_item)

    return translated_data
