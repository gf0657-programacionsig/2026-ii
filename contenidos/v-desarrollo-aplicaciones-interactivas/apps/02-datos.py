import geopandas as gpd
import pandas as pd
import streamlit as st

DATOS = "https://raw.githubusercontent.com/gf0657-programacionsig/2026-ii/main/datos"


# Los datos se leen una sola vez: streamlit guarda el resultado y lo reutiliza en cada ejecución
@st.cache_data
def cargar_cantones():
    cantones = gpd.read_file(f"{DATOS}/ign/cantones.gpkg").to_crs(4326)
    poblacion = pd.read_csv(f"{DATOS}/inec/cantones-2022.csv")
    return cantones.merge(poblacion[["codigo_canton", "poblacion", "area_km2", "densidad"]], on="codigo_canton", how="left")


st.title("Cantones de Costa Rica")
st.markdown("División territorial del [IGN](https://www.snitcr.go.cr/) y estimación de población 2022 del [INEC](https://inec.cr/).")

cantones = cargar_cantones()

# Indicadores en tres columnas
col1, col2, col3 = st.columns(3)
col1.metric("Cantones", len(cantones))
col2.metric("Población 2022", f"{cantones['poblacion'].sum():,.0f}".replace(",", " "))
col3.metric("Área (km²)", f"{cantones['area_km2'].sum():,.0f}".replace(",", " "))

# Tabla interactiva: sin la columna de geometría, que no es una columna de datos
tabla = cantones.drop(columns="geometry").sort_values("poblacion", ascending=False)
st.dataframe(
    tabla,
    hide_index=True,
    width="stretch",
    column_config={
        "codigo_provincia": None,  # columna oculta
        "codigo_canton": "Código",
        "provincia": "Provincia",
        "canton": "Cantón",
        "poblacion": st.column_config.NumberColumn("Población", format="localized"),
        "area_km2": st.column_config.NumberColumn("Área (km²)", format="%.1f"),
        "densidad": st.column_config.NumberColumn("Densidad (hab/km²)", format="%.1f"),
    },
)

st.download_button("Descargar la tabla (CSV)", tabla.to_csv(index=False).encode("utf-8"), "cantones-2022.csv", "text/csv")
