from google import genai
from dotenv import load_dotenv
import os
import json
from google.genai import types

load_dotenv()

PROMPT = (
    "You are a helpful python tutor. Please answer questions related to python only "
    "in a concise manner. If the question is not related to python, politely decline to answer."
)
CHAT_FILE = "chat_history.json"

def getClient():
    # Grabs GEMINI_API_KEY from environment variables automatically
    return genai.Client()

def howMayIhelpYou(messages):
    client = getClient()
    config = types.GenerateContentConfig(system_instruction=PROMPT)
    resp = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=messages, 
        config=config
    )
    return resp.text

def save_chat_history(messages):
    serializable_history = []
    # Loop over the real SDK objects and create a clean JSON-friendly list
    for message in messages:
        text_val = "".join([part.text for part in message.parts if part.text])
        serializable_history.append({
            "role": message.role, 
            "text": text_val
        })
        
    with open(CHAT_FILE, "w", encoding="utf-8") as file_obj:
        json.dump(serializable_history, file_obj, ensure_ascii=False, indent=4)

def load_chat_history():
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r", encoding="utf-8") as file_obj:
            try:
                raw_messages = json.load(file_obj)
                sdk_messages = []
                # CRITICAL: Reconstruct JSON data back into SDK types
                for item in raw_messages:
                    sdk_messages.append(
                        types.Content(
                            role=item["role"],
                            parts=[types.Part.from_text(text=item["text"])]
                        )
                    )
                return sdk_messages, False # Found history, not first time
            except json.JSONDecodeError:
                # If file is empty or corrupted, start fresh
                return [], True
    else:
        return [], True

try: 
    messages = []
    client = getClient()
    messages, first_time = load_chat_history()
    
    # Fixed logic condition here
    if not first_time:
         print("Chat resumed. Continue your python session! Type 'exit' or 'quit' to end.")
    else:
         print("Welcome to the Python Tutor Chat! Type 'exit' or 'quit' to end the conversation.")
         
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            # Call save function which handles serialization smoothly
            save_chat_history(messages)
            print("Exiting the program. History saved.")
            break
            
        if not user_input.strip():
            continue
            
        # Append User Message using modern helper .from_text()
        messages.append(types.Content(role="user", parts=[types.Part.from_text(text=user_input)]))
        
        ai_response = howMayIhelpYou(messages)
        print("AI answer:", ai_response)
        
        # Append AI Message
        messages.append(types.Content(role="model", parts=[types.Part.from_text(text=ai_response)]))
        
except Exception as e:
    print(f"An error occurred: {e}")