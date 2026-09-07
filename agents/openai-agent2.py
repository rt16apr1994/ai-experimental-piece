from agents import Agent,Runner, function_tool
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
@function_tool
def get_current_time():
    print("1.Tool called")
    """
    Return the current data and time

    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
@function_tool
def get_wheather(city:str):
    print("2.Tool called")
    """
    Return the current wheather of the city

    """
    wheather_data ={

        "New York": "Sunny, 25°C",
        "Delhi": "Cloudy, 30°C",
        "Bhopal": "Rainy, 22°C",
    }
    return wheather_data.get(city, "City not found")

agent=Agent(name="My Agent",
            instructions="You are a helpful assistant.",
            tools=[get_current_time, get_wheather])

user_question=input("Question:")

response=Runner.run_sync(agent,user_question)
print("Response is:",response.final_output)

