import streamlit as st
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"Name is {self.name} and Age is {self.age}"

p=Person("Dayanand",30)
st.write(p)