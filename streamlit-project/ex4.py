import streamlit as st
import os
from dotenv import load_dotenv
import json
from openai import OpenAI
import time

CHAT_FILE = "chat_history.json"

def save_chat_history(messages):
    with open(CHAT_FILE, "w") as f:
        json.dump(messages, f, indent=4)

def load_chat_history():
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r") as f:
            return json.load(f)
    else:
        return [{"role": "system",
                  "content": "You are a python tutor."
                             "Answetr questions in a concise and clear manner."
                             "for any other questions, politely decline and redirect the user to ask python related questions."
                 }]
def get_openai_client():
    load_dotenv()
    return OpenAI()
ai_client = get_openai_client()

def stream_chat_with_ai(message,temp,model):
    placeholder = st.empty()
    placeholder.markdown("💬 **Pymentor is thinking...**")
    stream = ai_client.responses.create(model=model,input=message,stream=True,temperature=temp
    )
    full_response = ""
    for event in stream:
        if event.type == "response.output_text.delta":
            token = event.delta
            full_response += token
            placeholder.markdown(full_response)
    return full_response
st.set_page_config(page_title="Pymentor", page_icon="💬", layout="centered")
st.title("🐍 Pymentor-Python Tutorial Chatbot")
st.write("💡Welcome to your AI powered python assistant!")
st.caption("💬 Streaming | 🗣️ Resume chat | 🛂 Control Enabled")

st.sidebar.header("⚙️Chat Settings")
model=st.sidebar.selectbox("Select Model", ["gpt-4o-mini", "gpt-4o"])
temp=st.sidebar.slider("Temperature", min_value=0.0, max_value=2.0, value=0.5, step=0.1)

if "message" not in st.session_state:
    st.session_state.message = load_chat_history()

message_count = len([msg for msg in st.session_state.message if msg["role"] != "system"])
st.sidebar.write(f"💬 Total Messages: {message_count}")
for msg in st.session_state.message:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).markdown(msg["content"])

with st.form("chat_app", clear_on_submit=True):
    user_input = st.text_area("Ask python questions...", key="user_input", height=100,placeholder="Type your question here...")
    submit_button = st.form_submit_button("Ask Pymentor")

if submit_button:
    if user_input.strip() == "":
        st.warning("Please enter a question before submitting.")
    else:
        st.chat_message("user").markdown(user_input)
        st.session_state.message.append({"role": "user", "content": user_input})
        with st.chat_message("assistant"):
            typing_placeholder = st.empty()
            typing_placeholder.markdown("⌛ **Pymentor is thinking...**")
            time.sleep(0.5)  # Simulate a brief thinking delay
            ai_reply = stream_chat_with_ai(st.session_state.message, temp, model)
            typing_placeholder.empty()
        st.session_state.message.append({"role": "assistant", "content": ai_reply})
        save_chat_history(st.session_state.message)
    st.rerun()
