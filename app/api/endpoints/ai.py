from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from openai import AzureOpenAI # Or OpenAI if you stick with that
from app.core.config import ai_client # Import the initialized client

router = APIRouter()

# --- Pydantic Models for Request/Response ---
class ChatRequest(BaseModel):
    prompt: str
    model: str = "gpt-4o" # Or your specific Azure deployment name for gpt-4o
    temperature: float = 1.0
    max_tokens: int = 4096
    top_p: float = 1.0

class ChatResponse(BaseModel):
    response: str

# --- Dependency to get the AI client ---
def get_ai_client():
    if ai_client is None:
        raise HTTPException(status_code=503, detail="AI Service is not configured or available.")
    return ai_client

# --- API Endpoint ---
@router.post("/chat", response_model=ChatResponse)
async def chat_with_model(
    request: ChatRequest,
    client: AzureOpenAI = Depends(get_ai_client) # Inject the client
):
    try:
        response = await client.chat.completions.create(
            messages=[
                # You might want a more sophisticated system prompt
                {"role": "system", "content": "You are a helpful dietitian assistant."},
                {"role": "user", "content": request.prompt}
            ],
            # Ensure this model name matches your Azure Deployment name for gpt-4o
            model=request.model,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
            top_p=request.top_p,
        )
        # Accessing the response content might vary slightly depending on the OpenAI library version
        # Check the structure of the 'response' object if this fails
        content = response.choices[0].message.content
        if content is None:
             raise HTTPException(status_code=500, detail="AI model returned empty content.")
        return ChatResponse(response=content)

    except Exception as e:
        # Log the error e for debugging
        print(f"Error calling OpenAI API: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to get response from AI model: {e}")
