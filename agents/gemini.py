from google import genai
from datetime import datetime
from dotenv import load_dotenv

def get_genai_client():
    load_dotenv()
    client=genai.Client()
    return client

def get_current_time():
    print("Tool called")
    """
    Return the current data and time

    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

client=get_genai_client()
user_question=input("Question:")
response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_question,
    config={"tools":[get_current_time]}

)
print("Response is:",response.text)