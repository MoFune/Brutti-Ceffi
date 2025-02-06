#!/usr/bin/env python
# coding: utf-8

# In[25]:


import streamlit as st
import pandas as pd

# Caricare i dati dal CSV
df = pd.read_csv("elmi_fixed.csv")

# Titolo della pagina
st.title("Brutti Ceffi del Met Museum")


# Visualizzare la galleria di elmi
for _, row in df_filtrato.iterrows():
    st.image(row["Immagine"], caption=row["Nome"], use_container_width=True)
    st.write(f"**Epoca:** {row['Epoca']} | **Provenienza:** {row['Provenienza']}")
    st.write(f"**Materiale:** {row['Materiale']}")


# In[ ]:




