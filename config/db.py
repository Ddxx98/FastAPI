from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://deexith2016:uLIQpYH99ipgK715@cluster0.f1nw27g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["webhook_service"]
accounts_collection = db["accounts"]
destinations_collection = db["destinations"]

server_info = client.server_info()
if server_info:
    print("The client is connected to the cluster.")
else:
    print("The client is not connected to the cluster.")
