# app/schemas/meal_log.py
from pydantic import BaseModel
from datetime import datetime

class MealLog(BaseModel):
    user_id: str
    meal_date: datetime
    meal_type: str
    description: str
    calorie_estimate: int = None
    image_url: str = None
