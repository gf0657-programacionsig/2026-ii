# StreamlitDuplicateElementId: dos controles del mismo tipo con los mismos argumentos
# streamlit identifica cada control por su tipo y su etiqueta; dos iguales son ambiguos.
# Solución: etiquetas distintas o un argumento key único por control.
import streamlit as st

minimo = st.slider("Valor", 0, 100)
maximo = st.slider("Valor", 0, 100)
