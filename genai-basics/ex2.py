from google import genai
import os
from dotenv import load_dotenv
load_dotenv()


client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
resp=client.models.generate_content(model="gemini-2.5-flash", contents="up to what year are you trained on?")
print(resp.text)