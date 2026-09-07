import streamlit as st

def print_details(name, age):
    st.write(f"Name: {name}, Age: {age}")

name = st.text_input("What's your name?")
age = st.number_input("What's your age?", step=1)
st.button("Print Details", on_click=print_details, kwargs={"name": name, "age": age})