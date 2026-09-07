import streamlit as st
st.markdown("<h3 style='color: blue;'>This is a heading</h3>", unsafe_allow_html=True)
st.success("This is a success message")
st.info("This is an info message")
st.warning("This is a warning message")
st.error("This is an error message")
exp=ZeroDivisionError("This is zero division exception message")
st.exception(exp)