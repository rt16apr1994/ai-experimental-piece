import streamlit as st

file_upload=st.file_uploader("Upload file",type=["jpg","png","jpeg"])
if file_upload is not None:
    st.write("file uploaded",st.image(file_upload))
