# Convenciones del repositorio

Este documento describe las convenciones de Git y de contenido usadas en
este repositorio. Además de mantener el orden del proyecto, sirve como
material de referencia para el curso.

## Mensajes de commit

- El título se redacta en **tercera persona del presente de indicativo**: el
  mensaje describe lo que el commit hace al aplicarse ("[este commit]
  corrige…").

  ```text
  Corrige posición del logo EG en el encabezado de la primera página
  Agrega la lección 3 sobre condicionales y ciclos
  Actualiza la bibliografía de la semana 10
  ```

- Título de unos 50 caracteres (máximo 72), sin punto final y específico
  sobre el cambio ("Actualiza fechas de exámenes cortos", no "Cambios").
- Cuerpo opcional, separado del título por una línea en blanco, que explica
  el **porqué** del cambio cuando no es obvio. El *qué* ya lo muestra el
  diff; el contexto y la motivación son lo que se pierde si no se escribe.
- Un cambio lógico por commit. Si el mensaje necesita la palabra "y" para
  describir dos cambios sin relación, probablemente son dos commits.
- Cuando un commit se elabora con asistencia de una herramienta de
  inteligencia artificial, se declara con un trailer al final del cuerpo,
  por ejemplo:

  ```text
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
  ```

## Flujo de trabajo

- La rama principal es `main` y siempre debe quedar en estado publicable.
- **Cambios sustantivos** (contenidos o evaluación del programa, lecciones
  nuevas del sitio web, cambios de estructura): rama propia + *pull request*.
  El nombre de la rama es corto y descriptivo, en minúsculas y con guiones:
  `programa-ajuste-evaluacion`, `sitio-leccion-01`.
- **Cambios triviales** (erratas, fechas, regeneración de archivos
  derivados): commit directo a `main`.

## Estructura de los capítulos del sitio web

Todos los capítulos (lecciones en `contenidos/`, tanto `.md` como `.ipynb`)
siguen la misma estructura de secciones, en este orden:

1. `# Título del capítulo`
2. `## Trabajo previo` — con subsecciones `### Lecturas` y, si aplica,
   `### Tutoriales` u otros recursos que deben revisarse antes de la clase.
3. `## Introducción` — presentación breve del tema y su motivación.
4. Secciones de contenido (`##`) propias del tema.
5. `## Resumen` — síntesis breve, típicamente en viñetas, de las ideas
   principales del capítulo.
6. `## Ejercicios` — con numeración continua y, cuando el capítulo lo
   amerite, subdividida en subsecciones espejo de las secciones de
   contenido (`### Datos`, `### Ciencia de datos`, …), con un destino
   `(ejercicios-x)=` sobre cada una. Cada sección de contenido cierra
   entonces con una línea `*Ejercicios de esta sección: [...](#ejercicios-x).*`,
   lo que permite intercalar teoría y práctica durante las clases sin
   alterar la estructura del capítulo. Los destinos `(x)=` son globales
   al proyecto: usar nombres únicos entre capítulos.
7. `## Referencias bibliográficas` — al final, según la sección
   [Referencias bibliográficas](#referencias-bibliográficas).

En los **cuadernos de notas** (`.ipynb`) los enlaces se escriben para que
funcionen también con el cuaderno abierto en Colab, donde MyST no
interviene: (1) los enlaces a otras páginas del sitio usan la URL
absoluta (`https://gf0657-programacionsig.github.io/2026-ii/<pagina>/`),
no rutas relativas; (2) los punteros a los ejercicios espejo van como
texto plano ("*Ejercicios de esta sección: …, en la sección de
ejercicios al final del cuaderno.*"), sin destinos `(x)=` ni enlaces
`#ancla` — los destinos de MyST no existen en Colab (el enlace queda
muerto y la línea `(x)=` se ve como texto suelto) y las anclas HTML
`<a id>` no sobreviven al build de MyST.

Las guías de la sección Software (`contenidos/software/`) son un género
distinto: instrucciones de instalación, configuración y acceso, con pasos
numerados cuando corresponda, sin la estructura completa de capítulos;
las lecciones remiten a ellas en lugar de repetir instrucciones.

Las entradas de la sección Evaluaciones (`contenidos/evaluaciones/`,
archivos `examen-corto-NN.md`, `tarea-NN.md`, `proyecto-final.md`) son
también un género propio: anuncian cada evaluación con un párrafo
introductorio (modalidad, valor porcentual y propósito, tomados del
programa del curso) y las secciones `## Fecha`, `## Temas a evaluar`
(lista de enlaces relativos a las lecciones) y, cuando aplique,
`## Preparación` u otras con las indicaciones propias de la evaluación.
Estas páginas son las que se enlazan desde Mediación Virtual.

### Soluciones a los ejercicios

Las soluciones se escriben junto con cada lección y se guardan en
`privado/soluciones-ejercicios/NN-<leccion>.md` (fuera del repositorio
público) hasta que pasa la clase correspondiente. Después de la clase, la
solución se publica en el apéndice "Soluciones a los ejercicios", al final
del sitio:

1. El archivo se mueve a `contenidos/soluciones/NN-soluciones-<leccion>.md`,
   sin el bloque de notas internas del encabezado. El infijo `soluciones-`
   evita que el *slug* de la página (MyST descarta el prefijo numérico)
   choque con el de la lección.
2. Se agrega la entrada en la parte "Soluciones a los ejercicios" del TOC
   en `myst.yml`, dentro del subgrupo de la sección del curso a la que
   pertenece la lección (los subgrupos repiten los títulos de las
   secciones: "I. Introducción…", "II. El lenguaje…"); si la lección
   inaugura una sección, se crea su subgrupo.
3. Al final del párrafo introductorio de la sección Ejercicios de la
   lección se agrega la oración "Las [soluciones de estos
   ejercicios](../soluciones/NN-soluciones-<leccion>.md) se publican
   después de la clase correspondiente." En los cuadernos de notas el
   enlace usa la URL absoluta del sitio, para que funcione también con el
   cuaderno abierto en Colab.

Las páginas de soluciones son un género propio, como las guías de
Software: título `Soluciones — <título de la lección>` (y, en el
*frontmatter*, `short_title: "<título de la lección>"`, que es lo que
muestra el menú lateral dentro de su subgrupo, sin el prefijo), un párrafo
introductorio que enlaza a la lección y una sección `## Ejercicio N` por
ejercicio, sin la estructura completa de capítulos ni numeración de tablas
y figuras. Para los ejercicios abiertos se describen los elementos de una
buena respuesta y los errores esperables, en lugar de una respuesta única.

El repositorio es público: este mecanismo controla la presentación en el
sitio web, no el secreto de las soluciones.

Las secciones 2, 5, 6 y 7 pueden omitirse solo cuando no aplican (ej. un
capítulo introductorio sin trabajo previo). Los nombres de las bibliotecas de
Python se escriben en minúsculas en la prosa (pandas, plotly, folium),
como en el programa del curso; los títulos de las obras citadas conservan
su forma original. Las **negritas** destacan cada concepto del capítulo
en su primera aparición y los términos clave del resumen; no se usan para
énfasis. Los **hipervínculos** amplían información en la primera mención:
Wikipedia en español para conceptos auxiliares que el capítulo menciona
pero no desarrolla, y el sitio oficial para herramientas, organizaciones
y estándares; los conceptos que el propio capítulo desarrolla no se
enlazan. Las tablas y figuras se numeran
consecutivamente dentro de cada capítulo (`Tabla 1`, `Figura 1`, …) y llevan
leyenda con la fuente. Las tablas en HTML se envuelven en `<figure>` con la
leyenda en `<figcaption>` antes del `<table>` — **no** usar `<caption>`
dentro de la tabla, porque MyST lo descarta y la leyenda no aparece en el
sitio:

Las celdas con valores numéricos llevan `class="align-right"`, definida
en la hoja de estilos del sitio (`estilos.css`).

```html
<figure style="text-align: center; margin: 20px 0;">
    <figcaption><strong>Tabla N</strong>. Descripción. Fuente: ...</figcaption>
    <table class="table table-bordered table-striped" style="margin: 0 auto;">
    ...
    </table>
</figure>
```

### Enlaces con DOI en las referencias

MyST detecta los DOI en los enlaces (tanto `doi.org` como URLs de editor
con `/doi/10.xxxx/...`) y genera automáticamente una sección "References"
en inglés, duplicando la sección propia de referencias. Para evitarlo, en
los enlaces Markdown de las referencias se codifica la barra del DOI como
`%2F` en el destino, manteniendo la URL normal como texto visible:

```markdown
[https://www.science.org/doi/10.1126/science.1213847](https://www.science.org/doi/10.1126%2Fscience.1213847)
```

Los enlaces en HTML (`<a href="...">`) no son procesados por MyST y no
necesitan este ajuste.

**Excepción**: cuando el destino es directamente `doi.org`, MyST genera la
sección "References" aunque la barra esté codificada como `%2F` e incluso
si el enlace está en HTML. En esos casos se usa la URL del artículo en el
sitio de la revista en lugar del DOI (verificado con la lección 07).

### Ejecución de notebooks

Los notebooks se publican con sus salidas guardadas (el sitio no los
ejecuta), por lo que antes de confirmarlos se ejecutan de punta a punta
con el ambiente conda del curso:

```bash
NUMEXPR_MAX_THREADS=16 jupyter nbconvert --to notebook --execute --inplace <archivo>.ipynb
```

La variable `NUMEXPR_MAX_THREADS` evita que NumExpr imprima mensajes
informativos en las salidas.

### Gráficos interactivos y mapas en notebooks

El sitio se publica como HTML estático, por lo que las salidas basadas en
JavaScript requieren patrones específicos (verificados en el sitio de
TPB-708 2026-I, que usa el mismo tema `book-theme`):

- **plotly**: no usar `fig.show()`, que no se renderiza en el sitio. Cada
  notebook define al inicio una función auxiliar y la usa en todo el
  capítulo:

  ```python
  from IPython.display import display

  def mostrar(fig):
      """Despliega un gráfico de plotly de forma compatible con book-theme."""
      display(fig)
  ```

  `display(fig)` produce una salida con el MIME
  `application/vnd.plotly.v1+json`, que el sitio, Jupyter y Colab
  renderizan de forma interactiva.
- **folium**: no requiere tratamiento especial. Una celda que termina en el
  objeto del mapa (`m`) guarda la salida como `text/html` (un *iframe*
  autocontenido) que el sitio muestra correctamente.
- **leafmap** (y otros basados en *widgets* de Jupyter, como ipyleaflet):
  sus salidas **no** se publican en el sitio. Después de cada celda de
  código se agrega una captura de pantalla PNG en un bloque `<figure>`
  numerado como el resto de las figuras del capítulo, con la imagen en el
  subdirectorio `img/` de la sección.

## Referencias bibliográficas

Todo el material del curso — capítulos del sitio web, pautas de tareas y
del proyecto, evaluaciones — usa el formato **APA 7** con el aparato en
español:

- Apellidos e iniciales de los autores ("Wickham, H."), no nombres
  completos.
- Conjunción «y» antes del último autor, no «&», y sin coma antes de la
  conjunción.
- «En» para capítulos o secciones de una obra mayor.
- Títulos con mayúscula solo en la primera palabra (y en nombres propios),
  en el idioma original de la obra.
- Ediciones en español: «(2.ª ed.)».
- Rangos de páginas con semiraya: «452–454», no «452-454».
- «Recuperado el [fecha]» únicamente en fuentes diseñadas para cambiar y
  sin edición ni versión (ej. sitios de documentación como los citados en
  el programa); las obras con edición, versión o fecha de publicación no
  llevan fecha de recuperación.
- Citas en el texto: «(Autor, año)» o «Autor (año)»; en las leyendas de
  tablas y figuras se usa la forma narrativa («Fuente: Autor (año)»).

Este mismo formato es el que se pide a los estudiantes en las tareas y en
el documento del proyecto final. La única excepción es el **programa
impreso del curso**, cuyo cronograma cita con nombres completos
("Charles Severance (2016, capítulos 1-3)") por requerimiento de la
plantilla oficial de la Escuela de Geografía.

## Marca del curso

El logo del curso es una **brújula** que enmarca una serpiente
caricaturesca enrollada en forma de 8 (con cruce del cuerpo, ojos y
lengua), en la paleta de Python: amarillo `#FFD43B` con contorno azul
profundo `#14324F` y aro azul `#3776AB`, sobre fondo claro. La
serpiente y la paleta identifican al lenguaje sin imitar el logo de la
Python Software Foundation, que es marca registrada. En `marca/` están la
variante **general** (`logo-general.svg/png`), sin año, que se usa como
avatar de la organización de GitHub y sirve para todas las ediciones, y
la **de edición** (`logo-2026-ii.svg/png`), con la banda del ciclo. El
sitio usa el logo horizontal (`logo.svg` y `logo-oscuro.svg` en la raíz,
configurados en `myst.yml` como `logo` y `logo_dark`) y el `favicon.ico`
(la S sola, generado de `marca/marca-favicon.svg`). Los logos de la UCR
y de la Escuela de Geografía de la portada (`img/`) provienen del
programa del curso.

## Qué no se versiona

- El directorio `privado/` (calificaciones, documentos administrativos
  recibidos) está excluido mediante `.gitignore` y nunca debe publicarse.
- `programa/referencia.docx` se deriva de la plantilla interna de la Escuela
  de Geografía y se regenera localmente; tampoco se versiona.
- Antes de agregar archivos nuevos, verificar que no contengan datos
  personales de estudiantes ni documentos internos de la Escuela.
