

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
    
    def get_user_by_id(self, user_id: str):
        try:
            user = User.objects.get(id=user_id)
            return user.to_dict() if hasattr(user, 'to_dict') else user.to_mongo().to_dict()
        except User.DoesNotExist:
            raise ValueError("User not found")
        except Exception as e:
            raise Exception(f"Error getting user: {str(e)}")