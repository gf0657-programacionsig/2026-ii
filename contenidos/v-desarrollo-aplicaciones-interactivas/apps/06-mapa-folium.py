import copy

import geopandas as gpd
import pandas as pd
import streamlit as st
from shapely.geometry import Point
from streamlit_folium import st_folium

DATOS = "https://raw.githubusercontent.com/gf0657-programacionsig/2026-ii/main/datos"


@st.cache_data
def cargar_cantones():
    cantones = gpd.read_file(f"{DATOS}/ign/cantones.gpkg").to_crs(4326)
    poblacion = pd.read_csv(f"{DATOS}/inec/cantones-2022.csv")
    return cantones.merge(poblacion[["codigo_canton", "poblacion", "area_km2", "densidad"]], on="codigo_canton", how="left")


st.set_page_config(layout="wide")  # disposición ancha: el mapa necesita espacio
st.title("Densidad de población por cantón, 2022")
cantones = cargar_cantones()

# El mapa de coropletas, como en el cuaderno de geopandas I; es un folium.Map. Se construye una
# sola vez (cache_resource, porque un mapa de folium no se puede serializar) y cada ejecución
# trabaja con una copia idéntica: así streamlit-folium reconoce el mismo mapa en cada ejecución
# y conserva la vista (centro y acercamiento) con cada clic, en lugar de dibujarlo desde cero
@st.cache_resource
def crear_mapa():
    return cargar_cantones().explore(
        column="densidad", cmap="YlOrRd", scheme="Quantiles", k=5,
        location=[9.75, -84.15], zoom_start=8,  # centro y acercamiento fijos (sin la Isla del Coco)
        tooltip=["canton", "provincia", "densidad"], tiles="OpenStreetMap",
        style_kwds={"color": "white", "weight": 0.5}, missing_kwds={"color": "#E6E6E6"},
        legend_kwds={"caption": "Densidad de población, 2022 (hab/km²)"},
    )


mapa = copy.deepcopy(crear_mapa())

col_mapa, col_datos = st.columns([2, 1])
with col_mapa:
    # st_folium() dibuja el mapa y retorna lo que la persona hace en él
    salida = st_folium(mapa, height=500, use_container_width=True, returned_objects=["last_clicked"])

# Con el clic, se busca el cantón que contiene el punto y se recuerda en la sesión
if salida and salida.get("last_clicked"):
    punto = Point(salida["last_clicked"]["lng"], salida["last_clicked"]["lat"])
    encontrado = cantones[cantones.contains(punto)]
    if not encontrado.empty:
        st.session_state["canton"] = encontrado.iloc[0]

with col_datos:
    st.subheader("Cantón")
    if "canton" in st.session_state:
        canton = st.session_state["canton"]
        st.metric(canton["canton"], f"{canton['poblacion']:,.0f} hab.".replace(",", " ") if pd.notna(canton["poblacion"]) else "sin datos")
        st.write(f"Provincia: {canton['provincia']}")
        st.write(f"Área: {canton['area_km2']:,.1f} km²".replace(",", " ") if pd.notna(canton["area_km2"]) else "Área: sin datos")
        st.write(f"Densidad: {canton['densidad']:,.1f} hab/km²".replace(",", " ") if pd.notna(canton["densidad"]) else "Densidad: sin datos")
    else:
        st.info("Haga clic en un cantón del mapa.")
