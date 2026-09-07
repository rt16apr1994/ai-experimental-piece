from google import genai
from dotenv import load_dotenv
import os
load_dotenv()
from google.genai import types

SYSTEM_PROMPT = "You are a helpful python tutor. Please answer questions related to python only in concise manner. If the question is not related to python, politely decline to answer."  

def getClient():
    client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    return client

def chat_with_ai(content_list):
    config = types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)
    resp=client.models.generate_content(model="gemini-2.5-flash", contents=content_list, config=config)
    return resp.text

try:
    content_lists = []
    print("Welcome to the Python Tutor Chat! Type 'exit' or 'quit' to end the conversation.")
    client=getClient()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the program.")
            break
        else:   
            content_lists.append(types.Content(role="user", parts=[types.Part(text=user_input)]))
            ai_response = chat_with_ai(content_lists)
            print("AI answer:", ai_response)
            content_lists.append(types.Content(role="model", parts=[types.Part(text=ai_response)]))
except Exception as e:
    print("API key not valid or an error occurred.")
    print(f"An error occurred: {e}")
