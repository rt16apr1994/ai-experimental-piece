from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime
import pygame
import sounddevice as sd
from scipy.io.wavfile import write

def get_openai_client():
    load_dotenv()
    return OpenAI()


def transcribe_audio(file_path):   
    with open(file_path, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=audio_file
        )
    return response.text

def get_ai_response(user_text):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
            "role": "system",
            "content": "You are a helpful assistant."
            },
            {
            "role": "user",
            "content": user_text
          }
        ]
    )
    return response.output_text

def convert_txt_to_audio(ai_reply):
    response=client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=ai_reply
    )
    audio_bytes=response.read()
    file_name = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"audio/{file_name}.mp3", "wb") as f:
        f.write(audio_bytes)
    print(f"Audio successfully saved to: audio/{file_name}.mp3")
    file_path=os.path.join("audio", f"{file_name}.mp3")
    file_abs_path=os.path.abspath(file_path)
    play_audio(file_abs_path)

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
def record_audio():
    fs = 44100  # Sample rate
    seconds = 10  # Duration of recording
    print("Recording...")
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    file_name = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"audio/{file_name}.wav"
    write(file_path, fs, myrecording)  # Save as WAV file
    print(f"Recording saved to: {file_path}")
    return file_path    

client = get_openai_client()
print("AI voice Assistant is ready. Please type 'exit' to quit.")
os.makedirs("audio", exist_ok=True)
while True:
    audio_path=record_audio()
    if audio_path.lower() == "exit":
        break
    if not os.path.exists(audio_path):
        print(f"Error: The file '{audio_path}' does not exist.")
        continue
    try:
        print("transcribing audio...")
        user_text = transcribe_audio(audio_path)
        print(f"Transcribed text: {user_text}")
        print("🤔thinking......")
        ai_reply = get_ai_response(user_text)
        print(f"AI reply: {ai_reply}")
        convert_txt_to_audio(ai_reply)
    except Exception as e:
        print(f"An error occurred: {e}")