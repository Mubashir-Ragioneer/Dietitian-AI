from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class MealLog(BaseModel):
    user_id: str
    meal_date: datetime
    meal_type: str
    description: str
    calorie_estimate: Optional[int] = None
    image_url: Optional[str] = None
    created_at: datetime = datetime.utcnow() 