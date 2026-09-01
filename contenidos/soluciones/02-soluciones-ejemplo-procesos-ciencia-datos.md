---
short_title: "Ejemplo de procesos de ciencia de datos"
---

# Soluciones — Ejemplo de procesos de ciencia de datos

Soluciones y pautas de respuesta de los ejercicios del cuaderno de notas [Ejemplo de procesos de ciencia de datos](../i-introduccion-ciencia-datos-programacion/02-ejemplo-procesos-ciencia-datos.ipynb). Los ejercicios son operativos o abiertos; en cada caso se indican el criterio de éxito y los puntos de discusión.

## Ejercicio 1 (copia propia en Colab)

Operativo; el criterio de éxito es que cada estudiante tenga su copia en Drive y la ejecute completa sin errores. Problemas típicos: ejecutar sobre el cuaderno abierto desde GitHub sin guardar copia (los cambios se pierden) y no esperar a que la instalación de pygbif termine antes de ejecutar la celda de carga.

## Ejercicio 2 (cambiar la especie)

Abierto; el criterio de éxito es que el cuaderno completo vuelva a ejecutarse sin errores con la especie nueva y que las visualizaciones tengan sentido. Puntos de discusión:

- Si se elige una especie con muchísimos registros (ej. *Pharomachrus mocinno*, ~54 000) la descarga tarda varios minutos y el mapa se vuelve lento o inutilizable: oportunidad de discutir volumen de datos y muestreo. Conviene revisar el conteo en gbif.org antes.
- Si el nombre científico está mal escrito o es ambiguo, GBIF puede devolver 0 registros o registros de un taxón inesperado: oportunidad de discutir la importancia de los identificadores taxonómicos.
- El centro y el zoom del mapa (`location`, `zoom_start`) están fijados para la lapa verde; con especies de otra distribución conviene ajustarlos — quien lo note está leyendo el código, no solo ejecutándolo.

## Ejercicio 3 (cambiar el año inicial)

- Con un año más reciente (ej. 2020) la cantidad baja y el gráfico de líneas se acorta; con un año muy antiguo (ej. 1900) casi no cambia respecto a no filtrar, porque la gran mayoría de los registros son recientes (sesgo temporal de los datos de ciencia ciudadana — punto valioso de discusión).
- El conteo posterior al filtro siempre es ≤ al de la importación; si a alguien le da igual, probablemente no re-ejecutó las celdas en orden: oportunidad de discutir el estado del kernel y el orden de ejecución.

## Ejercicio 4 (agregar `elevation` a la muestra)

- Basta agregar `'elevation'` a la lista de columnas de la celda de la muestra en la sección de estructuración.
- En la muestra de 10 filas (con `random_state=42`), la mayoría de los valores de `elevation` aparecen como `NaN`: es la manifestación concreta de los valores faltantes vistos en la lección (la proporción exacta depende de la fecha de consulta de los datos).
- ¿Por qué `NaN` y no una celda vacía? Es la representación de pandas para los valores faltantes numéricos — puente hacia la unidad de Python/pandas.
