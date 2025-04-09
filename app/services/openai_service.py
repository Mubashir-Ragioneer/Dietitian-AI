import openai
from app.core.config import settings

openai.api_key = settings.OPENAI_API_KEY

async def generate_plan(user_data: dict, meal_logs: list, additional_info: dict = None) -> dict:
    prompt = f"""
    User details: {user_data}
    Recent meal logs: {meal_logs}
    Additional information: {additional_info or {}}
    
    Generate a personalized diet, workout, and wellness plan based on the above information.
    The plan should be comprehensive and tailored to the user's goals and needs.
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert dietitian and fitness trainer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        generated_text = response.choices[0].message.content
        
        # Parse the generated text into structured data
        # This is a simplified example - you might want to implement more sophisticated parsing
        plan = {
            "meal_plan": {"details": generated_text},  # Parse meal plan section
            "workout_plan": {"details": generated_text},  # Parse workout plan section
            "wellness_recommendations": {"details": generated_text}  # Parse wellness recommendations
        }
        
        return plan
    except Exception as e:
        raise Exception(f"Error generating plan: {str(e)}") 