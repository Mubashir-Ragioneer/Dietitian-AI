# app/api/endpoints/plan.py
from fastapi import APIRouter, HTTPException
from datetime import datetime
from bson import ObjectId
import openai
from app.db.database import db
from app.schemas.plan import PlanGenerationRequest, PlanOut

router = APIRouter()

@router.post("/generate", response_model=PlanOut)
async def generate_plan(req: PlanGenerationRequest):
    # Retrieve user profile
    user = await db["users"].find_one({"_id": ObjectId(req.user_id)})
    if not user:
         raise HTTPException(status_code=404, detail="User not found")
    
    # Retrieve meal logs (optional: add filtering by date)
    meal_logs = []
    async for doc in db["meal_logs"].find({"user_id": req.user_id}):
         meal_logs.append(doc)
    
    # Build prompt for GPT-4
    prompt = (
        f"User details: {user}\n"
        f"Meal logs: {meal_logs}\n"
        f"Additional info: {req.additional_info}\n"
        "Generate a personalized diet, workout, and wellness plan."
    )
    try:
         response = openai.Completion.create(
             engine="gpt-4",
             prompt=prompt,
             max_tokens=500,
             temperature=0.7,
         )
         generated_text = response.choices[0].text.strip()
         # For a PoC, simulate segmentation of the output
         meal_plan = {"plan": "Meal plan derived from AI output"}
         workout_plan = {"plan": "Workout plan derived from AI output"}
         wellness_recommendations = {"plan": "Wellness recommendations from AI output"}

         plan_data = {
              "user_id": req.user_id,
              "plan_date": datetime.utcnow(),
              "meal_plan": meal_plan,
              "workout_plan": workout_plan,
              "wellness_recommendations": wellness_recommendations,
              "created_at": datetime.utcnow(),
         }
         result = await db["plan_suggestions"].insert_one(plan_data)
         plan_data["id"] = str(result.inserted_id)
         return plan_data
    except Exception as e:
         raise HTTPException(status_code=500, detail=str(e))

@router.get("/{user_id}", response_model=list)
async def get_plans(user_id: str):
    plans = []
    cursor = db["plan_suggestions"].find({"user_id": user_id})
    async for document in cursor:
         document["id"] = str(document["_id"])
         plans.append(document)
    return plans
