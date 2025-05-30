import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Initiation avec streamlit")
st.subheader("Auteur : Beni")
st.markdown("***Cette application affiche différents types de graphiques***")

# tracer lineaire

random_data = np.random.normal(size=1000)
st.line_chart(random_data)


# tracer un diagramme à barre
st.write(
    "Figure 1 : Visualisation des communes selon la population"
)
bar_data = pd.DataFrame(
    [100,19,88,54],
    ["bandal","Gombe","kintambo","kalamu"]
)

st.bar_chart(bar_data)
st.markdown(
    "Cette figure, nous montre que la plupart de enquêtés,"
    " provienne de la commune de Bandal, suivi de la commune de Kintambo"
    " la commune de Gombe est faiblement représentée."
)


df = pd.read_excel("data/try.xlsx")

df_s = pd.DataFrame(
    df["sexe"]
    )

# Create pie chart
fig = px.pie(df, names='sexe', values='Value', title='Pie Chart Example')

# Display in Streamlit
st.plotly_chart(fig)

st.pie_chart(df)