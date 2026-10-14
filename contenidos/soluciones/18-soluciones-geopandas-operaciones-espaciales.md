---
short_title: "geopandas II: operaciones espaciales"
---

# Soluciones — geopandas II: operaciones espaciales

Soluciones y pautas de respuesta de los ejercicios del cuaderno de notas [geopandas II: operaciones espaciales](../iv-procesamiento-datos-geoespaciales/18-geopandas-operaciones-espaciales.ipynb). Los ejercicios 1 a 10 tienen en el propio cuaderno una celda de verificación con `assert`, que examina el objeto creado; para los demás se describen los elementos de una buena respuesta y los errores esperables. Todas las soluciones suponen ejecutadas las celdas del cuaderno (`paises`, `paises_ee` reparada, `paises_bm`, `centroamerica`, `rios`, `rios_ee`, `lagos`, `aeropuertos`, `ciudades`, `ciudades_ee`, `aeropuertos_pais`, `capitales`, `lagos_pais`, `AZUL`, `NARANJA`) y las importaciones, incluida `Geod`.

## Ejercicio 1 (vecinos de Brasil)

```python
brasil = paises[paises["nombre"] == "Brasil"].geometry.iloc[0]
vecinos_brasil = paises[paises.touches(brasil)]

vecinos_brasil[["nombre", "continente"]].sort_values("nombre")
```

- Verificación: GeoDataFrame de 10 filas que incluye a Francia.
- Brasil toca a los diez países de la capa: Argentina, Bolivia, Colombia,
  Guyana, Paraguay, Perú, Surinam, Uruguay, Venezuela y **Francia**, cuyo
  polígono incluye la Guayana Francesa (Natural Earth la representa como
  parte del multipolígono de Francia, continente Europa). Es un ejemplo de
  que el predicado opera sobre las geometrías tal como están en la capa, no
  sobre la idea que uno tiene de ellas.
- Errores esperables: usar `intersects` (incluye a Brasil mismo: 11 filas);
  usar `paises_ee` con `brasil` tomado de `paises` (SRC distintos: ningún
  vecino, sin mensaje de error).

## Ejercicio 2 (países que atraviesa el Danubio)

```python
danubio_linea = rios_ee[rios_ee["nombre"] == "Donau"].geometry.iloc[0]
paises_danubio = paises_ee[paises_ee.intersects(danubio_linea)]

print(len(paises_danubio), sorted(paises_danubio["nombre"]))
print("crosses da lo mismo:", paises_ee.crosses(danubio_linea).sum() == len(paises_danubio))

fig, ax_2 = plt.subplots(figsize=(9, 6))

paises_danubio.plot(ax=ax_2, color="#DCE9F5", edgecolor="white", linewidth=0.8)
rios_ee[rios_ee["nombre"] == "Donau"].plot(ax=ax_2, color=AZUL, linewidth=2)

for punto, nombre in zip(paises_danubio.representative_point(), paises_danubio["nombre"]):
    ax_2.annotate(nombre, (punto.x, punto.y), ha="center", fontsize=8)

ax_2.set_title("Países que atraviesa el Danubio")
ax_2.set_axis_off()

plt.show()
```

- Verificación: 9 países, título, ejes ocultos y al menos dos capas.
- Alemania, Austria, Eslovaquia, Hungría, Croacia, Serbia, Rumania, Bulgaria
  y Ucrania (en la capa a 1:110 M el río no toca Moldavia). `intersects` y
  `crosses` dan lo mismo aquí porque la línea entra y sale de cada
  polígono; darían resultados distintos si el río terminara exactamente en
  una frontera o corriera a lo largo de ella (tocaría sin cruzar), o si
  estuviera completamente dentro de un país (`within`, no `crosses`).
- Errores esperables: tomar la geometría de `rios` (WGS84) y filtrar
  `paises_ee` (Equal Earth): cero países sin aviso; olvidar `.iloc[0]` (un
  GeoDataFrame en lugar de una geometría: el predicado se alinea por
  índice y da todo falso).

## Ejercicio 3 (aeropuertos por continente)

```python
aeropuertos_continente = aeropuertos_pais["continente"].value_counts()

print(aeropuertos_continente)
print("Sin continente:", aeropuertos_pais["continente"].isna().sum())
```

- Verificación: Series con América del Norte primero y suma 789.
- América del Norte 239, Asia 214, Europa 153, África 85, América del Sur
  69, Oceanía 29. Los 104 aeropuertos sin continente son los que no caen en
  ningún polígono a 1:110 M (islas y costas), como se vio en la sección.
- Errores esperables: rehacer la unión con `how="inner"` y afirmar que no
  hay aeropuertos sin continente; agrupar por `nombre_right` (país) en vez
  de continente.

## Ejercicio 4 (ciudades y población por país)

```python
union = gpd.sjoin(ciudades_ee, paises_ee[["codigo", "geometry"]], predicate="within")
resumen = union.groupby("codigo").agg(ciudades=("nombre", "count"), poblacion_ciudades=("poblacion", "sum"))

paises_ciudades = paises_ee.merge(resumen, on="codigo", how="left")
paises_ciudades[["ciudades", "poblacion_ciudades"]] = paises_ciudades[["ciudades", "poblacion_ciudades"]].fillna(0).astype(int)

print("Países sin ciudades principales:", (paises_ciudades["ciudades"] == 0).sum())
paises_ciudades.sort_values("ciudades", ascending=False)[["nombre", "ciudades", "poblacion_ciudades"]].head(10)
```

- Verificación: GeoDataFrame de 177 filas, 210 ciudades en total y 16
  países con cero.
- Estados Unidos tiene 9 ciudades principales en la capa, China 5, y
  Francia y Sudáfrica 4 (Francia por sus territorios de ultramar;
  Sudáfrica por sus tres capitales y Johannesburgo); 16 países no tienen
  ninguna (Groenlandia, Uruguay, Omán, Puerto Rico y otros cuyas capitales
  caen fuera del polígono o no están en la capa de 243 ciudades).
- Errores esperables: unir con `ciudades` (WGS84) y `paises_ee`: cero
  filas con aviso; unir con `paises_ee` completo, con lo que `nombre`
  recibe sufijos y `groupby("nombre")` falla; olvidar `fillna(0)` (los
  países sin ciudades quedan en NaN y la suma de ceros falla).

## Ejercicio 5 (ciudad principal más cercana a cada aeropuerto de África)

```python
aeropuertos_africa = aeropuertos_pais[aeropuertos_pais["continente"] == "África"].drop(columns=["index_right"]).to_crs(8857)

aeropuertos_ciudad = gpd.sjoin_nearest(
    aeropuertos_africa,
    ciudades_ee[["nombre", "pais", "geometry"]],
    how="left",
    distance_col="distancia_m"
)
aeropuertos_ciudad["distancia_km"] = (aeropuertos_ciudad["distancia_m"] / 1000).round(0)

aeropuertos_ciudad.sort_values("distancia_km", ascending=False)[["nombre_left", "nombre_right", "nombre", "pais", "distancia_km"]].head()
```

- Verificación: GeoDataFrame de 85 filas en EPSG:8857 con `distancia_km` y
  un máximo mayor de 500 km.
- Los más alejados son Asuán (767 km de El Cairo), Kananga (712 km de
  Kinsasa), Mbuji-Mayi (660 km de Buyumbura), Bengasi (641 km de Trípoli)
  y Lúxor (559 km de El Cairo): aeropuertos del interior, a cientos de
  kilómetros de cualquiera de las 60 ciudades principales de África en la
  capa. Como `aeropuertos_africa` ya traía
  `nombre_left` y `nombre_right` de la unión anterior, la columna de la
  ciudad queda como `nombre` sin sufijo.
- Errores esperables: no eliminar `index_right` (`ValueError: 'index_right'
  cannot be a column name in the frames being joined`); medir en WGS84
  (distancias en grados, con aviso); poner las ciudades a la izquierda (el
  resultado tendría 243 filas, una por ciudad).

## Ejercicio 6 (distancia de cada capital al centroide de su país)

```python
centroamerica_crtm05 = centroamerica.to_crs(8908)
centroamerica_crtm05["centroide"] = centroamerica_crtm05.centroid

capitales_centroide = capitales.to_crs(8908).merge(centroamerica_crtm05[["codigo", "centroide"]], left_on="codigo_pais", right_on="codigo")
capitales_centroide["distancia_km"] = (capitales_centroide.geometry.distance(capitales_centroide["centroide"]) / 1000).round(0)

capitales_centroide[["pais", "distancia_km"]].sort_values("distancia_km", ascending=False)
```

- Verificación: 7 filas en EPSG:8908 con distancias entre 5 y 300 km.
- Managua es la capital más lejana de su centro geométrico (154 km: el
  centroide de Nicaragua cae en el interior y la capital está en el
  Pacífico), seguida de Ciudad de Guatemala (120 km) y Tegucigalpa
  (102 km); San José (12 km) y Belmopán (9 km) están casi en el centro de
  sus países. La celda alinea las dos
  GeoSeries por índice tras el `merge()`, que reinicia el índice en ambas.
- Errores esperables: `distance()` entre GeoSeries con índices distintos
  (resultado lleno de NaN: hay que alinear con `merge()` o usar
  `align=False`); medir en WGS84; calcular el centroide en WGS84 y luego
  reproyectar el punto (el centroide depende del SRC).

## Ejercicio 7 (aeropuertos a menos de 300 km de San José)

```python
san_jose_crtm05 = ciudades.to_crs(8908)[ciudades["nombre"] == "San José"].geometry.iloc[0]
zona_300 = san_jose_crtm05.buffer(300_000)

aeropuertos_crtm05 = aeropuertos.to_crs(8908)
aeropuertos_cerca = aeropuertos_crtm05[aeropuertos_crtm05.within(zona_300)]

print(aeropuertos_cerca[["nombre", "iata"]])

fig, ax_7 = plt.subplots(figsize=(8, 6))

centroamerica.to_crs(8908).plot(ax=ax_7, color="#DCE9F5", edgecolor="white", linewidth=0.8)
gpd.GeoSeries([zona_300], crs=8908).plot(ax=ax_7, color=AZUL, alpha=0.2)
aeropuertos_cerca.plot(ax=ax_7, color=NARANJA, markersize=40)

for punto, nombre in zip(aeropuertos_cerca.geometry, aeropuertos_cerca["nombre"]):
    ax_7.annotate(nombre, (punto.x, punto.y), xytext=(5, 5), textcoords="offset points", fontsize=8)

ax_7.set_title("Aeropuertos de la capa a menos de 300 km de San José")
ax_7.set_axis_off()

plt.show()
```

- Verificación: 2 aeropuertos en EPSG:8908, título y ejes ocultos.
- El Tobías Bolaños (San José) y el Enrique Malek (David, Panamá); el
  Augusto C. Sandino de Managua queda a unos 340 km. Una unión espacial
  (`gpd.sjoin(aeropuertos_crtm05, gpd.GeoDataFrame(geometry=[zona_300],
  crs=8908), predicate="within")`) da lo mismo.
- Errores esperables: `buffer(300)` (300 metros); construir la zona en
  WGS84 (`buffer(300_000)` en grados abarca el planeta entero); comparar
  la zona en CRTM05 con los aeropuertos en WGS84 (cero resultados).

## Ejercicio 8 (grupos de ingreso)

```python
grupos_ingreso = paises_bm.dissolve(by="grupo_ingreso", aggfunc={"poblacion": "sum", "nombre": "count"}).rename(columns={"nombre": "paises"})

print(grupos_ingreso[["paises", "poblacion"]])

fig, ax_8 = plt.subplots(figsize=(12, 6))

grupos_ingreso.reset_index().plot(ax=ax_8, column="grupo_ingreso", cmap="Set2", edgecolor="white", linewidth=0.5,
                                  legend=True, legend_kwds={"loc": "lower left", "title": "Grupo de ingreso"})

ax_8.set_title("Países por grupo de ingreso (Natural Earth)")
ax_8.set_axis_off()

plt.show()
```

- Verificación: 5 grupos, el más poblado es "4. Ingreso mediano bajo" y el
  mapa tiene leyenda.
- El grupo de ingreso mediano bajo es el más poblado (India, Nigeria,
  Pakistán, Bangladés...) y el de ingreso mediano bajo también es el que
  más países tiene (47), seguido del mediano alto (44, con China) y del
  bajo (37). `reset_index()` convierte el índice en columna para
  colorearla como categórica.
- Errores esperables: `groupby()` en lugar de `dissolve()` (se pierde la
  geometría); `column="grupo_ingreso"` sin `reset_index()` (`KeyError`:
  es el índice); usar `poblacion_estimada` de Natural Earth (2019) en
  vez de la de 2024 (resultado parecido, pero no es lo pedido).

## Ejercicio 9 (lagos compartidos)

```python
partes = lagos_pais.groupby("nombre_1")["nombre_2"].transform("count")
lagos_compartidos = lagos_pais[partes > 1].copy()
lagos_compartidos["porcentaje"] = (lagos_compartidos["area_km2"] / lagos_compartidos.groupby("nombre_1")["area_km2"].transform("sum") * 100).round(1)

print(lagos_compartidos["nombre_1"].nunique(), "lagos compartidos")
lagos_compartidos[["nombre_1", "nombre_2", "area_km2", "porcentaje"]].sort_values(["nombre_1", "porcentaje"], ascending=[True, False])
```

- Verificación: 8 lagos distintos y porcentajes que suman 100 por lago.
- Ocho lagos compartidos: Erie, Huron, Ontario y Superior (Canadá y
  Estados Unidos), Malawi (Tanzania, Malaui y Mozambique), Tanganica
  (Tanzania, República Democrática del Congo, Zambia y Burundi: el que más
  países reparte), Titicaca (Perú 65 %, Bolivia 35 %) y Victoria (Tanzania
  54 %, Uganda 42 %, Kenia 4 %).
- Errores esperables: calcular el porcentaje sobre el área del lago
  original (`lagos_ee.area`) sin alinear por nombre; filtrar con
  `value_counts()` sin `transform()` (hay que volver a unir); olvidar
  `.copy()` (`SettingWithCopyWarning`).

## Ejercicio 10 (ríos de Asia)

```python
asia_ee = paises_ee[paises_ee["continente"] == "Asia"]
rios_asia = gpd.clip(rios_ee, asia_ee)
rios_asia["longitud_km"] = (rios_asia.length / 1000).round(0)

print(rios_asia[["nombre", "longitud_km"]].sort_values("longitud_km", ascending=False))

fig, ax_10 = plt.subplots(figsize=(10, 6))

asia_ee.plot(ax=ax_10, color="#DCE9F5", edgecolor="white", linewidth=0.5)
rios_asia.plot(ax=ax_10, color=AZUL, linewidth=1.5)

for linea, nombre in zip(rios_asia.representative_point(), rios_asia["nombre"]):
    ax_10.annotate(nombre, (linea.x, linea.y), xytext=(4, 4), textcoords="offset points", fontsize=8, color=AZUL)

ax_10.set_title("Ríos de la capa recortados con los países de Asia")
ax_10.set_axis_off()

plt.show()
```

- Verificación: 5 ríos, el tramo más largo es el del Chang, título y ejes
  ocultos.
- Chang (4 437 km), Mekong (4 115), Brahmaputra (2 480), Ob (1 830) y el
  fragmento "Yangtze" (4). Del Ob solo queda el tramo en Kazajistán: Rusia
  está clasificada como Europa en la capa de Natural Earth, así que el
  recorte con "Asia" elimina Siberia entera. El resultado es correcto para
  la clasificación de la capa, no para la geografía: hay que conocer los
  datos.
- Errores esperables: recortar con `paises` (WGS84) y medir en grados;
  recortar en WGS84 y luego reproyectar (vale igual, pero mide tras
  reproyectar); esperar que el Nilo o el Lena aparezcan (África y Rusia
  "europea").

## Ejercicio 11 (predicción: filas de tres uniones espaciales)

- Predicción esperada: `a` 210 (solo las ciudades dentro de algún
  polígono: `inner`), `b` 243 (todas las ciudades, 33 sin país), `c` 226
  (un par país-ciudad por fila, 210, más los 16 países sin ciudad que
  `how="left"` conserva). La explicación está en el bloque desplegable del
  cuaderno.
- Errores esperables: predecir 177 para `c` (una fila por país: eso lo
  daría un `groupby()` posterior, no la unión); predecir 243 para `a`.

## Ejercicio 12 (IA: ciudades y población por país)

- Elementos de una buena respuesta: el prompt con la estructura de rol,
  contexto (ambas capas con su SRC), tarea y formato; el código con
  `gpd.sjoin(ciudades_ee, paises_ee[...], predicate="within")`, un
  `groupby("codigo").agg(...)` y un `merge()` con `paises_ee` a la
  izquierda y `fillna(0)`; las cuatro comprobaciones: las dos capas en
  EPSG:8857, puntos a la izquierda con `within` (o países a la izquierda
  con `contains` y luego agrupar, que también es correcto), 177 filas en
  el resultado final y 210 ciudades sumadas, y dos o tres países
  comparados con la solución del ejercicio 4.
- Errores esperables del asistente: `pd.merge()` o `paises_ee` a la
  derecha (DataFrame sin geometría); `how="inner"` en el `merge()` final
  (desaparecen los 16 países sin ciudades); reproyectar innecesariamente
  a WGS84; contar con `len()` dentro de un ciclo `for` sobre los países
  (funciona, pero es lento y no es el patrón pedido).

## Ejercicio 13 (operaciones espaciales con la capa de la tarea 3)

- Elementos de una buena respuesta: la capa del ejercicio 12 de la parte I
  relacionada con al menos otra (cantones del SNIT, `centroamerica`,
  `paises`): una unión espacial con conteo por polígono, un `sjoin_nearest`
  con distancia o un `buffer()` seguido de `within`/`sjoin`; ambas capas
  reproyectadas al mismo SRC proyectado (CRTM05 para Costa Rica) antes de
  medir; el número de entidades sin pareja, explicado; y una celda de texto
  que diga qué pregunta responde cada operación.
- Errores esperables: unir capas en SRC distintos (cero filas con aviso);
  buffers en grados; contar por polígono con los polígonos a la izquierda
  sin agrupar (índices repetidos); usar `centroid` para ubicar etiquetas de
  cantones costeros o con islas (cae fuera: `representative_point()`).
