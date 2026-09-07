import streamlit as st
pas=st.text_input("What is your password?",type="password")
if pas:
    st.write("Password entered")