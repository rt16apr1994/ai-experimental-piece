import streamlit as st

no1=st.number_input("Enter first number")
no2=st.number_input("Enter second number")  
Add=st.button("Add")
if Add:
    st.write("Addition is",no1+no2)