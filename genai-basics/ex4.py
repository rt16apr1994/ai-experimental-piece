from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

def getClient():
    client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    return client

def howMayIhelpYou(client, question):
    resp=client.models.generate_content(model="gemini-2.5-flash", contents=question)
    return resp.text

client=None

try: 
        client=getClient()
        while True:
            question=input("You:")
            if question.lower() in ["exit", "quit"]:
                print("Exiting the program.")
                break
            else:
                response=howMayIhelpYou(client, question)
                print(response)
except Exception as e:
        print("API key not valid")
        print(f"An error occurred: {e}")



