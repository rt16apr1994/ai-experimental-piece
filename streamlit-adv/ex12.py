import streamlit as st

agree=st.checkbox("I agree to the terms and conditions")

if agree:
    st.write("You have agreed to the terms and conditions.")
