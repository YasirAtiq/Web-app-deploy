###The WEB Interface version of the TO-DO LIST APP
##Importing
import streamlit as st

from Backend import *

##Making the todo list
todos = read_todos()


##Define add_todo()
def add_todo():
    t = st.session_state["new_todo"] + "\n"
    todos.append(t)
    modifying_todo(todos)


##Adding title to the web app
st.title('My Todo app')
st.subheader("My First TO-DO APP")
st.write("This app is to increase your productivity.")

##Adding elements:
# The checkboxes and list of the todos
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        modifying_todo(todos)
        del st.session_state[todo]
        st.rerun()


# Input and label
st.text_input(label="", placeholder="Enter the TO-DO:",
              on_change=add_todo, key="new_todo")

st.session_state
