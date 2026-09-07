import streamlit as st
st.title("💬Chat Application")
if "message" not in st.session_state:
    st.session_state.message=[]
user_input=st.chat_input("Type your message here...")
if user_input:
   st.session_state.message.append({"role": "user", "content": user_input})
   st.session_state.message.append({"role": "assistant", "content": "🐕‍🦺" + user_input})
for msg in st.session_state.message:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])