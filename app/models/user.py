from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    age: int
    gender: str
    weight: float
    height: float
    dietary_restrictions: Optional[str] = None
    activity_level: str
    goal: str
    created_at: datetime = datetime.utcnow() 