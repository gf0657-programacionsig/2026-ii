# Imagen Sentinel-2 del refugio Gandoca-Manzanillo

Fuente: escena Sentinel-2 L2A (reflectancia de superficie) del programa
[Copernicus](https://www.copernicus.eu/) de la Unión Europea, obtenida del
catálogo abierto de [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com/dataset/sentinel-2-l2a)
con el programa `preparar-datos.py` (requiere rasterio y requests), que
busca la escena en el catálogo STAC y lee de los GeoTIFF originales solo
la ventana del refugio.

## Archivo

- `gandoca-20240204.tif` (1 811 × 1 231 celdas de 10 m, `uint16`, sin
  dato 0, EPSG:32617 WGS 84 / UTM zona 17N): cuatro bandas de la escena
  `S2B_MSIL2A_20240204T160509_R054_T17PLL_20240204T213428` del 4 de
  febrero de 2024 (7,5 % de nubes en la escena completa), recortadas a la
  parte terrestre del Refugio Nacional de Vida Silvestre Mixto
  Gandoca-Manzanillo, en el Caribe sur de Costa Rica (este 312 120 a
  330 230 m, norte 1 054 330 a 1 066 640 m).

| Banda | Descripción | Longitud de onda central |
|---|---|---|
| 1 | Azul (B02) | 490 nm |
| 2 | Verde (B03) | 560 nm |
| 3 | Roja (B04) | 665 nm |
| 4 | Infrarroja cercana, NIR (B08) | 842 nm |

Los valores son reflectancias escaladas: reflectancia = (valor − 1 000) /
10 000, según la convención de los productos L2A con línea base de
procesamiento 04.00 o posterior. Los datos de Sentinel-2 se distribuyen
con la licencia abierta de Copernicus.
