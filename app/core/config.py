import os
from dotenv import load_dotenv
from openai import OpenAI, AzureOpenAI # Use AzureOpenAI for clarity with Azure

# Load environment variables from .env file
load_dotenv()

# --- OpenAI Settings ---
# Use AzureOpenAI for Azure endpoints
# It requires api_version which you might need to get from your Azure deployment details
# If your Azure deployment doesn't need api_version, you might stick with OpenAI
# but using AzureOpenAI is generally recommended for Azure.
# Check your Azure AI Studio for the correct endpoint, key, and potentially api_version.

AZURE_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("OPENAI_BASE_URL")
# You might need this - find it in your Azure deployment details
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01") # Example version

if not AZURE_OPENAI_API_KEY or not AZURE_OPENAI_ENDPOINT:
    # Handle missing configuration appropriately
    # For now, we might allow the client to be None or raise an error
    print("Warning: Azure OpenAI API Key or Endpoint not configured.")
    ai_client = None
else:
    ai_client = AzureOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_version=AZURE_OPENAI_API_VERSION,
    )

# --- Database Settings (Example - Assuming you have this elsewhere) ---
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/default_db")

# You could add other settings here as needed