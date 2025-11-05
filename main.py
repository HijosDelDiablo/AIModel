from fastapi import FastAPI
from routes import userRoute
from services import UserService

app = FastAPI()

user_service = UserService()
user_route = userRoute.UserRoute(user_service)
app.include_router(user_route.router)