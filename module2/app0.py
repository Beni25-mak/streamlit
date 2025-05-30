import streamlit as st


# st.title("Streamlit :red[Tutorial]")
# st.header(":blue[Introduction to Databases]")
# st.subheader("web applications")
# st.text("My first web page in a few lines,je suis # beni nzimba ")

st.markdown("# Streamlit :red[Tutorial]")
st.markdown("## :blue[Introduction to Databases]")
st.markdown("### web applications")
st.markdown(""">_"if, at first, you **do not** succed, call it version 1.0"
            **kyahri R.R. Woulfe**_""")
html_string="""<p style="front-family:courier;color:red">streamlit accepts:</p>
        <ul>
            <li> Built-in text elements </li>
            <li> Markdown</li>
            <li> HTML</li>
        <ul>"""
st.markdown(html_string, unsafe_allow_html=True)