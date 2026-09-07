from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm=ChatOpenAI(model="gpt-4o-mini",frequency_penalty=1.0,temperature=0.5,top_p=0.9)
aimessage=llm.invoke("what is top 3 model?")
print("Response is:",aimessage.content)