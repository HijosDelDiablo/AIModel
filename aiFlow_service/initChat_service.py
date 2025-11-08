

from mongoengine import connect, disconnect
from services import UserService, SessionService
from templates.userTemplate import user_chain
from langchain_ollama import OllamaLLM

from utils import convert_objectid

from ai_utils import ConnectionModelStandard

class InitChatService:
    
    def __init__(self):
        # Cargar credenciales desde .env y conectar con autenticación
        self.connection_model = ConnectionModelStandard()

    

    def initial_chat_chain(
        self,
        user_id: str,
        text: str,
        session_id: str = None,
        user_service: UserService = None,
        session_service: SessionService = None
    ):
        try:
            user = user_service.get_user_by_id(user_id)
            if not user: return ValueError("User not found")
            if session_id:
                session = session_service.get_session_by_id(session_id)
                if not session:
                    return ValueError("Session not found")
                
            else:
                session = session_service.create_session(user_id, messageLocal=text)
                
                session_id = session["_id"]

            # Invocar el modelo IA para responder el primer mensaje
            llm = self.connection_model.get_llm()
            respuesta = user_chain(llm, text, knowledge_base="Bienvenido a la conversación!")
            newAnswer = session_service.updateSession(session_id=session_id, messageLocal=respuesta, participantLocal='bot')

            return convert_objectid({
                "session_id": session_id,
                "respuesta": respuesta,
                "user": user,
                "session": session,
                "newAnswer": newAnswer
            })
        except Exception as e:
            print(f"Error in initial_chat_chain: {e}")
            return e