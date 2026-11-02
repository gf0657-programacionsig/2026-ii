import geopandas as gpd
import pandas as pd
import streamlit as st

DATOS = "https://raw.githubusercontent.com/gf0657-programacionsig/2026-ii/main/datos"


@st.cache_data
def cargar_cantones():
    cantones = gpd.read_file(f"{DATOS}/ign/cantones.gpkg").to_crs(4326)
    poblacion = pd.read_csv(f"{DATOS}/inec/cantones-2022.csv")
    return cantones.merge(poblacion[["codigo_canton", "poblacion", "area_km2", "densidad"]], on="codigo_canton", how="left")


st.title("Cantones de Costa Rica")
cantones = cargar_cantones()

# Controles en la barra lateral: cada uno retorna el valor elegido
st.sidebar.header("Filtros")
provincias = ["Todas"] + sorted(cantones["provincia"].unique())
provincia = st.sidebar.selectbox("Provincia", provincias)
poblacion_minima = st.sidebar.slider("Población mínima", 0, 100_000, 0, step=5_000)
ordenar_por = st.sidebar.radio("Ordenar por", ["poblacion", "area_km2", "densidad"],
                               format_func=lambda v: {"poblacion": "Población", "area_km2": "Área", "densidad": "Densidad"}[v])
descendente = st.sidebar.checkbox("De mayor a menor", value=True)

# El filtrado es pandas con los valores de los controles
seleccion = cantones if provincia == "Todas" else cantones[cantones["provincia"] == provincia]
seleccion = seleccion[seleccion["poblacion"].fillna(0) >= poblacion_minima]  # fillna: los cantones sin dato no se pierden
seleccion = seleccion.sort_values(ordenar_por, ascending=not descendente)

col1, col2 = st.columns(2)
col1.metric("Cantones seleccionados", len(seleccion))
col2.metric("Población", f"{seleccion['poblacion'].sum():,.0f}".replace(",", " "))

# Pestañas: cada bloque with dibuja dentro de su pestaña
pestana_tabla, pestana_resumen = st.tabs(["Tabla", "Resumen por provincia"])
with pestana_tabla:
    st.dataframe(seleccion.drop(columns="geometry")[["provincia", "canton", "poblacion", "area_km2", "densidad"]],
                 hide_index=True, width="stretch")
with pestana_resumen:
    resumen = seleccion.groupby("provincia")[["poblacion", "area_km2"]].sum().round(0)
    st.dataframe(resumen, width="stretch")

with st.expander("Acerca de los datos"):
    st.markdown("Cantones del IGN (84, simplificados a 100 m) y estimación de población 2022 del INEC (82 cantones: "
                "Monteverde y Puerto Jiménez quedan sin datos).")
