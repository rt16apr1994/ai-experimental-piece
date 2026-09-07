import streamlit as st

name=st.text_input("Whats your name:")

if name:
   st.session_state.username=name

if "username" in st.session_state:
    st.write("name is:",st.session_state.username)