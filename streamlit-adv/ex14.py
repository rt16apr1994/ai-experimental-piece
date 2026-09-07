import streamlit as st
import datetime
select_date=st.date_input("select date", min_value=datetime.date(2020, 1, 1), max_value=datetime.date(2027, 12, 31))
st.write("date selected",select_date.strftime("%d-%m-%Y"))
st.write("date selected",select_date.day)
st.write("month selected",select_date.month)
st.write("year selected",select_date.year)    
