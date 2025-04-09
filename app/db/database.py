# app/db/database.py
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = AsyncIOMotorClient(settings.MONGO_DETAILS)
db = client.ai_dietitian  # Name of your database
