import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import json
import os
import time
from datetime import datetime

CHAT_DIR="chats"

def get_openai_client():
    load_dotenv()
    return OpenAI()

ai_client=get_openai_client()
os.makedirs(CHAT_DIR,exist_ok=True)

def new_chat():
    chat_id=datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path=os.path.join(CHAT_DIR,f"{chat_id}.json")
    messages=[{
        "role":"system",
        "content":(
                        "You are PyMentor, a Python Tutor."
                        "Answer only question related to Python Programming."
                        "For any other question politely refuse"
            )
    }]
    save_chat(file_path,messages)
    return chat_id

def save_chat(path,message):
    with open(path,"w") as f:
         json.dump(message,f,indent=4)
        
        
def load_chat(path):
     with open(path,"r") as f:
          return json.load(f)
    
def list_chats():
    file_list=os.listdir(CHAT_DIR)
    sorted_list=sorted(file_list,reverse=True)
    return sorted_list


def stream_chat_with_ai(message,temperature,model):
    placeholder=st.empty()
    stream=ai_client.responses.create(
        input=message,
        stream=True,
        temperature=temperature,
        model=model)
    
    full_response=""
    for event in stream:
        if event.type=="response.output_text.delta":
           token=event.delta
           full_response+=token
           placeholder.markdown(full_response)
    return full_response            

st.set_page_config(page_title="PyMentor V3",layout="centered")
st.title("🐍 PyMentor- Python Tutor Chatbot")
st.write("💡 Welcome To Your AI Powred Python Assistant")
st.caption("⌨️ Multiple Chats |🗨️ Streaming | 🔃 Resume Chat | 🎮 Controls Enabled")

st.sidebar.header("🫴🏽 Chat Settings")

if "current_chat" not in st.session_state:
    st.session_state.current_chat=new_chat()

all_chat_files=list_chats()
sel_index=all_chat_files.index(f"{st.session_state.current_chat}.json")
selected_chat=st.sidebar.selectbox("Select Chat",all_chat_files,index=sel_index)

if selected_chat.replace(".json","")!=st.session_state.current_chat:
    st.session_state.current_chat=selected_chat.replace(".json","")
    st.rerun()

if st.sidebar.button("➕ New Chat"):
    st.session_state.current_chat=new_chat()
    st.rerun()
    
model=st.sidebar.selectbox("Choose Model",["gpt-4o-mini","gpt-5.1"])
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=2.0,value=0.7,step=0.1)

chat_path=os.path.join(CHAT_DIR,f"{st.session_state.current_chat}.json")
messages=load_chat(chat_path)



message_count=len([m for m in messages if m["role"]!="system"])
st.sidebar.metric("🗣️Messages",message_count)

for msg in messages:
    if msg["role"]!="system":
        st.chat_message(msg["role"]).markdown(msg["content"])    

with st.form("chat_app",clear_on_submit=True):
    user_input=st.text_area("Ask a Python question:",height=100,placeholder="ex: Explain List in Python")
    submit=st.form_submit_button("Ask PyMentor")
if submit and user_input.strip():
         st.chat_message("user").markdown(user_input)
         messages.append({"role":"user","content":user_input})
         with st.chat_message("assistant"):
             typing=st.empty()
             typing.markdown("⌛ Pymentor is typing...")
             time.sleep(0.5)
             ai_reply=stream_chat_with_ai(messages,temperature,model)
             typing.write("")
         messages.append({"role":"assistant","content":ai_reply}) 
         save_chat(chat_path,messages)  
         st.rerun()
if st.sidebar.button("🗑️ Delete Chat"):
    os.remove(chat_path)
    st.session_state.current_chat=new_chat()
    st.rerun()        
             