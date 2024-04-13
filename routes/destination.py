from fastapi import APIRouter, HTTPException
from models.user import Destinations
from models.user import Destination
from config.db import destinations_collection
from config.db import accounts_collection
from bson.objectid import ObjectId

destination = APIRouter()
@destination.post("/destination")
async def create_destination(destination: Destinations):
    account_id = ObjectId(destination.account_id)

    # Check if account exists
    if not accounts_collection.find_one({"_id": account_id}):
        raise HTTPException(status_code=404, detail="Account not found")
    if destinations_collection.find_one({"account_id": account_id}):
        raise HTTPException(status_code=404, detail="Destination already existed")

    destination_dict = destination.dict()
    destination_dict["account_id"] = account_id
    
    # Insert destination into MongoDB
    destination_id = str(destinations_collection.insert_one(destination_dict).inserted_id)
    return {"message": "Destination created successfully", "destination_id": destination_id}

@destination.put("/destination/{account_id}")
async def add_destination(account_id: str,destination: Destination):
    #find the destination and update the destination array
    print(account_id)
    if not destinations_collection.find_one({"account_id": ObjectId(account_id)}):
        raise HTTPException(status_code=404, detail="Destination not found")
    destinations_collection.update_one({"account_id": ObjectId(account_id)}, {"$push": {"destination": destination.dict()}})
    return {"message": "Destination updated successfully"}

@destination.get("/destinations/{account_id}")
async def get_destinations(account_id: str):
    account_id = ObjectId(account_id)

    # Check if account exists
    if not accounts_collection.find_one({"_id": account_id}):
        raise HTTPException(status_code=404, detail="Account not found")
    data = destinations_collection.find_one({"account_id":account_id})
    if not data:
        raise HTTPException(status_code=404, detail="Destination not found")
    return {"data":str(data["destination"])}

