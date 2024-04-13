from fastapi import APIRouter, HTTPException, Header
from config.db import accounts_collection
from config.db import destinations_collection
import aiohttp

webhook = APIRouter()

@webhook.post("/server/incoming_data/")
async def incoming_data(data: dict, TOKEN: str = Header(None)):
    # Check if header is present
    if not TOKEN:
        raise HTTPException(status_code=401, detail="Un Authenticate")

    # Find account by token
    account = accounts_collection.find_one({"app_secret_token": str(TOKEN)})
    if not account:
        raise HTTPException(status_code=401, detail="Un Authenticate")

    # Find destinations for the account
    responseData = ""
    destinations = destinations_collection.find_one({"account_id": account["_id"]})
    async with aiohttp.ClientSession() as session:
        for destination in destinations["destination"]:
            url = destination["url"]
            http_method = destination["http_method"]
            if http_method == "GET" and not isinstance(data, dict):
                raise HTTPException(status_code=400, detail="Invalid Data")
            headers = destination["headers"]
            
            # Make HTTP request to destination
            async with session.request(http_method, url, json=data, headers=headers) as response:
                responseData = await response.json()
                # Check response status and handle accordingly (e.g., logging)
                print(f"Response from {url}: {response.status}")
    
    return {"message": "Data sent to destinations successfully","response":str(responseData)}



    # import requests
    # Retrieve destinations for the account
    # destinations = destinations_collection.find_one({"account_id": account["_id"]})
    # if not destinations:
    #     raise HTTPException(status_code=404, detail="No destinations found for this account")

    # # Iterate through destinations and send data
    # for destination in destinations["destination"]:
    #     url = destination["url"]
    #     method = destination["http_method"]
    #     headers = destination["headers"]

    #     # Prepare data based on HTTP method
    #     if method.lower() == "get":
    #         # Append data as query parameters
    #         response = requests.get(url, params=data, headers=headers)
    #     elif method.lower() in ["post", "put"]:
    #         response = requests.request(method, url, json=data, headers=headers)
    #     else:
    #         # Unsupported HTTP method
    #         raise HTTPException(status_code=400, detail="Unsupported HTTP method")

    #     # Check response status and handle errors if needed
    #     if response.status_code != 200:
    #         # Handle error response
    #         raise HTTPException(status_code=response.status_code, detail=response.text)

    # return {"message": "Data sent to destinations successfully"}