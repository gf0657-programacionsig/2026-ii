# Tarea 3

La tercera tarea del curso es un ejercicio **individual**, con un valor del **15 %** de la calificación final, según lo establecido en el [programa del curso](../../programa/programa.md). Su propósito es incorporar datos geoespaciales al tema elegido en la tarea 1, procesarlos con geopandas y presentar los resultados en tablas, gráficos y mapas, en un cuaderno de notas de Jupyter publicado en Internet. Como en la tarea 2, el cuaderno puede desarrollarse en **Google Colab** o **localmente**, en VS Code o en Jupyter con el ambiente conda del curso; en ambos casos se entrega en un repositorio de GitHub.

Los mapas de esta tarea son el componente geoespacial de la aplicación web del proyecto final: conviene dejar el código de carga de las capas y de los mapas en funciones o celdas que puedan reutilizarse.

## Fecha y hora límite de entrega

Viernes 13 de noviembre de 2026, 11:59 p.m.

## Objetivos

Cada estudiante debe mostrar que es capaz de:

1. Cargar, explorar y reproyectar capas de datos vectoriales con la biblioteca **geopandas**, incluida la conversión de tablas con coordenadas en capas de puntos.
2. Relacionar capas mediante **operaciones espaciales** (unión espacial, zonas de influencia, recorte, agregación) en el sistema de referencia de coordenadas adecuado.
3. Elaborar **mapas estáticos** (geopandas y matplotlib) y **mapas web interactivos** (folium o leafmap) adecuados a la pregunta que responden, con leyenda y unidades.
4. Presentar el análisis en un cuaderno de notas (*notebook*) de Jupyter, con texto interpretativo y referencias, y publicarlo en un repositorio de GitHub.

## Entregables

El entregable es la dirección de un repositorio en GitHub (ej. `https://github.com/usuario/tarea-03`) que contenga:

- El cuaderno de notas, un archivo `.ipynb` **ejecutado**, es decir, con las salidas de todas las celdas (tablas, gráficos y mapas) guardadas. Si trabaja en Colab, el menú *Archivo > Guardar una copia en GitHub* lo sube al repositorio; si trabaja localmente, súbalo como cualquier otro archivo.
- Los archivos de datos que el cuaderno carga (capas en GeoPackage o GeoJSON, tablas en CSV u otros), en el mismo repositorio, salvo que se carguen directamente desde una URL de la fuente original o del repositorio del curso.
- Un archivo `README.md` breve con el título del trabajo, el nombre del autor y un enlace al cuaderno.

El visor de GitHub muestra los mapas estáticos, pero no los mapas web, porque no ejecuta JavaScript. Como con los gráficos de plotly de la tarea 2, el profesor abrirá y ejecutará el cuaderno en Colab, con la dirección `https://colab.research.google.com/github/usuario/tarea-03/blob/main/cuaderno.ipynb`. Compruebe antes de entregar que el cuaderno se ejecuta allí de principio a fin sin errores (en Colab, leafmap se instala con la celda de instalación del cuaderno del curso).

La entrega debe realizarse a través de la plataforma Mediación Virtual. El cuaderno debe cargar los datos desde una **URL** (la del archivo en el repositorio, con el botón *Raw* de GitHub, o la de la fuente original), no desde una ruta local de su computadora, para que pueda ejecutarse en cualquier lugar.

## Consideraciones adicionales

**Esta tarea es estrictamente individual**.

Puede usar asistentes de inteligencia artificial para explicar, depurar, generar y verificar código, según los [lineamientos del curso](../i-introduccion-ciencia-datos-programacion/07-asistentes-ia.md): debe **declarar su uso** en una sección del cuaderno (cuál herramienta, con qué propósito y en cuáles partes), comprender y ser capaz de explicar todo el código que entregue, y verificar los resultados. El profesor puede pedirle en clase que explique cualquier parte de su cuaderno.

## Desarrollo

A partir del tema de las tareas anteriores, desarrolle un cuaderno de notas con la estructura de un análisis de datos presentada en la parte III de la serie *pandas*, con, como mínimo, los siguientes elementos:

- **Título e introducción**: el tema, las preguntas que se responden (al menos tres, de las cuales al menos dos son preguntas geográficas: ¿dónde?, ¿cuántos hay en cada cantón o país?, ¿qué está cerca de qué?), las fuentes de los datos, con su cita bibliográfica y su enlace, y una descripción de las capas (tipo de geometría, SRC y variables principales). Puede reutilizar texto de las tareas anteriores.
- **Carga y preparación de las capas** con geopandas: al menos **dos capas vectoriales**, cargadas desde una URL. Una debe estar relacionada con el tema (una capa del SNIT, un GeoJSON, una tabla con coordenadas convertida con `points_from_xy()`, registros de GBIF, Natural Earth u otra fuente; vea la tabla 3 de la lección [Datos geoespaciales](../iv-procesamiento-datos-geoespaciales/16-datos-geoespaciales.md)); la otra puede ser una capa de referencia, como los cantones, las provincias o los aeródromos del IGN del [repositorio del curso](https://github.com/gf0657-programacionsig/2026-ii/tree/main/datos/ign) o los países de Natural Earth. Para cada capa, la exploración inicial (SRC, número de filas, tipos de geometría, primeras filas) y las transformaciones que el análisis requiera (reproyección, filtros, columnas nuevas, unión con una tabla de atributos como la de la tarea 2), explicadas brevemente en celdas de texto.
- **Al menos una operación espacial** entre las dos capas: una unión espacial (por ejemplo, para contar las entidades de una capa por cantón o por país), el vecino más cercano, una zona de influencia, un recorte o una agregación con `dissolve()`. En una celda de texto, indique qué pregunta responde y en qué SRC la realizó.
- **Al menos una tabla** con formato para presentar, derivada de la operación espacial o de los atributos de las capas (por ejemplo, el conteo por cantón, ordenado), acompañada de un párrafo que diga qué muestra.
- **Al menos un gráfico** (matplotlib o plotly) con un tipo adecuado a la pregunta que responde, título, etiquetas de los ejes con unidades y un párrafo de interpretación. Puede ser el gráfico de la tabla anterior.
- **Al menos dos mapas**, cada uno con un párrafo de interpretación (qué muestra y qué se observa en el territorio):
    - Un **mapa estático**, con geopandas y matplotlib: un mapa de coropletas de una variable (con escala de color o clasificación adecuada a su distribución y los polígonos sin datos en gris) o un mapa de puntos o líneas sobre una capa de referencia; con título, leyenda con unidades y sin ejes.
    - Un **mapa web interactivo**, con folium, leafmap o `explore()`: con un mapa base, al menos dos capas con nombre, el control de capas, etiquetas emergentes (*tooltip* o *popup*) con los atributos principales y, si colorea una variable, leyenda con título y unidades. Todas las capas deben estar en WGS84.
- **Conclusiones**: las respuestas a las preguntas de la introducción y sus limitaciones (por ejemplo, la escala de las capas o la cobertura de los datos).
- **Referencias bibliográficas** en formato APA, con las fuentes de los datos y cualquier otra fuente consultada.
- **Declaración de uso de asistentes de IA**, o la indicación de que no se usaron.

Opcionalmente, el cuaderno puede incorporar un **raster** (altitud, clima o una imagen de satélite) consultado en los puntos de interés o resumido por zona, como en el cuaderno de rasterio; no es obligatorio y no se califica aparte.

El cuaderno debe ser **coherente** y estar **bien presentado**: celdas de texto con encabezados que organicen el documento, código comentado y salidas legibles (sin tablas de cientos de filas ni mensajes de error).

## Calificación

Entre paréntesis, se muestra el porcentaje correspondiente a cada aspecto que se calificará:

- (10 %) Coherencia y presentación general del cuaderno (estructura, encabezados, texto, código comentado).
- (10 %) Introducción: tema, preguntas, fuentes de los datos con sus citas y descripción de las capas (geometría, SRC y variables).
- (15 %) Carga y preparación de las capas con geopandas (lectura desde una URL, exploración, reproyección y transformaciones explicadas).
- (15 %) Operación espacial (correcta, en el SRC adecuado, con la pregunta que responde explicada).
- (10 %) Tabla de resumen y gráfico, con formato e interpretación (5 % cada uno).
- (15 %) Mapa estático (tipo adecuado, corrección, escala de color, título, leyenda con unidades, interpretación).
- (15 %) Mapa web interactivo (mapa base, capas con nombre, control de capas, etiquetas emergentes, leyenda, interpretación).
- (5 %) Conclusiones y referencias bibliográficas.
- (5 %) Entrega correcta: repositorio con el cuaderno ejecutado y los datos accesibles, y declaración de uso de IA.

## Recursos

Los contenidos evaluados en esta tarea se cubrieron en las siguientes lecciones y cuadernos del sitio del curso:

- [Datos geoespaciales: modelos, formatos y sistemas de referencia de coordenadas](../iv-procesamiento-datos-geoespaciales/16-datos-geoespaciales.md), con la tabla de fuentes de datos geoespaciales abiertos.
- [geopandas I: datos vectoriales](../iv-procesamiento-datos-geoespaciales/17-geopandas-datos-vectoriales.ipynb): carga, SRC, unión con tablas, mapas estáticos de coropletas y `explore()`.
- [geopandas II: operaciones espaciales](../iv-procesamiento-datos-geoespaciales/18-geopandas-operaciones-espaciales.ipynb): predicados, unión espacial, vecino más cercano, zonas de influencia, agregación y recorte.
- [rasterio: datos raster](../iv-procesamiento-datos-geoespaciales/19-rasterio-datos-raster.ipynb), si incorpora un raster.
- [folium: mapas web interactivos](../iv-procesamiento-datos-geoespaciales/20-folium-mapas-web.ipynb) y [leafmap: análisis geoespacial y mapeo interactivo](../iv-procesamiento-datos-geoespaciales/21-leafmap-mapeo-interactivo.ipynb): mapas web con capas, control de capas, etiquetas emergentes y leyenda.

Los ejercicios finales de los cuadernos 17, 18, 20 y 21 (identificar una capa relacionada con el tema, relacionarla con otra y mostrarla en un mapa web) son el borrador natural de esta tarea.

Las capas del IGN del repositorio del curso (provincias, cantones y aeródromos, en EPSG:8908) se cargan directamente desde su URL, por ejemplo `https://raw.githubusercontent.com/gf0657-programacionsig/2026-ii/main/datos/ign/cantones.gpkg`. Para subir una capa propia a GitHub sin la línea de comandos: en el repositorio, botón *Add file > Upload files*, arrastre el archivo (GeoPackage, GeoJSON o CSV) y confirme con *Commit changes*. Luego abra el archivo, haga clic en *Raw* y copie la dirección del navegador: esa es la URL que se pasa a `read_file()` o a `read_csv()`.
