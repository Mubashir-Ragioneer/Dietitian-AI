# app/api/endpoints/progress_logs.py
from fastapi import APIRouter
from datetime import datetime
from app.db.database import db
from app.schemas.progress_log import ProgressLog

router = APIRouter()

@router.post("/", response_model=dict)
async def create_progress_log(progress: ProgressLog):
    progress_data = progress.dict()
    progress_data["created_at"] = datetime.utcnow()
    result = await db["progress_logs"].insert_one(progress_data)
    return {"message": "Progress log created", "id": str(result.inserted_id)}

@router.get("/{user_id}", response_model=list)
async def get_progress_logs(user_id: str):
    logs = []
    cursor = db["progress_logs"].find({"user_id": user_id})
    async for document in cursor:
         document["id"] = str(document["_id"])
         logs.append(document)
    return logs
