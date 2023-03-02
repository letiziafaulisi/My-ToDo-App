import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    """new function to add a new element to the to do list"""
    todo= st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

st.title("My ToDo app")
st.subheader("This is an app to encrease your productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label = "", placeholder = "Add a new ToDo", on_change=add_todo, key='new_todo')
