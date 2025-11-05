

from mongoengine import connect, disconnect
from models.User import User

class UserService:
    def __init__(self):
        # Conectar a MongoDB
        disconnect()
        connect('AI-ModelDB', host='mongodb://localhost:27017')
        

    def get_all_users(self):
        users = User.objects()
        return [user.to_dict() for user in users]

    def create_user(self, username: str, email: str, age: int):
        user = User(username=username, email=email, age=age)
        user.save()
        return user.to_dict()