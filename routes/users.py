from fastapi import APIRouter, HTTPException
from models.user import Account
from config.db import db
from bson.objectid import ObjectId
from config.db import accounts_collection
from config.db import destinations_collection

user = APIRouter()

@user.post("/users")
async def create_account(account: Account):
    # Check if email already exists
    if accounts_collection.find_one({"email": account.email}):
        print(account)
        raise HTTPException(status_code=400, detail="Email already exists")

    # Insert account into MongoDB
    account_id = str(accounts_collection.insert_one(account.dict()).inserted_id)
    return {"message": "Account created successfully","account_id": account_id}

@user.put("/users")
async def update_account(account : Account):
    user = accounts_collection.find_one({"email": account.email})
    if not user:
        raise HTTPException(status_code=400, detail="User not exists")
    accounts_collection.update_one({"_id": user["_id"]}, {"$set": account.dict()})
    return {"message": "Account updated successfully","account_id": str(user["_id"])}

@user.delete("/users/{id}")
async def delete_account(id: str):
    # Check if email exists
    if not accounts_collection.find_one({"_id": ObjectId(id)}):
        raise HTTPException(status_code=404, detail="Account not found")
    # Delete account from MongoDB
    destinations_collection.delete_one({"account_id":ObjectId(id)})
    accounts_collection.delete_one({"_id": ObjectId(id)})
    return {"message": "Account deleted successfully"}

@user.get("/users/{email}")
async def get_account(email: str):
    # get user data and give id in response
    user = accounts_collection.find_one({"email": email})
    if user:
        return {"id": str(user["_id"])}
    return {"message": "Account not found"}

@user.get("/secrete/{id}")
async def get_secretCode(id: str):
    print("Hello")
    user = accounts_collection.find_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"secretCode": user["app_secret_token"]}