# app/schemas/user.py
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserRegistration(BaseModel):
    name: str
    email: EmailStr
    age: int
    gender: str
    weight: float
    height: float
    dietary_restrictions: str = None
    activity_level: str
    goal: str

class UserOut(BaseModel):
    id: str
    name: str
    email: EmailStr
    age: int
    gender: str
    weight: float
    height: float
    dietary_restrictions: str = None
    activity_level: str
    goal: str
    created_at: datetime
