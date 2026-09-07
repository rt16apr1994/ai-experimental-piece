from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
def load_env():
    load_dotenv()

def initialize_llm():
    llm=ChatOpenAI(model="gpt-4o-mini")
    return llm

def start_chat(llm):
    print("AI is thinking...")
    print("Type exit to quit")
    coversation_history=[SystemMessage(content="You are a helpful assistant who answers politely and clearly.")]
    while True:
        user_input=input("User:")
        if user_input.lower()=="exit":
            print("Exiting...")
            break
        coversation_history.append(HumanMessage(content=user_input))
        aimessage=llm.invoke(coversation_history)
        print("AI:",aimessage.content)
        coversation_history.append(AIMessage(content=aimessage.content))
        print("Conversation history:",coversation_history)

load_env()
llm = initialize_llm()
start_chat(llm)
print("Chat ended.")