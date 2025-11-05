# connection file

from pymongo import MongoClient

def get_database():

    CONNECTION_STRING = "mongodb://localhost:27017"
    client = MongoClient(CONNECTION_STRING)
    print("Connected to MongoDB, ", client)
    return client['AI-ModelDB']
