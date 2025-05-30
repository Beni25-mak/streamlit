import streamlit as st

st.markdown('# Streamlit : red[Tutorial]')

if st.checkbox("Accept the conditions"):
    st.write("Thanks for accepting me!")
else:
    st.write("Please, accept me!")

