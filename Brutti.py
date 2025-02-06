#!/usr/bin/env python
# coding: utf-8

# In[25]:


import streamlit as st
import pandas as pd

# Caricare il dataset
df = pd.read_csv("elmi_fixed2.csv")

# Riempire i valori NaN nelle immagini con un placeholder
df["Immagine"] = df["Immagine"].fillna("https://via.placeholder.com/300")

# Stile CSS per un design più moderno
st.markdown(
    """
    <style>
    .elmo-card {
        border-radius: 12px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        padding: 10px;
        margin-bottom: 20px;
        background-color: white;
    }
    .elmo-image {
        border-radius: 8px;
    }
    .expand-button {
        background-color: #007bff;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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
st.title("Brutti Ceffi")
st.write("Una collezione di elmi dal Met Museum")

cols = st.columns(2)
for i, (_, row) in enumerate(df_filtrato.iterrows()):
    with cols[i % 2]:
        with st.container():
            st.markdown(f"""
                <div class="elmo-card">
                <a href="{row['Immagine']}" target="_blank">
                <img src="{row['Immagine']}" class="elmo-image" width="100%">
                </a>
                <h3><a href="{row['Immagine']}" target="_blank">{row['Nome']}</a></h3>
                <p><b>🏺 Materiale:</b> {row['Materiale']}<br>
                <b>📅 Epoca:</b> {row['Epoca']}<br>
                <b>🌍 Provenienza:</b> {row['Provenienza']}</p>
                <a href="{row['Url']}" target="_blank" class="expand-button">Mostra dettagli</a>
                </div>
            """, unsafe_allow_html=True)

# Aggiungere un pulsante per scaricare il dataset
st.sidebar.download_button(
    label="📥 Scarica il dataset",
    data=df.to_csv(index=False),
    file_name="elmi.csv",
    mime="text/csv"
)


# In[ ]:




