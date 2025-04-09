# app/api/endpoints/meal_logs.py
from fastapi import APIRouter
from datetime import datetime
from app.db.database import db
from app.schemas.meal_log import MealLog

router = APIRouter()

@router.post("/", response_model=dict)
async def create_meal_log(meal: MealLog):
    meal_data = meal.dict()
    meal_data["created_at"] = datetime.utcnow()
    result = await db["meal_logs"].insert_one(meal_data)
    return {"message": "Meal log created", "id": str(result.inserted_id)}

@router.get("/{user_id}", response_model=list)
async def get_meal_logs(user_id: str):
    logs = []
    cursor = db["meal_logs"].find({"user_id": user_id})
    async for document in cursor:
         document["id"] = str(document["_id"])
         logs.append(document)
    return logs
