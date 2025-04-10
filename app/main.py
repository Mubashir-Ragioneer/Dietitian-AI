# app/main.py
from fastapi import FastAPI
# Only import routers that exist
from app.api.endpoints import user as user_router
from app.api.endpoints import ai as ai_router
# Remove config import if not used, or import specific variables if needed
# from app.core.config import settings # Remove this if not using settings

# Hardcode title or fetch from config variable if defined
app = FastAPI(title="Dietitian AI App")

# Include routers for existing endpoints
app.include_router(user_router.router, prefix="/users", tags=["Users"])
app.include_router(ai_router.router, prefix="/ai", tags=["AI"])
# Remove includes for non-existent routers
# app.include_router(meal_logs.router, prefix="/meal-logs", tags=["Meal Logs"])
# app.include_router(progress_logs.router, prefix="/progress-logs", tags=["Progress Logs"])
# app.include_router(plan.router, prefix="/plan", tags=["Plans"])


@app.get("/")
async def home():
    return {"message": "Welcome to the AI Dietitian App Backend"}

# if __name__ == "__main__":
#     import uvicorn
#     # Use the app instance directly when running this script
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
