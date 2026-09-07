from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
# Initialize the client (automatically reads the OPENAI_API_KEY environment variable)
def get_openai_client():
    return OpenAI()
client = get_openai_client()

def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=audio_file
        )
    return response.text

def chat_with_ai(transcribed_text,question):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[

               {
                   "role": "user",
                   "content": f"""Here is the transcribed text from the audio: {transcribed_text}. Please answer the following question based on this text: {question}"""
               }
                
        ]
     )
    return response.output_text

audio_path="audio/audio2.m4a"

print("Enter the audio file path:")
audio_path = input().strip()

if not os.path.isfile(audio_path):
    print(f"Error: The file '{audio_path}' does not exist.")
else:
    print("Please type exit to quit")
    while True:
        print("Enter your question about the audio:")
        question = input().strip()
        if question.lower() == "exit":
            break
        transcribed_text = transcribe_audio(audio_path)
        answer = chat_with_ai(transcribed_text, question)
        print(f"🐕‍🦺Answer: {answer}")