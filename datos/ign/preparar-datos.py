"""Prepara las capas del IGN que usa el curso, a partir de las copias de los
servicios WFS del SNIT conservadas en el repositorio del curso TPB-708 2026-I.

Produce, en EPSG:5367 (CR05 / CRTM05) y con geometrías simplificadas:

- provincias.gpkg: 7 provincias.
- cantones-2011.gpkg: 82 cantones, la división territorial del Censo 2011,
  que es la de los datos del INEC en datos/inec/. Los cantones de
  Monteverde (612, creado en 2021) y Puerto Jiménez (613, 2022) se funden
  con Puntarenas (601) y Golfito (607), de los que se segregaron.
- aerodromos.gpkg: 119 aeródromos (puntos), con el nombre y el código del distrito.

Uso: python3 preparar-datos.py (requiere geopandas; ejecutar en datos/ign/).
"""

import geopandas as gpd

ORIGEN = "https://github.com/tpb708-programacionsig/2026-i/raw/refs/heads/main/datos/ign"
CRTM05 = 5367
TOLERANCIA_M = 100  # simplificación de las geometrías, en metros

# Provincias
provincias = gpd.read_file(f"{ORIGEN}/provincias.gpkg").to_crs(CRTM05)
provincias = provincias.rename(columns={"CÓDIGO_PROVINCIA": "codigo_provincia", "PROVINCIA": "provincia"})
provincias = provincias[["codigo_provincia", "provincia", "geometry"]].sort_values("codigo_provincia")
provincias["geometry"] = provincias.geometry.simplify(TOLERANCIA_M, preserve_topology=True)
provincias.to_file("provincias.gpkg", driver="GPKG")
print("provincias.gpkg:", provincias.shape)

# Cantones (división territorial de 2011)
cantones = gpd.read_file(f"{ORIGEN}/cantones.gpkg").to_crs(CRTM05)
cantones = cantones.rename(columns={
    "CÓDIGO_DE_PROVINCIA": "codigo_provincia", "PROVINCIA": "provincia",
    "CÓDIGO_CANTÓN": "codigo_canton", "CANTÓN": "canton"
})
assert cantones.shape[0] == 84, cantones.shape
cantones["codigo_canton"] = cantones["codigo_canton"].replace({612: 601, 613: 607})
cantones = cantones.dissolve(
    by="codigo_canton", aggfunc={"canton": "first", "codigo_provincia": "first", "provincia": "first"}
).reset_index()
cantones = cantones[["codigo_provincia", "provincia", "codigo_canton", "canton", "geometry"]]
assert cantones.shape[0] == 82 and set(cantones["canton"]) >= {"Puntarenas", "Golfito"}
cantones["geometry"] = cantones.geometry.simplify(TOLERANCIA_M, preserve_topology=True)
cantones.to_file("cantones-2011.gpkg", driver="GPKG")
print("cantones-2011.gpkg:", cantones.shape)

# Aeródromos
aerodromos = gpd.read_file(f"{ORIGEN}/aerodromos.gpkg").to_crs(CRTM05)
aerodromos = aerodromos.rename(columns={"ubicacion": "codigo_distrito"})
aerodromos = aerodromos[["nombre", "codigo_distrito", "geometry"]]
aerodromos.to_file("aerodromos.gpkg", driver="GPKG")
print("aerodromos.gpkg:", aerodromos.shape)
