import streamlit as st
import functions_ToDo 

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions_ToDo.write_todos(todos)

todos = functions_ToDo.get_todos()

st.title('My ToDo app')
st.subheader('Add your todos here')
st.write('This app is a simple todo app that allows you to add, edit, and complete todos')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions_ToDo.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='', placeholder='Add a new todo...',
              on_change=add_todo, key='new_todo')