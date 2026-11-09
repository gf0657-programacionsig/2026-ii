---
short_title: "leafmap: análisis geoespacial y mapeo interactivo"
---

# Soluciones — leafmap: análisis geoespacial y mapeo interactivo

Soluciones y pautas de respuesta de los ejercicios del cuaderno de notas [leafmap: análisis geoespacial y mapeo interactivo](../iv-procesamiento-datos-geoespaciales/21-leafmap-mapeo-interactivo.ipynb). Los ejercicios 1 a 10 tienen en el propio cuaderno una celda de verificación con `assert`, que examina las capas y los controles del mapa creado con la función auxiliar `capas()`; para los demás se describen los elementos de una buena respuesta y los errores esperables. Todas las soluciones suponen ejecutadas las celdas del cuaderno (`provincias`, `cantones`, `aerodromos`, `poblacion`, `ALTITUD`, `GANDOCA`, `CENTRO_CR`, `WMS_IGN_200`, `capas()`, `AZUL`, `NARANJA`) y las importaciones.

## Ejercicio 1 (mapa de un cantón con mapas base y medición)

```python
mapa_1 = leafmap.Map(center=(9.94, -84.02), zoom=13, height="500px", scale_control=True, measure_control=True)  # Montes de Oca
mapa_1.add_basemap("OpenTopoMap")
mapa_1.add_basemap("Esri.WorldImagery")
mapa_1
```

La distancia depende de los lugares elegidos (por ejemplo, de la sede Rodrigo Facio al Mall San Pedro hay unos 700 m). Una buena respuesta anota la distancia medida y, si se quiere, la compara con la de la herramienta de medición de folium o con `distance()` de geopandas en CRTM05. Error esperable: escribir los nombres de los mapas base con otra capitalización, que `add_basemap()` no acepta (imprime la lista y no agrega nada: el error silencioso de la clínica).

## Ejercicio 2 (provincias con add_gdf)

```python
mapa_2 = leafmap.Map(center=CENTRO_CR, zoom=8, height="500px")
mapa_2.add_basemap("Esri.WorldGrayCanvas")
mapa_2.add_gdf(
    provincias,
    layer_name="Provincias",
    style={"color": "white", "weight": 1.5, "fillColor": AZUL, "fillOpacity": 0.4},
    hover_style={"fillOpacity": 0.8},
    info_mode="on_click",
    zoom_to_layer=False
)
mapa_2
```

El recuadro de atributos de leafmap es un panel fijo en la esquina inferior derecha que muestra todas las columnas de la entidad (con `info_mode="on_click"`, hasta que se hace clic en otra); la etiqueta emergente de folium sigue al cursor y muestra solo las columnas elegidas en `fields`, con alias. leafmap es más rápido de escribir; folium da más control sobre qué se muestra y cómo.

## Ejercicio 3 (coropletas de la población por cortes naturales)

```python
mapa_3 = leafmap.Map(center=CENTRO_CR, zoom=8, height="500px")
mapa_3.add_data(
    cantones,
    column="poblacion",
    scheme="NaturalBreaks",
    k=5,
    cmap="PuBu",
    legend_title="Población, 2022 (habitantes)",
    layer_name="Población",
    style={"color": "white", "weight": 0.7, "fillOpacity": 0.8},
    info_mode="on_hover"
)
mapa_3
```

Los cortes naturales (Jenks) buscan los saltos de la distribución: con la población, que es muy asimétrica (San José y Alajuela con más de 300 000 habitantes, la mayoría de los cantones por debajo de 60 000), la clase superior queda con dos o tres cantones y las clases bajas se reparten el resto, mientras que los quintiles ponen 16 o 17 cantones en cada clase sin importar los saltos. Los quintiles convienen para comparar posiciones relativas (qué cantones están en el quinto superior); los cortes naturales, para mostrar los grupos que de verdad existen en los datos. En ambos casos el esquema debe decirse en el título o la leyenda.

## Ejercicio 4 (aeródromos y aeropuertos internacionales)

```python
aeropuertos = pd.DataFrame({
    "nombre": ["Juan Santamaría", "Daniel Oduber Quirós", "Tobías Bolaños", "Limón"],
    "ciudad": ["Alajuela", "Liberia", "Pavas, San José", "Limón"],
    "longitud": [-84.2115, -85.5418, -84.1400, -83.0207],
    "latitud": [9.9934, 10.5940, 9.9575, 9.9564],
})

mapa_4 = leafmap.Map(center=CENTRO_CR, zoom=8, height="500px")
mapa_4.add_circle_markers_from_xy(aerodromos.drop(columns="geometry"), x="longitud", y="latitud",
                                  radius=4, color=NARANJA, fill_color=NARANJA, fill_opacity=0.8,
                                  popup=["nombre"], layer_name="Aeródromos")
mapa_4.add_points_from_xy(aeropuertos, x="longitud", y="latitud", popup=["nombre", "ciudad"],
                          layer_name="Aeropuertos internacionales")
mapa_4
```

Al acercarse al valle Central, el grupo que reúne a Juan Santamaría y Tobías Bolaños (a 8 km uno del otro) se separa en dos marcadores: el agrupamiento depende del nivel de acercamiento, y con cuatro puntos solo actúa cuando dos caen cerca en pantalla. Error esperable: pasar el GeoDataFrame con su columna `geometry` a los métodos `*_from_xy()`; funciona, pero conviene quitarla porque la ventana emergente la mostraría como texto.

## Ejercicio 5 (capas WMS en el Arenal)

```python
mapa_5 = leafmap.Map(center=(10.49, -84.85), zoom=12, height="500px")
mapa_5.add_basemap("OpenTopoMap")
for capa, nombre in [("lago_o_laguna_200k", "Lagos y lagunas"), ("reddrenaje_200k", "Red de drenaje"),
                     ("curvas_de_nivel_200k", "Curvas de nivel")]:
    mapa_5.add_wms_layer(url=WMS_IGN_200, layers=capa, name=f"{nombre} 1:200 000 (IGN)",
                         format="image/png", transparent=True, attribution="Instituto Geográfico Nacional, SNIT")
mapa_5
```

El inspector no muestra nada para las capas WMS: son imágenes que el servidor dibuja, sin atributos ni valores en el cliente (para consultarlas haría falta la operación `GetFeatureInfo` del propio servicio, que leafmap no envuelve). Sí muestra los valores de los rasters locales y los atributos de las capas vectoriales. Error esperable: acercamiento menor que 12, con el que la red de drenaje y las curvas no se dibujan.

## Ejercicio 6 (temperatura mundial de WorldClim)

```python
TEMPERATURA = leafmap.download_file(f"{DATOS_WC}/temperatura.tif", "temperatura.tif", quiet=True)

mapa_6 = leafmap.Map(center=(10, 0), zoom=2, height="500px")
mapa_6.add_raster(TEMPERATURA, colormap="RdBu_r", vmin=-10, vmax=30, nodata=-3.4e38, opacity=0.8,
                  layer_name="Temperatura", zoom_to_layer=False)
paleta_6 = matplotlib.colormaps["RdBu_r"]
mapa_6.add_colorbar(colors=[matplotlib.colors.to_hex(paleta_6(v)) for v in np.linspace(0, 1, 9)],
                    vmin=-10, vmax=30, caption="Temperatura media anual (°C)")
mapa_6
```

Saturan en azul (por debajo de −10 °C) la Antártida, Groenlandia, el Ártico canadiense y ruso y el Tíbet; en rojo (por encima de 30 °C) casi nada: solo algunas celdas del Sahara, el desierto de Danakil y el golfo Pérsico, porque la media **anual** rara vez supera 30 °C. Una buena respuesta nota que el rango elegido deja la paleta divergente centrada en 10 °C, no en 0: para centrarla en 0 habría que usar `vmin=-30, vmax=30` (y entonces casi toda la zona tropical queda en el extremo rojo). Error esperable: omitir `nodata`, con lo que el valor −3,4 × 10³⁸ del océano entra en la escala y el mapa sale de un solo color; el archivo sí declara su valor sin dato, así que aquí `nodata` es redundante pero inofensivo.

## Ejercicio 7 (mapa dividido: Esri frente a Sentinel-2)

```python
mapa_7 = leafmap.Map(center=(9.59, -82.63), zoom=13, height="500px")
mapa_7.split_map(
    left_layer="Esri.WorldImagery",
    right_layer=GANDOCA,
    right_args={"indexes": [3, 2, 1], "vmin": 1000, "vmax": 3500, "layer_name": "Sentinel-2"},
    left_label="Esri World Imagery", right_label="Sentinel-2, 2024-02-04"
)
mapa_7
```

No son de la misma fecha: el mosaico de Esri combina imágenes de varios años y proveedores (la fecha se consulta en el servicio de Esri), y la de Sentinel-2 es del 4 de febrero de 2024. Esri tiene mucha más resolución (submétrica en buena parte del país, frente a los 10 m de Sentinel-2), por lo que se distinguen casas y caminos; Sentinel-2 muestra nubes en la zona montañosa y es una sola fecha, lo que la hace comparable con otras fechas del mismo satélite, cosa que el mosaico no permite.

## Ejercicio 8 (COG de la altitud)

```python
leafmap.image_to_cog(ALTITUD, "altitud-cog.tif")
valido_8 = leafmap.cog_validate("altitud-cog.tif")[0]
print("¿Es COG?", valido_8)
print(f"Original: {os.path.getsize(ALTITUD) / 1e3:.0f} KB | COG: {os.path.getsize('altitud-cog.tif') / 1e3:.0f} KB")

mapa_8 = leafmap.Map(center=CENTRO_CR, zoom=7, height="500px")
mapa_8.add_raster("altitud-cog.tif", colormap="YlGn", vmin=0, vmax=2000, layer_name="Altitud COG", zoom_to_layer=False)
mapa_8
```

El original pesa unos 68 KB y el COG, unos 54 KB. El COG organiza los datos en **bloques** con sus índices al inicio del archivo y agrega **vistas previas** (copias a menor resolución, para los niveles de acercamiento lejanos); esa estructura es lo que permite a un servidor o a GDAL leer solo el bloque y la resolución que la vista necesita, en lugar del archivo entero. Las vistas previas agregan datos, pero `image_to_cog()` comprime con deflate, y por eso aquí el resultado pesa menos que el original (que se escribió sin compresión); con un original ya comprimido, el COG pesa algo más. Con un archivo de decenas de KB la diferencia es irrelevante; con una imagen de gigabytes, es la diferencia entre poder consultarla por Internet o no.

## Ejercicio 9 (dibujar la laguna de Gandoca y recortar)

```python
mapa_9 = leafmap.Map(center=(9.59, -82.60), zoom=14, height="500px")
mapa_9.add_raster(GANDOCA, indexes=[3, 2, 1], vmin=1000, vmax=3500, layer_name="Sentinel-2", zoom_to_layer=False)
mapa_9
```

Después de dibujar el polígono con la herramienta de la izquierda:

```python
mapa_9.save_draw_features("laguna.geojson")
laguna_9 = gpd.read_file("laguna.geojson")
print("Área:", round(laguna_9.to_crs(8908).area.sum() / 1e4, 1), "ha")

import rasterio
import rasterio.mask

# Recorte con rasterio: la laguna (WGS84) se reproyecta al SRC de la imagen
with rasterio.open(GANDOCA) as imagen:
    recorte, transformacion = rasterio.mask.mask(imagen, laguna_9.to_crs(imagen.crs).geometry, crop=True)
    perfil = imagen.profile
perfil.update(height=recorte.shape[1], width=recorte.shape[2], transform=transformacion)
with rasterio.open("laguna.tif", "w", **perfil) as destino:
    destino.write(recorte)

with rasterio.open("laguna.tif") as recorte:
    print(recorte.width, "×", recorte.height, "celdas |", recorte.count, "bandas |", recorte.crs)
```

La laguna de Gandoca tiene unas 30 a 40 ha según cuánto se incluya del canal y los manglares; el recorte queda en EPSG:32617 (el SRC de la imagen), con unas 60 × 70 celdas de 10 m para un polígono de ese tamaño, y se abre en QGIS como cualquier GeoTIFF. Una buena respuesta describe el polígono dibujado y compara el área con el tamaño del recorte. Errores esperables: ejecutar la segunda celda antes de dibujar (`user_roi` es `None` y `save_draw_features()` no escribe nada, por lo que `read_file()` falla), o dibujar un marcador en lugar de un polígono (el área es cero y el recorte, imposible). `leafmap.clip_image()` no sirve aquí: requiere fiona, ausente del ambiente del curso, y además no reproyecta la máscara, por lo que falla con `Input shapes do not overlap raster`.

## Ejercicio 10 (motor de folium y exportación)

```python
import leafmap.foliumap as foliumap

mapa_10 = foliumap.Map(center=CENTRO_CR, zoom=8, height="500px")
mapa_10.add_basemap("Esri.WorldGrayCanvas")
mapa_10.add_data(cantones, column="poblacion", scheme="NaturalBreaks", k=5, cmap="PuBu",
                 legend_title="Población, 2022 (habitantes)", layer_name="Población",
                 style={"color": "white", "weight": 0.7, "fillOpacity": 0.8})
mapa_10.add_points_from_xy(aeropuertos, x="longitud", y="latitud", popup=["nombre", "ciudad"],
                           layer_name="Aeropuertos internacionales")
mapa_10.add_layer_control()

ruta_10 = "poblacion-leafmap.html"
mapa_10.to_html(ruta_10)
print(f"{ruta_10}: {os.path.getsize(ruta_10) / 1e6:.2f} MB")
mapa_10
```

El mapa exportado tiene los controles de folium: acercamiento, control de capas, leyenda y las ventanas emergentes; no tiene las herramientas de dibujo, el inspector ni la barra de herramientas de ipyleaflet, que solo existen en el cuaderno. El mapa equivalente del cuaderno de folium (ejercicio 5 de ese cuaderno) es prácticamente el mismo archivo, construido con más líneas y más control sobre cada elemento (límites de las clases, alias de las etiquetas, color de los faltantes).

## Ejercicio 11 (predicción)

El primer mapa, de folium, queda vacío: la capa en CRTM05 llega a Leaflet con coordenadas en metros, que no puede ubicar, y no hay error. El segundo, de leafmap, muestra el cantón, porque `add_gdf()` reproyecta a WGS84 antes de convertir a GeoJSON. Una buena predicción identifica el SRC impreso (EPSG:8908) como la causa y recuerda el error silencioso 2 del cuaderno de folium; una respuesta completa añade que la reproyección automática no cubre las columnas de coordenadas de una tabla (`add_points_from_xy()` las toma como longitud y latitud en WGS84).

## Ejercicio 12 (código generado por un asistente)

Elementos de una buena respuesta: el asistente, el prompt completo y el código tal como lo entregó; la comprobación con `help()` o con la referencia de la API de que los métodos y argumentos existen en leafmap 0.63 (los asistentes suelen inventar argumentos como `palette`, `legend=True` o `add_colormap()` con parámetros de otras versiones, o mezclar el motor de maplibre); la comprobación de que el código usa `import leafmap` (ipyleaflet) y no `leafmap.foliumap`, salvo que se pida publicar; la comprobación de que las columnas (`poblacion`) y los nombres de capa coinciden; y la comprobación de que `add_raster()` lleva `vmin=0`, `vmax=3500` y, si el archivo no lo declara, `nodata=-32768`. Errores esperables en el código generado: `add_data()` con `scheme="natural_breaks"` (minúsculas, que no existe), `add_raster()` sin `vmin`/`vmax` (mapa lavado), `add_colorbar()` con argumentos de `add_colormap()`, y coropletas sin tratar los dos valores faltantes.

## Ejercicio 13 (mapa de la tarea 3 con leafmap)

Respuesta abierta. Elementos de una buena respuesta: la capa del tema con `add_gdf()` o `add_data()` y estilo legible; un raster pertinente al tema (el del ejercicio 15 del cuaderno de rasterio o una capa de WorldClim) con `add_raster()`, paleta y rango adecuados a la variable (secuencial para altitud o precipitación, divergente para temperatura) y valor sin dato correcto; un `split_map()` que compare el raster con `"Esri.WorldImagery"`; y una celda de texto que diga qué pregunta del tema ayuda a responder el raster y qué motor usaría para publicar (folium, con `leafmap.foliumap` o con folium directo, porque ipyleaflet no sobrevive al HTML estático). Errores esperables: raster en un SRC distinto sin problema (leafmap lo reproyecta al vuelo, pero conviene saberlo), rango de la paleta que satura o lava el mapa, y confundir el inspector con la ventana emergente.
