# Git, GitHub y GitHub Pages

## Trabajo previo

### Lecturas

Antes de la clase, revise las siguientes lecturas, ambas en inglés. La primera es un tutorial que recorre los conceptos y comandos básicos de Git y su relación con GitHub; la segunda explica cómo publicar una página web con GitHub Pages. Además, [cree una cuenta gratuita en GitHub](https://github.com/signup) antes de la clase; elija el nombre de usuario con cuidado, pues identificará sus trabajos durante el curso.

Abba, I. V. (2021). *Git and GitHub tutorial – Version control for beginners*. freeCodeCamp. https://www.freecodecamp.org/news/git-and-github-for-beginners/
\
\
GitHub. (s. f.-b). *Quickstart for GitHub Pages*. GitHub Docs. Recuperado el 11 de agosto de 2026, de https://docs.github.com/en/pages/quickstart

## Introducción

En la lección de [introducción a la ciencia de datos](01-introduccion-ciencia-datos.md), los sistemas de control de versiones se presentaron entre las herramientas que hacen posible la reproducibilidad. Este capítulo los estudia con detalle: qué es el control de versiones, cómo funciona Git, qué agrega GitHub y cómo se publica una página web con GitHub Pages. Son herramientas de uso constante en el curso: las tareas y el proyecto final se desarrollan en repositorios de GitHub, y este mismo sitio web se publica con GitHub Pages. Al final del capítulo, el documento Markdown elaborado en los ejercicios de la [lección anterior](04-markdown.md) se convertirá en una página web publicada en Internet.

## Control de versiones

Un sistema de **control de versiones** registra la historia de los cambios de un conjunto de archivos, de manera que sea posible consultar quién cambió qué y cuándo, comparar versiones y recuperar cualquier estado anterior (Chacon y Straub, 2014). Resuelve un problema que cualquiera ha enfrentado: sin control de versiones, la historia de un documento termina dispersa en copias como `informe.docx`, `informe-final.docx` e `informe-final-v2-DEFINITIVO.docx`, sin registro de qué cambió entre una y otra.

Además de ordenar la historia, el control de versiones facilita la **colaboración**: varias personas pueden modificar los mismos archivos y el sistema se encarga de reunir sus cambios y de señalar los conflictos. Para la ciencia de datos tiene un valor adicional, ligado a la reproducibilidad: el historial documenta la procedencia del código y de los datos de un análisis, y permite examinar y reproducir cualquiera de sus versiones, no solo la más reciente.

*Ejercicios de esta sección: [ejercicios sobre GitHub](#ejercicios-github).*

## Git

**Git** es un sistema de control de versiones **distribuido**: cada copia de un proyecto contiene su historial completo, sin depender de un servidor central. Fue creado en 2005 por [Linus Torvalds](https://es.wikipedia.org/wiki/Linus_Torvalds) para gestionar el desarrollo del núcleo del sistema operativo [Linux](https://es.wikipedia.org/wiki/Linux) y hoy es el sistema de control de versiones más utilizado (Chacon y Straub, 2014). Es software libre y está disponible en [git-scm.com](https://git-scm.com/).

Sus conceptos fundamentales son:

- **Repositorio**: un directorio cuyo historial es gestionado por Git. Contiene los archivos del proyecto y, en un subdirectorio oculto (`.git`), toda su historia.
- **Commit** (confirmación): una "fotografía" del estado de los archivos en un momento dado, acompañada de la fecha, la autoría y un mensaje que describe el cambio. El historial de un repositorio es la secuencia de sus *commits*.
- **Rama** (*branch*): una línea de desarrollo que avanza en paralelo a otras, útil para preparar cambios sin afectar la versión principal. La rama principal suele llamarse `main`.
- **Repositorio remoto**: una copia del repositorio alojada en un servidor —por ejemplo, en GitHub— con la que se sincroniza el repositorio local.

El flujo de trabajo básico consiste en modificar archivos en el **directorio de trabajo**, seleccionar los cambios que formarán parte del siguiente *commit* en el **área de preparación** (*staging area*), confirmarlos en el repositorio local y sincronizarlos con el repositorio remoto, como ilustra la figura 1.

```{mermaid}
flowchart LR
  DT([Directorio<br>de trabajo]) -- git add --> AP([Área de<br>preparación])
  AP -- git commit --> RL([Repositorio<br>local])
  RL -- git push --> RR([Repositorio<br>remoto])
  RR -- git pull --> DT
```

<p style="text-align: center;"><strong>Figura 1</strong>. Flujo de trabajo básico de Git. Elaboración propia con base en Chacon y Straub (2014).</p>

Git se maneja principalmente desde la línea de comandos. La tabla 1 resume los comandos que implementan el flujo anterior.

<figure style="text-align: center; margin: 20px 0;">
    <figcaption><strong>Tabla 1</strong>. Comandos principales de Git. Elaboración propia con base en Chacon y Straub (2014).</figcaption>
    <table class="table table-bordered table-striped" style="margin: 0 auto;">
    <thead>
      <tr>
        <th>Comando</th>
        <th>Descripción</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>git init</code></td>
        <td style="text-align: left;">Crea un repositorio nuevo en el directorio actual.</td>
      </tr>
      <tr>
        <td><code>git clone</code></td>
        <td style="text-align: left;">Copia un repositorio remoto, con todo su historial, en la computadora local.</td>
      </tr>
      <tr>
        <td><code>git status</code></td>
        <td style="text-align: left;">Muestra el estado del directorio de trabajo y del área de preparación.</td>
      </tr>
      <tr>
        <td><code>git add</code></td>
        <td style="text-align: left;">Agrega cambios al área de preparación.</td>
      </tr>
      <tr>
        <td><code>git commit</code></td>
        <td style="text-align: left;">Confirma los cambios preparados en el repositorio local, con un mensaje descriptivo.</td>
      </tr>
      <tr>
        <td><code>git push</code></td>
        <td style="text-align: left;">Envía los <em>commits</em> locales al repositorio remoto.</td>
      </tr>
      <tr>
        <td><code>git pull</code></td>
        <td style="text-align: left;">Trae los cambios del repositorio remoto y los incorpora en el repositorio local.</td>
      </tr>
      <tr>
        <td><code>git log</code></td>
        <td style="text-align: left;">Muestra el historial de <em>commits</em>.</td>
      </tr>
    </tbody>
    </table>
</figure>

En esta lección, Git se practica desde el navegador, a través de GitHub, que ejecuta las operaciones por nosotros. La línea de comandos se retomará cuando se instale el ambiente local del curso, en la próxima semana: el ambiente conda incluye Git, y [Visual Studio Code](../software/vscode.md) lo integra en su vista de control de código fuente (*Source Control*).

Un buen mensaje de *commit* es breve y describe el cambio de forma específica ("Corrige la fórmula de densidad de población", no "cambios"). Como referencia, las convenciones que siguen los materiales de este curso están documentadas en el archivo [CONTRIBUTING](https://github.com/gf0657-programacionsig/2026-ii/blob/main/CONTRIBUTING.md) de su repositorio.

*Ejercicios de esta sección: [ejercicios sobre GitHub](#ejercicios-github).*

## GitHub

**GitHub** es una plataforma en la nube que aloja repositorios Git y agrega, sobre ellos, servicios de colaboración: gestión de incidencias (*issues*), solicitudes de cambios (*pull requests*), revisión de código y automatización, además de la publicación de sitios web con GitHub Pages (GitHub, s. f.-a). Es la plataforma de este tipo más utilizada; existen alternativas como [GitLab](https://about.gitlab.com/) y [Bitbucket](https://bitbucket.org/).

Un repositorio de GitHub puede ser **público** (visible para cualquier persona, aunque solo quienes tengan permiso pueden modificarlo) o **privado**. Su página principal muestra los archivos y, renderizado debajo de ellos, el contenido del archivo **README.md**: un documento escrito en [Markdown](04-markdown.md) que presenta el proyecto, explica qué contiene el repositorio y cómo usarlo.

Aunque el uso pleno de Git requiere la línea de comandos o un editor, GitHub permite realizar las operaciones esenciales directamente en el navegador: crear repositorios, crear y editar archivos —cada edición genera un *commit*—, examinar el historial y comparar versiones. Así se trabaja durante esta semana. En el curso, GitHub es también el medio de entrega: cada tarea y el proyecto final se desarrollan en repositorios propios, y los materiales del curso están en la organización [gf0657-programacionsig](https://github.com/gf0657-programacionsig).

*Ejercicios de esta sección: [ejercicios sobre GitHub](#ejercicios-github).*

## GitHub Pages

**GitHub Pages** es el servicio de GitHub que publica [sitios web estáticos](https://es.wikipedia.org/wiki/P%C3%A1gina_web_est%C3%A1tica) directamente desde un repositorio, sin necesidad de un servidor propio (GitHub, s. f.-b). En las cuentas gratuitas está disponible para repositorios públicos. El sitio publicado queda en una URL con la forma:

```text
https://usuario.github.io/repositorio/
```

En su modalidad más simple, se activa en la configuración del repositorio (*Settings > Pages*), eligiendo la rama que se publicará (típicamente `main`). GitHub convierte entonces los documentos Markdown del repositorio en páginas HTML mediante [Jekyll](https://jekyllrb.com/), un generador de sitios estáticos: la página inicial se toma del archivo `index.md` (o `index.html`) y, en su ausencia, del `README.md`. Cada *push* a la rama publicada vuelve a generar el sitio; el proceso puede seguirse en la pestaña *Actions* del repositorio y tarda unos minutos.

Este es el mecanismo con el que se publicará la documentación de las tareas del curso. Sitios más elaborados —como este, generado con [MyST](https://mystmd.org/) mediante un flujo de GitHub Actions— usan el mismo servicio con procesos de construcción propios.

*Ejercicios de esta sección: [ejercicios sobre GitHub Pages](#ejercicios-pages).*

## Resumen

- Un sistema de **control de versiones** registra la historia de los cambios de un conjunto de archivos: quién cambió qué y cuándo, con la posibilidad de comparar y recuperar versiones y de reunir el trabajo de varias personas. Ese historial es parte de la procedencia de un análisis reproducible.
- **Git** es el sistema de control de versiones más utilizado. Su flujo básico prepara los cambios (`git add`), los confirma en *commits* con mensajes descriptivos (`git commit`) y los sincroniza con un repositorio remoto (`git push`, `git pull`).
- **GitHub** aloja repositorios Git en la nube y agrega colaboración y servicios; su archivo **README.md**, escrito en Markdown, presenta cada repositorio. Las operaciones esenciales pueden realizarse desde el navegador.
- **GitHub Pages** publica sitios web estáticos desde un repositorio; con Jekyll, los documentos Markdown se convierten en páginas HTML. Es el mecanismo de publicación de la documentación de las tareas y de este sitio web.

## Ejercicios

Los ejercicios se agrupan según la sección del capítulo a la que corresponden; se recomienda realizarlos al concluir la sección respectiva. Continúan el trabajo de la lección de Markdown: el documento elaborado en aquellos ejercicios se convertirá aquí en un repositorio con una página web publicada.

(ejercicios-github)=
### Control de versiones, Git y GitHub

1. En su cuenta de GitHub, cree un repositorio público llamado `practica-markdown`, marcando la opción *Add a README file*. Edite el `README.md` desde el navegador (ícono de lápiz), reemplace su contenido con el documento Markdown que elaboró en los [ejercicios de la lección anterior](04-markdown.md), escriba un mensaje de *commit* que describa el cambio y confírmelo (*Commit changes*). Verifique que el documento se muestre renderizado en la página principal del repositorio.
2. Realice un segundo cambio —por ejemplo, agregue una sección con una tabla o corrija un texto— con su propio mensaje de *commit*. Abra el historial del archivo (*History*), compare las dos versiones y observe cómo se señalan las líneas agregadas y eliminadas. Abra también la vista *Raw* y compare la fuente Markdown con la versión renderizada.

(ejercicios-pages)=
### GitHub Pages

3. Active GitHub Pages en el repositorio (*Settings > Pages*), publicando la rama `main`. Siga el proceso de publicación en la pestaña *Actions* y, al concluir, visite `https://su-usuario.github.io/practica-markdown/`. Compare la página publicada con el `README.md` renderizado en GitHub: contenido igual, presentación distinta.
4. En una celda de texto de un cuaderno o en un documento aparte, explique en qué lugar del [espectro de reproducibilidad](01-introduccion-ciencia-datos.md) quedaría un análisis cuyo código, datos y documentación se publican en un repositorio como el que acaba de crear, y qué aporta el historial de *commits* a esa valoración.

## Referencias bibliográficas

Abba, I. V. (2021). *Git and GitHub tutorial – Version control for beginners*. freeCodeCamp. https://www.freecodecamp.org/news/git-and-github-for-beginners/
\
\
Chacon, S. y Straub, B. (2014). *Pro Git* (2.ª ed.). Apress. https://git-scm.com/book/es/v2
\
\
GitHub. (s. f.-a). *What is GitHub?* GitHub Docs. Recuperado el 11 de agosto de 2026, de https://docs.github.com/en/get-started/start-your-journey/what-is-github
\
\
GitHub. (s. f.-b). *Quickstart for GitHub Pages*. GitHub Docs. Recuperado el 11 de agosto de 2026, de https://docs.github.com/en/pages/quickstart
