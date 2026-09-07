
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


transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=open("audio/audio.m4a", "rb"),
    prompt="Please transcribe the following audio file into text.",
    response_format="text", 
    language="en"
)


print("Transcription:", transcription)
