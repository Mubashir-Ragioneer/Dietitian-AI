# app/schemas/user.py
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional # Import Optional if needed for UserProfile

# Schema for user registration endpoint
class UserRegistration(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=6) # Password needed for registration

# Schema for user output (doesn't include password)
class UserOut(BaseModel):
    id: str
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        # Formerly orm_mode, needed if returning ORM objects directly
        # Pydantic V2 uses model_config
        from_attributes = True

# --- Optional: Schema for User Profile Data ---
# You might store these details in a separate "profiles" collection
# or add them to the user document later via an update endpoint.
# class UserProfile(BaseModel):
#     age: Optional[int] = None
#     gender: Optional[str] = None
#     weight: Optional[float] = None
#     height: Optional[float] = None
#     dietary_restrictions: Optional[str] = None
#     activity_level: Optional[str] = None
#     goal: Optional[str] = None
#     user_id: str # Link back to the user
