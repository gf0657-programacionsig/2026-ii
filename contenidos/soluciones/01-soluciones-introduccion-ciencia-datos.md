# Soluciones — Introducción a la ciencia de datos

Soluciones y pautas de respuesta de los ejercicios de la lección [Introducción a la ciencia de datos](../i-introduccion-ciencia-datos-programacion/01-introduccion-ciencia-datos.md). Varios de los ejercicios son abiertos y no tienen una única respuesta correcta; en esos casos se describen los elementos que debe incluir una buena respuesta.

## Ejercicio 1 (abierto — registro de GBIF)

No hay una única respuesta: cada estudiante elige especie y registro. Una buena respuesta debe incluir al menos cinco variables correctamente clasificadas **con justificación basada en los valores posibles** (no en los dígitos registrados). Variables típicas de una página de detalle de GBIF:

| Variable (campo GBIF) | Tipo esperado | Justificación breve |
|---|---|---|
| Nombre científico | Categórica nominal | Etiquetas sin orden |
| País / localidad | Categórica nominal | Etiquetas sin orden |
| Latitud y longitud decimales | Numéricas continuas | Cualquier valor en un rango; combinadas construyen una variable espacial de tipo punto (vale aceptar y discutir esa respuesta) |
| Incertidumbre de la coordenada (m) | Numérica continua | Medida; cualquier valor positivo |
| Altitud / profundidad | Numérica continua | Medida redondeada ≠ discreta |
| Número de individuos | Numérica discreta | Conteo; sin valores intermedios |
| Sexo | Categórica nominal | Categorías sin orden |
| Etapa de vida | Categórica (nominal u ordinal) | Aceptar ordinal si se argumenta juvenil < adulto |
| Tipo/base del registro | Categórica nominal | Categorías sin orden |
| Fecha del evento | Temporal | Punto en el tiempo; formato ISO 8601 |
| Categoría en la Lista Roja | Categórica ordinal | Orden creciente de riesgo (LC < NT < VU < EN < CR) |

La fecha del evento (`eventDate`) es una variable temporal, la tercera rama de la jerarquía de la figura 1.

**Valores faltantes**: casi cualquier registro tiene varios — típicamente altitud, sexo, número de individuos o localidad textual. Lo importante es identificarlos y notar que la ausencia no es un error de quien responde, sino una característica de los datos reales.

## Ejercicio 2 (conjunto de datos de Kaggle — sismos del USGS)

- El conjunto tiene 23 412 observaciones y 21 variables (según la versión publicada en Kaggle); cada observación es un sismo (u otro evento sísmico) significativo.
- Clasificación de las variables principales:

| Variable | Clasificación | Nota |
|---|---|---|
| Date, Time | Temporales | Fecha y hora separadas (en la lección se recomienda ISO 8601) |
| Latitude, Longitude | Numéricas continuas | Combinadas construyen la variable espacial de tipo punto |
| Depth, Magnitude | Numéricas continuas | Magnitud con decimales (ej. 6.5) |
| Type | Categórica nominal | Incluye Earthquake y Nuclear Explosion — sorprende y da pie a discusión |
| ID, Source, Status | Categóricas nominales | ID es número/código como etiqueta, igual que gbifID |
| *Seismic Stations* | Numéricas discretas | Conteos de estaciones |

- Tipo no representado: **ordinal** — no hay ninguna variable con categorías ordenadas. Notarlo es parte de la respuesta esperada: no todo conjunto de datos contiene todos los tipos. Propuestas de variable ordinal esperables: la escala de intensidad de Mercalli Modificada (I-XII) o el nivel de alerta del USGS (verde < amarillo < naranja < rojo). Error frecuente que conviene discutir: proponer una ordinal y clasificarla como nominal, ignorando el orden de sus categorías.
- El ejercicio adicional (otro conjunto de Kaggle) es abierto; se aplica el mismo criterio de los ejercicios 1 y 2: clasificación justificada por los valores posibles.

## Ejercicio 3 (cuaderno de procesos de ciencia de datos)

Las pautas de discusión de los ejercicios del cuaderno están en [Soluciones — Ejemplo de procesos de ciencia de datos](02-soluciones-ejemplo-procesos-ciencia-datos.md).

## Ejercicio 4 (abierto — espectro de reproducibilidad)

Respuesta personal; una buena respuesta debe:

1. Ubicar el trabajo en un punto concreto del espectro de la figura 3 (típicamente "solo publicación/documento", el extremo no reproducible).
2. Identificar qué faltaría para avanzar hacia la reproducibilidad completa, por ejemplo:
   - Disponibilidad de los **datos** en un repositorio o archivo público.
   - Disponibilidad del **código** (o del procedimiento convertido en código, si se hizo con pasos manuales en hoja de cálculo o SIG de escritorio).
   - **Documentación del ambiente**: versiones de software y bibliotecas (conectar con el `environment.yml` del curso).
   - **Enlace** entre documento, datos y código (repositorio Git).
3. Aplicar el criterio operativo: ¿podría otra persona regenerar los resultados sin ayuda del autor? Si la respuesta es no, el trabajo no es plenamente reproducible.

Conexión útil para la discusión: el propio sitio del curso es un ejemplo del extremo reproducible (código fuente, datos enlazados y ambiente documentado en un repositorio público).

## Ejercicio 5 (explorar el repositorio del curso)

- **environment.yml**: cualquier terna vale (ej. python=3.14.6, pandas=3.0.5, geopandas=1.1.4). Vale discutir por qué se fijan las versiones (reproducibilidad del ambiente).
- **Commit reciente**: abierto; el criterio es identificar archivo y mensaje. Los mensajes siguen la convención del repositorio (tercera persona, descriptivos) y algunos declaran asistencia de IA con un *trailer* — puede adelantar la discusión de la política de IA del curso (semana 2).
- **Fuente vs página**: diferencias esperables — sintaxis visible de Markdown (`#`, `[texto](url)`, `**negrita**`), la tabla 1 escrita en HTML, el diagrama mermaid como código; en el sitio todo aparece renderizado. Es la distinción texto plano → documento publicado de la subsección de documentación.
