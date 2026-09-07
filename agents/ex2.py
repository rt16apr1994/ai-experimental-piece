from openai import OpenAI
from dotenv import load_dotenv  
from datetime import datetime

def get_openai_client():
    load_dotenv()
    return OpenAI() 

def get_current_time():
    print("Tool called")
    """
    Return the current data and time

    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

tools = [

          {
            "type":"function",
            "name":"get_current_time",
            "description": "Returns the current date and time",
            "parameters": {

                                "type": "object",
                                "properties":{},
                                "required":[],
                                "additionalProperties":False
                        },
                        "strict":True
        }
]

system_prompt="""
           You are a helpful assistent.
           Use get_current_time whenever user asks current date and time.

"""

def model_planning(user_question):
    response=client.responses.create(
                                    model="gpt-4o-mini",
                                    instructions=system_prompt,
                                    input=user_question,
                                    tools=tools


                                 ) 
    return response

def process_response(response):
    for item in response.output:
            if item.type=="function_call":
                tool_name=item.name
                result=get_current_time()
                tool_output={
                    "type":"function_call_output",
                    "call_id":item.call_id,
                    "output":result


                }
                response=client.responses.create(
                                                model="gpt-4o-mini",
                                                input=[tool_output],
                                                previous_response_id=response.id,
                                                tools=tools


            )
    return response

client=get_openai_client()
user_question=input("enter question:")
response=model_planning(user_question)
response=process_response(response)
print("Response is:"+response.output_text)








