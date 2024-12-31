import requests
from app.db.mongo import mongodb

async def populate_sagas():
    response = requests.get("https://api.api-onepiece.com/v2/sagas/en")
    if response.status_code == 200:
        sagas = response.json()
        await mongodb.db.sagas.insert_many(sagas)