# Proyecto final: documento computacional

La segunda entrega del [proyecto final](proyecto-final.md) del curso es un trabajo **individual**, con un valor del **10 %** de la calificación final, que se presenta como examen final en modalidad "para la casa", según lo establecido en el [programa del curso](../../programa/programa.md). Consiste en un **documento computacional** (cuaderno de notas de Jupyter), con estructura de artículo, que documenta el proceso de desarrollo del proyecto, los datos y los métodos utilizados y los principales hallazgos. Se elabora después de la primera entrega, la [aplicación web y la presentación oral](proyecto-final-aplicacion.md), y dedica una de sus secciones a esa aplicación.

## Fecha y hora límite de entrega

Lunes 30 de noviembre de 2026, 11:59 p.m.

## Objetivos

Cada estudiante debe mostrar que es capaz de:

1. **Documentar** el proceso de desarrollo, los datos, los métodos y los hallazgos en un cuaderno de notas de Jupyter con estructura de artículo, con texto interpretativo y referencias en formato APA.

## Entregables

La entrega se realiza a través de la plataforma Mediación Virtual, en la actividad correspondiente.

La dirección de un repositorio en GitHub (puede ser el mismo del proyecto) con el cuaderno de notas (`.ipynb`) **ejecutado**, con las salidas de todas las celdas guardadas, y los archivos de datos que carga, salvo que se carguen desde una URL. Como en las tareas 2 y 3, el profesor abrirá y ejecutará el cuaderno en Colab, con la dirección `https://colab.research.google.com/github/usuario/repositorio/blob/main/cuaderno.ipynb`; compruebe antes de entregar que se ejecuta allí de principio a fin sin errores.

## Consideraciones adicionales

**El proyecto es estrictamente individual** y se desarrolla sobre el **mismo tema y las mismas fuentes de datos** de las tareas 1, 2 y 3.

Puede usar asistentes de inteligencia artificial para explicar, depurar, generar y verificar código, según los [lineamientos del curso](../i-introduccion-ciencia-datos-programacion/07-asistentes-ia.md): debe **declarar su uso** (cuál herramienta, con qué propósito y en cuáles partes) en una sección del documento, comprender y ser capaz de explicar todo el código que entregue, y verificar los resultados. El uso no declarado de estas herramientas, o la incapacidad de explicar el trabajo propio, se considera una falta a la honestidad académica, según lo establecido en el programa del curso.

## Desarrollo

Un cuaderno de notas de Jupyter con la **estructura de un artículo**, que puede reutilizar y actualizar el texto, las tablas, los gráficos y los mapas de las tareas 2 y 3, con, como mínimo, las siguientes secciones:

- **Título, autor y resumen**: un párrafo con el tema, los datos, los métodos y los hallazgos principales.
- **Introducción**: el tema y su relevancia, las preguntas del proyecto, las fuentes de los datos con sus citas y una descripción de las tablas y capas (tipo de geometría, SRC y variables principales).
- **Datos y métodos**: la carga y la preparación de los datos con pandas y geopandas (desde una URL), las operaciones espaciales realizadas, con la pregunta que responde cada una y su SRC, y las bibliotecas usadas con sus versiones.
- **Resultados**: las tablas, los gráficos (matplotlib o plotly) y los mapas (estáticos y web) que responden a las preguntas, cada uno con un párrafo de interpretación.
- **La aplicación**: la dirección de la aplicación publicada y del repositorio, una descripción de su estructura (qué carga, qué controles tiene y qué muestra), una captura de pantalla, las decisiones de diseño y los problemas que encontró al desarrollarla y publicarla, y cómo los resolvió.
- **Conclusiones**: las respuestas a las preguntas del proyecto y las limitaciones de los datos y del análisis.
- **Referencias bibliográficas** en formato APA, con las fuentes de los datos, la documentación de las bibliotecas y cualquier otra fuente consultada.
- **Declaración de uso de asistentes de IA**, o la indicación de que no se usaron.

El cuaderno debe ser **coherente** y estar **bien presentado**: celdas de texto con encabezados que organicen el documento, código comentado y salidas legibles (sin tablas de cientos de filas ni mensajes de error).

## Calificación

El documento se califica sobre 100. Entre paréntesis, se muestra el porcentaje correspondiente a cada aspecto que se calificará.

- (10 %) Coherencia y presentación general del cuaderno (estructura de artículo, encabezados, texto, código comentado, salidas legibles).
- (15 %) Resumen e introducción: tema, preguntas, fuentes con sus citas y descripción de los datos.
- (15 %) Datos y métodos: carga y preparación explicadas, operaciones espaciales con su pregunta y su SRC.
- (25 %) Resultados: tablas, gráficos y mapas correctos y adecuados a las preguntas, con interpretación.
- (15 %) Sección de la aplicación: descripción, decisiones de diseño, problemas y soluciones, enlaces y captura.
- (10 %) Conclusiones: respuestas a las preguntas del proyecto y limitaciones de los datos y del análisis.
- (10 %) Referencias bibliográficas en formato APA, declaración de uso de IA y entrega correcta (cuaderno ejecutado, datos accesibles, ejecución en Colab sin errores).

## Recursos

Los contenidos evaluados en esta entrega se cubrieron en las siguientes lecciones y cuadernos del sitio del curso:

- [pandas III: gráficos con matplotlib](../iii-analisis-visualizacion-datos/14-pandas-graficos-matplotlib.ipynb), con la estructura de un análisis de datos que sigue el documento, y [plotly: gráficos interactivos](../iii-analisis-visualizacion-datos/15-plotly-graficos-interactivos.ipynb).
- [geopandas I](../iv-procesamiento-datos-geoespaciales/17-geopandas-datos-vectoriales.ipynb) y [geopandas II](../iv-procesamiento-datos-geoespaciales/18-geopandas-operaciones-espaciales.ipynb): la carga de las capas y las operaciones espaciales.
- [folium: mapas web interactivos](../iv-procesamiento-datos-geoespaciales/20-folium-mapas-web.ipynb) y [leafmap: análisis geoespacial y mapeo interactivo](../iv-procesamiento-datos-geoespaciales/21-leafmap-mapeo-interactivo.ipynb): los mapas web del documento.
- [Herramientas agénticas de inteligencia artificial para programación](../v-desarrollo-aplicaciones-interactivas/23-herramientas-agenticas-ia.md): la declaración de uso de asistentes de IA.
- Los enunciados de la [tarea 2](tarea-02.md) y de la [tarea 3](tarea-03.md), cuyos productos se reutilizan y actualizan en el documento.
