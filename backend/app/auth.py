from fastapi import APIRouter
from pydantic import BaseModel, EmailStr


router = APIRouter()

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseException):
    token: str
    expires_in: str
