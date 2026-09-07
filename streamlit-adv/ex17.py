import streamlit as st
import datetime
if "bookings" not in st.session_state:
    st.session_state.bookings = []
st.title("📅Appointment Booking and cost calculation")
selected_date=st.date_input("select appointment date")
selected_time=st.time_input("select appointment time",value=datetime.time(10, 0))
sel_service=st.selectbox("select service",["Consultation","Premium","Emergency"])
duration=st.number_input("Enter duration in hours",min_value=1,max_value=8,step=1)
prices={"Consultation":500,"Premium":1000,"Emergency":2000}
if sel_service in prices:
    cost=prices[sel_service]*duration
    st.write(f"💰Total cost for {sel_service} service for {duration} hours is: ₹{cost}")
if st.button("Confirm Booking"):
    st.success(f"✅ Appointment booked")
    bookings=({
        "date": selected_date, 
        "time": selected_time,
        "service": sel_service
    })
    st.session_state.bookings.append(bookings)

if st.session_state.bookings:
    st.write("📅Booked Appointments:")
    for i,booking in enumerate(st.session_state.bookings,start=1):
        st.write(f"{i}. Date: {booking['date'].strftime('%d-%m-%Y')}, Time: {booking['time'].strftime('%H:%M:%S')}, Service: {booking['service']}")
else:
    st.write("No appointments booked yet.")