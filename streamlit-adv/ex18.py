import streamlit as st
message=st.chat_input("Type your message here...")
if message:
   st.write(message)