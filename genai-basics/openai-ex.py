import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load the environment variable from your .env file
load_dotenv()

# 2. Initialize the client (automatically reads OPENAI_API_KEY from environment)
client = OpenAI()

# 3. Call the chat completion endpoint
response = client.chat.completions.create(
    model="gpt-4o-mini",  # Best model for fast, cost-efficient tasks
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain quantum computing in one sentence."}
    ],
    temperature=0.7
)

# 4. Print the text response
print(response.choices[0].message.content)
