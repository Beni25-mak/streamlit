import streamlit as st

st.markdown ("# Présentation de :red[REACH-IMPACT]")
st.markdown ("### Liste des unités chez Reach-Impact:")

db_unite=["Redevabilté & Resiliance",
            "Data & GIS",
            "Intersectorielle",
            "Santé Publique & Nutrition",
            "JIMMY",
            "GTAC"]

if st.button("Show", type="primary"):
    st.write(db_unite)