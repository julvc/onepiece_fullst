from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

class MongoDB:
    client: AsyncIOMotorClient = None
    db_name: str = "onepiece" # Nombre de la base de datos
    db = None
    
    boats_collection = None
    bows_collection = None
    chapters_collection = None
    characters_collection = None
    crews_collection = None
    dials_collection = None
    episodes_collection = None
    films_collection = None
    fruits_collection = None
    hakis_collection = None
    locations_collection = None
    luffysgears_collection = None
    luffystechniques_collection = None
    sagas_collection = None
    swords_collection = None
    volumes_collection = None

mongodb = MongoDB()

def connect_to_mongo(uri: str):
    # Conexión al cliente de MongoDB
    mongodb.client = AsyncIOMotorClient(uri)
    mongodb.db = mongodb.client[mongodb.db_name]  # Asignamos la base de datos
    
    # Inicializamos las colecciones
    mongodb.boats_collection = mongodb.db.boats
    mongodb.bows_collection = mongodb.db.bows
    mongodb.chapters_collection = mongodb.db.chapters
    mongodb.characters_collection = mongodb.db.characters
    mongodb.crews_collection = mongodb.db.crews
    mongodb.dials_collection = mongodb.db.dials
    mongodb.episodes_collection = mongodb.db.episodes
    mongodb.films_collection = mongodb.db.films
    mongodb.fruits_collection = mongodb.db.fruits
    mongodb.hakis_collection = mongodb.db.hakis
    mongodb.locations_collection = mongodb.db.locations
    mongodb.luffysgears_collection = mongodb.db.luffysgears
    mongodb.luffystechniques_collection = mongodb.db.luffystechniques
    mongodb.sagas_collection = mongodb.db.sagas
    mongodb.swords_collection = mongodb.db.swords
    mongodb.volumes_collection = mongodb.db.volumes
    
def close_mongo_connection():
    mongodb.client.close()

# Helper function for ObjectId
def object_id(id):
    return ObjectId(id) if ObjectId.is_valid(id) else None