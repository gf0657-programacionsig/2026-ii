# Datos del IGN: división territorial administrativa y aeródromos

Fuente: Instituto Geográfico Nacional (IGN) de Costa Rica, capas publicadas
como servicios WFS en el Sistema Nacional de Información Territorial
(SNIT, https://www.snitcr.go.cr/), a escala 1:5000. Las copias de las que
parten estos archivos se descargaron del SNIT para el curso TPB-708 2026-I
y están en https://github.com/tpb708-programacionsig/2026-i/tree/main/datos/ign.

## Archivos

Todas las capas están en el sistema de referencia de coordenadas oficial
de Costa Rica, CR-SIRGAS / CRTM05 (EPSG:8908), que sustituyó a CR05 /
CRTM05 (EPSG:5367), el SRC en que el SNIT todavía publica estas capas. Se
distribuyen en formato GeoPackage y se generan con el programa
`preparar-datos.py` (requiere geopandas, incluido en el ambiente conda del
curso).

- `provincias.gpkg` (7 polígonos): `codigo_provincia`, `provincia`.
- `cantones.gpkg` (84 polígonos): `codigo_provincia`, `provincia`,
  `codigo_canton`, `canton`. Son los 84 cantones actuales, incluidos
  Monteverde (código 612, creado en 2021) y Puerto Jiménez (613, creado
  en 2022). Los códigos coinciden con los del INEC, de modo que las dos
  fuentes pueden unirse por `codigo_canton`; como los datos del INEC en
  `../inec/` siguen la división de 2011 (82 cantones), Monteverde y Puerto
  Jiménez quedan sin datos en esa unión.
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
  `cantones-2022.csv` (diferencias de hasta 1 km² por la simplificación),
  salvo en el cantón de Puntarenas: la capa del IGN incluye la Isla del
  Coco (unos 23 km²) y las cifras del INEC no, y además el INEC incluye en
  Puntarenas y Golfito las áreas de Monteverde y Puerto Jiménez.
