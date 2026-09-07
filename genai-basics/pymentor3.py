from google import genai
from dotenv import load_dotenv
import os
from google.genai import types
import json

load_dotenv()

SYSTEM_PROMPT = (
    "You are a helpful python tutor. Please answer questions related to python only "
    "in a concise manner. If the question is not related to python, politely decline to answer."
)  

def getClient():
    # Recommended: Grab GEMINI_API_KEY directly from environment variable automatically
    return genai.Client()

def chat_with_ai(client, content_list):
    config = types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)
    # Passed client into function to avoid global scoping/initialization issues
    resp = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=content_list, 
        config=config
    )
    return resp.text

try:
    client = getClient()
    content_lists = []

    # 1. Properly LOAD history (Convert raw JSON to SDK Objects)
    if os.path.exists("history.json"):
        with open("history.json", "r", encoding="utf-8") as f:
            raw_history = json.load(f)
            # Reconstruct types.Content and types.Part from dict
            for item in raw_history:
                content_lists.append(
                    types.Content(
                        role=item["role"],
                        parts=[types.Part.from_text(text=item["text"])]
                    )
                )
        print("Chat history loaded. Continue your python session!")
    else:
        print("Welcome to the Python Tutor Chat! Type 'exit' or 'quit' to end.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the program.")
            break
        
        if not user_input.strip():
            continue

        # Append user message
        content_lists.append(types.Content(role="user", parts=[types.Part.from_text(text=user_input)]))
        
        # Get response
        ai_response = chat_with_ai(client, content_lists)
        print("AI answer:", ai_response)
        
        # Append AI response
        content_lists.append(types.Content(role="model", parts=[types.Part.from_text(text=ai_response)]))
        
        # 2. Properly SAVE history (Extract data into basic dictionaries)
        serializable_history = []
        for content in content_lists:
            # Join parts to retrieve text (handles edge-cases)
            text_val = "".join([part.text for part in content.parts if part.text])
            serializable_history.append({
                "role": content.role,
                "text": text_val
            })

        with open("history.json", "w", encoding="utf-8") as f:
            json.dump(serializable_history, f, ensure_ascii=False, indent=4)

except Exception as e:
    print("An error occurred:")
    print(e)