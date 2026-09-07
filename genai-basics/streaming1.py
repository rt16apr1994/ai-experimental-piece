import os
from dotenv import load_dotenv
from httpcore import stream
from openai import OpenAI

# 1. Load the environment variable from your .env file
load_dotenv()

# 2. Initialize the client (automatically reads OPENAI_API_KEY from environment)
def get_openai_api_key():
    client = OpenAI()
    return client

# 3. Call the chat completion endpoint
def chat_with_ai(question):
    stream = client.responses.create(
    model="gpt-4o-mini",  # Best model for fast, cost-efficient tasks
    input=question,
    stream=True  # Enable streaming
   )
    for event in stream:
        if event.type == "response.output_text.delta":
            print(event.delta, end="") 

try:
    client = get_openai_api_key()
    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit"]:
            print("Exiting the program.")
            break
        else:
            chat_with_ai(question)
except Exception as e:
    print(f"An error occurred: {e}")



