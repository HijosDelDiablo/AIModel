from fastapi import APIRouter, Depends
from aiFlow_service.initChat_service import InitChatService
from services import UserService, SessionService
from aiFlow_service import ContinuousChatService
from dto import ConversationContinueDto


class AIRoute:
    def __init__(self, user_service: UserService, session_service: SessionService, init_chat_service: InitChatService,
                 continuous_chat_service: ContinuousChatService):
        self.user_service = user_service
        self.session_service = session_service
        self.init_chat_service = init_chat_service
        self.continuous_chat_service = continuous_chat_service
        self.router = APIRouter()
        self.router.add_api_route("/ai/send_message", self.send_message, methods=["POST"])
        self.router.add_api_route("/ai/continous_conversation", self.continous_conversation, methods=["POST"])
        


    async def send_message(
        self,
        user_id: str,
        text: str,
        session_id: str = None,
        user_service: UserService = Depends(UserService),
        session_service: SessionService = Depends(SessionService)
    ):

        result = self.init_chat_service.initial_chat_chain(
            user_id,
            text,
            session_id,
            user_service=user_service,
            session_service=session_service,
        )
        return result


    async def continous_conversation(
        self,
        data: ConversationContinueDto,
        user_service: UserService = Depends(UserService),
        session_service: SessionService = Depends(SessionService)
    ):
        result = self.continuous_chat_service.continue_chat_chain(
            data=data,
            user_service=user_service,
            session_service=session_service,
        )
        return result