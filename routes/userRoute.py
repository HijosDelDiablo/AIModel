from fastapi import APIRouter
from pydantic import BaseModel
from services import UserService

class CreateUserRequest(BaseModel):
    username: str
    email: str
    age: int

class UserRoute:
    def __init__(self, user_service: UserService):
        self.user_service = user_service
        self.router = APIRouter()
        self.router.add_api_route("/users", self.get_users, methods=["GET"])
        self.router.add_api_route("/create_user", self.create_user, methods=["POST"])

    async def get_users(self):
        try:
            users = self.user_service.get_all_users()
            return {"users": users}
        except Exception as e:
            print("Error en /users:", e)
            return {"error": str(e)}

    async def create_user(self, request: CreateUserRequest):
        try:
            user = self.user_service.create_user(request.username, request.email, request.age)
            return {"user": user}
        except Exception as e:
            print("Error en /create_user:", e)
            return {"error": str(e)}