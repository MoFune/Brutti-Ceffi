{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "cf99d4c3-e421-4325-b14a-cbe99ff5ae18",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "# Caricare i dati dal CSV\n",
    "df = pd.read_csv(\"elmi_fixed.csv\")\n",
    "\n",
    "# Titolo della pagina\n",
    "st.title(\"Brutti Ceffi del Met Museum\")\n",
    "\n",
    "# Filtro per epoca e provenienza\n",
    "epoche = df[\"Epoca\"].unique().tolist()\n",
    "provenienze = df[\"Provenienza\"].unique().tolist()\n",
    "\n",
    "filtro_epoca = st.multiselect(\"Filtra per epoca:\", epoche, default=epoche)\n",
    "filtro_provenienza = st.multiselect(\"Filtra per provenienza:\", provenienze, default=provenienze)\n",
    "\n",
    "# Filtrare il DataFrame\n",
    "df_filtrato = df[(df[\"Epoca\"].isin(filtro_epoca)) & (df[\"Provenienza\"].isin(filtro_provenienza))]\n",
    "df_filtrato[\"Immagine\"] = df_filtrato[\"Immagine\"].fillna(\"https://via.placeholder.com/300\")\n",
    "\n",
    "# Visualizzare la galleria di elmi\n",
    "for _, row in df_filtrato.iterrows():\n",
    "    st.image(row[\"Immagine\"], caption=row[\"Nome\"], use_column_width=True)\n",
    "    st.write(f\"**Epoca:** {row['Epoca']} | **Provenienza:** {row['Provenienza']}\")\n",
    "    st.write(f\"**Materiale:** {row['Materiale']}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": none,
   "id": "355e4d94-26e1-4043-b8b6-5ca089063ea8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
