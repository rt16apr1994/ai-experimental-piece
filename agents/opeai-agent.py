from agents import Agent,Runner, function_tool
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
@function_tool
def get_current_time():
    print("Tool called")
    """
    Return the current data and time

    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

agent=Agent(name="My Agent",
            instructions="You are a helpful assistant.",
            tools=[get_current_time])

user_question=input("Question:")

response=Runner.run_sync(agent,user_question)
print("Response is:",response.final_output)

