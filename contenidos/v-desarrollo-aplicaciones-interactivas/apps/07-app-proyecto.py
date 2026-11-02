# Aplicación de ejemplo del proyecto final: cantones de Costa Rica con su población.
# Ejecución: streamlit run apps/07-app-proyecto.py
import copy

import folium
import geopandas as gpd
import pandas as pd
import plotly.express as px
import streamlit as st
from shapely.geometry import Point
from streamlit_folium import st_folium

DATOS = "https://raw.githubusercontent.com/gf0657-programacionsig/2026-ii/main/datos"

# ---------- Configuración de la página (primera llamada a streamlit) ----------
st.set_page_config(page_title="Cantones de Costa Rica", page_icon="🗺️", layout="wide")


# ---------- Datos, en caché ----------
@st.cache_data
def cargar_cantones():
    cantones = gpd.read_file(f"{DATOS}/ign/cantones.gpkg").to_crs(4326)
    poblacion = pd.read_csv(f"{DATOS}/inec/cantones-2022.csv")
    return cantones.merge(poblacion[["codigo_canton", "poblacion", "area_km2", "densidad"]], on="codigo_canton", how="left")


@st.cache_data
def cargar_aerodromos():
    return gpd.read_file(f"{DATOS}/ign/aerodromos.gpkg").to_crs(4326)


def filtrar(provincia, poblacion_minima):
    cantones = cargar_cantones()
    seleccion = cantones if provincia == "Todas" else cantones[cantones["provincia"] == provincia]
    return seleccion[seleccion["poblacion"].fillna(0) >= poblacion_minima]


ETIQUETAS = {"poblacion": "Población (habitantes)", "densidad": "Densidad (hab/km²)", "area_km2": "Área (km²)"}


# El mapa depende de los filtros: un mapa en caché por cada combinación de valores (ver la sección de mapas)
@st.cache_resource
def crear_mapa(provincia, poblacion_minima, variable):
    seleccion = filtrar(provincia, poblacion_minima)
    aerodromos_seleccion = gpd.sjoin(cargar_aerodromos(), seleccion[["geometry"]], predicate="within")
    mapa = seleccion.explore(column=variable, cmap="YlOrRd", scheme="Quantiles", k=5, name="Cantones",
                             location=[9.75, -84.15], zoom_start=8,
                             tooltip=["canton", "provincia", variable], tiles="OpenStreetMap",
                             style_kwds={"color": "white", "weight": 0.5}, missing_kwds={"color": "#E6E6E6"},
                             legend_kwds={"caption": ETIQUETAS[variable] + ", 2022"})
    aerodromos_seleccion.explore(m=mapa, name="Aeródromos", color="#1F77B4", marker_kwds={"radius": 4}, tooltip=["nombre"])
    folium.LayerControl().add_to(mapa)
    return mapa


cantones = cargar_cantones()

# ---------- Controles ----------
st.sidebar.title("Filtros")
provincias = ["Todas"] + sorted(cantones["provincia"].unique())
provincia = st.sidebar.selectbox("Provincia", provincias)
poblacion_minima = st.sidebar.slider("Población mínima", 0, 100_000, 0, step=5_000)
variable = st.sidebar.selectbox("Variable del mapa y del gráfico", ["poblacion", "densidad", "area_km2"],
                                format_func=lambda v: {"poblacion": "Población", "densidad": "Densidad", "area_km2": "Área"}[v])

seleccion = filtrar(provincia, poblacion_minima)
aerodromos_seleccion = gpd.sjoin(cargar_aerodromos(), seleccion[["geometry"]], predicate="within")

# ---------- Página ----------
st.title("Cantones de Costa Rica: población y territorio, 2022")
st.markdown(f"**{provincia}** · {len(seleccion)} cantones · {aerodromos_seleccion.shape[0]} aeródromos")

col1, col2, col3 = st.columns(3)
col1.metric("Población", f"{seleccion['poblacion'].sum():,.0f}".replace(",", " "))
col2.metric("Área (km²)", f"{seleccion['area_km2'].sum():,.0f}".replace(",", " "))
col3.metric("Densidad (hab/km²)", f"{seleccion['poblacion'].sum() / seleccion['area_km2'].sum():,.0f}" if seleccion["area_km2"].sum() else "—")

pestana_tabla, pestana_grafico, pestana_mapa = st.tabs(["Tabla", "Gráfico", "Mapa"])

with pestana_tabla:
    tabla = seleccion.drop(columns="geometry").sort_values(variable, ascending=False)[["provincia", "canton", "poblacion", "area_km2", "densidad"]]
    st.dataframe(tabla, hide_index=True, width="stretch",
                 column_config={"provincia": "Provincia", "canton": "Cantón",
                                "poblacion": st.column_config.NumberColumn("Población", format="localized"),
                                "area_km2": st.column_config.NumberColumn("Área (km²)", format="%.1f"),
                                "densidad": st.column_config.NumberColumn("Densidad (hab/km²)", format="%.1f")})
    st.download_button("Descargar (CSV)", tabla.to_csv(index=False).encode("utf-8"), "cantones.csv", "text/csv")

with pestana_grafico:
    grafico = px.bar(tabla.head(15), x="canton", y=variable, labels={"canton": "Cantón", variable: ETIQUETAS[variable]},
                     title=f"{ETIQUETAS[variable]} de los cantones, 2022 ({provincia.lower() if provincia != 'Todas' else 'todas las provincias'})")
    st.plotly_chart(grafico, width="stretch")

with pestana_mapa:
    col_mapa, col_detalle = st.columns([3, 1])
    with col_mapa:
        mapa = copy.deepcopy(crear_mapa(provincia, poblacion_minima, variable))
        salida = st_folium(mapa, height=550, use_container_width=True, returned_objects=["last_clicked"])
    if salida and salida.get("last_clicked"):
        punto = Point(salida["last_clicked"]["lng"], salida["last_clicked"]["lat"])
        encontrado = cantones[cantones.contains(punto)]
        if not encontrado.empty:
            st.session_state["canton"] = encontrado.iloc[0]
    with col_detalle:
        st.subheader("Cantón")
        if "canton" in st.session_state:
            canton = st.session_state["canton"]
            st.write(f"**{canton['canton']}** ({canton['provincia']})")
            for columna in ["poblacion", "area_km2", "densidad"]:
                valor = canton[columna]
                formato = ",.0f" if columna == "poblacion" else ",.1f"
                st.write(f"{ETIQUETAS[columna]}: " + (f"{valor:{formato}}".replace(",", " ") if pd.notna(valor) else "sin datos"))
        else:
            st.info("Haga clic en un cantón.")

st.caption("Fuentes: Instituto Geográfico Nacional (SNIT) e Instituto Nacional de Estadística y Censos (2023). "
           "Datos preparados en el [repositorio del curso](https://github.com/gf0657-programacionsig/2026-ii/tree/main/datos).")
