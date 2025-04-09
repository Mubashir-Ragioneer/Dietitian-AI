from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ProgressLog(BaseModel):
    user_id: str
    log_date: datetime
    weight: Optional[float] = None
    energy_level: Optional[int] = None
    mood: Optional[str] = None
    notes: Optional[str] = None
    created_at: datetime = datetime.utcnow() 