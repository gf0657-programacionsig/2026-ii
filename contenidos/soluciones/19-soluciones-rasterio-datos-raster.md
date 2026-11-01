---
short_title: "rasterio: datos raster"
---

# Soluciones — rasterio: datos raster

Soluciones y pautas de respuesta de los ejercicios del cuaderno de notas [rasterio: datos raster](../iv-procesamiento-datos-geoespaciales/19-rasterio-datos-raster.ipynb). Los ejercicios 1 a 12 tienen en el propio cuaderno una celda de verificación con `assert`, que examina el objeto creado; para los demás se describen los elementos de una buena respuesta y los errores esperables. Todas las soluciones suponen ejecutadas las celdas del cuaderno (`altitud`, `temperatura`, `precipitacion`, `altitud_ca`, `altitud_m`, `temperatura_m`, `precipitacion_m`, `limites`, `paises`, `centroamerica`, `ciudades`, `pisos`, `paises_clima`, `gandoca`, `verde`, `rojo`, `nir`, `ndvi`, `estirar()`, `limites_gandoca`, `alto_ee`, `ancho_ee`, `transformacion_ee`, `AZUL`, `NARANJA`) y las importaciones, incluidas `mask`, `show`, `ListedColormap`, `Patch`, `calculate_default_transform`, `reproject` y `Resampling`.

## Ejercicio 1 (metadatos de la precipitación)

```python
print("Bandas:", precipitacion.count)
print("Forma (filas, columnas):", precipitacion.shape)
print("Tipo de dato:", precipitacion.dtypes)
print("SRC:", precipitacion.crs)
print("Resolución:", precipitacion.res)
print("Límites:", precipitacion.bounds)
print("Valor sin dato:", precipitacion.nodata)

alineadas = precipitacion.transform == altitud.transform
print("Transformaciones idénticas:", alineadas)
```

- Verificación: `alineadas` es `True`; la precipitación es `int16` con
  −32 768 como valor sin dato.
- La igualdad de las transformaciones (y de las dimensiones) garantiza que
  la celda `[i, j]` de un raster cubre exactamente el mismo lugar que la
  celda `[i, j]` del otro: solo así tiene sentido operar celda a celda
  (álgebra de mapas). Si los rasters no están alineados hay que
  reproyectar o remuestrear uno de ellos a la cuadrícula del otro antes.

## Ejercicio 2 (estadísticas de la precipitación)

```python
print("Mínimo:", precipitacion_m.min(), "| máximo:", precipitacion_m.max(),
      "| media:", round(float(precipitacion_m.mean())), "| mediana:", np.median(precipitacion_m.compressed()))

muy_lluviosas = precipitacion_m > 3000
print("Celdas con más de 3 000 mm:", muy_lluviosas.sum(),
      "(", round(float(muy_lluviosas.sum() / precipitacion_m.count() * 100), 2), "%)")

# Celda de precipitación máxima y sus coordenadas
fila, columna = np.unravel_index(np.argmax(precipitacion_m), precipitacion_m.shape)
print("Máximo en la celda", (fila, columna), "con centro en", precipitacion.xy(fila, columna))
```

- Verificación: `muy_lluviosas` es booleana, del tamaño del raster, con
  8 774 celdas verdaderas (1,1 % de la tierra firme).
- Estadísticas: mínimo 0 mm, máximo 11 191 mm, media 550 mm y mediana
  338 mm: la distribución es muy asimétrica (muchas celdas secas, pocas
  muy lluviosas).
- La celda máxima está en (−109,25, 10,25): la isla Clipperton, un atolón
  francés deshabitado en el Pacífico, a 1 000 km de México. Es una sola
  celda aislada, sin estaciones meteorológicas cerca: el valor es un
  artefacto de la interpolación de WorldClim, no una medición. La lección:
  los extremos de un raster interpolado se revisan antes de citarlos. (En
  tierra firme continental, las celdas más lluviosas están en el Chocó
  colombiano y en el noreste de la India.)
- Error esperable: usar `np.argmax` sobre el array sin máscara, que
  retorna el índice de un −32 768 si no se enmascara; o invertir fila y
  columna al llamar `xy()`.

## Ejercicio 3 (mapa de la precipitación)

```python
fig, ax_3 = plt.subplots(figsize=(12, 6))
imagen = ax_3.imshow(precipitacion_m, cmap="Blues", extent=limites, vmin=0, vmax=4000)
paises.boundary.plot(ax=ax_3, color="black", linewidth=0.3)
fig.colorbar(imagen, ax=ax_3, shrink=0.6, label="Precipitación anual (mm)")
ax_3.set_title("Precipitación anual (WorldClim 2.1, 10 minutos de arco)")
ax_3.set_axis_off()
plt.show()
```

- Verificación: una imagen con la paleta `Blues`, una colección (los
  límites), título y ejes ocultos.
- Lectura del mapa: las franjas más lluviosas siguen la zona de
  convergencia intertropical (Amazonia, cuenca del Congo, sudeste
  asiático, Indonesia y Nueva Guinea, Centroamérica) y las costas
  expuestas a los vientos (Chocó, Caribe de Centroamérica, costa oeste de
  India y Birmania). Las más secas son los desiertos subtropicales
  (Sahara, Arabia, Atacama, Namib, Australia central) y las regiones
  polares, donde el aire frío contiene poca humedad.

## Ejercicio 4 (altitud de las capitales de Centroamérica)

```python
codigos_ca = ["GTM", "BLZ", "HND", "SLV", "NIC", "CRI", "PAN"]
capitales_ca = ciudades[ciudades["codigo_pais"].isin(codigos_ca) & ciudades["capital"]].copy()

coordenadas_ca = list(zip(capitales_ca["longitud"], capitales_ca["latitud"]))
capitales_ca["altitud_10"] = [valor[0] for valor in altitud.sample(coordenadas_ca)]
capitales_ca["altitud_2_5"] = [valor[0] for valor in altitud_ca.sample(coordenadas_ca)]
capitales_ca["diferencia"] = capitales_ca["altitud_10"] - capitales_ca["altitud_2_5"]

capitales_ca[["nombre", "altitud_10", "altitud_2_5", "diferencia"]].sort_values("diferencia", ascending=False)
```

- Verificación: 7 filas con las dos columnas; Managua difiere en más de
  150 m.
- Resultados (10' / 2,5'): Managua 289 / 80 m (diferencia 209), San José
  1 315 / 1 111 (204), San Salvador 802 / 653, Tegucigalpa 1 208 / 1 081,
  Ciudad de Guatemala 1 599 / 1 509, Ciudad de Panamá 73 / 21, Belmopán
  74 / 52. La capa fina siempre da menos, porque las capitales están en
  valles o llanuras rodeadas de montañas: la celda de 18 km promedia el
  relieve vecino. Managua es el caso extremo: a orillas del lago Xolotlán
  (40 m), pero con las sierras de Managua dentro de la celda gruesa.
- Error esperable: muestrear la capa regional con puntos fuera de sus
  límites (retorna el valor sin dato), o confundir el orden
  (longitud, latitud).

## Ejercicio 5 (clases de precipitación)

```python
clases_prec = np.ma.masked_array(np.digitize(precipitacion_m, [250, 1000, 2000]), mask=precipitacion_m.mask)
etiquetas_prec = ["Árido (< 250 mm)", "Seco (250-1 000 mm)", "Húmedo (1 000-2 000 mm)", "Muy húmedo (> 2 000 mm)"]
for clase, etiqueta in enumerate(etiquetas_prec):
    print(f"{etiqueta}: {(clases_prec == clase).sum()} celdas")

colores_prec = ["#FEE391", "#A1DAB4", "#41B6C4", "#225EA8"]
fig, ax_5 = plt.subplots(figsize=(12, 6))
ax_5.imshow(clases_prec, cmap=ListedColormap(colores_prec), extent=limites, vmin=-0.5, vmax=3.5, interpolation="nearest")
paises.boundary.plot(ax=ax_5, color="black", linewidth=0.3)
ax_5.legend(handles=[Patch(color=c, label=e) for c, e in zip(colores_prec, etiquetas_prec)], loc="lower left", fontsize=9)
ax_5.set_title("Clases de precipitación anual")
ax_5.set_axis_off()
plt.show()
```

- Verificación: forma del raster, valores 0 a 3, 329 230 celdas áridas,
  leyenda y ejes ocultos.
- Conteos: árido 329 230, seco 342 760, húmedo 98 987, muy húmedo
  37 076. Dos de cada cinco celdas terrestres reciben menos de 250 mm;
  la Antártida pesa mucho en ese conteo (ver el ejercicio 6).
- Error esperable: olvidar la máscara (el océano cae en la clase 0) o
  usar una paleta continua sin `vmin`/`vmax` a medio paso.

## Ejercicio 6 (celdas frías y secas)

```python
frio_seco = (temperatura_m < 0) & (precipitacion_m < 250)
print("Celdas frías y secas:", frio_seco.sum(),
      "(", round(float(frio_seco.sum() / temperatura_m.count() * 100), 1), "% de la tierra firme)")
print("Altitud media:", round(float(altitud_m[frio_seco].mean())), "m")
```

- Verificación: máscara booleana del tamaño del raster con 239 782 celdas
  verdaderas (29,7 % de la tierra firme), altitud media de 2 141 m.
- Se concentran en la Antártida (189 000 de las 240 000 celdas, el 79 %),
  Groenlandia, el Ártico canadiense y siberiano y las mesetas de Asia
  central (Tíbet). La Antártida ocupa el 27 % de las celdas terrestres
  pero solo el 8 % de la superficie: en una cuadrícula en grados las
  celdas se estrechan hacia los polos, así que el porcentaje de celdas
  exagera las regiones polares. Para un porcentaje de superficie, se
  reproyecta a Equal Earth (ejercicio 12) o se pondera cada fila por el
  coseno de su latitud.
- Una buena respuesta dibuja la máscara (`ax.imshow(frio_seco, extent=limites)`)
  para ubicar las regiones.

## Ejercicio 7 (altitud de Chile)

```python
chile = paises[paises["nombre"] == "Chile"]
recorte_chile, transformacion_chile = mask(altitud, chile.geometry, crop=True)
altitud_chile = np.ma.masked_equal(recorte_chile[0], altitud.nodata)
print("Altitud media:", round(float(altitud_chile.mean())), "m | máxima:", altitud_chile.max(), "m")

fig, ax_7 = plt.subplots(figsize=(4, 10))
show(altitud_chile, transform=transformacion_chile, ax=ax_7, cmap="terrain", vmin=0, vmax=5000)
chile.boundary.plot(ax=ax_7, color="black", linewidth=0.8)
ax_7.set_title("Altitud de Chile (m)")
ax_7.set_axis_off()
plt.show()
```

- Verificación: array enmascarado con máximo 5 455 m y media entre 1 000
  y 1 100 m (1 052 m).
- Chile es una franja angosta entre el Pacífico y la cordillera de los
  Andes: a 18 km de resolución, buena parte de las celdas cae sobre la
  cordillera y el altiplano del norte, de modo que la media de celdas
  es alta aunque la población viva en la depresión intermedia y la costa.
  La media de un país es una media de territorio, no de población.
- Error esperable: pasar la geometría en Equal Earth (`ValueError`), u
  olvidar `[0]` y enmascarar el valor sin dato.

## Ejercicio 8 (precipitación media por país)

```python
columnas = ["nombre", "precipitacion_media"]
print(paises_clima.sort_values("precipitacion_media", ascending=False)[columnas].head(10).round(0))
print(paises_clima.sort_values("precipitacion_media")[columnas].head(10).round(0))
mas_lluvioso = paises_clima.loc[paises_clima["precipitacion_media"].idxmax(), "nombre"]

fig, ax_8 = plt.subplots(figsize=(12, 6))
paises_clima.to_crs(8857).plot(
    ax=ax_8, column="precipitacion_media", cmap="Blues", scheme="quantiles", k=5,
    edgecolor="black", linewidth=0.2, legend=True,
    legend_kwds={"title": "Precipitación media (mm)", "loc": "lower left", "fontsize": 8},
)
ax_8.set_title("Precipitación anual media por país (estadística zonal de WorldClim)")
ax_8.set_axis_off()
plt.show()
```

- Verificación: `mas_lluvioso` es `"Brunéi"`; leyenda, título y ejes
  ocultos.
- Más lluviosos: Brunéi (3 548 mm), Islas Salomón, Vanuatu, Papúa Nueva
  Guinea, Costa Rica (2 884 mm, quinto del mundo), Malasia, Indonesia,
  Sierra Leona, Liberia y Fiyi. Más secos: Egipto (20 mm), Libia, Sahara
  Occidental, Argelia, Catar, Mauritania, Emiratos Árabes Unidos, Arabia
  Saudita, Jordania y Yemen.
- Es consistente con el mapa del ejercicio 3: los países pequeños de la
  franja ecuatorial y los desérticos ocupan los extremos; los países
  grandes (Brasil, China, Estados Unidos) promedian climas distintos y
  quedan en el medio.

## Ejercicio 9 (falso color)

```python
falso_color = np.dstack([estirar(nir), estirar(rojo), estirar(verde)])

fig, ax_9 = plt.subplots(figsize=(12, 8))
ax_9.imshow(falso_color, extent=limites_gandoca)
ax_9.set_title("Refugio Gandoca-Manzanillo, Sentinel-2 (falso color: NIR, rojo, verde)")
ax_9.set_axis_off()
plt.show()
```

- Verificación: forma (1 231, 1 811, 3) y canal rojo con media mayor que
  el verde.
- La vegetación aparece en rojo intenso porque la clorofila refleja mucho
  en el infrarrojo cercano, que va al canal rojo de la pantalla, y poco en
  el rojo visible. El agua, que absorbe el infrarrojo, queda casi negra;
  el suelo desnudo y las construcciones, en tonos claros o cian. Se
  distinguen mejor que en color verdadero los límites entre bosque,
  humedal y áreas abiertas, y los cuerpos de agua pequeños (la laguna de
  Gandoca).

## Ejercicio 10 (NDWI)

```python
ndwi = (verde - nir) / (verde + nir)

fig, ax = plt.subplots(figsize=(12, 8))
imagen = ax.imshow(ndwi, cmap="RdBu", extent=limites_gandoca, vmin=-1, vmax=1)
fig.colorbar(imagen, ax=ax, shrink=0.7, label="NDWI")
ax.set_title("NDWI del refugio Gandoca-Manzanillo")
ax.set_axis_off()
plt.show()

area_agua_ha = float((ndwi > 0).sum() * 0.01)
print("Área con NDWI > 0:", round(area_agua_ha), "ha")
print("Área con NDVI < 0:", round(float((ndvi < 0).sum() * 0.01)), "ha")
```

- Verificación: `ndwi` con la forma de la imagen y valores entre −1 y 1;
  `area_agua_ha` entre 6 000 y 7 000 (6 652 ha).
- El NDVI negativo da 6 599 ha: coinciden casi exactamente, porque en
  esta imagen el agua es el mar, que separa cualquiera de los dos
  índices. El NDWI está diseñado para el agua (el verde la refleja y el
  NIR la absorbe) y separa mejor los cuerpos de agua pequeños y turbios y
  los humedales inundados, donde el NDVI puede ser cercano a cero o
  positivo por la vegetación flotante.
- Error esperable: usar las bandas enteras sin convertir (desbordamiento
  de `uint16`), o invertir el orden de la resta (el agua quedaría
  negativa).

## Ejercicio 11 (escritura de los pisos altitudinales)

```python
perfil_pisos = altitud.profile.copy()
perfil_pisos.update(dtype="uint8", nodata=255, compress="deflate")

with rasterio.open("pisos-altitudinales.tif", "w", **perfil_pisos) as destino:
    destino.write(pisos.filled(255).astype("uint8"), 1)
    destino.set_band_description(1, "Pisos altitudinales (0: < 500 m, 1: 500-1 500, 2: 1 500-3 000, 3: > 3 000)")

pisos_tif = rasterio.open("pisos-altitudinales.tif")
print(pisos_tif.crs == altitud.crs, pisos_tif.transform == altitud.transform)
print(np.unique(pisos_tif.read(1)))
```

- Verificación: una banda `uint8` con 255 como valor sin dato, mismo SRC
  y transformación que la altitud, valores 0, 1, 2, 3 y 255.
- `uint8` ocupa la cuarta parte que `float32` y basta para cuatro clases;
  el valor sin dato debe ser uno que ninguna clase use (255). El archivo
  puede abrirse en QGIS como raster categórico.
- Error esperable: no rellenar las celdas enmascaradas (`filled(255)`)
  antes de escribir, con lo que quedan con el valor que numpy tenga
  debajo de la máscara; o no cerrar el archivo antes de reabrirlo.

## Ejercicio 12 (reproyección de un raster categórico)

```python
pisos_ee = np.full((alto_ee, ancho_ee), 255, dtype="uint8")
with rasterio.Env(CHECK_WITH_INVERT_PROJ=True):
    reproject(
        source=pisos.filled(255).astype("uint8"), destination=pisos_ee,
        src_transform=altitud.transform, src_crs=altitud.crs, src_nodata=255,
        dst_transform=transformacion_ee, dst_crs="EPSG:8857", dst_nodata=255,
        resampling=Resampling.nearest,
    )
pisos_ee = np.ma.masked_equal(pisos_ee, 255)

print("Altoandino en grados:", round(float((pisos == 3).sum() / pisos.count() * 100), 1), "% de las celdas")
print("Altoandino en Equal Earth:", round(float((pisos_ee == 3).sum() / pisos_ee.count() * 100), 1), "% de la superficie")
```

- Verificación: forma de la cuadrícula de Equal Earth (1 533 × 3 150) y
  solo las clases 0 a 3.
- El piso altoandino es el 9,4 % de las celdas en grados pero el 4,8 %
  de la superficie: otra vez la Antártida, cuya meseta supera los 3 000 m
  en gran parte y se infla en la cuadrícula en grados.
- Con `Resampling.bilinear` sobre enteros de 8 bits, rasterio promedia
  las clases vecinas y redondea: aparecen valores intermedios sin sentido
  en los bordes entre clases (y, con `src_nodata` mal definido, mezclas
  con el 255). `np.unique()` lo delata. Para categorías, siempre
  `nearest` (o `mode`, que toma la clase más frecuente al reducir la
  resolución).

## Ejercicio 13 (predicción)

Salidas: `(0, 0)`; `(540, 1080)`; `(-179.9167, 89.9167)` (impresas como
`np.float64`); `(180.0, -90.0)`. La explicación está en el propio
ejercicio. Una buena respuesta razona cada caso a partir del origen
(−180, 90), la resolución (1/6 de grado) y la diferencia entre esquina
(`transform * (col, fila)`) y centro (`xy()`) de la celda. Error
esperable: invertir fila y columna en `index()` (que retorna (fila,
columna)) o suponer que `xy(0, 0)` retorna el origen exacto.

## Ejercicio 14 (código generado por un asistente)

Elementos de una buena respuesta:

- El prompt documentado con sus cuatro partes y el asistente usado.
- El código generado, ejecutado sin modificar o con las correcciones
  anotadas. El patrón esperado es el de la sección de estadísticas
  zonales: `mask()` por país, `np.ma.masked_equal()` con el valor sin
  dato, media y máximo, DataFrame y `merge()`.
- Las cuatro comprobaciones: (1) la media se calcula sobre el array
  enmascarado (si el asistente usa `recorte.mean()` sin enmascarar, las
  medias salen negativas); (2) los tipos de dato (la media de enteros
  es flotante; el máximo, entero); (3) `paises` y el raster están en
  EPSG:4326; (4) la columna de medias coincide con `precipitacion_media`
  de `paises_clima` (por ejemplo, Costa Rica 2 884 mm, Brunéi 3 548 mm).
- Errores esperables del asistente: olvidar `crop=True` (funciona, pero
  es lento), usar `rasterstats` (que no está instalado) sin avisar,
  o enmascarar con `np.nan` sobre un array de enteros (falla).

## Ejercicio 15 (raster para la tarea 3)

Elementos de una buena respuesta: el raster elegido tiene relación
directa con el tema (altitud o pendiente para un tema físico, cobertura
de la tierra o NDVI para uno de uso del suelo, precipitación para uno
hidrológico); la celda de texto documenta fuente, fecha, resolución,
bandas, SRC, valor sin dato y licencia; el raster se abre con rasterio
(localmente o por URL) y se recorta o resume con la capa vectorial del
tema (`mask()` con un cantón, una cuenca o un área protegida, en el SRC
del raster), y se enuncia la pregunta que ese resultado responde. Errores
esperables: un raster mundial a baja resolución para un tema local (las
celdas de 18 km no sirven para un cantón), geometrías en CRTM05 sobre un
raster en WGS84 sin reproyectar, o una estadística sin enmascarar el valor
sin dato.
