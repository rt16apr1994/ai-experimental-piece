import streamlit as st

def add(no1, no2):
    st.write(f"Sum is: {no1+no2}")

no1 = st.number_input("Enter first number",step=1)
no2 = st.number_input("Enter second number",step=1)
st.button("Add numbers", on_click=add, args=(no1, no2))