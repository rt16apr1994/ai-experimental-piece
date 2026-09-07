from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
# Initialize the client (automatically reads the OPENAI_API_KEY environment variable)
def get_openai_client():
    return OpenAI()
client = get_openai_client()
response=client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="marin",
    input="नमस्ते, यह OpenAI API की टेक्स्ट-टू-स्पीच क्षमताओं का एक टेस्ट है। सुनने का आनंद लें!"
)
os.makedirs("audio", exist_ok=True)
audio_bytes=response.read()
with open("audio/output1.mp3", "wb") as f:
    f.write(audio_bytes)
print("Audio successfully saved to: audio/output.mp3")