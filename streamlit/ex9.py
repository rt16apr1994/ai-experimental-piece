import streamlit as st
name=st.text_input("What is your name?", value="Guest")
if name:
    st.write("Welcome",name)

