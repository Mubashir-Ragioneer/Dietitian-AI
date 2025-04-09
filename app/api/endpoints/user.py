# app/api/endpoints/user.py
from fastapi import APIRouter, HTTPException
from datetime import datetime
from app.db.database import db
from app.schemas.user import UserRegistration, UserOut
from bson import ObjectId

router = APIRouter()

@router.post("/register", response_model=UserOut)
async def register_user(user: UserRegistration):
    user_data = user.dict()
    user_data["created_at"] = datetime.utcnow()
    # Check if email already exists
    existing_user = await db["users"].find_one({"email": user_data["email"]})
    if existing_user:
         raise HTTPException(status_code=400, detail="Email already registered")
    result = await db["users"].insert_one(user_data)
    new_user = await db["users"].find_one({"_id": result.inserted_id})
    new_user["id"] = str(new_user["_id"])  # Convert ObjectId to string
    return new_user
