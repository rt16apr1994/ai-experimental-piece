import streamlit as st
import os
from dotenv import load_dotenv
import json
from openai import OpenAI

def get_openai_client():
    load_dotenv()
    return OpenAI()
ai_client = get_openai_client()

def stream_chat_with_ai(message):
    placeholder = st.empty()
    placeholder.markdown("💬 **Pymentor is thinking...**")
    stream = ai_client.responses.create(model="gpt-4o-mini",input=message,stream=True
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

if "message" not in st.session_state:
    st.session_state.message = []

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
            ai_reply = stream_chat_with_ai(st.session_state.message)
        st.session_state.message.append({"role": "assistant", "content": ai_reply})
    st.rerun()
