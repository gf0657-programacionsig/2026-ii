---
short_title: "folium: mapas web interactivos"
---

# Soluciones — folium: mapas web interactivos

Soluciones y pautas de respuesta de los ejercicios del cuaderno de notas [folium: mapas web interactivos](../iv-procesamiento-datos-geoespaciales/20-folium-mapas-web.ipynb). Los ejercicios 1 a 9 tienen en el propio cuaderno una celda de verificación con `assert`, que examina el mapa creado con la función auxiliar `elementos()`; para los demás se describen los elementos de una buena respuesta y los errores esperables. Todas las soluciones suponen ejecutadas las celdas del cuaderno (`provincias`, `cantones`, `aerodromos`, `poblacion`, `cantones_crtm05`, `CENTRO_CR`, `limites`, `escala`, `estilo_densidad()`, `elementos()`, `AZUL`, `NARANJA`) y las importaciones, incluidas `plugins` y `branca.colormap as cm`.

## Ejercicio 1 (mapa de un cantón con tres mapas base)

La solución depende del cantón elegido; aquí, Montes de Oca, donde está la sede Rodrigo Facio de la Universidad de Costa Rica. Lo importante es que el acercamiento muestre el cantón completo (entre 12 y 14 para los cantones pequeños del valle Central; 10 u 11 para los grandes, como Talamanca o San Carlos) y que los tres mapas base estén en el control:

```python
mapa_1 = folium.Map(location=[9.94, -84.02], zoom_start=13, control_scale=True)  # Montes de Oca

folium.TileLayer("OpenTopoMap", name="Topográfico (OpenTopoMap)", show=False).add_to(mapa_1)
folium.TileLayer("Esri.WorldImagery", name="Imágenes de satélite (Esri)", show=False).add_to(mapa_1)

folium.LayerControl().add_to(mapa_1)
mapa_1
```

OpenTopoMap muestra mejor el relieve (curvas de nivel y sombreado), OpenStreetMap las calles y los nombres, y las imágenes de Esri la cobertura de la tierra (bosque, cultivos, urbanización). Un error esperable es olvidar `show=False`, con lo que el mapa arranca en el último mapa base agregado; no afecta la verificación, pero conviene notarlo.

## Ejercicio 2 (aeropuertos internacionales)

```python
aeropuertos = pd.DataFrame({
    "nombre": ["Juan Santamaría", "Daniel Oduber Quirós", "Tobías Bolaños", "Limón"],
    "ciudad": ["Alajuela", "Liberia", "Pavas, San José", "Limón"],
    "longitud": [-84.2115, -85.5418, -84.1400, -83.0207],
    "latitud": [9.9934, 10.5940, 9.9575, 9.9564],
})
aeropuertos = gpd.GeoDataFrame(aeropuertos, geometry=gpd.points_from_xy(aeropuertos["longitud"], aeropuertos["latitud"]), crs=4326)

mapa_2 = folium.Map(location=CENTRO_CR, zoom_start=8)
for aeropuerto in aeropuertos.itertuples():
    folium.Marker(
        location=[aeropuerto.geometry.y, aeropuerto.geometry.x],
        tooltip=aeropuerto.nombre,
        popup=folium.Popup(aeropuerto.ciudad, max_width=200),
        icon=folium.Icon(color="darkblue", icon="plane", prefix="fa")
    ).add_to(mapa_2)
mapa_2
```

El acercamiento 8 muestra los cuatro (Liberia, al noroeste, y Limón, al este, son los extremos); con 9 queda fuera alguno de los dos. Como las coordenadas ya están en el DataFrame, también es válido recorrerlo sin convertirlo en GeoDataFrame y usar `[aeropuerto.latitud, aeropuerto.longitud]`; el error esperable es invertir el orden.

## Ejercicio 3 (aeródromos agrupados y aeropuertos aparte)

```python
mapa_3 = folium.Map(location=CENTRO_CR, zoom_start=8)

agrupador = plugins.MarkerCluster(name="Aeródromos").add_to(mapa_3)
for aerodromo in aerodromos.itertuples():
    folium.Marker(location=[aerodromo.geometry.y, aerodromo.geometry.x], tooltip=aerodromo.nombre,
                  icon=folium.Icon(color="gray", icon="plane", prefix="fa")).add_to(agrupador)

internacionales = folium.FeatureGroup(name="Aeropuertos internacionales").add_to(mapa_3)
for aeropuerto in aeropuertos.itertuples():
    folium.Marker(location=[aeropuerto.geometry.y, aeropuerto.geometry.x], tooltip=aeropuerto.nombre,
                  icon=folium.Icon(color="red", icon="plane", prefix="fa")).add_to(internacionales)

folium.LayerControl().add_to(mapa_3)
mapa_3
```

Los aeródromos se concentran en las zonas costeras y rurales de difícil acceso por carretera: el Pacífico norte (Guanacaste), la península de Osa y Golfito, y el Caribe norte (Tortuguero, Barra del Colorado), donde el avión ligero sustituye a la carretera para turismo, producción agrícola y servicios. El valle Central, en cambio, apenas tiene: la densidad de carreteras y los dos aeropuertos del área metropolitana los hacen innecesarios.

## Ejercicio 4 (provincias según su número de cantones)

```python
cantones_por_provincia = cantones.groupby("codigo_provincia").size().rename("cantones").reset_index()
provincias = provincias.merge(cantones_por_provincia, on="codigo_provincia", how="left")
print(provincias[["provincia", "cantones"]].sort_values("cantones", ascending=False))

escala_4 = cm.LinearColormap(["#EFF3FF", "#6BAED6", "#08519C"], vmin=provincias["cantones"].min(),
                             vmax=provincias["cantones"].max(), caption="Número de cantones")

mapa_4 = folium.Map(location=CENTRO_CR, zoom_start=8, tiles="Esri.WorldGrayCanvas")
folium.GeoJson(
    provincias,
    name="Provincias",
    style_function=lambda entidad: {"fillColor": escala_4(entidad["properties"]["cantones"]),
                                    "color": "white", "weight": 1, "fillOpacity": 0.7},
    highlight_function=lambda entidad: {"weight": 3, "color": "#333333"},
    tooltip=folium.GeoJsonTooltip(fields=["provincia", "cantones"], aliases=["Provincia", "Cantones"])
).add_to(mapa_4)
escala_4.add_to(mapa_4)
folium.LayerControl().add_to(mapa_4)
mapa_4
```

San José tiene más cantones (20) y Heredia y Limón, menos (10 y 6, respectivamente; Puntarenas tiene 13 con Monteverde y Puerto Jiménez, y Alajuela 16). También es válido un diccionario de colores por valor o `value_counts()` con `map()`; lo que la verificación exige es que la columna `cantones` exista en `provincias` y sume 84. Un error esperable es unir por `provincia` con nombres que no coinciden, o usar `merge()` sin `how="left"` y perder provincias; otro, olvidar reasignar el resultado de `merge()` a `provincias`.

## Ejercicio 5 (coropletas de la población con Choropleth)

```python
cuantiles_5 = cantones["poblacion"].quantile([0.2, 0.4, 0.6, 0.8]).round().tolist()
limites_5 = [0] + cuantiles_5 + [math.ceil(cantones["poblacion"].max())]
print(limites_5)

mapa_5 = folium.Map(location=CENTRO_CR, zoom_start=8, tiles="Esri.WorldGrayCanvas")
coropletas_5 = folium.Choropleth(
    geo_data=cantones, data=cantones, columns=["codigo_canton", "poblacion"],
    key_on="feature.properties.codigo_canton", bins=limites_5,
    fill_color="PuBu", fill_opacity=0.8, line_color="white", line_weight=0.7,
    nan_fill_color="#E6E6E6", legend_name="Población, 2022 (habitantes)", highlight=True,
    name="Población"
).add_to(mapa_5)
coropletas_5.geojson.add_child(folium.GeoJsonTooltip(fields=["canton", "provincia", "poblacion"],
                                                     aliases=["Cantón", "Provincia", "Población"], localize=True))
folium.LayerControl().add_to(mapa_5)
mapa_5
```

Los límites son 0, 22 063, 36 136, 50 180, 75 899 y 352 381 habitantes. Los cantones que más cambian de clase son los grandes y poco poblados por unidad de área, que suben de clase en población y bajan en densidad: San Carlos (el más poblado del país después de San José y Alajuela, con densidad baja), Pérez Zeledón, Pococí, Sarapiquí y Talamanca; y al revés, los pequeños y densos del área metropolitana, como Tibás, Curridabat o Flores, que están en la clase alta de densidad y en clases medias de población. El mapa de densidad es más informativo para comparar cantones de tamaños tan distintos, porque la población total depende del área; el de población responde a otra pregunta (dónde vive más gente), y ambos son legítimos si el título y la leyenda lo dicen.

## Ejercicio 6 (lo mismo con explore())

```python
mapa_6 = cantones.explore(
    column="poblacion", scheme="Quantiles", k=5, cmap="PuBu",
    tooltip=["canton", "provincia", "poblacion"], tiles="Esri.WorldGrayCanvas",
    style_kwds={"color": "white", "weight": 0.7}, missing_kwds={"color": "#E6E6E6"},
    legend_kwds={"caption": "Población, 2022 (habitantes)"},
    name="Población", location=CENTRO_CR, zoom_start=8
)
plugins.MiniMap(toggle_display=True).add_to(mapa_6)
plugins.Fullscreen().add_to(mapa_6)
folium.LayerControl().add_to(mapa_6)
mapa_6
```

Elementos de una buena respuesta: la leyenda de `Choropleth` es una barra con los límites de las clases (que se amontonan cuando la variable es asimétrica); la de `explore()` es una escala por clases de branca con los mismos límites, calculados por mapclassify, más un recuadro para los valores faltantes (`NaN`). `explore()` conviene para explorar rápido, con una línea; `Choropleth` o un `GeoJson` con una escala propia convienen cuando se quiere controlar los límites, el texto de la leyenda, el tratamiento de los faltantes o combinar varias capas, y cuando no se quiere depender de mapclassify.

## Ejercicio 7 (capas WMS del IGN en el Arenal)

```python
mapa_7 = folium.Map(location=[10.49, -84.85], zoom_start=12, tiles="OpenTopoMap")

for capa, nombre in [("lago_o_laguna_200k", "Lagos y lagunas"), ("reddrenaje_200k", "Red de drenaje"),
                     ("curvas_de_nivel_200k", "Curvas de nivel")]:
    folium.WmsTileLayer(url=WMS_IGN_200, layers=capa, fmt="image/png", transparent=True,
                        name=f"{nombre} 1:200 000 (IGN)", attr="Instituto Geográfico Nacional, SNIT").add_to(mapa_7)

folium.LayerControl().add_to(mapa_7)
mapa_7
```

El `GetCapabilities` (https://geos.snitcr.go.cr/be/IGN_200/wms?service=WMS&request=GetCapabilities) lista, entre otras, `redvial_200k`, `viaferrea_200k`, `aerodromos_200k`, `aeropuertointernacional_200k`, `edificaciones_y_construcciones_200k`, `embalses_200k`, `lineas_de_costa_200k` y `salinas_200k`. Para la tarea 3 o el proyecto sirven según el tema: la red vial para accesibilidad, la red de drenaje y los embalses para temas hídricos, las edificaciones para asentamientos. Los servicios a 1:5 000 (`IGN_5`) y 1:25 000 (`IGN_25`) tienen cartografía más detallada (vías, edificaciones, curvas, cultivos y bosque de 2017). Un error esperable es usar el título de la capa en lugar de su nombre, lo que produce teselas vacías sin error en Python (el servidor responde con un documento de excepción); otro, usar un acercamiento menor que 12, por debajo de la escala mínima de la red de drenaje y las curvas de nivel, que entonces no se dibujan.

## Ejercicio 8 (altitud con otra paleta)

```python
paleta_8 = matplotlib.colormaps["YlGn"]
imagen_8 = paleta_8(np.clip(matriz.filled(0), 0, 2000) / 2000)
imagen_8[..., 3] = np.where(matriz.mask, 0, 0.6)

mapa_8 = folium.Map(location=CENTRO_CR, zoom_start=7, tiles="Esri.WorldImagery")
folium.raster_layers.ImageOverlay(
    image=imagen_8,
    bounds=[[limites_raster.bottom, limites_raster.left], [limites_raster.top, limites_raster.right]],
    mercator_project=True, name="Altitud (WorldClim)"
).add_to(mapa_8)
cm.LinearColormap([matplotlib.colors.to_hex(paleta_8(v)) for v in np.linspace(0, 1, 8)],
                  vmin=0, vmax=2000, caption="Altitud (m)").add_to(mapa_8)
plugins.MiniMap(toggle_display=True).add_to(mapa_8)
plugins.MeasureControl(primary_length_unit="kilometers").add_to(mapa_8)
folium.LayerControl().add_to(mapa_8)
mapa_8
```

El ancho de Costa Rica por el valle Central, de Puntarenas a Limón, es de unos 200 km en línea recta (entre 190 y 210 según los puntos elegidos). Con el rango de 0 a 2 000 m se gana contraste en las tierras bajas y medias, donde está casi todo el país (los pisos entre 0 y 1 500 m se distinguen mejor), y se pierde la distinción entre las cumbres: todo lo que supera 2 000 m (la cordillera de Talamanca, el Irazú, la Sierra Madre de Chiapas en Guatemala) satura en el mismo color, y el Chirripó (3 820 m) no se diferencia de un cerro de 2 000 m.

## Ejercicio 9 (guardar, aligerar y publicar)

```python
ruta_9 = "cantones-poblacion.html"
mapa_5.save(ruta_9)
print(f"{ruta_9}: {os.path.getsize(ruta_9) / 1e6:.2f} MB")

cantones_livianos = cantones[["codigo_canton", "canton", "provincia", "poblacion", "geometry"]].copy()
cantones_livianos["geometry"] = cantones_livianos.simplify(0.005)

mapa_liviano = folium.Map(location=CENTRO_CR, zoom_start=8, tiles="Esri.WorldGrayCanvas")
coropletas_livianas = folium.Choropleth(
    geo_data=cantones_livianos, data=cantones_livianos, columns=["codigo_canton", "poblacion"],
    key_on="feature.properties.codigo_canton", bins=limites_5, fill_color="PuBu", fill_opacity=0.8,
    line_color="white", line_weight=0.7, nan_fill_color="#E6E6E6",
    legend_name="Población, 2022 (habitantes)", highlight=True, name="Población"
).add_to(mapa_liviano)
coropletas_livianas.geojson.add_child(folium.GeoJsonTooltip(fields=["canton", "provincia", "poblacion"],
                                                            aliases=["Cantón", "Provincia", "Población"], localize=True))
folium.LayerControl().add_to(mapa_liviano)
mapa_liviano.save("cantones-poblacion-liviano.html")
print(f"cantones-poblacion-liviano.html: {os.path.getsize('cantones-poblacion-liviano.html') / 1e6:.2f} MB")
```

La versión original pesa alrededor de 1,4 MB (`Choropleth` incrusta el GeoJSON dos veces, en la capa y en los datos) y la simplificada unos 0,4 MB. Para publicar: copiar el archivo liviano al repositorio del sitio de la tarea 1 (con `git add`, `commit` y `push`, o arrastrándolo en la interfaz de GitHub), esperar el despliegue de GitHub Pages y agregar al `README.md` el enlace `https://<usuario>.github.io/<repositorio>/cantones-poblacion-liviano.html`. Una buena respuesta anota la dirección pública y comprueba que el mapa carga en el navegador; los errores esperables son publicar el archivo pesado (carga lenta) o enlazar la ruta local.

## Ejercicio 10 (predicción)

El mapa se centra en San José (acercamiento 12) y muestra el marcador y el contorno rojo del cantón en WGS84. La capa `CRTM05` aparece en el control de capas pero no dibuja nada: sus coordenadas en metros se interpretan como grados, fuera del rango válido, y Leaflet no las ubica. No hay error ni advertencia. Una buena predicción identifica las dos capas y anticipa que solo una es visible, y explica por qué con el error silencioso 2 de la clínica.

## Ejercicio 11 (código generado por un asistente)

Elementos de una buena respuesta: el asistente, el prompt completo y el código tal como lo entregó; la comprobación de que reproyecta a WGS84 antes de usar la capa (o la advertencia de que no lo hace, con la corrección); la comprobación de que los mapas base son OpenStreetMap y Esri (sin clave) y de que llevan atribución; la comprobación de que los límites de las clases cubren todos los valores (de lo contrario `Choropleth` lanza el `ValueError` de los límites) y de que la leyenda tiene título y unidades; y la comprobación de que los campos de la etiqueta existen en la capa. Errores esperables en el código generado: usar `"CartoDB positron"` como mapa base, poner `key_on="feature.properties.canton"` y unir por nombre, calcular los límites con `quantile()` sin incluir el máximo, y olvidar `nan_fill_color` para los dos cantones sin datos.

## Ejercicio 12 (mapa web de la capa de la tarea 3)

Respuesta abierta. Elementos de una buena respuesta: la capa reproyectada a WGS84; un mapa base acorde al tema (topográfico para temas físicos, OpenStreetMap para temas urbanos o de servicios) y las imágenes de satélite como alternativa; la capa con un estilo que la haga legible (color, grosor, opacidad), con etiqueta emergente breve y ventana emergente completa; agrupamiento si son cientos de puntos, o coropletas con límites y leyenda adecuados si son polígonos con una variable; al menos el control de capas y, si suman, el minimapa, la pantalla completa o la medición; el archivo guardado, publicado en GitHub Pages y enlazado, y la pregunta del tema que el mapa ayuda a explorar. Errores esperables: capa en el SRC proyectado (mapa vacío), coordenadas invertidas, mapa base con clave, archivo pesado sin simplificar, y etiquetas con todas las columnas, ilegibles.
