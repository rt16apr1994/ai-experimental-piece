import streamlit as st
adhar=st.text_input("What is your adhar number?", max_chars=6)
if adhar:
    st.write("Adhar number entered", adhar)