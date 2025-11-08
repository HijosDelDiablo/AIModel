from langchain_ollama import OllamaLLM
from mongoengine import connect, disconnect

from services import UserService, SessionService
from templates.userTemplate import user_chain 
from dto import ConversationContinueDto

# ai model imports
from ai_utils import ConnectionModelStandard


class ContinuousChatService:
    def __init__(self):
        self.connection_model = ConnectionModelStandard()

    def continue_chat_chain(
        self,
        data: ConversationContinueDto,
        user_service: UserService = None,
        session_service: SessionService = None
    ):
        try:
            userLocal = user_service.get_user_by_id(data.user_id)
            if not userLocal:
                return ValueError("User not found")
            session = session_service.get_session_by_id(data.session_id)
            if not session:
                return ValueError("Session not found")

            session = session_service.updateSession(session_id=data.session_id, messageLocal=data.messages, participantLocal='user')

            llm = self.connection_model.get_llm()
            respuesta = user_chain(llm, data.messages, knowledge_base="Continuing the conversation based on previous context.")
            session = session_service.updateSession(session_id=data.session_id, messageLocal=respuesta, participantLocal='bot')
            return {
                "session_id": data.session_id,
                "respuesta": respuesta,
                "user": userLocal,
                "session": session
            }

        except Exception as e:
            print(f"Error in continue_chat_chain: {e}")
            return e
        