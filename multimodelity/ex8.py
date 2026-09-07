from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
# Initialize the client (automatically reads the OPENAI_API_KEY environment variable)
def get_openai_client():
    return OpenAI()
client = get_openai_client()

def translate_audio(file_path):
    with open(file_path, "rb") as audio_file:
        response = client.audio.translations.create(
            model="whisper-1",
            file=audio_file
        )
    return response.text

audio_path="audio/audio2.m4a"

translate_text=translate_audio(audio_path)
print(translate_text)