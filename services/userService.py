

from models.User import User

# import utuls to connection with my dn
from database import ConnectionMongoStandard

class UserService:
    # inject database connection
    def __init__(self):
        self.connection = ConnectionMongoStandard()

    # service methods
        
    def get_all_users(self):
        try:

            users = User.objects()
            return [user.to_dict() for user in users]
        except Exception as e:
            raise Exception(f"Error getting users: {str(e)}")

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