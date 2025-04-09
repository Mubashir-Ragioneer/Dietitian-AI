# app/schemas/plan.py
from pydantic import BaseModel, Field
from datetime import datetime

class PlanGenerationRequest(BaseModel):
    user_id: str
    additional_info: dict = Field(default_factory=dict)

class PlanOut(BaseModel):
    user_id: str
    plan_date: datetime
    meal_plan: dict
    workout_plan: dict
    wellness_recommendations: dict
