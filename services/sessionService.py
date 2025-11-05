from mongoengine import connect, disconnect

class SessionService:
    def __init__(self):
        # Conectar a MongoDB
        disconnect()
        connect('AI-ModelDB', host='mongodb://localhost:27017')

    def create_session(self, user_id: str, token: str, expires_at: str):
        # Lógica para crear una sesión
        pass