import streamlit as st

selected_country=st.multiselectbox("select courses",["Java","python","c++"])

clicked=st.button("Click Me")

if clicked and selected_country != "--select--":
    st.write("country clicked",selected_country)