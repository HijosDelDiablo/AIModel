# connection file

from mongoengine import connect

def get_database():

    CONNECTION_STRING = "mongodb://localhost:27017"
    client = connect(host=CONNECTION_STRING, db='AI-ModelDB')
    print("Connected to MongoDB, ", client)
    return client
