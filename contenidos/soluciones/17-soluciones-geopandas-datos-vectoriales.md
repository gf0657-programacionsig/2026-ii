---
short_title: "geopandas I: datos vectoriales"
---

# Soluciones — geopandas I: datos vectoriales

Soluciones y pautas de respuesta de los ejercicios del cuaderno de notas [geopandas I: datos vectoriales](../iv-procesamiento-datos-geoespaciales/17-geopandas-datos-vectoriales.ipynb). Los ejercicios 1 a 9 tienen en el propio cuaderno una celda de verificación con `assert`, que examina el objeto creado; para los demás se describen los elementos de una buena respuesta y los errores esperables. Todas las soluciones suponen ejecutadas las celdas del cuaderno (`paises`, `paises_ee` con los códigos corregidos, `centroamerica`, `centroamerica_crtm05`, `ciudades`, `indicadores`, `paises_bm`, `america_sur_bm`, `AZUL`, `NARANJA`) y las importaciones de la primera celda, incluida `TwoSlopeNorm`.

## Ejercicio 1 (aeropuertos y países por continente)

```python
aeropuertos = gpd.read_file(DATOS_NE + "/aeropuertos.gpkg")
print(aeropuertos.crs, aeropuertos.shape, aeropuertos.geom_type.unique().tolist())

paises_por_continente = paises["continente"].value_counts()
paises_por_continente
```

- Verificación: GeoDataFrame de 893 filas; los continentes suman 177 y
  África es el que más países tiene (51).
- Salida esperada: EPSG:4326, (893, 4), `['Point']`.
- Errores esperables: contar con `groupby().size()` sin problema (vale
  igual); leer el archivo con `pd.read_csv()` (no es un CSV).

## Ejercicio 2 (África con sus ciudades)

```python
africa = paises_ee[paises_ee["continente"] == "África"]
ciudades_africa = ciudades[ciudades["codigo_pais"].isin(africa["codigo"])].to_crs(8857)

fig, ax_2 = plt.subplots(figsize=(8, 8))

africa.plot(ax=ax_2, color="#DCE9F5", edgecolor="white", linewidth=0.8)
ciudades_africa.plot(ax=ax_2, color=NARANJA, markersize=10)

ax_2.set_title("Países y ciudades principales de África")
ax_2.set_axis_off()

plt.show()
```

- Verificación: GeoDataFrame de 51 filas en EPSG:8857, título, ejes
  ocultos y al menos dos capas dibujadas.
- África tiene 51 países en la capa.
- Errores esperables: filtrar `paises` (WGS84) en lugar de `paises_ee` (la
  verificación del SRC falla); dibujar `ciudades` sin reproyectar (los
  puntos se amontonan en el origen, como en la clínica); olvidar
  `set_axis_off()`.

## Ejercicio 3 (San José en tres SRC)

```python
ciudades_merc = ciudades.to_crs(3857)
ciudades_ee = ciudades.to_crs(8857)

san_jose = ciudades["nombre"] == "San José"
for nombre, capa in [("WGS84", ciudades), ("Web Mercator", ciudades_merc), ("Equal Earth", ciudades_ee)]:
    print(nombre, capa[san_jose].geometry.x.iloc[0], capa[san_jose].geometry.y.iloc[0])
```

- Verificación: códigos EPSG 3857 y 8857, mismo número de filas (243).
- Salida esperada: WGS84 (−84,085, 9,935); Web Mercator (−9 360 000,
  1 112 000 aproximadamente); Equal Earth (−8 000 000, 1 200 000
  aproximadamente). Los tres pares describen el mismo lugar porque cada
  SRC mide desde un origen distinto y en unidades distintas (grados o
  metros); la reproyección solo cambia la representación numérica, no la
  ubicación.
- Errores esperables: usar `set_crs()` en vez de `to_crs()` (cambia la
  etiqueta sin transformar las coordenadas: las capas dejan de coincidir);
  filtrar por "San Jose" sin tilde (la capa usa el nombre con tilde).

## Ejercicio 4 (áreas de Centroamérica en CRTM05)

```python
centroamerica_bm = centroamerica_crtm05.rename(columns={"area_km2": "area_calculada_km2"}).merge(
    indicadores, on="codigo", how="left"
)
centroamerica_bm["diferencia_pct"] = (
    (centroamerica_bm["area_calculada_km2"] - centroamerica_bm["area_km2"]) / centroamerica_bm["area_km2"] * 100
).round(1)

# Efecto de la proyección: la misma geometría medida en Equal Earth
centroamerica_bm["area_equal_earth_km2"] = (centroamerica.to_crs(8857).area / 1_000_000).round(0).values
centroamerica_bm["efecto_proyeccion_pct"] = (
    (centroamerica_bm["area_calculada_km2"] - centroamerica_bm["area_equal_earth_km2"]) / centroamerica_bm["area_equal_earth_km2"] * 100
).round(2)

centroamerica_bm[["nombre", "area_calculada_km2", "area_km2", "diferencia_pct", "area_equal_earth_km2", "efecto_proyeccion_pct"]].sort_values("diferencia_pct", key=abs, ascending=False)
```

- Verificación: GeoDataFrame de 7 filas con `poblacion` y
  `diferencia_pct`; la mayor diferencia absoluta es la de Nicaragua.
- Nicaragua difiere un 7 % (128 700 km² calculados contra 120 340 del
  Banco Mundial) porque el Banco Mundial reporta superficie terrestre y
  la geometría incluye los lagos Cocibolca y Xolotlán, unos 9 000 km².
  Costa Rica difiere un 0,2 % de los 51 060 km² oficiales. El efecto de
  la proyección es otro: comparada con Equal Earth, CRTM05 infla el área
  un 0,0 % en Costa Rica (su zona de diseño), un 0,5 % en Panamá y un
  1,2 % en Guatemala, el país más lejano del meridiano −84°; la
  deformación de una transversal de Mercator crece con la distancia al
  meridiano central.
- Errores esperables: `indicadores.merge(centroamerica_crtm05)` (retorna
  un DataFrame); dejar las dos columnas `area_km2_x` y `area_km2_y` sin
  saber cuál es cuál (la de la capa es la calculada); atribuir la
  diferencia de Nicaragua a la proyección.

## Ejercicio 5 (esperanza de vida en América del Sur con etiquetas)

```python
fig, ax_5 = plt.subplots(figsize=(8, 9))

america_sur_bm.plot(
    ax=ax_5, column="esperanza_vida", cmap="viridis", edgecolor="white", linewidth=0.8,
    legend=True, legend_kwds={"label": "Años", "shrink": 0.6},
    missing_kwds={"color": "#E6E6E6", "label": "Sin datos"}
)

for punto, nombre in zip(america_sur_bm.representative_point(), america_sur_bm["nombre"]):
    ax_5.annotate(nombre, (punto.x, punto.y), ha="center", fontsize=8)

ax_5.set_title("Esperanza de vida al nacer en América del Sur, 2024")
ax_5.set_axis_off()

plt.show()
```

- Verificación: título, un texto por país (13, incluidas las Islas
  Malvinas, sin datos) y una barra de color.
- Errores esperables: usar `centroid` (para países con islas puede caer
  fuera del polígono; `representative_point()` garantiza un punto dentro);
  `ax.text()` con la geometría en lugar de `.x` y `.y`; omitir
  `missing_kwds` (las Malvinas desaparecen del mapa, pero la verificación
  del número de textos pasa igual).

## Ejercicio 6 (crecimiento de la población con paleta divergente)

```python
fig, ax_6 = plt.subplots(figsize=(12, 6))

paises_bm.plot(
    ax=ax_6, column="crecimiento_poblacion", cmap="RdBu", edgecolor="white", linewidth=0.3,
    norm=TwoSlopeNorm(vcenter=0, vmin=-4, vmax=4),
    legend=True, legend_kwds={"label": "Crecimiento anual de la población (%)", "shrink": 0.6},
    missing_kwds={"color": "#E6E6E6", "label": "Sin datos"}
)

ax_6.set_title("Crecimiento de la población, 2024")
ax_6.set_axis_off()

plt.show()
```

- Verificación: título, polígonos y barra de color con etiqueta.
- Interpretación: la población decrece (rojo) en Europa oriental y los
  Balcanes (Kosovo −5,4 %; Moldova, Albania, Letonia, Serbia, Bosnia y
  Herzegovina), en Japón, China y Cuba y en varias islas pequeñas del
  Pacífico y el Caribe; crece más rápido (azul) en África subsahariana
  (Chad, Sudán del Sur, Níger, con tasas de 3 % o más) y en la península
  arábiga (Catar 7,3 %, Emiratos Árabes Unidos, Arabia Saudita, Omán).
  26 países tienen crecimiento negativo.
- Errores esperables: paleta secuencial sin centro; omitir `norm` (el
  blanco queda en el promedio del rango, no en cero); `vmin`/`vmax`
  asimétricos respecto a cero.

## Ejercicio 7 (mapa interactivo clasificado)

```python
mapa_7 = paises_bm.explore(
    column="usuarios_internet_pct",
    scheme="Quantiles", k=5,
    cmap="YlGnBu",
    tooltip=["nombre", "continente", "usuarios_internet_pct"],
    tiles="OpenStreetMap",
    style_kwds={"color": "white", "weight": 0.5},
    missing_kwds={"color": "#E6E6E6"},
    legend_kwds={"caption": "Personas que usan Internet, 2024 (% de la población)"},
    location=[20, 0], zoom_start=2
)

mapa_7
```

- Verificación: objeto `folium.Map`.
- Comparación esperada: la clasificación por cuantiles separa los países
  en cinco grupos del mismo tamaño y hace visibles las diferencias entre
  países de valores cercanos, que en la escala continua se ven casi del
  mismo color; a cambio, oculta las diferencias dentro de cada clase y los
  extremos ya no destacan. Con 23 países sin datos, la clasificación se
  calcula solo con los que sí tienen.
- Errores esperables: en Colab, no instalar mapclassify (`!pip install
  mapclassify`); omitir `missing_kwds` (los países sin datos no se
  dibujan).

## Ejercicio 8 (lugares propios)

```python
lugares = pd.DataFrame({
    "nombre": ["Escuela de Geografía, UCR", "Aeropuerto Juan Santamaría", "Parque Nacional Volcán Poás"],
    "longitud": [-84.0512, -84.2088, -84.2330],
    "latitud": [9.9377, 9.9981, 10.1976]
})

lugares = gpd.GeoDataFrame(lugares, geometry=gpd.points_from_xy(lugares["longitud"], lugares["latitud"]), crs=4326)

mapa = centroamerica.explore(tiles="OpenStreetMap", color="#DCE9F5", style_kwds={"color": "white", "weight": 0.5}, location=[10, -84.2], zoom_start=8)
lugares.explore(m=mapa, color=NARANJA, marker_kwds={"radius": 6}, tooltip="nombre")
mapa

lugares_crtm05 = lugares.to_crs(8908)
lugares_crtm05.geometry.x, lugares_crtm05.geometry.y  # metros: cientos de miles en x, alrededor de un millón en y
```

- Verificación: GeoDataFrame con 3 filas o más, EPSG:4326, longitudes
  negativas y latitudes positivas.
- Los lugares y las coordenadas del ejemplo son ilustrativos; cada
  estudiante usa los suyos. Las coordenadas de Google Maps se copian con
  clic derecho sobre el punto ("latitud, longitud": hay que invertirlas).
  En CRTM05 las coordenadas quedan en metros: unos 490 000 en *x* y
  1 100 000 en *y* para San José.
- Errores esperables: `points_from_xy(latitud, longitud)` (los puntos caen
  en el océano Índico; la verificación lo detecta por el signo); omitir
  `crs=4326` (el mapa interactivo falla o los puntos no se ubican);
  coordenadas con coma decimal.

## Ejercicio 9 (guardar y releer)

```python
africa_bm = africa.merge(indicadores, on="codigo", how="left")
africa_bm.to_file("africa.gpkg", driver="GPKG")

africa_leido = gpd.read_file("africa.gpkg")
print(africa_leido.shape, africa_leido.crs == africa.crs)
```

- Verificación: 51 filas, el mismo SRC, la columna `poblacion` y el
  archivo en disco.
- Errores esperables: guardar sin unir (falla la verificación de
  `poblacion`); unir con `paises` sin los códigos corregidos (Sudán del
  Sur y Somalilandia quedan sin datos; la verificación pasa, pero el mapa
  tendría un país menos con datos); escribir GeoJSON sin reproyectar a
  WGS84.

## Ejercicio 10 (predicción: columna de texto)

- Predicción esperada: un color distinto por continente (8 colores de la
  paleta categórica por defecto de matplotlib, `tab10`) y la leyenda como
  lista de los ocho continentes (no una barra de color), incluidos
  "Antártida" y "Siete mares (océano abierto)" (las Tierras Australes
  Francesas). La explicación está en el bloque desplegable del cuaderno.
- Errores esperables: predecir una barra de color o un error por ser una
  columna de texto.

## Ejercicio 11 (IA: coropletas del crecimiento de la población)

- Elementos de una buena respuesta: el prompt con la estructura de rol,
  contexto (incluido el SRC), tarea y formato; el código con `plot(ax=ax,
  column="crecimiento_poblacion", cmap=<divergente>,
  norm=TwoSlopeNorm(vcenter=0, ...), legend=True, legend_kwds={"label":
  ...}, missing_kwds={...})` y `set_axis_off()`; las comprobaciones: no hay
  `to_crs()` innecesarios ni mezcla de SRC, el centro de la paleta está en
  cero (y no en el promedio del rango), los países sin datos están en
  gris, la etiqueta de la barra dice "%" o "por ciento anual", y tres
  países (por ejemplo, Ucrania rojo intenso, Níger azul intenso, Costa
  Rica cerca del blanco con 0,43 %) coinciden con sus valores en
  `paises_bm`.
- Errores esperables del asistente: `vmin`/`vmax` del rango de datos sin
  `TwoSlopeNorm` (el blanco no queda en cero); `cmap="coolwarm"` o
  `"RdBu_r"` con el sentido invertido sin aclararlo en la leyenda; omitir
  `missing_kwds`; usar `fig.colorbar()` manual en lugar de `legend=True`.

## Ejercicio 12 (fuente de datos para la tarea 3)

- Elementos de una buena respuesta: una fuente concreta y pertinente al
  tema de las tareas 1 y 2 (una capa WFS del SNIT, un CSV con
  coordenadas de GBIF, estaciones, sismos del USGS, etc.), cargada con
  `gpd.read_file()` o construida con `points_from_xy()` con el SRC
  correcto; la impresión de `crs`, `shape` y `geom_type`; el mapa sobre
  `centroamerica` o `paises` con ambas capas en el mismo SRC (reproyectar
  la nueva o la de fondo); y dos o tres preguntas que combinen la capa
  con otras (¿cuántos registros por país o cantón?, ¿cuáles no tienen
  ninguno?, ¿qué hay a cierta distancia?), que son las operaciones de la
  parte II.
- Errores esperables: dibujar las dos capas en SRC distintos (nada se
  superpone, como en la clínica); CSV con las columnas de coordenadas
  invertidas; capa sin SRC declarado.
