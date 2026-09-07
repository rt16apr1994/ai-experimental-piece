import streamlit as st
import datetime
select_time=st.time_input("select time")
st.write("time selected",select_time.strftime("%H:%M:%S"))
st.write("hour selected",select_time.hour)
st.write("minute selected",select_time.minute)      
st.write("second selected",select_time.second)