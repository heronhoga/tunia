import string

from pydantic import BaseModel

class RegisterRequest(BaseModel):
    username: str
    fullname: str
    email: str
    password: str

class RegisterResponse(BaseModel):
    error: bool
    message: str
    
    