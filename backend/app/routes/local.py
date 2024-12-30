from fastapi import APIRouter, HTTPException
from app.db import mongo

router = APIRouter()

collection = mongo.get_collection("onepiece_collection")

@router.post("/")
async def create_item(item: dict):
    result = collection.insert_one(item)
    return {"id": str(result.inserted_id)}

@router.get("/{item_id}")
async def read_item(item_id: str):
    item = collection.find_one({"_id": item_id})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{item_id}")
async def update_item(item_id: str, updated_item: dict):
    result = collection.update_one({"_id": item_id}, {"$set": updated_item})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item updated"}

@router.delete("/{item_id}")
async def delete_item(item_id: str):
    result = collection.delete_one({"_id": item_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}
