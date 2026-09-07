import base64
import mimetypes
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def get_openai_api_key():
    client = OpenAI()
    return client


client = get_openai_api_key()


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def chat_with_ai(image_path, user_input):
    # Dynamically detect MIME type based on file extension (e.g., image/jpeg, image/png, image/webp)
    mime_type, _ = mimetypes.guess_type(image_path)
    if not mime_type or not mime_type.startswith("image/"):
        mime_type = "image/jpeg"  # Safe default fallback

    base64_image = encode_image(image_path)

    response = client.responses.create(
        model="gpt-4o",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": user_input,
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:{mime_type};base64,{base64_image}",
                    },
                ],
            }
        ],
    )

    return response.output_text


print("Welcome to the Image Analysis Chatbot!")
image_path = input("Enter the path to the image: ")
user_input = input("Enter your question about the image: ")

result = chat_with_ai(image_path, user_input)
print("AI Response:", result)