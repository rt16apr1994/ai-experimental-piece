from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
aimessage=llm.invoke("what is the capital of France?")
print("Response is:",aimessage.content)