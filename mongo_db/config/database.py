from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb+srv://admin:fastapi333@cluster0.uhzzusu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.todo_db

collection_name = db["todo_collection"]