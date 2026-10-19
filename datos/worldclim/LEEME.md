# Datos de WorldClim

Fuente: [WorldClim](https://www.worldclim.org/), versión 2.1 (Fick y
Hijmans, 2017), rasters mundiales de clima promedio del periodo 1970-2000
y de altitud (derivada del modelo SRTM), publicados en WGS84 (EPSG:4326)
como GeoTIFF, un archivo por variable y mes. Los archivos originales se
descargan de https://geodata.ucdavis.edu/climate/worldclim/2_1/base/ con
el programa `preparar-datos.py` (requiere rasterio y numpy), que escribe
las capas de este directorio comprimidas y con una descripción por banda.

## Archivos

- `altitud.tif` (2 160 × 1 080 celdas, 10 minutos de arco, `int16`,
  sin dato −32 768): altitud en metros.
- `temperatura.tif` (mismas dimensiones, `float32`, sin dato
  −3,4 × 10³⁸): temperatura media anual en °C, promedio de las doce capas
  mensuales de temperatura media (`tavg`).
- `precipitacion.tif` (mismas dimensiones, `int16`, sin dato −32 768):
  precipitación anual en mm, suma de las doce capas mensuales (`prec`).
- `altitud-centroamerica.tif` (384 × 288 celdas, 2,5 minutos de arco,
  `int16`): altitud en metros de la ventana de longitud −93° a −77° y
  latitud 7° a 19° (de Guatemala a Panamá), leída de la capa mundial a
  2,5 minutos.

Las tres capas mundiales están alineadas (mismo SRC, dimensiones y
transformación) para operar entre ellas celda a celda. Un tercio de las
celdas tiene dato (la tierra firme, incluida la Antártida).

## Referencia

Fick, S. E. y Hijmans, R. J. (2017). WorldClim 2: New 1-km spatial
resolution climate surfaces for global land areas. *International Journal
of Climatology, 37*(12), 4302–4315.
