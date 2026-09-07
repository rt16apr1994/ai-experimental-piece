import streamlit as st
st.title("💬Chat Application")
name=st.sidebar.text_input("Enter your name", key="name")
age=st.sidebar.number_input("Enter your age", key="age")
st.write(f"Hello {name}, you are {age} years old.")