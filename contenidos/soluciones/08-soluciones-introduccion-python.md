---
short_title: "Introducción a Python"
---

# Soluciones — Introducción a Python

Soluciones y pautas de respuesta de los ejercicios de la lección [Introducción a Python](../ii-lenguaje-programacion-python/08-introduccion-python.md). Para los ejercicios operativos y abiertos se describen los elementos que debe incluir una buena respuesta y los errores esperables.

## Ejercicio 1 (Zen de Python)

Operativo y abierto. Elementos de una buena respuesta:

- `import this` despliega los 19 principios (en inglés) como salida de
  la celda; error esperable: escribirlo en una celda de texto.
- Vale cualquier par de principios explicado con palabras propias; los
  más ligados a la legibilidad —y los más fáciles de conectar con el
  capítulo— son "Readability counts", "Beautiful is better than ugly",
  "Explicit is better than implicit" y "Simple is better than complex".
- La conexión esperada: la legibilidad facilita entender, mantener y
  reutilizar programas (propios y ajenos) — el mismo argumento de la
  sección de principios de diseño.
- Respuesta débil esperable: traducir el principio sin explicarlo ni
  conectarlo con el capítulo.

## Ejercicio 2 (reescritura según PEP 8)

Solución esperada (espejo del ejemplo de la sección):

```python
# Densidad de población de Costa Rica (INEC, Censo 2022; área en km2)
poblacion = 5044197
area = 51100

print("Densidad de población de Costa Rica (hab/km2):", poblacion / area)
```

- Salida ≈ 98.7 en ambas versiones (verificar que el resultado no
  cambió). Lo evaluable: nombres significativos en minúscula, espacios
  alrededor de `=` y tras las comas, comentario con la fuente y texto
  del print corregido (mayúsculas y tildes en el TEXTO impreso sí
  van: la restricción de tildes es para los NOMBRES de variables —
  distinción que conviene remarcar).
- Errores esperables: "corregir" también los valores (no hace falta),
  dejar `Y` en mayúscula solo renombrada (`Poblacion`), y creer que
  cambiar el estilo cambia el resultado.

## Ejercicio 3 (exploración de PyPI)

Sin solución única; lista de verificación:

- El paquete elegido debe relacionarse con el tema de interés (la
  búsqueda en PyPI es por palabras en inglés; conviene sugerir
  términos si alguien no encuentra resultados).
- Deben anotarse: nombre, qué hace (de la descripción del proyecto) y
  fecha de la versión más reciente (aparece en la página del paquete;
  "Release history" muestra todas).
- Punto de discusión: una fecha de última versión muy antigua sugiere
  un proyecto abandonado — criterio que reaparecerá al elegir
  bibliotecas para las tareas y el proyecto.
- Ejemplos que suelen aparecer: pygbif (biodiversidad, ya usado en el
  curso), rasterstats, osmnx, earthengine-api, xarray.

## Ejercicio 4 (instalación de Miniconda y del ambiente)

- Operativo; los pasos y los errores esperables están en la guía de
  Miniconda. Verificaciones: `conda env list` muestra `geopython` (y
  `base`); `python --version` con el ambiente activado reporta
  Python 3.14.6 (la versión fijada en environment.yml).
- Errores esperables: ejecutar `conda` en CMD/PowerShell en vez de
  Anaconda Prompt (comando no reconocido); ejecutar `conda env create`
  fuera de la carpeta donde está environment.yml (archivo no
  encontrado); ejecutar `python --version` sin activar el ambiente
  (reporta otra versión o falla).

## Ejercicio 5 (cuaderno local en VS Code)

- Operativo. El kernel debe ser `geopython`; al ejecutar la primera
  celda, VS Code puede pedir instalar el paquete ipykernel — aceptar.
- Salidas esperadas: `Hola mundo` y la versión de Python (3.14.6, con
  detalles de compilación), igual a la del ejercicio 4 porque es el
  mismo ambiente.
- Errores esperables: no ver `geopython` en la lista de kernels (falta
  la extensión de Python/Jupyter o hay que refrescar con el comando
  *Python: Select Interpreter*); guardar el archivo sin la extensión
  `.ipynb`.
