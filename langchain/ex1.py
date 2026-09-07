from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm=ChatOpenAI(model="gpt-4o-mini")
aimessage=llm.invoke("what is the capital of France?")
print("Response is:",aimessage.content)