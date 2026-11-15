---
short_title: "streamlit: aplicaciones web de ciencia de datos"
---

# Soluciones — streamlit: aplicaciones web de ciencia de datos

Soluciones de los ejercicios del cuaderno [streamlit: aplicaciones web de ciencia de datos](../v-desarrollo-aplicaciones-interactivas/22-streamlit-aplicaciones-web.ipynb). Cada aplicación se guarda en el archivo indicado dentro de la carpeta `apps/`, se ejecuta con `streamlit run apps/<archivo>.py` y pasa la celda de verificación correspondiente del cuaderno. Los nombres de los controles y de los archivos son los que piden los enunciados; el resto (textos, formatos, orden de los elementos) admite variantes.

## Ejercicio 1

La terminal imprime algo como:

```text
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

Con *Always rerun* activado, cada vez que se guarda el archivo la página se actualiza sola, sin recargarla a mano. Al detener la aplicación con Ctrl+C en la terminal, la pestaña del navegador queda como estaba, pero deja de responder: en la esquina superior derecha aparece el aviso de que se perdió la conexión ("Connection error" o un ícono gris), y cualquier control deja de tener efecto hasta que la aplicación se ejecute de nuevo.

Una buena respuesta anota la dirección local, menciona la dirección de red (la que verían otras computadoras de la misma red) y describe la desconexión.

## Ejercicio 2

`apps/ejercicio-02.py`:

```python
import streamlit as st

st.title("Calculadora de densidad")

poblacion = st.number_input("Población", min_value=0, value=5_044_197, step=1_000)
area = st.number_input("Área (km²)", min_value=0.0, value=51_147.0, step=100.0)

# Sin la condición, un área de cero produce ZeroDivisionError y la aplicación se detiene con un error
if area > 0:
    st.metric("Densidad (hab/km²)", f"{poblacion / area:,.1f}")
else:
    st.metric("Densidad (hab/km²)", "—")
    st.warning("El área debe ser mayor que cero.")
```

Con los valores iniciales, la densidad es 98,6 hab/km². Con el área en cero, sin la condición, la aplicación muestra el error `ZeroDivisionError: float division by zero` en la página (y `AppTest` lo reporta en `app.exception`); con la condición, muestra el guion y la advertencia.

## Ejercicio 3

`apps/ejercicio-03.py`:

```python
import pandas as pd
import streamlit as st

DATOS = "https://raw.githubusercontent.com/gf0657-programacionsig/2026-ii/main/datos"


@st.cache_data
def cargar_distritos():
    return pd.read_csv(f"{DATOS}/inec/distritos-2022.csv")


st.title("Distritos de Costa Rica")
distritos = cargar_distritos()

col1, col2, col3 = st.columns(3)
col1.metric("Distritos", len(distritos))
col2.metric("Población 2022", f"{distritos['poblacion'].sum():,.0f}".replace(",", " "))
col3.metric("Ocupantes por vivienda", f"{distritos['promedio_ocupantes'].mean():.2f}")

tabla = distritos.nlargest(20, "poblacion")[["provincia", "canton", "distrito", "poblacion"]]
st.dataframe(
    tabla, hide_index=True, width="stretch",
    column_config={"provincia": "Provincia", "canton": "Cantón", "distrito": "Distrito",
                   "poblacion": st.column_config.NumberColumn("Población", format="localized")},
)
st.download_button("Descargar la tabla (CSV)", tabla.to_csv(index=False).encode("utf-8"), "distritos-mas-poblados.csv", "text/csv")
```

Los indicadores muestran 487 distritos, 5 044 197 habitantes y 3,07 ocupantes por vivienda (el promedio simple de los promedios distritales; un promedio ponderado por viviendas daría otro valor, y es válido si se explica).

## Ejercicio 4

Sin el decorador, la función se ejecuta en cada interacción: con `time.time()` antes y después de la lectura, el `st.caption()` muestra unos segundos (depende de la red) cada vez que se toca un control, y la aplicación se siente lenta. Con `@st.cache_data`, la primera ejecución tarda lo mismo y las siguientes muestran milésimas de segundo, porque streamlit retorna la copia guardada sin ejecutar el cuerpo.

Una buena explicación dice que la caché guarda el resultado de la función asociado a sus argumentos, y que no debe usarse cuando el resultado cambia mientras la aplicación corre (datos en vivo de una API, una tabla que otra persona edita): en esos casos se usa el argumento `ttl` (tiempo de vida de la entrada, por ejemplo `ttl=600` para diez minutos) o no se usa caché.

## Ejercicio 5

`apps/ejercicio-05.py`, a partir de `apps/03-controles.py`:

```python
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

st.sidebar.header("Filtros")
provincias = ["Todas"] + sorted(cantones["provincia"].unique())
provincia = st.sidebar.selectbox("Provincia", provincias)
poblacion_minima = st.sidebar.slider("Población mínima", 0, 100_000, 0, step=5_000)

# Un control deslizante con dos valores retorna una tupla (mínimo, máximo)
densidad_min, densidad_max = int(cantones["densidad"].min()), int(cantones["densidad"].max()) + 1
rango = st.sidebar.slider("Rango de densidad", densidad_min, densidad_max, value=(densidad_min, densidad_max))

columnas = ["provincia", "canton", "poblacion", "area_km2", "densidad"]
elegidas = st.sidebar.multiselect("Columnas", columnas, default=columnas)

seleccion = cantones if provincia == "Todas" else cantones[cantones["provincia"] == provincia]
seleccion = seleccion[seleccion["poblacion"].fillna(0) >= poblacion_minima]
seleccion = seleccion[seleccion["densidad"].between(rango[0], rango[1]) | seleccion["densidad"].isna()]

st.metric("Cantones seleccionados", len(seleccion))
st.dataframe(seleccion.drop(columns="geometry")[elegidas], hide_index=True, width="stretch")
```

El rango inicial es (14, 9020) y la tabla tiene los 84 cantones; con el rango 100–1000 quedan 24. Dos detalles que conviene observar: `value=(mínimo, máximo)` es lo que convierte el control deslizante en un rango, y los cantones sin dato de densidad (Monteverde y Puerto Jiménez) se conservan con `isna()`; sin esa condición desaparecen en silencio, lo que es aceptable si se decide a propósito.

## Ejercicio 6

Al abrirse muestra `Variable: 0 | Estado de sesión: 0`. Tras tres clics muestra `Variable: 1 | Estado de sesión: 3`. En cada ejecución `contador` vuelve a empezar en 0; el botón retorna `True` solo en la ejecución provocada por el clic, así que `contador` llega a 1 en esa ejecución y nada más. `st.session_state["clics"]` se inicializa una sola vez, porque la condición `not in` protege la asignación, y conserva su valor entre ejecuciones.

Un error frecuente en la predicción es suponer que `contador` acumula (3) o que el estado de sesión también vuelve a cero. Otro, al experimentar, es quitar la condición `not in`: entonces el estado se reinicia en cada ejecución y los dos valores coinciden.

## Ejercicio 7

`apps/ejercicio-07.py`:

```python
import geopandas as gpd
import pandas as pd
import plotly.express as px
import streamlit as st

DATOS = "https://raw.githubusercontent.com/gf0657-programacionsig/2026-ii/main/datos"
ETIQUETAS = {"poblacion": "Población (habitantes)", "area_km2": "Área (km²)", "densidad": "Densidad (hab/km²)"}


@st.cache_data
def cargar_cantones():
    cantones = gpd.read_file(f"{DATOS}/ign/cantones.gpkg").to_crs(4326)
    poblacion = pd.read_csv(f"{DATOS}/inec/cantones-2022.csv")
    return cantones.merge(poblacion[["codigo_canton", "poblacion", "area_km2", "densidad"]], on="codigo_canton", how="left")


st.title("Cantones de Costa Rica, 2022")
cantones = cargar_cantones()

tipo = st.radio("Tipo de gráfico", ["Barras", "Histograma"], horizontal=True)
variable = st.selectbox("Variable", list(ETIQUETAS), format_func=lambda v: ETIQUETAS[v].split(" (")[0])

if tipo == "Barras":
    mayores = cantones.nlargest(15, variable)
    grafico = px.bar(mayores, x="canton", y=variable, labels={"canton": "Cantón", variable: ETIQUETAS[variable]},
                     title=f"Los 15 cantones con mayor {ETIQUETAS[variable].split(' (')[0].lower()}, 2022")
else:
    grafico = px.histogram(cantones, x=variable, nbins=20, labels={variable: ETIQUETAS[variable]},
                           title=f"Distribución de {ETIQUETAS[variable].split(' (')[0].lower()} de los 84 cantones, 2022")
    grafico.update_layout(yaxis_title="Número de cantones")

st.plotly_chart(grafico, width="stretch")
```

`horizontal=True` pone las opciones del `st.radio()` en una fila. El eje vertical del histograma se titula aparte, porque plotly lo nombra "count" por defecto.

## Ejercicio 8

`apps/ejercicio-08.py`, a partir de `apps/05-mapa-puntos.py`:

```python
import geopandas as gpd
import streamlit as st

DATOS = "https://raw.githubusercontent.com/gf0657-programacionsig/2026-ii/main/datos"


@st.cache_data
def cargar_aerodromos():
    aerodromos = gpd.read_file(f"{DATOS}/ign/aerodromos.gpkg")
    provincias = gpd.read_file(f"{DATOS}/ign/provincias.gpkg")
    # Unión espacial en CRTM05 (ambas capas): cada aeródromo recibe la provincia que lo contiene
    aerodromos = gpd.sjoin(aerodromos, provincias[["provincia", "geometry"]], predicate="within").drop(columns="index_right")
    aerodromos = aerodromos.to_crs(4326)
    aerodromos["longitud"] = aerodromos.geometry.x
    aerodromos["latitud"] = aerodromos.geometry.y
    return aerodromos.drop(columns="geometry")


st.title("Aeródromos de Costa Rica")
aerodromos = cargar_aerodromos()

provincia = st.selectbox("Provincia", ["Todas"] + sorted(aerodromos["provincia"].unique()))
seleccion = aerodromos if provincia == "Todas" else aerodromos[aerodromos["provincia"] == provincia]

st.map(seleccion, latitude="latitud", longitude="longitud", size=1500, color="#D97B1B", zoom=7)
st.caption(f"{len(seleccion)} aeródromos en {provincia.lower() if provincia != 'Todas' else 'todas las provincias'}. Fuente: IGN.")
```

Los 119 aeródromos quedan dentro de alguna provincia (ninguno se pierde en la unión); Guanacaste tiene 37. La unión espacial se hace en CRTM05, el SRC original de las dos capas, antes de reproyectar a WGS84 para el mapa.

## Ejercicio 9

`apps/ejercicio-09.py`, a partir de `apps/06-mapa-folium.py`:

```python
import copy

import folium
import geopandas as gpd
import streamlit as st
from shapely.geometry import Point
from streamlit_folium import st_folium

DATOS = "https://raw.githubusercontent.com/gf0657-programacionsig/2026-ii/main/datos"
COLORES = ["#1F77B4", "#D97B1B", "#2CA02C", "#D62728", "#9467BD", "#8C564B", "#17BECF"]


@st.cache_data
def cargar_capas():
    provincias = gpd.read_file(f"{DATOS}/ign/provincias.gpkg").to_crs(4326)
    aerodromos = gpd.read_file(f"{DATOS}/ign/aerodromos.gpkg").to_crs(4326)
    return provincias, aerodromos


@st.cache_resource
def crear_mapa():
    provincias, aerodromos = cargar_capas()
    mapa = provincias.explore(column="provincia", cmap=COLORES, categorical=True, legend=False, name="Provincias",
                              location=[9.75, -84.15], zoom_start=8, tiles="OpenStreetMap",
                              tooltip=["provincia"], style_kwds={"color": "white", "weight": 1, "fillOpacity": 0.5})
    aerodromos.explore(m=mapa, name="Aeródromos", color="black", marker_kwds={"radius": 4}, tooltip=["nombre"])
    folium.LayerControl().add_to(mapa)
    return mapa


st.set_page_config(layout="wide")
st.title("Provincias y aeródromos de Costa Rica")
provincias, aerodromos = cargar_capas()

col_mapa, col_datos = st.columns([2, 1])
with col_mapa:
    salida = st_folium(copy.deepcopy(crear_mapa()), height=500, use_container_width=True, returned_objects=["last_clicked"])

if salida and salida.get("last_clicked"):
    punto = Point(salida["last_clicked"]["lng"], salida["last_clicked"]["lat"])
    encontrada = provincias[provincias.contains(punto)]
    if not encontrada.empty:
        st.session_state["provincia"] = encontrada.iloc[0]["provincia"]

with col_datos:
    st.subheader("Provincia")
    if "provincia" in st.session_state:
        nombre = st.session_state["provincia"]
        # Unión espacial: los aeródromos dentro de la provincia elegida
        dentro = gpd.sjoin(aerodromos, provincias[provincias["provincia"] == nombre][["geometry"]], predicate="within")
        st.metric(nombre, f"{len(dentro)} aeródromos")
        st.dataframe(dentro[["nombre"]], hide_index=True, width="stretch")
    else:
        st.info("Haga clic en una provincia del mapa.")
```

El mapa con dos capas se construye encadenando `explore()` con `m=`, como en el cuaderno de geopandas I, y el control de capas se agrega con folium. El patrón `cache_resource` + `copy.deepcopy()` es el del cuaderno: sin él, cada clic devuelve el mapa a la vista inicial. Los tres clics de prueba deben mostrar provincias distintas con sus conteos (por ejemplo, Guanacaste 37, Limón y Puntarenas con muchos; Cartago con pocos).

## Ejercicio 10

No hay una respuesta única. Una buena entrega tiene un repositorio público con `app.py`, `requirements.txt` (con versiones fijadas, incluidos streamlit-folium y mapclassify si se usan `explore()` con `scheme` o `st_folium()`) y `README.md`; `app.py` empieza con `st.set_page_config()`, carga las capas de la tarea 3 desde URL en funciones con `@st.cache_data`, tiene al menos un control en la barra lateral, un indicador, la tabla sin la columna de geometría y el mapa web con `st_folium()`; y corre con `streamlit run app.py` sin errores y con `AppTest` sin excepciones. Los errores esperables son los de la clínica: rutas locales, controles duplicados, un control usado antes de leerse, el GeoDataFrame con geometría en `st.dataframe()`.

## Ejercicio 11

La dirección tiene la forma `https://<nombre>.streamlit.app`. Las causas más frecuentes de fallo, en orden: una biblioteca que falta en `requirements.txt` (`ModuleNotFoundError` en el registro), una versión que no existe o que no es compatible con la versión de Python de Community Cloud, un archivo de datos leído con una ruta local, y el archivo principal o la rama mal indicados al crear la aplicación. Una buena respuesta copia la línea del registro que nombra el error y dice qué cambió para corregirlo.

## Ejercicio 12

Respuesta abierta. Lo que suele haber que corregir en el código generado: `use_container_width=True` (sustituir por `width="stretch"`), `st.cache` o `st.experimental_memo` (sustituir por `st.cache_data`), `folium_static()` (sustituir por `st_folium()`), lectura de datos desde una ruta local o sin caché, y un `requirements.txt` sin versiones o con bibliotecas que la aplicación no usa. Una buena respuesta muestra las cuatro comprobaciones hechas: la versión indicada en el prompt coincide con `st.__version__`, los datos vienen de URL en una función con `@st.cache_data`, la aplicación corre sin errores en la terminal y con `AppTest`, y `requirements.txt` cubre todas las importaciones.
