# Un GeoDataFrame en st.dataframe(): la columna de geometría no se puede convertir al formato Arrow
# No hay error: streamlit la convierte a texto, muestra un aviso en la terminal y la tabla
# arrastra una columna enorme de coordenadas. Solución: drop(columns="geometry") antes de mostrar.
import geopandas as gpd
import streamlit as st

DATOS = "https://raw.githubusercontent.com/gf0657-programacionsig/2026-ii/main/datos"
provincias = gpd.read_file(f"{DATOS}/ign/provincias.gpkg")
st.dataframe(provincias)
