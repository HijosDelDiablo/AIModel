from fastapi import FastAPI
from routes import userRoute, sessionRoute
from routes import AIRoute
from aiFlow_service.initChat_service import InitChatService
from services import UserService, SessionService
import requests
from aiFlow_service import ContinuousChatService

from dotenv import load_dotenv
load_dotenv()
import os

app = FastAPI()
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")

@app.get("/")
async def root():
    # Authorization URL for Google OAuth 2.0 (v2 endpoint)
    return {
        "url": f"https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline&prompt=consent"
    }


@app.get("/authorize")
async def authorize(code: str):
    """
    Exchange authorization code for tokens and return userinfo.
    This endpoint matches the redirect URI set in Google Console (e.g. http://localhost:8000/authorize).
    """
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    # Exchange the code
    response = requests.post(token_url, data=data)
    resp_json = response.json()
    access_token = resp_json.get("access_token")
    # You can also get an id_token here (a JWT) in resp_json.get('id_token') if needed
    if not access_token:
        return {"error": "failed_to_get_access_token", "details": resp_json}

    # Fetch user info from Google's userinfo endpoint
    user_info = requests.get(
        "https://www.googleapis.com/oauth2/v3/userinfo",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    return {"tokens": resp_json, "userinfo": user_info.json()}

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
