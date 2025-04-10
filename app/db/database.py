# app/db/database.py
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client.ai_dietitian  # Name of your database

# Optional: Add connection/disconnection functions if managing explicitly
# async def connect_db():
#     # Motor usually handles connection pooling, explicit connect might not be needed
#     # unless you want to ping the server on startup
#     try:
#         await client.admin.command('ping')
#         print("Successfully connected to MongoDB.")
#     except Exception as e:
#         print(f"Error connecting to MongoDB: {e}")

# async def close_db():
#      client.close()
#      print("MongoDB connection closed.")
