import os
import base64
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
# Initialize the client (automatically reads the OPENAI_API_KEY environment variable)
client = OpenAI()

# --------------------------------------------------
# Generate and Save Image
# --------------------------------------------------


response = client.images.generate(
    model="gpt-image-1",
    prompt="A smiling cute baby",
    size="1024x1024",              # Options: "1024x1024", "1024x1792", "1792x1024"            # Options: "standard" or "hd"   # Returns raw bytes directly
    n=3,
)

os.makedirs("generated",exist_ok=True)
# Decode base64 image data and save to disk
for i, img_data in enumerate(response.data):
    img_b64 = img_data.b64_json
    img_bytes = base64.b64decode(img_b64)
    output_file = f"generated/image_{i+1}.png"
    with open(output_file, "wb") as f:
        f.write(img_bytes)
    print(f"Image successfully saved to: {output_file}")
