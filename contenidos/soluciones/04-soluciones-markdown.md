# Soluciones — El lenguaje de marcado Markdown

Soluciones y pautas de respuesta de los ejercicios de la lección [El lenguaje de marcado Markdown](../i-introduccion-ciencia-datos-programacion/04-markdown.md). Los ejercicios son operativos o de redacción libre; en estos casos se describen los elementos que debe incluir una buena respuesta y los errores esperables.

## Ejercicio 1 (fuente de una celda de texto en Colab)

Operativo. Elementos de una buena respuesta:

- Al hacer doble clic, Colab muestra la fuente Markdown en un panel de
  edición con vista previa al lado: la correspondencia marca→salida se
  ve en vivo.
- Se espera que identifiquen `#` (título), `-` (lista) y el texto plano
  de las celdas del ejercicio de la lección 3.
- La marca nueva se renderiza al salir de la celda (clic fuera o
  `Shift + Enter`). Error esperable: agregar la marca pero quedarse en
  el modo de edición y pensar que "no funcionó".

## Ejercicio 2 (documento en VS Code con vista previa)

Sin solución única; lista de verificación para revisar:

- Archivo con extensión `.md` (sin ella no hay vista previa ni
  resaltado; error esperable más común).
- Título `#` + al menos dos `##`; negritas/itálicas; lista; enlace
  `[texto](URL)`; imagen remota `![alt](URL)` (recordar el texto
  alternativo); tabla con `|` y línea de guiones; bloque de código con
  ```` ```python ````.
- `Ctrl + K V` abre la vista previa lado a lado (requiere las
  extensiones de la guía de VS Code).
- Errores esperables: olvidar la línea en blanco antes de una lista o
  tabla (queda pegada al párrafo anterior); olvidar la fila de guiones
  de la tabla (no se renderiza como tabla); espacios de más en las
  barras verticales (inofensivos: conviene mostrarlo).
- Vale la pena revisar que el tema elegido apunte al proyecto: este
  documento se reutiliza en los ejercicios de la lección de Git/GitHub
  (será el README o primera página del repositorio de práctica).

## Ejercicio 3 (notación matemática y superíndice)

Ejemplo de respuesta con valores reales (cantón de San José, 2022:
población ≈ 352 381, área ≈ 44.6 km²):

```md
La densidad de población del cantón de San José es:

$$d = \frac{352381}{44.6} \approx 7901 \text{ hab/km}^2$$

La extensión de Costa Rica es de 51 100 km<sup>2</sup>.
```

- Basta cualquier fórmula geográfica coherente con valores reales
  citables (densidad, tasa de crecimiento, pendiente); lo evaluable es
  el uso correcto de `$$…$$` y de `<sup>…</sup>`.
- Errores esperables: usar `^2` esperando superíndice fuera de la
  notación matemática (no es sintaxis de Markdown; dentro de `$…$` sí
  funciona), y olvidar cerrar el segundo `$$`.
