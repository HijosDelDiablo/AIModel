from langchain_ollama import OllamaLLM
from mongoengine import connect, disconnect

from services import UserService, SessionService
from templates.userTemplate import user_chain 
from dto import ConversationContinueDto
class ContinuousChatService:
    def __init__(self):
        disconnect()
        connect('AI-ModelDB', host='mongodb://localhost:27017')
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

            llm = OllamaLLM(model="mistral", base_url="http://localhost:11434")
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
        