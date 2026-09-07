import streamlit as st
if "count" not in st.session_state:
    st.session_state.count=0

def increment_counter():
    st.session_state.count += 1
clicked=st.button("Add")
if clicked:
    increment_counter()
st.write("count is",st.session_state.count)