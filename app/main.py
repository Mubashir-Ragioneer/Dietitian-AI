# app/main.py
from fastapi import FastAPI
from app.api.endpoints import user, meal_logs, progress_logs, plan
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

# Include routers for each endpoint group
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(meal_logs.router, prefix="/meal-logs", tags=["Meal Logs"])
app.include_router(progress_logs.router, prefix="/progress-logs", tags=["Progress Logs"])
app.include_router(plan.router, prefix="/plan", tags=["Plans"])

@app.get("/")
async def home():
    return {"message": "Welcome to the AI Dietitian App Backend"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
