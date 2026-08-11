# Visual Studio Code

[Visual Studio Code (VS Code)](https://code.visualstudio.com/) es un editor de código fuente gratuito desarrollado por Microsoft. En este curso se usa para editar documentos Markdown y, más adelante, para programar en Python y trabajar con cuadernos de notas en la computadora local. Esta guía explica cómo instalarlo y configurarlo; como introducción general al editor, puede revisarse el tutorial [Getting started with Visual Studio Code](https://code.visualstudio.com/docs), de Microsoft.

## Instalación

1. Ingrese al sitio web de [Visual Studio Code](https://code.visualstudio.com/) y descargue el instalador correspondiente a su sistema operativo.
2. Ejecute el instalador y siga las instrucciones. En Windows, se recomienda marcar las siguientes opciones durante la instalación:
    - **Add "Open with Code" action to Windows Explorer file context menu**.
    - **Add "Open with Code" action to Windows Explorer directory context menu**.
    - **Add to PATH**.
3. Al finalizar la instalación, abra VS Code.

## Instalación de extensiones

Las extensiones agregan funcionalidades adicionales a VS Code. Para instalar una extensión:

1. Abra el panel de extensiones con `Ctrl + Shift + X`.
2. Busque la extensión por su nombre.
3. Haga clic en **Install**.

### Extensiones recomendadas para Markdown

- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
- [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)
- [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf)

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

## Cuadernos de notas en VS Code

VS Code puede abrir y ejecutar los archivos `.ipynb` de los [cuadernos de notas](../i-introduccion-ciencia-datos-programacion/03-cuadernos-jupyter.md), como alternativa a Google Colab y a las aplicaciones del proyecto Jupyter. Requiere las extensiones de Python y de Jupyter mencionadas en la sección anterior y una instalación local de Python, que se realiza en la semana 3 del curso. Los pasos generales son:

1. Abra el archivo `.ipynb` en VS Code (*File > Open File*).
2. Haga clic en **Select Kernel**, en la esquina superior derecha, y elija el ambiente de Python del curso.
3. Ejecute las celdas con el botón de ejecución o con `Shift + Enter`, como en cualquier otra aplicación de cuadernos.

## Teclas rápidas recomendadas

- Paleta de comandos: `Ctrl + Shift + P`
- Buscar y abrir un archivo: `Ctrl + P`
- Abrir el panel de extensiones: `Ctrl + Shift + X`
- Guardar un archivo: `Ctrl + S`
- Ir a una línea: `Ctrl + G`
- Mover una línea hacia arriba y hacia abajo: `Alt + Flecha arriba / Flecha abajo`
- Cortar una línea completa: `Ctrl + X`
- Activar la vista previa de un documento Markdown: `Ctrl + K V`
- Activar y desactivar el modo Zen: `Ctrl + K Z`
- Dividir la vista: *View > Editor Layout > Split Up / Split Down / Split Left / Split Right*
- Editar varias líneas simultáneamente: `Alt + Clic` (coloca un cursor adicional en cada sitio en el que se desea editar)

La lista completa de teclas rápidas está disponible para [Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf), [macOS](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf) y [Linux](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf).
