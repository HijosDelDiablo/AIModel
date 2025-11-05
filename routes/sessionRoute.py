from services import SessionService

from fastapi import APIRouter


class SessionRoute:
    def __init__(self, session_service: SessionService):
        self.session_service = session_service
        self.router = APIRouter()
        # Aquí se pueden agregar rutas relacionadas con las sesiones