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
5. `## Ejercicios` — en los capítulos prácticos (típicamente notebooks).
6. `## Referencias bibliográficas` — en formato APA, al final.

Las secciones 2, 5 y 6 pueden omitirse solo cuando no aplican (ej. un
capítulo introductorio sin trabajo previo). Las tablas y figuras se numeran
consecutivamente dentro de cada capítulo (`Tabla 1`, `Figura 1`, …) y llevan
leyenda con la fuente. Las tablas en HTML se envuelven en `<figure>` con la
leyenda en `<figcaption>` antes del `<table>` — **no** usar `<caption>`
dentro de la tabla, porque MyST lo descarta y la leyenda no aparece en el
sitio:

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

### Gráficos interactivos y mapas en notebooks

El sitio se publica como HTML estático, por lo que las salidas basadas en
JavaScript requieren patrones específicos (verificados en el sitio de
TPB-708 2026-I, que usa el mismo tema `book-theme`):

- **Plotly**: no usar `fig.show()`, que no se renderiza en el sitio. Cada
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
- **Folium**: no requiere tratamiento especial. Una celda que termina en el
  objeto del mapa (`m`) guarda la salida como `text/html` (un *iframe*
  autocontenido) que el sitio muestra correctamente.
- **Leafmap** (y otros basados en *widgets* de Jupyter, como ipyleaflet):
  sus salidas **no** se publican en el sitio. Después de cada celda de
  código se agrega una captura de pantalla PNG en un bloque `<figure>`
  numerado como el resto de las figuras del capítulo, con la imagen en el
  subdirectorio `img/` de la sección.

## Qué no se versiona

- El directorio `privado/` (calificaciones, documentos administrativos
  recibidos) está excluido mediante `.gitignore` y nunca debe publicarse.
- `programa/referencia.docx` se deriva de la plantilla interna de la Escuela
  de Geografía y se regenera localmente; tampoco se versiona.
- Antes de agregar archivos nuevos, verificar que no contengan datos
  personales de estudiantes ni documentos internos de la Escuela.
