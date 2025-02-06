#!/usr/bin/env python
# coding: utf-8

# In[25]:


import streamlit as st
import pandas as pd

# Caricare il dataset
df = pd.read_csv("elmi_fixed2.csv")

# Riempire i valori NaN nelle immagini con un placeholder
df["Immagine"] = df["Immagine"].fillna("https://via.placeholder.com/300")

# Creare la barra laterale con i filtri
st.sidebar.header("Filtri")
selected_epoca = st.sidebar.multiselect("Seleziona l'epoca", df["Epoca"].unique())
selected_provenienza = st.sidebar.multiselect("Seleziona la provenienza", df["Provenienza"].unique())
selected_materiale = st.sidebar.multiselect("Seleziona il materiale", df["Materiale"].unique())

# Filtrare i dati
df_filtrato = df.copy()
if selected_epoca:
    df_filtrato = df_filtrato[df_filtrato["Epoca"].isin(selected_epoca)]
if selected_provenienza:
    df_filtrato = df_filtrato[df_filtrato["Provenienza"].isin(selected_provenienza)]
if selected_materiale:
    df_filtrato = df_filtrato[df_filtrato["Materiale"].isin(selected_materiale)]

# Mostrare gli elmi in una griglia con 3 colonne
st.title("Brutti Ceffi del Met Museum")

cols = st.columns(3)
for i, (_, row) in enumerate(df_filtrato.iterrows()):
    with cols[i % 3]:
        st.image(row["Immagine"], caption=row["Nome"], use_column_width=True)
        st.write(f"**Epoca:** {row['Epoca']} | **Provenienza:** {row['Provenienza']}")
        st.write(f"**Materiale:** {row['Materiale']}")
        st.markdown(f"[🔍 Vedi in alta risoluzione]({row['Immagine']})")

# Aggiungere un pulsante per scaricare il dataset
st.sidebar.download_button(
    label="📥 Scarica il dataset",
    data=df.to_csv(index=False),
    file_name="elmi.csv",
    mime="text/csv"
)


# In[ ]:




