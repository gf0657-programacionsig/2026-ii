# Datos del IGN: división territorial administrativa y aeródromos

Fuente: Instituto Geográfico Nacional (IGN) de Costa Rica, capas publicadas
como servicios WFS en el Sistema Nacional de Información Territorial
(SNIT, https://www.snitcr.go.cr/), a escala 1:5000. Las copias de las que
parten estos archivos se descargaron del SNIT para el curso TPB-708 2026-I
y están en https://github.com/tpb708-programacionsig/2026-i/tree/main/datos/ign.

## Archivos

Todas las capas están en el sistema de referencia de coordenadas oficial
de Costa Rica, CR05 / CRTM05 (EPSG:5367), en formato GeoPackage, y se
generan con el programa `preparar-datos.py` (requiere geopandas, incluido
en el ambiente conda del curso).

- `provincias.gpkg` (7 polígonos): `codigo_provincia`, `provincia`.
- `cantones-2011.gpkg` (82 polígonos): `codigo_provincia`, `provincia`,
  `codigo_canton`, `canton`. Es la división territorial del Censo 2011,
  la misma de los datos del INEC en `../inec/`: los cantones de Monteverde
  (código 612, creado en 2021) y Puerto Jiménez (613, creado en 2022) se
  fundieron con Puntarenas (601) y Golfito (607), de los que se
  segregaron. Los códigos coinciden con los del INEC, de modo que las dos
  fuentes pueden unirse por `codigo_canton`.
- `aerodromos.gpkg` (119 puntos): `nombre` y `codigo_distrito` (código de
  cinco dígitos de la división territorial administrativa).

## Advertencias

- Las geometrías de provincias y cantones están **simplificadas** con una
  tolerancia de 100 m, para que los archivos sean pequeños y los mapas se
  dibujen rápido. Son adecuadas para mapas a escala nacional, no para
  mediciones precisas ni para mapas a escala local.
- Los nombres de dos cantones difieren entre el IGN y el INEC: "Vázquez de
  Coronado" (IGN) y "Vásquez de Coronado" (INEC); "León Cortés Castro"
  (IGN) y "León Cortés" (INEC). Es una razón más para unir por código y no
  por nombre.
- El área de los polígonos coincide con la que publica el INEC en
  `cantones-2022.csv` (diferencias menores a 0,05 km²), salvo en el cantón
  de Puntarenas: la capa del IGN incluye la Isla del Coco (unos 23 km²) y
  las cifras del INEC no.
