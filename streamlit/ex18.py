import streamlit as st
count=0
clicked=st.button("Add")
if clicked:
    count+=1
st.write("count is",count)