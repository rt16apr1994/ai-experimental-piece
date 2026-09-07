import streamlit as st

def greetings():
    st.write("Hello, welcome to User ji")

st.button("Press me",on_click=greetings)