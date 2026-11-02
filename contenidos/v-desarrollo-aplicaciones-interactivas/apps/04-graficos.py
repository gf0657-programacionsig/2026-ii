import geopandas as gpd
import pandas as pd
import plotly.express as px
import streamlit as st

DATOS = "https://raw.githubusercontent.com/gf0657-programacionsig/2026-ii/main/datos"


@st.cache_data
def cargar_cantones():
    cantones = gpd.read_file(f"{DATOS}/ign/cantones.gpkg").to_crs(4326)
    poblacion = pd.read_csv(f"{DATOS}/inec/cantones-2022.csv")
    return cantones.merge(poblacion[["codigo_canton", "poblacion", "area_km2", "densidad"]], on="codigo_canton", how="left")


st.title("Población de los cantones, 2022")
cantones = cargar_cantones()

cuantos = st.slider("Número de cantones", 5, 30, 10)
mayores = cantones.nlargest(cuantos, "poblacion")

# El gráfico se construye como en el cuaderno de plotly; st.plotly_chart() lo dibuja en la página
grafico = px.bar(
    mayores, x="canton", y="poblacion", color="provincia",
    labels={"canton": "Cantón", "poblacion": "Población (habitantes)", "provincia": "Provincia"},
    title=f"Los {cuantos} cantones más poblados de Costa Rica, 2022",
)
st.plotly_chart(grafico, width="stretch")

# Un segundo gráfico, de dispersión, con escala logarítmica y etiquetas al pasar el cursor
dispersion = px.scatter(
    cantones, x="area_km2", y="poblacion", hover_name="canton", color="provincia", log_x=True, log_y=True,
    labels={"area_km2": "Área (km²)", "poblacion": "Población (habitantes)", "provincia": "Provincia"},
    title="Área y población de los cantones, 2022",
)
st.plotly_chart(dispersion, width="stretch")
