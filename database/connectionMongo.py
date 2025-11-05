# connection file

from mongoengine import connect, disconnect

def get_database():

    CONNECTION_STRING = "mongodb://localhost:27017"
    disconnect()
    client = connect(host=CONNECTION_STRING, db='AI-ModelDB')
    print("Connected to MongoDB, ", client)
    return client
