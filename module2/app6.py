import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("data/try.xlsx")

df = pd.DataFrame(df)

st.title ("Tableau N.1 : Répartition des enquêtés")
st.header ("Age , Sexe et la Commune des résidences")

st.write (
    "Ce tableau nous permet de visualiser les données du terrain."
    " Nous sommes en pleine reconstitution avec streamlit."
)

st.dataframe(df.head())
#st.dataframe(df.info)
st.write(f"la taille de dataset:{df.shape}")
st.write(f"le total est :{df.shape[0]} interviews")
st.write(f"le nb des colonnes est :{df.shape[1]} variables")
#st.bar_chart(df["commune"])

#df.count()

# st.dataframe(df)
# st.bar_chart(df)

#df_aggregate = df.groupby("sexe")["commune"].count()

#st.write(df_aggregate)

df_compte = df["sexe"].value_counts()
df_pourcentage = df_compte / len(df) * 100

#df_pourcentage = pd.DataFrame(df_pourcentage)
#st.write(df_compte)
#st.write(df_pourcentage)

# Table de répartition
repartition = pd.DataFrame({
        'Effectif': df_compte,
        'Pourcentage (%)': df_pourcentage.round(2)
    })

st.subheader("Tableau de répartition")
st.dataframe(repartition)

# --- Graphique ---
st.subheader("Visualisation")
fig, ax = plt.subplots()
repartition['Effectif'].plot(kind='bar', ax=ax, color=['skyblue', 'lightcoral'])
ax.set_ylabel("Effectif")
ax.set_xlabel("Sexe")
ax.set_title("Répartition des sexes")
st.pyplot(fig)

