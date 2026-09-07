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


def solve_math_ai(question, system_prompt):
    response = client.responses.create(
    model="gpt-4o-mini",  # Best model for fast, cost-efficient tasks
    input=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]
   )
    print(response.output_text)



try:
    client = get_openai_api_key()
    print("I'm a math expert. I can help you solve math problems.")
    while True:
        question = input("Enter a math question (or type 'exit' to quit): ")
        if question.lower() in ["exit", "quit"]:
            print("Exiting the program.")
            break
        else:
            solve_math_ai(question, "You are a math expert. You can help solve math problems with direct answers.")
except Exception as e:
    print(f"An error occurred: {e}")
