import streamlit as st
address=st.text_area("What is your address?", height=500)
if address:
    st.write("Address entered")
    st.write(address)