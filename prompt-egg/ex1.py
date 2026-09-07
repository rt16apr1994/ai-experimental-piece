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

def create_prompt(topic):
    return [
        {"role": "system", "content": "You are a python tutor."},
        {"role": "user", "content": f"Explain python {topic} in simple words with one example."}
    ]


def chat_with_ai(prompt):
    response = client.responses.create(
    model="gpt-4o-mini",  # Best model for fast, cost-efficient tasks
    input=prompt
   )
    print(response.output_text)

try:
    client = get_openai_api_key()
    while True:
        topic = input("Enter a topic to learn about (or type 'exit' to quit): ")
        if topic.lower() in ["exit", "quit"]:
            print("Exiting the program.")
            break
        else:
            prompt = create_prompt(topic)
            chat_with_ai(prompt)
except Exception as e:
    print(f"An error occurred: {e}")



