# Visual Studio Code

[Visual Studio Code (VS Code)](https://code.visualstudio.com/) es un editor de código fuente gratuito desarrollado por Microsoft. En este curso se usa para editar documentos Markdown y, más adelante, para programar en Python y trabajar con cuadernos de notas en la computadora local. Esta guía explica cómo instalarlo y configurarlo; como introducción general al editor, puede revisarse el tutorial [Getting started with Visual Studio Code](https://code.visualstudio.com/docs/getstarted/getting-started), de Microsoft.

## Instalación

1. Ingrese al sitio web de [Visual Studio Code](https://code.visualstudio.com/) y descargue el instalador correspondiente a su sistema operativo.
2. Instale el programa según su sistema operativo:
    - **Windows**: ejecute el instalador y siga las instrucciones. Se recomienda marcar las siguientes opciones durante la instalación:
        - **Add "Open with Code" action to Windows Explorer file context menu**.
        - **Add "Open with Code" action to Windows Explorer directory context menu**.
        - **Add to PATH**.
    - **macOS**: abra el archivo descargado y arrastre la aplicación **Visual Studio Code** a la carpeta **Applications**.
    - **Linux**: descargue el paquete `.deb` o `.rpm` según su distribución e instálelo con el gestor de paquetes.
3. Al finalizar la instalación, abra VS Code.

La interfaz de VS Code está en inglés y esta guía usa los nombres de menús y botones en ese idioma. Si prefiere la interfaz en español, puede instalar la extensión [Spanish Language Pack for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-es), según se explica en la sección de instalación de extensiones.

## Carpetas de trabajo

VS Code puede abrir archivos individuales (*File > Open File*), pero la forma habitual de trabajar es abrir una **carpeta** completa (*File > Open Folder*): el panel del explorador, a la izquierda, muestra entonces todos los archivos de la carpeta y permite crear, renombrar y organizar archivos sin salir del editor. Esta forma de trabajo es la apropiada para proyectos compuestos por varios archivos, como los repositorios de Git que se usan en el curso.

Mientras se edita un archivo, un punto en su pestaña indica que hay cambios sin guardar; los cambios se guardan con `Ctrl + S` y otras vistas, como la vista previa de Markdown, se actualizan al guardar. Si lo prefiere, puede activar el guardado automático con *File > Auto Save*.

## Terminal integrada

VS Code incluye una terminal integrada, que se abre con *View > Terminal* o con ``Ctrl + ` ``. En ella pueden ejecutarse comandos sin salir del editor. En este curso se usará a partir de la semana 3, para manejar los ambientes de conda y ejecutar comandos de Git y de Python.

## Instalación de extensiones

Las extensiones agregan funcionalidades adicionales a VS Code. Para instalar una extensión:

1. Abra el panel de extensiones con `Ctrl + Shift + X`.
2. Busque la extensión por su nombre.
3. Haga clic en **Install**.

### Extensiones recomendadas para Markdown

- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)

Como extensiones opcionales, [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) ofrece una vista previa con funciones adicionales a la integrada en VS Code y [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf) permite exportar documentos Markdown a PDF.

### Extensiones recomendadas para Python

Estas extensiones se usan a partir de la instalación de Python en la computadora local, en la semana 3 del curso.

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [Pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint)
- [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)

### Otras extensiones recomendadas

- [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)
- [vscode-icons](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons)

Puede explorar la lista completa de extensiones en el [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/VSCode).

## Asistente de inteligencia artificial (GitHub Copilot)

VS Code integra el asistente de IA [GitHub Copilot](https://github.com/features/copilot), cuyo uso en el curso comienza en la semana 5. Su activación, sus planes (incluido Copilot Pro gratuito con GitHub Education) y las recomendaciones de uso se explican en la [guía de GitHub Copilot](copilot.md).

## Cuadernos de notas en VS Code

VS Code puede abrir y ejecutar los archivos `.ipynb` de los [cuadernos de notas](../i-introduccion-ciencia-datos-programacion/03-cuadernos-jupyter.md), como alternativa a Google Colab y a las aplicaciones del proyecto Jupyter. Requiere las extensiones de Python y de Jupyter mencionadas en la sección anterior y una instalación local de Python, que se realiza siguiendo la [guía de Miniconda](miniconda.md). Los cuadernos del curso pueden descargarse como archivos `.ipynb` con el botón de descarga (ícono de flecha hacia abajo) en la parte superior de su página en el sitio web, o desde Colab (*Archivo > Descargar > Descargar .ipynb*). Los pasos generales son:

1. Cree un cuaderno nuevo con el comando **Create: New Jupyter Notebook** de la paleta de comandos (`Ctrl + Shift + P`) y guárdelo con la extensión `.ipynb`, o abra un cuaderno existente (*File > Open File*).
2. Haga clic en **Select Kernel**, en la esquina superior derecha, y elija el ambiente de Python del curso (`geopython`), creado con la guía de Miniconda.
3. Ejecute las celdas con el botón de ejecución o con `Shift + Enter`, como en cualquier otra aplicación de cuadernos.

## Teclas rápidas recomendadas

En macOS, sustituya `Ctrl` por `Cmd` en las combinaciones siguientes.

- Paleta de comandos: `Ctrl + Shift + P`
- Buscar y abrir un archivo: `Ctrl + P`
- Abrir el panel de extensiones: `Ctrl + Shift + X`
- Abrir la terminal integrada: ``Ctrl + ` ``
- Guardar un archivo: `Ctrl + S`
- Ir a una línea: `Ctrl + G`
- Mover una línea hacia arriba y hacia abajo: `Alt + Flecha arriba / Flecha abajo`
- Cortar una línea completa: `Ctrl + X`
- Activar la vista previa de un documento Markdown: `Ctrl + Shift + V` (en la misma pestaña) o `Ctrl + K V` (a la par del documento)
- Activar y desactivar el modo Zen: `Ctrl + K Z`
- Dividir la vista: `Ctrl + \` (también en *View > Editor Layout*)
- Editar varias líneas simultáneamente: `Alt + Clic` (coloca un cursor adicional en cada sitio en el que se desea editar)

La lista completa de teclas rápidas está disponible para [Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf), [macOS](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf) y [Linux](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf).
