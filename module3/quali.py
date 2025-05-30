import streamlit as st  
import pandas as pd 
import numpy as np  
import matplotlib.pyplot as plt

st.title(" :red[Anlayse des données qualitative]")
#st.subheader(":blue[Auteur] :blue[M. Beni Nzimba]")

st. header(":red[0. Avant-propos]")
st.write("Dans ce premier point, nous présentons les différentes analyses des données."
         " concernant les variables qualitatives sexe et communes des personnes interviwés")

st.header (":red[1. Présentation des variables]")
st.subheader(":red[A. Tableaux]")
st.subheader(":blue[Tableau 1: présentation des données]")

#### partie : Python

# Upload du fichier
uploaded_file = st.file_uploader("Choisissez un fichier Excel", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        st.write(df)
    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier : {e}")
else:
    st.warning("Veuillez uploader un fichier Excel.")

#excel_file = "try.xlsx"

#df = pd.read_excel(excel_file)

#df_d = pd.DataFrame(df)
#df_d.head()
#df_d.info()
#df_d.shape[0]

#st.dataframe(df.head())
st.write(
    f"le tableau 1, répresente les données d'une manière succintes, le tableau nous renseigne que"
    f"nous avons les individus, les variables âge, sexe et commune. Au total :blue[{df.shape[0]} individus.]"
    )

st.subheader(":blue[Tableau 2 : Répartition des individus selon le sexe.]")

effectif = df['sexe'].value_counts()
pourcentage = effectif/len(df)*100
rep_sex = pd.DataFrame({
    'Effectif': effectif,
    'Pourcentage(%)':pourcentage.round(1)
})

st.dataframe(rep_sex)

st.write(
    f"le tableau 2, nous renseigne que la plupart des individus avaient de sexe masculin soit :blue[6(66,67%)] "
    f" contre les personnes de sexe feminin :blue[3(33,33%)]"
)

st.subheader(":blue[Tableau 3 : Répartition des individus selon la commune de résidence]")

effectif0 = df['commune'].value_counts()
pourcentage0 = effectif0/len(df)*100
rep_com = pd.DataFrame({
    'Effectif0': effectif0,
    'Pourcentage(%)':pourcentage0.round(1)
})

st.dataframe(rep_com)

st.write(
    f"le tableau 3, nous renseigne que la plupart des individus proviennent de Kintambo soit :blue[5(55,6%)] "
    f" contre :blue[4(44,4%)] proviennet de la commune de bandal"
)

st.subheader(":red[B. Graphiques]")

# --- Graphique ---
st.subheader(":blue[Figure 1 : Distribution des individus selon le sexe]")
fig, ax = plt.subplots()
rep_sex['Effectif'].plot(kind='bar', ax=ax, color=['skyblue', 'lightcoral'])
ax.set_ylabel("Effectif")
ax.set_xlabel("Sexe")
ax.set_title("Répartition des sexes")
st.pyplot(fig)

# --- Graphique ---
st.subheader(":blue[Figure 2 : Distribution des individus selon la commune de résidence]")
fig, ax = plt.subplots()
rep_com['Effectif0'].plot(kind='bar', ax=ax, color=['skyblue', 'lightcoral'])
ax.set_ylabel("Effectif0")
ax.set_xlabel("commune")
ax.set_title("Répartition des communes")
st.pyplot(fig)

st. header(":red[2. Conclusion]")

st.markdown("Nous présentons nos sincères merci, pour la curiosité que"
            " :blue[**le seigneur Jesus-christ**], nous avoir dopter de cette capacités" 
            "pour comprendre et mettre en place mes analyses sur streamlit")

st.write(f"Auteur : :blue[Beni nzimba]")
st.write(f"Fait à Kinshasa,   :red[le 30 mai 2025]")