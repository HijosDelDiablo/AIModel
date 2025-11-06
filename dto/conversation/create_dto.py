from pydantic import BaseModel

class ConversationContinueDto(BaseModel):
    user_id: str
    messages: str
    session_id: str
