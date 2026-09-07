import streamlit as st
page=st.sidebar.radio("Go to",["Home","Profile","Settings"])
if page=="Settings":
    st.write("🎑This is the settings page.")
    st.write("You can adjust your preferences here.")
elif page=="Profile":
    st.write("🥲This is your profile page.")
    st.write("You can view and edit your profile information here.")    
else:
    st.write("🏡Welcome to the home page!")
    st.write("This is where you can find the latest updates and news.")
