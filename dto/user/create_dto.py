from pydantic import BaseModel, EmailStr


class CreateUserDTO(BaseModel):
    username: str
    email: EmailStr
    age: int