# Proyecto final

El proyecto final del curso es un trabajo **individual**, con un valor del **35 %** de la calificación final, según lo establecido en el [programa del curso](../../programa/programa.md). Su propósito es sintetizar los conocimientos y las habilidades aprendidos durante el curso mediante el desarrollo del tema elegido en la tarea 1 en tres productos: (1) una **aplicación web interactiva**, desarrollada en streamlit y publicada en Internet, con visualizaciones tabulares, gráficas y geoespaciales; (2) una **presentación oral** presencial de la aplicación y de los resultados; y (3) un **documento computacional** (cuaderno de notas de Jupyter), con estructura de artículo, que documente el proceso de desarrollo, los datos y los métodos utilizados y los principales hallazgos.

La aplicación reúne, con controles que los filtren, las tablas, los gráficos y los mapas construidos en las tareas 2 y 3: el código de carga de los datos, de los gráficos y de los mapas de esas tareas se reutiliza en funciones de la aplicación. A diferencia de las tareas, la aplicación se desarrolla **localmente**, en VS Code con el ambiente conda del curso, porque Google Colab no ejecuta aplicaciones de streamlit.

## Fechas y horas límite de entrega

| Componente | Valor en la calificación final | Fecha y hora límite |
|---|---|---|
| Aplicación web interactiva publicada en Internet | 20 % | Martes 24 de noviembre de 2026, 11:59 p.m. |
| Presentación oral presencial | 5 % | Martes 24 de noviembre de 2026, en la clase |
| Documento computacional (examen final en modalidad para la casa) | 10 % | Lunes 30 de noviembre de 2026, 11:59 p.m. |

## Objetivos

Cada estudiante debe mostrar que es capaz de:

1. Desarrollar una **aplicación web de ciencia de datos** con la biblioteca **streamlit**, que cargue datos en caché, los filtre mediante controles y los presente en indicadores, tablas, gráficos interactivos (plotly) y mapas web interactivos (folium, leafmap o `explore()` mediante streamlit-folium).
2. Organizar el código de una aplicación en un repositorio de GitHub, con sus dependencias declaradas, y **publicarla** en Streamlit Community Cloud.
3. **Comunicar oralmente** el tema, la aplicación y los hallazgos del proyecto, y responder preguntas sobre el código.
4. **Documentar** el proceso de desarrollo, los datos, los métodos y los hallazgos en un cuaderno de notas de Jupyter con estructura de artículo, con texto interpretativo y referencias en formato APA.

## Entregables

Las entregas se realizan a través de la plataforma Mediación Virtual, en la actividad correspondiente a cada componente.

**1. Aplicación web** (martes 24 de noviembre, el mismo día de la presentación). Dos direcciones:

- La de un repositorio **público** en GitHub (ej. `https://github.com/usuario/proyecto-final`) con, como mínimo, en la raíz:
    - `app.py`: la aplicación.
    - `requirements.txt`: las bibliotecas que la aplicación importa, una por línea, con la versión fijada con `==` (la del ambiente en que se probó, que muestra `conda list`). No incluye los módulos de la biblioteca estándar de Python.
    - `README.md`: el título del proyecto, el nombre del autor, una descripción breve, el enlace a la aplicación publicada y las fuentes de los datos.
    - `datos/`: opcional, solo si los datos no se cargan desde una URL externa (la de la fuente original, la del repositorio del curso o la de su propio repositorio de la tarea 3).
- La de la aplicación publicada en Streamlit Community Cloud (ej. `https://usuario-proyecto-final.streamlit.app`).

**2. Presentación oral** (martes 24 de noviembre, en clase). No requiere entregar archivos: se presenta la aplicación publicada, en vivo, desde el navegador. Puede apoyarse en unas pocas diapositivas, si lo desea.

**3. Documento computacional** (lunes 30 de noviembre). La dirección de un repositorio en GitHub (puede ser el mismo del proyecto) con el cuaderno de notas (`.ipynb`) **ejecutado**, con las salidas de todas las celdas guardadas, y los archivos de datos que carga, salvo que se carguen desde una URL. Como en las tareas 2 y 3, el profesor abrirá y ejecutará el cuaderno en Colab, con la dirección `https://colab.research.google.com/github/usuario/repositorio/blob/main/cuaderno.ipynb`; compruebe antes de entregar que se ejecuta allí de principio a fin sin errores.

## Consideraciones adicionales

**El proyecto es estrictamente individual** y se desarrolla sobre el **mismo tema y las mismas fuentes de datos** de las tareas 1, 2 y 3.

Puede usar asistentes de inteligencia artificial para explicar, depurar, generar y verificar código, según los [lineamientos del curso](../i-introduccion-ciencia-datos-programacion/07-asistentes-ia.md): debe **declarar su uso** (cuál herramienta, con qué propósito y en cuáles partes) en el `README.md` de la aplicación y en una sección del documento, comprender y ser capaz de explicar todo el código que entregue, y verificar los resultados. Durante la presentación oral, el profesor puede pedirle que explique cualquier parte de la aplicación. El uso no declarado de estas herramientas, o la incapacidad de explicar el trabajo propio, se considera una falta a la honestidad académica, según lo establecido en el programa del curso.

Streamlit Community Cloud duerme las aplicaciones sin visitas después de algunos días; antes de la presentación, abra la suya para despertarla. Si la publicación falla, el registro (*Manage app*) muestra la causa, que casi siempre es una biblioteca que falta en `requirements.txt`.

## Desarrollo

### Aplicación web interactiva

A partir de la aplicación de ejemplo del [cuaderno de streamlit](../v-desarrollo-aplicaciones-interactivas/22-streamlit-aplicaciones-web.ipynb) (`apps/07-app-proyecto.py`), desarrolle una aplicación de **una sola página** sobre su tema, con, como mínimo, los siguientes elementos:

- **Configuración y encabezado**: `st.set_page_config()` como primera llamada a streamlit, con el título de la pestaña del navegador y la disposición; un título, y un párrafo introductorio que diga de qué trata la aplicación, cuáles datos usa y cómo se usa.
- **Carga de los datos en caché**: todas las capas y tablas se cargan en funciones decoradas con `@st.cache_data`, desde una **URL** (la de la fuente original, la del repositorio del curso o la de su repositorio, con el botón *Raw* de GitHub) o desde archivos del repositorio con rutas **relativas** a `app.py`. Las capas que van a un mapa se reproyectan a WGS84.
- **Al menos dos controles** en la barra lateral (por ejemplo, una lista de selección de provincia o de categoría y un deslizador de un valor mínimo o de un rango de años) que filtren los datos con pandas. **Todos** los elementos de la página, no solo el mapa, deben responder a los mismos filtros, de modo que la tabla, el gráfico y el mapa muestren siempre la misma selección. Si ninguna fila cumple los filtros, la aplicación lo indica con un mensaje (`st.warning()`) en lugar de fallar.
- **Indicadores**: al menos dos `st.metric()` con cifras de resumen de la selección (conteo, suma, promedio) con sus unidades.
- **Una tabla** interactiva, con `st.dataframe()`, de los datos filtrados, sin la columna de geometría, con los nombres de las columnas y los formatos numéricos configurados con `column_config` y, opcionalmente, un `st.download_button()` para descargarla como CSV.
- **Al menos un gráfico de plotly**, con `st.plotly_chart()`, de un tipo adecuado a la pregunta que responde, con título, etiquetas de los ejes con unidades y que cambie con los filtros.
- **Un mapa web interactivo**, con `st_folium()` de streamlit-folium, construido con folium, leafmap o `explore()`: con un mapa base, al menos **dos capas con nombre** (la capa del tema y una de referencia, como en la tarea 3), el control de capas, etiquetas emergentes (*tooltip* o *popup*) con los atributos principales y, si colorea una variable, leyenda con título y unidades. El mapa se construye en una función con `@st.cache_resource`, cuyos argumentos son los valores de los controles de los que depende, y se dibuja una copia hecha con `copy.deepcopy()`, para que conserve la vista entre clics, como se explica en el cuaderno. Todas las capas en WGS84.
- **Disposición**: la página se organiza con columnas, pestañas (`st.tabs()`, una para la tabla, una para los gráficos y una para el mapa, por ejemplo) o secciones con encabezados; cada tabla, gráfico y mapa lleva título.
- **Fuentes**: al pie de la página, las fuentes de los datos con sus enlaces (`st.caption()` o `st.markdown()`).

Antes de entregar, compruebe que la aplicación corre con `streamlit run app.py` sin errores ni advertencias en la terminal, que `AppTest` no reporta excepciones y que la versión publicada en Community Cloud se ve y responde igual que la local. La aplicación debe ser **coherente** y estar **bien presentada**: textos sin errores ortográficos, cifras con formato y unidades, sin mensajes de depuración ni código obsoleto.

Opcionalmente, la aplicación puede incluir más controles, más gráficos, una capa raster o la interacción con los clics en el mapa, como en la aplicación de ejemplo; estos elementos no se califican aparte, pero mejoran la coherencia y la presentación.

### Presentación oral

Cada estudiante dispone de **15 minutos** para presentar y de **5 minutos** para responder preguntas del profesor y de sus compañeros. La presentación se hace con la aplicación publicada, abierta en el navegador, y cubre:

1. El **tema** y las preguntas que responde la aplicación, y las fuentes de los datos (2 minutos).
2. Una **demostración** de la aplicación: los controles, la tabla, el gráfico y el mapa, y cómo responden a los filtros (6-7 minutos).
3. Los **hallazgos principales**: qué muestran los datos sobre el tema (3 minutos).
4. El **proceso de desarrollo**: una decisión de diseño, un problema que tuvo que resolver y cómo usó los asistentes de IA, si los usó (3 minutos).

### Documento computacional

Un cuaderno de notas de Jupyter con la **estructura de un artículo**, que puede reutilizar y actualizar el texto, las tablas, los gráficos y los mapas de las tareas 2 y 3, con, como mínimo, las siguientes secciones:

- **Título, autor y resumen**: un párrafo con el tema, los datos, los métodos y los hallazgos principales.
- **Introducción**: el tema y su relevancia, las preguntas del proyecto, las fuentes de los datos con sus citas y una descripción de las tablas y capas (tipo de geometría, SRC y variables principales).
- **Datos y métodos**: la carga y la preparación de los datos con pandas y geopandas (desde una URL), las operaciones espaciales realizadas, con la pregunta que responde cada una y su SRC, y las bibliotecas usadas con sus versiones.
- **Resultados**: las tablas, los gráficos (matplotlib o plotly) y los mapas (estáticos y web) que responden a las preguntas, cada uno con un párrafo de interpretación.
- **La aplicación**: la dirección de la aplicación publicada y del repositorio, una descripción de su estructura (qué carga, qué controles tiene y qué muestra), una captura de pantalla, las decisiones de diseño y los problemas que encontró al desarrollarla y publicarla, y cómo los resolvió.
- **Conclusiones**: las respuestas a las preguntas del proyecto y las limitaciones de los datos y del análisis.
- **Informe de participación en las jornadas del Día del SIG** (jueves 19 de noviembre): las actividades en las que participó, qué aprendió y qué relación tienen con el tema del proyecto o con el curso.
- **Referencias bibliográficas** en formato APA, con las fuentes de los datos, la documentación de las bibliotecas y cualquier otra fuente consultada.
- **Declaración de uso de asistentes de IA**, o la indicación de que no se usaron.

El cuaderno debe ser **coherente** y estar **bien presentado**: celdas de texto con encabezados que organicen el documento, código comentado y salidas legibles (sin tablas de cientos de filas ni mensajes de error).

## Calificación

Cada componente se califica sobre 100 y pesa en la calificación final del curso según la tabla de la sección de fechas. Entre paréntesis, se muestra el porcentaje correspondiente a cada aspecto que se calificará.

**Aplicación web interactiva (20 % de la calificación final)**

- (10 %) Coherencia y presentación general de la aplicación (título, introducción, organización de la página, textos y cifras con formato y unidades).
- (15 %) Repositorio y publicación: `app.py`, `requirements.txt` completo y con versiones, `README.md` con el enlace, y la aplicación publicada y en funcionamiento en Streamlit Community Cloud.
- (10 %) Carga de los datos en funciones con caché, desde una URL o una ruta relativa, con las capas en WGS84.
- (15 %) Controles: al menos dos, que filtran correctamente **todos** los elementos de la página, con manejo de la selección vacía.
- (10 %) Indicadores y tabla (5 % cada uno), con formato y unidades y sin la columna de geometría.
- (15 %) Gráfico de plotly (tipo adecuado, título, etiquetas con unidades, respuesta a los filtros).
- (20 %) Mapa web interactivo (mapa base, dos capas con nombre, control de capas, etiquetas emergentes, leyenda, conservación de la vista entre clics, respuesta a los filtros).
- (5 %) Fuentes de los datos al pie de la aplicación y declaración de uso de IA en el `README.md`.

**Presentación oral (5 % de la calificación final)**

- (30 %) Claridad y estructura: tema, preguntas, fuentes y hallazgos presentados en orden y en el tiempo asignado.
- (40 %) Demostración de la aplicación publicada, en funcionamiento, con explicación de sus controles y visualizaciones.
- (30 %) Respuestas a las preguntas, incluidas las preguntas sobre el código de la aplicación.

**Documento computacional (10 % de la calificación final)**

- (10 %) Coherencia y presentación general del cuaderno (estructura de artículo, encabezados, texto, código comentado, salidas legibles).
- (15 %) Resumen e introducción: tema, preguntas, fuentes con sus citas y descripción de los datos.
- (15 %) Datos y métodos: carga y preparación explicadas, operaciones espaciales con su pregunta y su SRC.
- (25 %) Resultados: tablas, gráficos y mapas correctos y adecuados a las preguntas, con interpretación.
- (15 %) Sección de la aplicación: descripción, decisiones de diseño, problemas y soluciones, enlaces y captura.
- (10 %) Conclusiones e informe de participación en el Día del SIG (5 % cada uno).
- (10 %) Referencias bibliográficas en formato APA, declaración de uso de IA y entrega correcta (cuaderno ejecutado, datos accesibles, ejecución en Colab sin errores).

## Recursos

Los contenidos evaluados en el proyecto se cubrieron en las siguientes lecciones y cuadernos del sitio del curso:

- [streamlit: aplicaciones web de ciencia de datos](../v-desarrollo-aplicaciones-interactivas/22-streamlit-aplicaciones-web.ipynb): controles, caché, tablas, gráficos, mapas con streamlit-folium, la aplicación de ejemplo del proyecto (`apps/07-app-proyecto.py`), la publicación en Streamlit Community Cloud, la clínica de errores y el prompt para asistentes de IA. Los ejercicios 10 a 12 de ese cuaderno son la primera versión de la aplicación del proyecto.
- [folium: mapas web interactivos](../iv-procesamiento-datos-geoespaciales/20-folium-mapas-web.ipynb) y [leafmap: análisis geoespacial y mapeo interactivo](../iv-procesamiento-datos-geoespaciales/21-leafmap-mapeo-interactivo.ipynb): el mapa web de la aplicación.
- [geopandas I](../iv-procesamiento-datos-geoespaciales/17-geopandas-datos-vectoriales.ipynb) y [geopandas II](../iv-procesamiento-datos-geoespaciales/18-geopandas-operaciones-espaciales.ipynb): la carga de las capas y las operaciones espaciales.
- [pandas III: gráficos con matplotlib](../iii-analisis-visualizacion-datos/14-pandas-graficos-matplotlib.ipynb), con la estructura de un análisis de datos que sigue el documento, y [plotly: gráficos interactivos](../iii-analisis-visualizacion-datos/15-plotly-graficos-interactivos.ipynb), con los gráficos de la aplicación.
- La [documentación de streamlit](https://docs.streamlit.io/), la [referencia de la API](https://docs.streamlit.io/develop/api-reference) y la [guía de Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud).
