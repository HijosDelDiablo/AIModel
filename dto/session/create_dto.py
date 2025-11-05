from pydantic import BaseModel

class CreateSessionDTO(BaseModel):
    user_id: str
    token: str
    expires_at: str