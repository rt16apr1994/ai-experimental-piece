import streamlit as st
name=st.text_input("What is your name?", placeholder="Guest")
if name:
    st.write("Welcome",name)

