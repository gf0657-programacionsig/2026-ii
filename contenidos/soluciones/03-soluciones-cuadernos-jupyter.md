# Soluciones — Cuadernos de notas Jupyter

Soluciones y pautas de respuesta de los ejercicios de la lección [Cuadernos de notas Jupyter](../i-introduccion-ciencia-datos-programacion/03-cuadernos-jupyter.md).

## Ejercicio 1 (cuaderno mínimo con ambos tipos de celda)

Operativo y autocontenido: el texto y el código se copian tal cual (la sintaxis de Markdown y de Python aún no se ha estudiado; el objetivo es el manejo del cuaderno). Salida esperada: `168`. Error típico: pegar el Markdown en una celda de código (error de sintaxis de Python) — oportunidad para reforzar la diferencia entre tipos de celda.

## Ejercicio 2 (estado del kernel)

- Salidas esperadas: `NameError` primero y `10080` al final; nótese que `minutos = horas * 60` reutiliza la variable `horas` del ejercicio 1 (estado compartido entre celdas).
- El primer paso produce `NameError`; tras definir la variable y re-ejecutar, funciona aunque la definición esté después en el documento: el estado depende del orden de ejecución.
- Los números entre corchetes lo delatan (la celda de arriba tiene un número mayor que la de abajo).
- La explicación esperada en la celda de texto: el kernel conserva las variables en memoria en el orden en que se ejecutaron las celdas, no en el orden del documento.

## Ejercicio 3 (reiniciar y ejecutar todo)

- Con el cuaderno en desorden, *Reiniciar y ejecutar todo* falla en la celda que usa la variable antes de definirla: es la prueba de reproducibilidad fallando.
- La solución esperada es mover la definición antes del uso (o corregir el código). Conexión con la práctica del curso: los cuadernos publicados se ejecutan completos antes de confirmarse.

## Ejercicio 4 (el archivo .ipynb por dentro)

- En el JSON: `"cell_type": "markdown"` y `"cell_type": "code"`, la fuente en `"source"` y las salidas en `"outputs"` (con `"execution_count"` para el orden).
- Conexión con el ejercicio 5 de la lección [Introducción a la ciencia de datos](../i-introduccion-ciencia-datos-programacion/01-introduccion-ciencia-datos.md) (fuente vs. página renderizada) y con el control de versiones: el `.ipynb` es texto y por eso Git puede versionarlo.
