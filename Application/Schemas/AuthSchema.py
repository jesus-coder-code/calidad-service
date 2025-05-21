from pydantic import BaseModel, EmailStr


class AuthRequest(BaseModel):
    username: str
    password: str


class AuthResponse(BaseModel):
    access_token: str


class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
