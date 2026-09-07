import streamlit as st
import datetime
st.title("📅Appointment Booking and cost calculation")
selected_date=st.date_input("select appointment date")
selected_time=st.time_input("select appointment time",value=datetime.time(10, 0))
sel_service=st.selectbox("select service",["Consultation","Premium","Emergency"])
duration=st.number_input("Enter duration in hours",min_value=1,max_value=8,step=1)
prices={"Consultation":500,"Premium":1000,"Emergency":2000}
if sel_service in prices:
    cost=prices[sel_service]*duration
    st.write(f"💰Total cost for {sel_service} service for {duration} hours is: ₹{cost}")
if st.button("Book Appointment"):
    st.success(f"✅ Appointment booked")
    st.write("📅Date selected",selected_date.strftime("%d-%m-%Y"))
    st.write("⏰ time",selected_time.strftime("%H:%M:%S"))
    st.write("💼 service:",sel_service)
