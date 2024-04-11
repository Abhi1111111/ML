import streamlit as st
st.write("hello world")
x=st.text_input("favourite movie?")
st.write(f"favourite movie is {x}")
is_clicked=st.button("click me")
