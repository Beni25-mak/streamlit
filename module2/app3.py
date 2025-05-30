import streamlit as st

st.markdown("# Streamlit :red[tutorial]")

widget = st.radio ("which widget do you prefer?", ["Button","Checkbox"])

st.write("Here's your widget")

if widget == "Button":
    if st.button("show", type="primary"):
        pass
else:
    if st.checkbox("show"):
        pass
