import streamlit as st
import functions

todos = functions.get_todos()
st.title("My ToDo app")
st.subheader("This is an app to encrease your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label = "", placeholder = "Add a new ToDo")

