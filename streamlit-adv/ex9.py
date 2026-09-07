import streamlit as st

selected_course=st.multiselect("select courses",["Java","Python","c++"],default=["Python"])

clicked=st.button("Click Me")

if clicked:
    st.write("courses selected",selected_course)