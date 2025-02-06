#!/usr/bin/env python
# coding: utf-8

# In[25]:


import streamlit as st
import pandas as pd

# Caricare i dati dal CSV
df = pd.read_csv("elmi_fixed.csv")

# Titolo della pagina
st.title("Brutti Ceffi del Met Museum")

# Filtro per epoca e provenienza
epoche = df["Epoca"].unique().tolist()
provenienze = df["Provenienza"].unique().tolist()

filtro_epoca = st.multiselect("Filtra per epoca:", epoche, default=epoche)
filtro_provenienza = st.multiselect("Filtra per provenienza:", provenienze, default=provenienze)

# Filtrare il DataFrame
df_filtrato = df[(df["Epoca"].isin(filtro_epoca)) & (df["Provenienza"].isin(filtro_provenienza))]
df_filtrato["Immagine"] = df_filtrato["Immagine"].fillna("https://via.placeholder.com/300")

# Visualizzare la galleria di elmi
for _, row in df_filtrato.iterrows():
    st.image(row["Immagine"], caption=row["Nome"], use_column_width=True)
    st.write(f"**Epoca:** {row['Epoca']} | **Provenienza:** {row['Provenienza']}")
    st.write(f"**Materiale:** {row['Materiale']}")


# In[ ]:




