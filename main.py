from fastapi import FastAPI
from routes import userRoute, sessionRoute
from routes import AIRoute
from aiFlow_service.initChat_service import InitChatService
from services import UserService, SessionService
from routes import AI
from aiFlow_service import ContinuousChatService

app = FastAPI()

user_service = UserService()
user_route = userRoute.UserRoute(user_service)
app.include_router(user_route.router)

session_service = SessionService()
session_route = sessionRoute.SessionRoute(session_service)
app.include_router(session_route.router)


# Instanciar InitChatService y AIRoute
init_chat_service = InitChatService()
continuous_chat_service = ContinuousChatService()
ai_route = AIRoute(user_service, session_service, init_chat_service, continuous_chat_service)
app.include_router(ai_route.router)
