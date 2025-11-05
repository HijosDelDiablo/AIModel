from mongoengine import connect, disconnect
from services import UserService, SessionService
from templates.userTemplate import user_chain
from langchain_ollama import OllamaLLM


class InitChatService:
    
    def __init__(self):
        disconnect()
        connect('AI-ModelDB', host='mongodb://localhost:27017')

    

def initial_chat_chain(
    user_id: str,
    text: str,
    session_id: str = None,
    user_service: UserService = None,
    session_service: SessionService = None
):
    user = user_service.get_user_by_id(user_id)

    if session_id:
        session = session_service.get_session_by_id(session_id)
    else:
        session = session_service.create_session(user_id)
        session_id = session["_id"]

    # Invocar el modelo IA para responder el primer mensaje
    llm = OllamaLLM(model="mistral", base_url="http://localhost:11434")
    respuesta = user_chain(llm, text, knowledge_base="Bienvenido a la conversación!")

    return {
        "session_id": session_id,
        "respuesta": respuesta,
        "user": user,
        "session": session
    }
