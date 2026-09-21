---
short_title: "Fundamentos de Python III: estructuras de datos y servicios web"
---

# Soluciones — Fundamentos de Python III: estructuras de datos y servicios web

Soluciones y pautas de respuesta de los ejercicios del cuaderno de notas [Fundamentos de Python III: estructuras de datos y servicios web](../ii-lenguaje-programacion-python/11-estructuras-datos-apis.ipynb). Los ejercicios 1, 3, 4, 5 y 8 tienen en el propio cuaderno una celda de verificación con `assert`, que comprueba automáticamente el resultado; para los demás se describen los elementos de una buena respuesta y los errores esperables.

## Ejercicio 1 (split y sorted)

```python
temas = "geografía;sig;python;datos".split(";")
temas_ordenados = sorted(temas)
```

- Verificación: `['geografía', 'sig', 'python', 'datos']` y
  `['datos', 'geografía', 'python', 'sig']`.
- Errores esperables: usar `", "` como separador (la hilera usa `;`),
  y usar `temas.sort()` — el tercer assert lo detecta (la lista
  original quedaría modificada) y remite a sorted().

## Ejercicio 2 (predicción: sort vs sorted)

- Respuesta esperada: imprime `None` y luego `[1, 2, 3]`. La
  explicación completa está en el desplegable del cuaderno.
- Predicción errónea típica: "[1, 2, 3] dos veces". Conexión con el
  ejercicio 3 de la parte II (retornar/imprimir/modificar).

## Ejercicio 3 (diccionario del cantón)

Ejemplo con el cantón de Puntarenas (los valores dependen del cantón
elegido; lo evaluable es la estructura, la fuente en comentario y la
densidad calculada desde las claves):

```python
# Cantón de Puntarenas (INEC, Estimación de Población y Vivienda 2022)
mi_canton = {
    "nombre": "Puntarenas",
    "poblacion": 141697,
    "area": 1816.86,
    "tiene_costa": True
}

mi_canton["densidad"] = mi_canton["poblacion"] / mi_canton["area"]
```

- Errores esperables: calcular la densidad con los números "a mano"
  en vez de con las claves (el assert de coherencia lo detecta) y
  `"tiene_costa": "True"` como hilera (assert de tipo).

## Ejercicio 4 (lista de diccionarios de cantones)

```python
# Cantones de la provincia de Heredia (INEC, Estimación de Población y Vivienda 2022)
cantones_datos = [
    {"nombre": "Heredia", "poblacion": 131901, "area": 283.12},
    {"nombre": "Barva", "poblacion": 47699, "area": 56.02},
    {"nombre": "Santo Domingo", "poblacion": 45932, "area": 25.4}
]

for canton in cantones_datos:
    densidad = canton["poblacion"] / canton["area"]
    print(f"{canton['nombre']}: {densidad:.1f} hab/km2")
```

- Los valores dependen de los cantones elegidos: lo evaluable es la
  coherencia con la fuente y su cita. La verificación del cuaderno solo
  revisa la estructura (≥3 cantones, claves, áreas positivas).
- Error esperable: comillas dobles anidadas en la f-string
  (`f"{canton["nombre"]}"` falla en las versiones de Python anteriores
  a la 3.12). Las versiones actuales lo aceptan, pero las comillas
  simples adentro son más legibles y funcionan en cualquier versión.

## Ejercicio 5 (GBIF con otra especie)

Espejo del ejemplo, cambiando el nombre científico:

```python
respuesta = requests.get(
    "https://api.gbif.org/v1/species/match",
    params={"name": "Panthera onca", "strict": True}
)
clave_taxon = respuesta.json()["usageKey"]

respuesta_registros = requests.get(
    "https://api.gbif.org/v1/occurrence/search",
    params={"taxonKey": clave_taxon, "country": "CR",
            "hasCoordinate": True, "limit": 5}
)
datos = respuesta_registros.json()
print(datos["count"])
for registro in datos["results"]:
    print(registro["species"], registro.get("year", "sin año"),
          registro["decimalLatitude"], registro["decimalLongitude"])
```

- Errores esperables: nombre común en vez de científico (el match no
  encuentra usageKey → KeyError; sugerir revisar el JSON de la
  respuesta), y olvidar hasCoordinate (algunos registros sin lat/lon
  → KeyError en el for; conectar con get()).

## Ejercicio 6 (sismos del USGS)

```python
respuesta = requests.get(
    "https://earthquake.usgs.gov/fdsnws/event/1/query",
    params={
        "format": "geojson",
        "starttime": "2025-01-01",
        "endtime": "2025-12-31",
        "minmagnitude": 4,
        "minlatitude": 8, "maxlatitude": 11.3,
        "minlongitude": -86, "maxlongitude": -82.5
    }
)
datos = respuesta.json()

sismos = datos["features"]
print(f"Sismos de magnitud >= 4 en 2025: {len(sismos)}")

magnitud_maxima = sismos[0]["properties"]["mag"]
for sismo in sismos:
    if sismo["properties"]["mag"] > magnitud_maxima:
        magnitud_maxima = sismo["properties"]["mag"]
print(f"Magnitud máxima: {magnitud_maxima}")
```

- La cantidad y la magnitud dependen del momento de la consulta (el
  catálogo se revisa retroactivamente): verificar la estructura del
  código, no el número. También es válido max() con una lista de
  magnitudes construida con append (patrón de la parte II).
- Errores esperables: buscar la magnitud en el nivel superior del
  sismo (está anidada en "properties") y usar la lista vacía sin
  revisar (si len(sismos) == 0, sismos[0] da IndexError — punto de
  discusión sobre casos límite).

## Ejercicio 7 (explicar errores con un asistente)

Abierto; lista de verificación de la documentación (que es a la vez
la declaración de uso de IA):

- Asistente identificado; prompt con los cuatro componentes (rol,
  contexto, tarea, formato) y con el mensaje de error completo.
- Resumen de la respuesta y evaluación propia: ¿coincide con lo
  anotado en el ejercicio 7 de la parte II? ¿el asistente agregó algo
  dudoso o inventado? (si lo hay, señalarlo es un acierto, no un
  error).
- Error esperable: prompts sin contexto ("¿qué significa este
  error?" sin el código) y aceptar la respuesta sin contrastarla.

## Ejercicio 8 (depuración asistida)

Los dos errores del programa:

1. **Con mensaje** (detiene el programa): `provincia["areas"]` →
   KeyError; la clave correcta es `"area"`.
2. **Silencioso** (resultado incorrecto): dentro del if nunca se
   actualiza `densidad_max`, por lo que la condición `densidad >
   densidad_max` (con densidad_max siempre en 0) es verdadera para
   TODAS las provincias y `mas_densa` queda con la última (Cartago),
   no con la más densa (Heredia); además el print muestra 0.0.

Programa corregido:

```python
mas_densa = ""
densidad_max = 0
for provincia in provincias_datos:
    densidad = provincia["poblacion"] / provincia["area"]
    if densidad > densidad_max:
        mas_densa = provincia["nombre"]
        densidad_max = densidad
print(f"La provincia más densa es {mas_densa} ({densidad_max:.1f} hab/km2)")
```

- Verificación: Heredia, 180.3 (los asserts lo comprueban).
- El propósito didáctico: el error 1 lo encuentra cualquiera (y el
  asistente lo explica bien); el error 2 es el valioso — "corre sin
  errores ≠ es correcto" (lección 06) y hay que DESCRIBIRLE al
  asistente el síntoma ("imprime 0.0 y la provincia equivocada") para
  que ayude. En la documentación, revisar si el prompt del error 2
  incluye el síntoma y no solo el código.
