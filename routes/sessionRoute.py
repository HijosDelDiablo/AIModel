from services import SessionService
from dto import CreateSessionDTO
from fastapi import APIRouter
from pydantic import BaseModel

class CreateSessionRequest(BaseModel):
    user_id: str

class SessionRoute:
    def __init__(self, session_service: SessionService):
        self.session_service = session_service
        self.router = APIRouter()
        self.router.add_api_route("/sessions/create", self.create_session, methods=["POST"])
        self.router.add_api_route("/sessions/user/{user_id}", self.get_sessions_by_user, methods=["GET"])
        self.router.add_api_route("/sessions/{session_id}", self.get_session, methods=["GET"])

    async def create_session(self, request: CreateSessionRequest):
        try:
            session = self.session_service.create_session(request.user_id)
            return {"session": session}
        except Exception as e:
            return {"error": str(e)}

    async def get_sessions_by_user(self, user_id: str):
        try:
            sessions = self.session_service.get_sessions_by_user(user_id)
            return {"sessions": sessions}
        except Exception as e:
            return {"error": str(e)}

    async def get_session(self, session_id: str):
        try:
            session = self.session_service.get_session_by_id(session_id)
            return {"session": session}
        except Exception as e:
            return {"error": str(e)}