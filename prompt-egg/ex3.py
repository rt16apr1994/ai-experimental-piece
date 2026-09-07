import os
from urllib import response
from dotenv import load_dotenv
from httpcore import stream
from openai import OpenAI

# 1. Load the environment variable from your .env file
load_dotenv()

# 2. Initialize the client (automatically reads OPENAI_API_KEY from environment)
def get_openai_api_key():
    client = OpenAI()
    return client


def chat_with_ai(sentence):
    SYSTEM_PROMPT = """You are english grammar expert teacher.
                    you help user solving only english grammar related problems.
                    if user enters incorrect sentences or spelling mistakes then correct them
                    you don't explain untill you are asked.
                    Example:
                    User: I has a apple.
                    You: I have an apple."""
    response = client.responses.create(
    model="gpt-4o-mini",  # Best model for fast, cost-efficient tasks
    input=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": sentence}
    ]
   )
    print(response.output_text)

try:
    client = get_openai_api_key()
    print("I'm an English grammar expert. I can help you correct your sentences.")
    while True:
        sentence = input("Enter a sentence to correct (or type 'exit' to quit): ")
        if sentence.lower() in ["exit", "quit"]:
            print("Exiting the program.")
            break
        else:
            chat_with_ai(sentence)
except Exception as e:
    print(f"An error occurred: {e}")



