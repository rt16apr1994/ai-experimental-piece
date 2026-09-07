from google import genai
import os
from dotenv import load_dotenv

client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# List all models supported for content generation
for model in client.models.list():
    if "generateContent" in model.supported_generation_methods:
        print(model.name)