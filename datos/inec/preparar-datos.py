# Prepara los archivos CSV de provincias, cantones y distritos a partir del
# Excel "Resultados Estimación de Población y Vivienda 2022" del INEC
# (cuadros 11 y 12), descargado de
# https://admin.inec.cr/sites/default/files/2023-11/reResultadosEstimacionPoblacionVivienda2022_3.xlsx
#
# En el Excel, la jerarquía provincia > cantón > distrito no viene en
# columnas: las filas de provincia tienen relleno de color y las de cantón
# están en negrita. Este script la reconstruye a partir de ese formato y
# genera un archivo por nivel. Los códigos de provincia (1-7) y de cantón
# (101-706) se asignan según el orden de los cuadros, que sigue la
# División Territorial Administrativa vigente en el Censo 2011
# (82 cantones; no incluye Monteverde ni Puerto Jiménez, creados después).
#
# Uso (desde este directorio): python3 preparar-datos.py

import csv
import openpyxl

ARCHIVO = "reResultadosEstimacionPoblacionVivienda2022_3.xlsx"
RELLENO_PROVINCIA = "FFB8DBE1"


def leer_cuadro(hoja, columnas, fila_inicial, fila_final):
    """Lee las filas de datos de un cuadro y retorna una lista de
    diccionarios con el nivel (provincia, canton o distrito) de cada una."""
    filas = []
    for r in range(fila_inicial, fila_final + 1):
        celda = hoja.cell(r, 1)
        if celda.value is None:
            continue
        if celda.fill.fgColor.rgb == RELLENO_PROVINCIA:
            nivel = "provincia"
        elif celda.font.b:
            nivel = "canton"
        else:
            nivel = "distrito"
        fila = {"nombre": str(celda.value).strip(), "nivel": nivel}
        for nombre_columna, indice in columnas.items():
            fila[nombre_columna] = hoja.cell(r, indice).value
        filas.append(fila)
    return filas


wb = openpyxl.load_workbook(ARCHIVO)

# Cuadro 11: población y viviendas (filas 9 a 584; la 7 es el total nacional)
cuadro_11 = leer_cuadro(
    wb["11"],
    {"poblacion": 2, "hombres": 3, "mujeres": 4, "viviendas": 6,
     "viviendas_ocupadas": 7, "viviendas_desocupadas": 8,
     "promedio_ocupantes": 9},
    9, 584
)

# Cuadro 12: área, densidad y tasas (mismas filas y orden que el cuadro 11)
cuadro_12 = leer_cuadro(
    wb["12"],
    {"area_km2": 2, "densidad": 3, "tasa_crecimiento_poblacion": 4,
     "tasa_crecimiento_viviendas": 5, "relacion_hombre_mujer": 6},
    9, 584
)

assert len(cuadro_11) == len(cuadro_12), "Los cuadros 11 y 12 difieren en filas"
for f11, f12 in zip(cuadro_11, cuadro_12):
    assert (f11["nombre"], f11["nivel"]) == (f12["nombre"], f12["nivel"]), \
        f"Filas desalineadas: {f11['nombre']} / {f12['nombre']}"

# Unión de los dos cuadros y reconstrucción de la jerarquía
provincias, cantones, distritos = [], [], []
codigo_provincia = 0
codigo_canton = 0
provincia_actual = canton_actual = None

for f11, f12 in zip(cuadro_11, cuadro_12):
    variables = {
        "poblacion": f11["poblacion"],
        "hombres": f11["hombres"],
        "mujeres": f11["mujeres"],
        "viviendas": f11["viviendas"],
        "viviendas_ocupadas": f11["viviendas_ocupadas"],
        "viviendas_desocupadas": f11["viviendas_desocupadas"],
        "promedio_ocupantes": round(f11["promedio_ocupantes"], 2),
        "area_km2": round(f12["area_km2"], 2),
        "densidad": round(f12["densidad"], 1),
        "tasa_crecimiento_poblacion": round(f12["tasa_crecimiento_poblacion"], 2),
        "tasa_crecimiento_viviendas": round(f12["tasa_crecimiento_viviendas"], 2),
        "relacion_hombre_mujer": round(f12["relacion_hombre_mujer"], 1),
    }
    if f11["nivel"] == "provincia":
        codigo_provincia += 1
        codigo_canton = 0
        provincia_actual = f11["nombre"]
        provincias.append({"codigo_provincia": codigo_provincia,
                           "provincia": provincia_actual, **variables})
    elif f11["nivel"] == "canton":
        codigo_canton += 1
        canton_actual = f11["nombre"]
        cantones.append({"codigo_provincia": codigo_provincia,
                         "provincia": provincia_actual,
                         "codigo_canton": codigo_provincia * 100 + codigo_canton,
                         "canton": canton_actual, **variables})
    else:
        distritos.append({"codigo_provincia": codigo_provincia,
                          "provincia": provincia_actual,
                          "codigo_canton": codigo_provincia * 100 + codigo_canton,
                          "canton": canton_actual,
                          "distrito": f11["nombre"], **variables})

assert len(provincias) == 7, len(provincias)
assert len(cantones) == 82, len(cantones)
assert len(distritos) == 487, len(distritos)

# Verificación de consistencia: la población de cada provincia es la suma
# de la de sus cantones, y la de cada cantón, la suma de sus distritos
for p in provincias:
    suma = sum(c["poblacion"] for c in cantones
               if c["codigo_provincia"] == p["codigo_provincia"])
    assert suma == p["poblacion"], f"Provincia {p['provincia']}: {suma} != {p['poblacion']}"
for c in cantones:
    suma = sum(d["poblacion"] for d in distritos
               if d["codigo_canton"] == c["codigo_canton"])
    assert suma == c["poblacion"], f"Cantón {c['canton']}: {suma} != {c['poblacion']}"


def escribir_csv(nombre, filas):
    with open(nombre, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
        escritor.writeheader()
        escritor.writerows(filas)
    print(f"{nombre}: {len(filas)} filas")


escribir_csv("provincias-2022.csv", provincias)
escribir_csv("cantones-2022.csv", cantones)
escribir_csv("distritos-2022.csv", distritos)
