import streamlit as st
import functions

# isntaliraj streamlit
# aplikaciju pokreni iz terminala komandom streamlit run web.py


todos = functions.get_todos()

st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This add is to increase your productivity')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Add new todo...')


