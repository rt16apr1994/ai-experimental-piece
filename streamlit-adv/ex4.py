import streamlit as st

def greetings(name):
    st.write(f"Hello, welcome, {name}!")

name = st.text_input("What's your name?")
st.button("Press me", on_click=greetings, args=(name,))