import streamlit as st

gender=st.radio("select gender",["male","female","other"])
st.write("gender selected",gender)