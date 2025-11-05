from fastapi import FastAPI
from routes import userRoute, sessionRoute
from services import UserService, SessionService
from routes.AI.aiRoute import router as ai_router


app = FastAPI()

user_service = UserService()
user_route = userRoute.UserRoute(user_service)
app.include_router(user_route.router)

session_service = SessionService()
session_route = sessionRoute.SessionRoute(session_service)
app.include_router(session_route.router)

app.include_router(ai_router)
