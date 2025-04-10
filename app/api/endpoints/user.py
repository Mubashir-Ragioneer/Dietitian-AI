# app/api/endpoints/user.py
from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime
from app.db.database import db
from app.schemas.user import UserRegistration, UserOut
from bson import ObjectId
from passlib.context import CryptContext

router = APIRouter()

# Configure password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

@router.post("/register", response_model=UserOut)
async def register_user(user: UserRegistration):
    # Check if email already exists
    existing_user = await db["users"].find_one({"email": user.email})
    if existing_user:
         raise HTTPException(status_code=400, detail="Email already registered")

    # Check if username already exists
    existing_username = await db["users"].find_one({"username": user.username})
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already taken")

    # Hash the password before storing
    hashed_password = get_password_hash(user.password)

    user_data = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password,
        "created_at": datetime.utcnow()
    }

    # Insert the new user
    result = await db["users"].insert_one(user_data)
    new_user = await db["users"].find_one({"_id": result.inserted_id})

    # Prepare the response, ensuring ObjectId is converted and password is not returned
    if new_user:
        return UserOut(
            id=str(new_user["_id"]),
            username=new_user["username"],
            email=new_user["email"],
            created_at=new_user["created_at"]
        )
    else:
        # This case should ideally not happen if insert was successful, but good practice to handle
        raise HTTPException(status_code=500, detail="User registration failed.")
