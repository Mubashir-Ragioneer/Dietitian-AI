# app/schemas/progress_log.py
from pydantic import BaseModel
from datetime import datetime

class ProgressLog(BaseModel):
    user_id: str
    log_date: datetime
    weight: float = None
    energy_level: int = None
    mood: str = None
    notes: str = None
