from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

def getClient():
    client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    return client

def howMayIhelpYou(client):
    question=input("You:")
    resp=client.models.generate_content(model="gemini-2.5-flash", contents=question)
    return resp.text

client=getClient()
response=howMayIhelpYou(client)
print(response)


