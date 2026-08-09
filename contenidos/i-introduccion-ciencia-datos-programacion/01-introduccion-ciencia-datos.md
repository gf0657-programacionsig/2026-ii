# Introducción a la ciencia de datos

## Trabajo previo

### Lecturas

Çetinkaya-Rundel, Mine, & Hardin, Johanna (2021). *Chapter 1: Hello data* en *Introduction to Modern Statistics* (1st ed.). OpenIntro, Inc. https://openintro-ims.netlify.app/data-hello
\
\
Wickham, Hadley; Çetinkaya-Rundel, Mine; & Grolemund, Garret (2023). *Introduction* en *R for Data Science: Import, Tidy, Transform, Visualize, and Model Data* (2nd ed.). O'Reilly Media. https://r4ds.hadley.nz/intro

## Introducción

Los científicos tratan de responder preguntas mediante métodos rigurosos y observaciones cuidadosas. Estas observaciones, recopiladas de notas de campo, encuestas y experimentos, entre otras fuentes, forman la columna vertebral de una investigación y se denominan datos (Çetinkaya-Rundel & Hardin, 2021).

La ciencia de datos es un campo multidisciplinario que estudia los datos para extraer información útil y ayudar a tomar decisiones. Combina conocimientos de matemáticas, estadística, inteligencia artificial e ingeniería de computación para analizar grandes cantidades de datos.

## Datos

En términos generales, los **datos** son representaciones simbólicas (numéricas, alfabéticas, visuales o de cualquier otro tipo) susceptibles de ser comunicadas, interpretadas y procesadas para generar información o conocimiento. La norma internacional ISO/IEC 2382 (Information technology - Vocabulary) describe los datos como *hechos relacionados con un objeto o evento, que pueden registrarse o transmitirse con fines de procesamiento* (ISO/IEC 2382, 2015). Por su parte, Beyer y Laney (2012) señalan que los datos son la *materia prima de la información y, en su conjunto, pueden constituir activos de gran valor para organizaciones y sistemas de conocimiento*. Los datos, por sí mismos, no siempre constituyen información, sino que adquieren sentido al ser analizados, contextualizados y combinados.

Por ejemplo, la tabla 1 muestra un conjunto de datos conformado por registros de presencia de la especie [*Bradypus variegatus*](https://es.wikipedia.org/wiki/Bradypus_variegatus) (perezoso de tres dedos).

<figure style="text-align: center; margin: 20px 0;">
    <table class="table table-bordered table-striped" style="margin: 0 auto;">
    <caption><strong>Tabla 1</strong>. Registros de presencia de <em>Bradypus variegatus</em>. Fuente: GBIF <a href="https://doi.org/10.15468/dl.8m47hn">(https://doi.org/10.15468/dl.8m47hn).</a></caption>
        <thead>
            <tr>
                <th>Tipo de registro</th>
                <th>País</th>
                <th>Localidad</th>
                <th>Longitud</th>
                <th>Latitud</th>
                <th>Fecha</th>
                <th>Observador</th>
            </tr>
        </thead>
        <tbody>
        <tr>
            <td>HUMAN_OBSERVATION</td>
            <td>VE</td>
            <td>Casa Maria und nähere Umgebung, Bejuma / Carabobo</td>
            <td class="align-right">-68.254486</td>
            <td class="align-right">10.282892</td>
            <td>2015-02-19T00:00</td>
            <td>881932368</td>
        </tr>
        <tr>
            <td>PRESERVED_SPECIMEN</td>
            <td>CO</td>
            <td>Unguia</td>
            <td class="align-right">-77.213341</td>
            <td class="align-right">8.097215</td>
            <td>1950</td>
            <td>P. Hershkovitz</td>
        </tr>
        <tr>
            <td>HUMAN_OBSERVATION</td>
            <td>CR</td>
            <td>La Selva Reserve</td>
            <td class="align-right">-84.003922</td>
            <td class="align-right">10.431209</td>
            <td>2019-03-24</td>
            <td>User 16594</td>
        </tr>
        <tr>
            <td>HUMAN_OBSERVATION</td>
            <td>CR</td>
            <td>Talamanca</td>
            <td class="align-right">-82.802523</td>
            <td class="align-right">9.669042</td>
            <td>2017-10-21</td>
            <td>User 5551</td>
        </tr>
        <tr>
            <td>HUMAN_OBSERVATION</td>
            <td>VE</td>
            <td>Casa Maria und nähere Umgebung, Bejuma / Carabobo</td>
            <td class="align-right">-68.254486</td>
            <td class="align-right">10.282892</td>
            <td>2013-04-22T00:00</td>
            <td>1665984680</td>
        </tr>
        <tr>
            <td>HUMAN_OBSERVATION</td>
            <td>CO</td>
            <td>Vereda Brasilar | Cerro Maco</td>
            <td class="align-right">-75.194920</td>
            <td class="align-right">9.885820</td>
            <td>2018-07-27</td>
            <td>User 12345</td>
        </tr>
        <tr>
            <td>HUMAN_OBSERVATION</td>
            <td>CR</td>
            <td>Manuel Antonio N.P.</td>
            <td class="align-right">-84.149261</td>
            <td class="align-right">9.415193</td>
            <td>2000-02-04</td>
            <td>Volunteer 1</td>
        </tr>
        <tr>
            <td>PRESERVED_SPECIMEN</td>
            <td>PA</td>
            <td>Pacific end of Panama Canal Zone, Canal Zone</td>
            <td class="align-right">-79.777222</td>
            <td class="align-right">9.133283</td>
            <td>1915-01-01/2020-01-01</td>
            <td>Scientist X</td>
        </tr>
        <tr>
            <td>HUMAN_OBSERVATION</td>
            <td>PA</td>
            <td>Almirante</td>
            <td class="align-right">-82.400000</td>
            <td class="align-right">9.300000</td>
            <td>1960-01-22</td>
            <td>Local Observer</td>
        </tr>
        <tr>
            <td>HUMAN_OBSERVATION</td>
            <td>PA</td>
            <td>Achiote Road</td>
            <td class="align-right">-79.990768</td>
            <td class="align-right">9.203782</td>
            <td>2009-01-11T00:00</td>
            <td>Research Team</td>
        </tr>
    </tbody>
    </table>
</figure>

El conjunto de datos de la tabla 1 consta de diez observaciones (filas) y siete variables (columnas).

### Observaciones y variables

La presentación y descripción efectivas de los datos constituyen el primer paso en un análisis (Çetinkaya-Rundel & Hardin, 2021). Una de las formas más comunes de representar datos es mediante tablas en las cuales cada fila es una **observación** y cada columna es una **variable**. Una observación corresponde a un elemento de datos que ha sido estudiado y cada variable a una característica de ese elemento. En la tabla 1, por ejemplo, cada observación corresponde a un registro de presencia de *Bradypus variegatus*, descrito por siete variables.

Como otro ejemplo, la tabla 2 muestra registros de presencia de varias especies, con un conjunto más amplio de tipos de variables.

<table border="0" cellspacing="10" class="dataframe">
  <style>
    .dataframe {
        border-spacing: 10px 10px;
    }
    .dataframe td, .dataframe th {
        padding-left: 5px;
        padding-right: 5px;
        padding-top: 2px;
        padding-bottom: 2px;
    }
  </style>
  <caption><strong>Tabla 2. Registros de presencia de especies.</strong></caption>
  <thead>
    <tr>
      <th>Nombre científico</th>
      <th>Longitud</th>
      <th>Latitud</th>
      <th>Fecha</th>
      <th>Sexo</th>
      <th>Edad (años)</th>
      <th>Peso (g)</th>
      <th>Longitud (cm)</th>
      <th>Estado de conservación</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Panthera onca</i></td>
      <td>-84.5678</td>
      <td>10.1234</td>
      <td>2024-05-12</td>
      <td>Macho</td>
      <td>5</td>
      <td>56700</td>
      <td>170</td>
      <td>Casi amenazada (NT)</td>
    </tr>
    <tr>
      <td><i>Ara macao</i></td>
      <td>-83.2345</td>
      <td>9.8765</td>
      <td>2024-06-18</td>
      <td>Hembra</td>
      <td>3</td>
      <td>1000</td>
      <td>85</td>
      <td>Preocupación menor (LC)</td>
    </tr>
    <tr>
      <td><i>Dendrobates auratus</i></td>
      <td>-82.1234</td>
      <td>8.5432</td>
      <td>2024-07-22</td>
      <td>Macho</td>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>Preocupación menor (LC)</td>
    </tr>
    <tr>
      <td><i>Cebus imitator</i></td>
      <td>-85.4321</td>
      <td>10.6543</td>
      <td>2024-08-30</td>
      <td>Hembra</td>
      <td>8</td>
      <td>3000</td>
      <td>45</td>
      <td>Vulnerable (VU)</td>
    </tr>
    <tr>
      <td><i>Iguana iguana</i></td>
      <td>-84.7890</td>
      <td>9.3456</td>
      <td>2024-09-15</td>
      <td>Macho</td>
      <td>4</td>
      <td>4000</td>
      <td>150</td>
      <td>Preocupación menor (LC)</td>
    </tr>
    <tr>
      <td><i>Basiliscus basiliscus</i></td>
      <td>-83.4567</td>
      <td>8.9876</td>
      <td>2024-10-05</td>
      <td>Hembra</td>
      <td>2</td>
      <td>200</td>
      <td>80</td>
      <td>Preocupación menor (LC)</td>
    </tr>
    <tr>
      <td><i>Ateles geoffroyi</i></td>
      <td>-84.1234</td>
      <td>10.2345</td>
      <td>2024-11-12</td>
      <td>Macho</td>
      <td>6</td>
      <td>7000</td>
      <td>50</td>
      <td>En peligro (EN)</td>
    </tr>
    <tr>
      <td><i>Boa imperator</i></td>
      <td>-82.3456</td>
      <td>9.8765</td>
      <td>2024-12-01</td>
      <td>Hembra</td>
      <td>10</td>
      <td>12000</td>
      <td>300</td>
      <td>Preocupación menor (LC)</td>
    </tr>
    <tr>
      <td><i>Sotalia fluviatilis</i></td>
      <td>-83.9876</td>
      <td>8.1234</td>
      <td>2024-12-20</td>
      <td>Macho</td>
      <td>12</td>
      <td>35000</td>
      <td>210</td>
      <td>En peligro (EN)</td>
    </tr>
    <tr>
      <td><i>Chelonia mydas</i></td>
      <td>-84.1234</td>
      <td>9.6543</td>
      <td>2025-01-05</td>
      <td>Hembra</td>
      <td>50</td>
      <td>150000</td>
      <td>120</td>
      <td>En peligro (EN)</td>
    </tr>
  </tbody>
</table>

### Tipos de variables

Las variables de los datos de la tabla 2 son de varios tipos, cuya jerarquía se muestra en la figura 1.

<figure style="text-align: center;">
  <img
    src="https://raw.githubusercontent.com/datos-geoespaciales-biodiversidad/python/refs/heads/main/img/tipos-variables-estadisticas.png"
    alt="Tipos de variables"
  >
  <figcaption><strong>Figura 1</strong>. Tipos de variables. Fuente: (Çetinkaya-Rundel & Hardin, 2021).</figcaption>
</figure>

#### Numéricas

Corresponden a números a los cuales se les pueden aplicar operaciones como suma, resta, multiplicación, división y otras similares. Las variables numéricas pueden ser discretas o continuas.

##### Discretas

Toman valores específicos que se pueden contar. La variable `edad`, en este caso, es discreta.

##### Continuas

Pueden tomar cualquier valor dentro de un intervalo o rango continuo. Estas variables se caracterizan por su capacidad para representar medidas precisas y pueden asumir un número infinito de valores, incluso dentro de un rango limitado (ej. entre 0 y 1). Las variables `peso` y `longitud` son continuas.

#### Categóricas

Las variables categóricas (también llamadas cualitativas), son aquellas que describen una característica o cualidad de una observación y pueden utilizarse para clasificar las observaciones en grupos o categorías. A diferencia de las variables numéricas, que expresan cantidades, las variables categóricas expresan atributos no numéricos. Las variables categóricas pueden ser nominales u ordinales.

##### Nominales

No existe un orden inherente o jerarquía entre las categorías. Las variables `nombre científico` y `sexo` son nominales.

##### Ordinales

Hay un orden o jerarquía clara entre las categorías, como en el caso de la variable `estado de conservación`.

## Ciencia de datos

Los datos, en su estado original, carecen de contexto e interpretación. La **ciencia de datos** es una disciplina que permite convertir datos sin procesar en comprensión y conocimiento. Combina estadística, matemáticas y programación de computadoras. A diferencia de otros enfoques de generación de conocimiento, la ciencia de datos intenta resolver problemas mediante el uso de grandes volúmenes de datos y de técnicas avanzadas de modelado, apoyándose fuertemente en la programación de computadoras y en el aprendizaje automático (*machine learning*). El surgimiento y la popularidad de la ciencia de datos están motivados por un incremento acelerado de la cantidad de datos existentes, así como por la disponibilidad de herramientas computacionales para procesarlos y analizarlos. Además, estos avances tecnológicos han sido apoyados por un cambio cultural propiciado por movimientos como el de ciencia abierta (*open science*), el cual promueve el acceso libre a la investigación científica, incluidas las publicaciones, los datos, las metodologías y el código fuente.

La figura 2 ilustra el ciclo de vida de un proyecto típico de ciencia de datos, el cual incluye los procesos de importar, ordenar, transformar, visualizar, modelar y comunicar. Todos se articulan mediante programación de computadoras.

<figure style="text-align: center;">
  <img
    src="https://raw.githubusercontent.com/datos-geoespaciales-biodiversidad/python/refs/heads/main/img/modelo-ciencia-datos.svg"
    alt="Procesos de ciencia de datos"
  >
  <figcaption><strong>Figura 2</strong>. Procesos de ciencia de datos. Fuente: (Wickham et al., 2023).</figcaption>
</figure>

**Importar** los datos generalmente implica leerlos de un archivo, una base de datos o una [interfaz de programación de aplicaciones (API)](https://es.wikipedia.org/wiki/API) y cargarlos en estructuras apropiadas para este propósito en un lenguaje de programación.

**Ordenar** o estructurar los datos significa colocarlos en estructuras rectangulares de filas y columnas, similares a tablas, de manera que cada fila sea una observación y cada columna una variable.

**Transformar** los datos incluye, entre otras operaciones, la generación de algún subconjunto de observaciones o variables del conjunto original, la creación de nuevas variables a partir de las ya existentes o el cálculo de estadísticas como conteos y promedios.

Una vez que los datos están bien estructurados y con las variables que se requieren para el análisis, se puede proceder a la generación de conocimiento mediante dos mecanismos: la visualización y la modelización. Ambos tienen fortalezas y debilidades y es común iterar varias veces entre uno y otro.

**Visualizar** los datos en tablas, gráficos, mapas u otros formatos permite encontrar patrones inesperados o formular nuevas preguntas. Una buena visualización también puede indicar si se están formulando preguntas equivocadas o utilizando datos que no son apropiados para el problema que se desea resolver. Es importante tener en cuenta que las visualizaciones deben ser interpretadas por seres humanos. Por este motivo, visualizaciones como gráficos estadísticos y mapas deben ser seleccionadas con cuidado y elaborarse detalladamente.

**Modelar** es crear una representación abstracta y estructurada de los datos, con el fin de facilitar su análisis y realizar predicciones. Al ser herramientas matemáticas o computacionales, los modelos muchas veces pueden mejorarse mediante el empleo de mayores capacidades de cómputo, lo que los hace menos dependientes de la intervención humana, como en el caso de las visualizaciones.

**Comunicar** es el último paso y es una actividad crítica de cualquier proyecto de análisis de datos o de ciencia en general. No importa lo bien que los modelos y visualizaciones ayuden a entender los datos si los resultados no pueden ser comunicados a otras personas.

Estos procesos se ilustran en un cuaderno de notas Jupyter con [ejemplos de procesamiento de datos de biodiversidad mediante ciencia de datos](https://colab.research.google.com/drive/1VMj1WfamqtJe6V9OAeDZ2BE2SdiEI6up?usp=sharing).

## Reproducibilidad

La **reproducibilidad** es la capacidad de un ensayo o experimento de ser reproducido por otros. Más formalmente, en investigación cuantitativa, un análisis se considera reproducible si *el código fuente y los datos utilizados por un investigador para llegar a un resultado están disponibles y son suficientes para que otro investigador, trabajando de manera independiente, pueda llegar al mismo resultado* (Gandrud, 2020).

El concepto de reproducibilidad es cada vez más importante debido, entre otras razones, al aumento exponencial de datos disponibles y a la aplicación de la programación de computadoras, para procesar estos datos, por parte de especialistas de muchas disciplinas. Sin embargo, en años recientes, se ha generado una creciente preocupación debido a que muchos estudios científicos publicados fallan las pruebas de reproducibilidad.

Singleton et al. (2016) han identificado los siguientes retos para la reproducibilidad en ciencia de datos geoespaciales:

1. Los datos deben ser de dominio público y estar disponibles para los investigadores.
2. El software utilizado debe ser de código abierto (*open source*) y estar disponible para ser revisado.
3. Siempre que sea posible, los [flujos de trabajo](https://es.wikipedia.org/wiki/Flujo_de_trabajo) deben ser públicos y con enlaces a los datos, software y métodos de análisis, junto con la documentación necesaria.
4. El proceso de [revisión por pares (*peer review process*)](https://es.wikipedia.org/wiki/Revisi%C3%B3n_por_pares) y la publicación académica deben requerir la presentación de un modelo de flujo de trabajo e idealmente la disponibilidad de los materiales necesarios para la replicación.
5. En los casos en los que la reproducibilidad total no sea posible (ej. datos sensibles), los investigadores deben esforzarse por incluir todos los aspectos que puedan de un marco de trabajo abierto.

En general, el estándar mínimo de reproducibilidad requiere que los datos y el código fuente estén disponibles para otros investigadores (Peng, 2011). Sin embargo, dependiendo de las circunstancias y recursos disponibles, existe todo un espectro de posibilidades, que se ilustra en la figura 3.

<figure style="text-align: center;">
  <img
    src="https://raw.githubusercontent.com/datos-geoespaciales-biodiversidad/python/refs/heads/main/img/espectro-reproducibilidad.png"
    alt="Espectro de reproducibilidad"
  >
  <figcaption><strong>Figura 3</strong>. Espectro de reproducibilidad. Fuente: <a href="https://www.youtube.com/watch?v=ZjXb53pOor0">Anita Graser</a> con base en (Peng, 2011).</figcaption>
</figure>

## Herramientas

La implementación de un proyecto de ciencia de datos requiere del uso de herramientas informáticas como lenguajes de programación, sintaxis y formatos para documentación y sistemas de control de versiones.

### Lenguajes de programación

Como se ha mencionado, la programación de computadoras es una actividad presente durante todos los procesos de ciencia de datos. Hay muchos lenguajes que pueden utilizarse en este campo. Entre los más populares, pueden mencionarse [Python](https://www.python.org/), [R](https://www.r-project.org/), [SQL](https://www.iso.org/standard/76583.html) y [JavaScript](https://ecma-international.org/publications-and-standards/standards/ecma-262/).

### Sintaxis y formatos para documentación

La documentación es vital durante todo el ciclo de vida de una investigación reproducible. Se recomienda utilizar mecanismos estandarizados y abiertos como el [lenguaje de marcado de hipertexto (HTML, en inglés, *HyperText Markup Language*)](https://es.wikipedia.org/wiki/HTML) o [Markdown](https://en.wikipedia.org/wiki/Markdown), con los cuales pueden crearse documentos mediante editores de texto simples (i.e. no se requiere de software propietario), y exportables a varios formatos (ej. [LaTeX](https://es.wikipedia.org/wiki/LaTeX), [PDF](https://es.wikipedia.org/wiki/PDF)).

### Sistemas de control de versiones

Para dar mantenimiento, tanto al código fuente como a la documentación, es necesario un sistema de [control de versiones](https://es.wikipedia.org/wiki/Control_de_versiones) como [Git](https://es.wikipedia.org/wiki/Git), el cual permite llevar el registro de los cambios en archivos y también facilita el trabajo colaborativo al reunir las modificaciones hechas por varias personas. Git es usado en varias plataformas que comparten código fuente (ej. [GitHub](https://github.com/), [GitLab](https://about.gitlab.com/)) y que ofrecen servicios relacionados, como hospedaje de sitios web.

## Referencias bibliográficas

Beyer, M. A. & Laney, D. (2012). *The Importance of 'Big Data': A Definition*. Gartner. https://www.gartner.com/doc/2057415
\
\
Çetinkaya-Rundel, Mine, & Hardin, Johanna (2021). *Chapter 1: Hello data* en *Introduction to Modern Statistics* (1st ed.). OpenIntro, Inc. https://openintro-ims.netlify.app/data-hello
\
\
Gandrud, C. (2020). *Reproducible research with R and RStudio* (3.a ed.). CRC Press.
\
\
ISO/IEC 2382. (2015). *Information Technology - Vocabulary*. International Organization for Standardization.
\
\
Peng, R. D. (2011). Reproducible research in computational science. *Science*, 334(6060), 1226-1227. https://doi.org/10.1126/science.1213847
\
\
Singleton, A. D., Spielman, S., & Brunsdon, C. (2016). Establishing a framework for Open Geographic Information science. *International Journal of Geographical Information Science*, 30(8), 1507–1521. https://doi.org/10.1080/13658816.2015.1137579
\
\
Wickham, Hadley; Çetinkaya-Rundel, Mine; & Grolemund, Garret (2023). *Introduction* en *R for Data Science: Import, Tidy, Transform, Visualize, and Model Data* (2nd ed.). O'Reilly Media. https://r4ds.hadley.nz/intro
