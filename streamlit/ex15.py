import streamlit as st
age=st.number_input("What is your age?",min_value=0,max_value=100,step=2)
if age:
    st.write("Age entered", age)