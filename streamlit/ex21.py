import streamlit as st
if "count" not in st.session_state:
    st.session_state.count=0
clicked=st.button("Add")
if clicked:
    st.session_state.count+=1
st.write("count is",st.session_state.count)