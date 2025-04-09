from datetime import datetime
from typing import Dict
from pydantic import BaseModel

class Plan(BaseModel):
    user_id: str
    plan_date: datetime
    meal_plan: Dict
    workout_plan: Dict
    wellness_recommendations: Dict
    created_at: datetime = datetime.utcnow() 