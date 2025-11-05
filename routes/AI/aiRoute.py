from fastapi import APIRouter, Depends
from services import UserService, SessionService
from aiFlow_service.initChat_service import initial_chat_chain

router = APIRouter()

@router.post("/ai/send_message")
async def send_message(
    user_id: str,
    text: str,
    session_id: str = None,
    user_service: UserService = Depends(UserService),
    session_service: SessionService = Depends(SessionService)
):
    result = initial_chat_chain(
        user_id,
        text,
        session_id,
        user_service=user_service,
        session_service=session_service
    )
    return result

class AIRoute:
    def __init__(self):
        pass
