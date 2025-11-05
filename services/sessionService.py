from mongoengine import connect, disconnect
from models.Session import Session
from models.User import User

class SessionService:
    def __init__(self):
        # Conectar a MongoDB
        disconnect()
        connect('AI-ModelDB', host='mongodb://localhost:27017')

    def create_session(self, user_id: str):
        # Buscar el usuario
        try:
            user = User.objects.get(id=user_id)
            session = Session(user=user)
            session.save()
            return session.to_dict() if hasattr(session, 'to_dict') else session.to_mongo().to_dict()
        except User.DoesNotExist:
            raise ValueError("User not found")
        except Exception as e:
            raise Exception(f"Error creating session: {str(e)}")

    def get_sessions_by_user(self, user_id: str):
        try:
            user = User.objects.get(id=user_id)
            sessions = Session.objects(user=user)
            return [session.to_dict() if hasattr(session, 'to_dict') else session.to_mongo().to_dict() for session in sessions]
        except User.DoesNotExist:
            raise ValueError("User not found")
        except Exception as e:
            raise Exception(f"Error getting sessions: {str(e)}")

    def get_session_by_id(self, session_id: str):
        try:
            session = Session.objects.get(id=session_id)
            data = session.to_dict() if hasattr(session, 'to_dict') else session.to_mongo().to_dict()
            # Agregar datos completos del usuario
            if session.user:
                data['user'] = session.user.to_dict() if hasattr(session.user, 'to_dict') else session.user.to_mongo().to_dict()
            return data
        except Session.DoesNotExist:
            raise ValueError("Session not found")
        except Exception as e:
            raise Exception(f"Error getting session: {str(e)}")