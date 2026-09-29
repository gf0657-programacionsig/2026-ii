# Tarea 2

La segunda tarea del curso es un ejercicio **individual**, con un valor del **15 %** de la calificación final, según lo establecido en el [programa del curso](../../programa/programa.md). Su propósito es procesar con pandas los datos del tema elegido en la tarea 1 y presentar los resultados en tablas y gráficos, en un cuaderno de notas de Jupyter publicado en Internet. El cuaderno puede desarrollarse en **Google Colab** o **localmente**, en VS Code o en Jupyter con el ambiente conda del curso; en ambos casos se entrega en un repositorio de GitHub.

## Fecha y hora límite de entrega

Viernes 16 de octubre de 2026, 11:59 p.m.

## Objetivos

Cada estudiante debe mostrar que es capaz de:

1. Cargar, explorar, transformar y resumir datos tabulares con la biblioteca **pandas**.
2. Elaborar gráficos con la biblioteca **matplotlib** (o con **plotly**), adecuados a la pregunta que responden y con título, etiquetas y unidades.
3. Presentar un análisis de datos en un cuaderno de notas (*notebook*) de Jupyter, con texto interpretativo y referencias.
4. Publicar el cuaderno en un repositorio de GitHub.

## Entregables

1. Dirección de un repositorio en GitHub (ej. `https://github.com/usuario/tarea-02`) que contenga:
    - El cuaderno de notas, un archivo `.ipynb` **ejecutado**, es decir, con las salidas de todas las celdas (tablas y gráficos) guardadas, de modo que GitHub lo muestre completo sin necesidad de ejecutarlo. Si trabaja en Colab, el menú *Archivo > Guardar una copia en GitHub* lo sube al repositorio; si trabaja localmente, súbalo como cualquier otro archivo.
    - Los archivos de datos (CSV, Excel u otros) que el cuaderno carga, en el mismo repositorio, salvo que se carguen directamente desde una URL de la fuente original.
    - Un archivo `README.md` breve con el título del trabajo, el nombre del autor y un enlace al cuaderno.
2. La dirección que abre el cuaderno en Google Colab. Es **opcional si los gráficos son de matplotlib** y **obligatoria si son de plotly**: el visor de cuadernos de GitHub no ejecuta JavaScript y no muestra los gráficos de plotly, por lo que solo en Colab pueden revisarse. Tanto si trabajó en Colab como localmente, la forma más simple es la dirección `https://colab.research.google.com/github/usuario/tarea-02/blob/main/cuaderno.ipynb`, que abre en Colab el archivo del repositorio, sin copiarlo ni compartirlo. También puede compartir el cuaderno desde Colab (menú *Compartir*, con acceso para cualquier persona con el enlace).

La entrega debe realizarse a través de la plataforma Mediación Virtual. El cuaderno debe cargar los datos desde una **URL** (la del archivo en el repositorio, con el botón *Raw* de GitHub, o la de la fuente original), no desde una ruta local de su computadora, para que pueda ejecutarse en cualquier lugar.

## Consideraciones adicionales

**Esta tarea es estrictamente individual**.

Puede usar asistentes de inteligencia artificial para explicar, depurar, generar y verificar código, según los [lineamientos del curso](../i-introduccion-ciencia-datos-programacion/07-asistentes-ia.md): debe **declarar su uso** en una sección del cuaderno (cuál herramienta, con qué propósito y en cuáles partes), comprender y ser capaz de explicar todo el código que entregue, y verificar los resultados. El profesor puede pedirle en clase que explique cualquier parte de su cuaderno.

## Desarrollo

A partir de los datos del tema elegido en la tarea 1 (u otros, si aquellos resultaron inadecuados; en ese caso, descríbalos en la introducción), desarrolle un cuaderno de notas con la estructura de un análisis de datos presentada en la parte III de la serie *pandas*, con, como mínimo, los siguientes elementos:

- **Título e introducción**: el tema, las preguntas que se responden (al menos tres), la fuente de los datos, con su cita bibliográfica y su enlace, y una descripción de las variables principales. Puede reutilizar texto de la tarea 1.
- **Carga y preparación de los datos** con pandas: lectura desde una URL, exploración inicial (dimensiones, tipos de datos, primeras filas) y las transformaciones que el análisis requiera (filtros, columnas nuevas, limpieza de valores faltantes, uniones). Cada transformación se explica brevemente en una celda de texto.
- **Al menos una tabla** con formato para presentar, que resuma los datos mediante agrupación (`groupby()`), filtrado o estadísticas descriptivas, acompañada de un párrafo que diga qué muestra.
- **Al menos tres gráficos**, cada uno con:
    - Un **tipo adecuado** a la pregunta que responde (barras, líneas, histograma, dispersión u otro), según la tabla de la parte III de la serie *pandas*. Los tres deben ser de tipos distintos.
    - **Título** descriptivo, **etiquetas** de los ejes con **unidades** y, si hay más de una serie, leyenda.
    - Un párrafo de **interpretación**: qué muestra el gráfico y qué se observa en los datos.
- **Conclusiones**: las respuestas a las preguntas de la introducción y sus limitaciones.
- **Referencias bibliográficas** en formato APA, con las fuentes de los datos y cualquier otra fuente consultada.
- **Declaración de uso de asistentes de IA**, o la indicación de que no se usaron.

El cuaderno debe ser **coherente** y estar **bien presentado**: celdas de texto con encabezados que organicen el documento, código comentado y salidas legibles (sin tablas de cientos de filas ni mensajes de error).

## Calificación

Entre paréntesis, se muestra el porcentaje correspondiente a cada aspecto que se calificará:

- (10 %) Coherencia y presentación general del cuaderno (estructura, encabezados, texto, código comentado).
- (10 %) Introducción: tema, preguntas, fuentes de los datos con sus citas y descripción de las variables.
- (20 %) Carga y preparación de los datos con pandas (lectura desde una URL, exploración y transformaciones explicadas).
- (10 %) Tabla de resumen con formato e interpretación.
- (40 %) Gráficos (tipo adecuado, corrección, título, etiquetas y unidades, interpretación).
- (5 %) Conclusiones y referencias bibliográficas.
- (5 %) Entrega correcta: repositorio con el cuaderno ejecutado y los datos accesibles, enlace a Colab cuando corresponda, y declaración de uso de IA.

## Recursos

Los contenidos evaluados en esta tarea se cubrieron en los siguientes cuadernos del sitio del curso:

- [pandas I: Series y DataFrames](../iii-analisis-visualizacion-datos/12-pandas-series-dataframes.ipynb)
- [pandas II: agrupación, uniones y datos faltantes](../iii-analisis-visualizacion-datos/13-pandas-agrupacion-uniones.ipynb)
- [pandas III: gráficos con matplotlib](../iii-analisis-visualizacion-datos/14-pandas-graficos-matplotlib.ipynb), que incluye la estructura de un cuaderno de análisis de datos, el modelo de esta tarea.

Para subir un archivo de datos a GitHub sin la línea de comandos: en el repositorio, botón *Add file > Upload files*, arrastre el archivo y confirme con *Commit changes*. Luego abra el archivo, haga clic en *Raw* y copie la dirección del navegador: esa es la URL que se pasa a `read_csv()`. El cuaderno `.ipynb` se sube de la misma forma; GitHub lo muestra con sus salidas.
