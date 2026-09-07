from google import genai
from dotenv import load_dotenv
import os
load_dotenv()
from google.genai import types

PROMPT = "You are a helpful python tutor. but you can answer general questions as well."

def getClient():
    client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    return client

def howMayIhelpYou(messages):
    client = getClient()
    config = types.GenerateContentConfig(
        system_instruction=PROMPT,
        #temperature=1.8,
        #max_output_tokens=50,
        top_p=1.0
    )
    resp=client.models.generate_content(model="gemini-2.5-flash-lite", contents=messages, config=config)
    return resp.text

client=None
try: 
        messages=[]
        client=getClient()
        while True:
            question=input("You:")
            if question.lower() in ["exit", "quit"]:
                print("Exiting the program.")
                break
            else:
                messages.append({"role":"user","parts":[types.Part.from_text(text=question)]})
                response=howMayIhelpYou(messages)
                print("AI answer:",response) 
                messages.append({"role":"model","parts":[types.Part.from_text(text=response)]})
except Exception as e:
        print("API key not valid")
        print(f"An error occurred: {e}")