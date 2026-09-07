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


def chat_with_ai(question):
    SYSTEM_PROMPT = """You are ai expirt in coding.
                    You only know python nothing else.
                    you help user solving only python related problems.
                    if user ask any other question then roste them """
    response = client.responses.create(
    model="gpt-4o-mini",  # Best model for fast, cost-efficient tasks
    input=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question}
    ]
   )
    print(response.output_text)

try:
    client = get_openai_api_key()
    while True:
        question = input("Enter a question about Python (or type 'exit' to quit): ")
        if question.lower() in ["exit", "quit"]:
            print("Exiting the program.")
            break
        else:
            chat_with_ai(question)
except Exception as e:
    print(f"An error occurred: {e}")



