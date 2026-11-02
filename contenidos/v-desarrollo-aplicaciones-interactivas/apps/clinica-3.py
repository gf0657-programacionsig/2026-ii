# FileNotFoundError: una ruta de la computadora propia que no existe en el servidor
# La aplicación corre localmente si el archivo está ahí, pero en Community Cloud solo existe
# lo que está en el repositorio. Solución: una URL, o una ruta relativa a app.py de un archivo
# que sí esté en el repositorio.
import pandas as pd
import streamlit as st

cantones = pd.read_csv("C:/Users/estudiante/Descargas/cantones-2022.csv")
st.dataframe(cantones)
