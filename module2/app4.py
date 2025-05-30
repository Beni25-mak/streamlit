import streamlit as st

st.sidebar.title("Streamlit :red[Tutorial]")
st.sidebar.header(":blue[Introduction to Databases]")
st.sidebar.subheader(": web application")


option= st.selectbox(
    'choose a DBMS to connect to',
    ("MYSQL","Oracle","PHP","Python")
)