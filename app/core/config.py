# app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

class Settings:
    APP_NAME = "AI Dietitian App Backend"
    MONGO_DETAILS = os.getenv("MONGO_DETAILS")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    # Add more settings as needed (e.g., secret keys for JWT)

settings = Settings()
