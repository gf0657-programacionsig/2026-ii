# Un control que se usa antes de leerse: el programa se ejecuta de arriba abajo
# NameError: la variable provincia se usa en la línea 6 y el control que la define está en la 8.
import streamlit as st

st.title("Cantones")
st.write(f"Provincia elegida: {provincia}")
provincia = st.selectbox("Provincia", ["Alajuela", "Cartago", "Heredia"])
