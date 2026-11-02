import geopandas as gpd
import streamlit as st

DATOS = "https://raw.githubusercontent.com/gf0657-programacionsig/2026-ii/main/datos"


@st.cache_data
def cargar_aerodromos():
    aerodromos = gpd.read_file(f"{DATOS}/ign/aerodromos.gpkg").to_crs(4326)
    aerodromos["longitud"] = aerodromos.geometry.x
    aerodromos["latitud"] = aerodromos.geometry.y
    return aerodromos.drop(columns="geometry")  # un DataFrame común, con las coordenadas como columnas


st.title("Aeródromos de Costa Rica")
aerodromos = cargar_aerodromos()

st.map(aerodromos, latitude="latitud", longitude="longitud", size=1500, color="#D97B1B", zoom=7)
st.caption(f"{len(aerodromos)} aeródromos. Fuente: IGN.")
