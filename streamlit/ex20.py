import streamlit as st

name=st.text_input("Whats your name:", key="username")

if st.session_state.username!="":
   st.write("name is:",st.session_state.username)
