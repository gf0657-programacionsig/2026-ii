import streamlit as st

st.title("Mi primera aplicación")
st.write("Esta página la produce un programa de Python de unas pocas líneas.")

nombre = st.text_input("Escriba su nombre", "estudiante")
st.write(f"Hola, {nombre}. Cada vez que cambia el texto, el programa completo se ejecuta de nuevo.")
