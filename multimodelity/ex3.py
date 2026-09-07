import base64
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Initialize the client (automatically reads the OPENAI_API_KEY environment variable)
client = OpenAI()

# Function to encode a local image into base64 format
def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


# --------------------------------------------------
# Analyze and Describe Image (Responses API)
# --------------------------------------------------

image_path = input("Enter the path to the image: ")  # Prompt user for image path
user_input = input("Enter your question about the image: ")  # Prompt user for question
base64_image = encode_image(image_path)

# Call the Responses API
response = client.responses.create(
    model="gpt-4o",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": user_input
                },
                {
                    "type": "input_image",
                    "image_url": f"data:image/png;base64,{base64_image}"
                },
            ],
        }
    ],
)

# Extract and print the generated text
print("### Image Description:\n")
print(response.output_text)