from agents import Agent,Runner, function_tool
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
@function_tool
def get_fee_for_course(course:str)->str:
    print("Tool called")
    """
    Return the fee for the course
    Args:
        course: name of the course
    """
    course_fee ={

        "Python": "$100",
        "Java": "$150",
        "C++": "$200",
    }
    return course_fee.get(course, "Course not found")

agent=Agent(name="My Agent",
            instructions="You are a helpful assistant.",
            tools=[get_fee_for_course])

user_question=input("Question:")

response=Runner.run_sync(agent,user_question)
print("Response is:",response.final_output)

