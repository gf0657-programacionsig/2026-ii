# Google Colab

[Google Colab](https://colab.research.google.com/) es el servicio en la nube con el que se trabaja con [cuadernos de notas](../i-introduccion-ciencia-datos-programacion/03-cuadernos-jupyter.md) durante las primeras semanas del curso, sin instalar nada en la computadora local. Esta guía explica lo necesario para usarlo.

La interfaz de Colab se muestra en el idioma de la cuenta de Google o del navegador; esta guía usa los nombres de menús en español.

## Cuenta de Google

Para usar Colab se requiere una cuenta de Google, ya que los cuadernos se guardan en Google Drive. Una cuenta personal (ej. Gmail) funciona de inmediato, sin configuración adicional; si no tiene una, [créela](https://accounts.google.com/signup) antes de la primera clase.

## Acceso

1. Ingrese a [colab.research.google.com](https://colab.research.google.com/) con su cuenta de Google. Se mostrará el cuaderno de bienvenida, que puede recorrer como introducción al servicio.
2. Los cuadernos del curso se abren con la insignia "*Open in Colab*" que aparece al inicio de cada uno, en el sitio web del curso.
3. Para crear un cuaderno propio, use *Archivo > Nuevo cuaderno en Drive*. También es posible crearlo desde Google Drive (*Nuevo > Más > Google Colaboratory*), aunque si la opción no aparece en el menú es necesario conectar primero la aplicación (*Nuevo > Más > Conectar más aplicaciones*); por simplicidad, se recomienda ingresar siempre por [colab.research.google.com](https://colab.research.google.com/).

## Guardado del trabajo

Los cuadernos del curso se abren desde GitHub en modo de solo lectura: los cambios no se guardan hasta crear una copia propia con *Archivo > Guardar una copia en Drive*. Las copias quedan en la carpeta *Colab Notebooks* del Google Drive de la cuenta.

## Descarga, subida y compartición de cuadernos

- **Descargar**: *Archivo > Descargar > Descargar .ipynb* guarda el cuaderno como archivo en la computadora. Este archivo puede abrirse después en otras aplicaciones de cuadernos, como Visual Studio Code, o agregarse a un repositorio de Git, como se hará a partir de la semana 3 del curso.
- **Subir o abrir de otras fuentes**: *Archivo > Subir cuaderno* abre un archivo `.ipynb` de la computadora; el cuadro de diálogo de *Archivo > Abrir cuaderno* también permite abrir cuadernos guardados en Google Drive o publicados en repositorios de GitHub.
- **Compartir**: el botón **Compartir**, en la esquina superior derecha, genera un enlace al cuaderno con los permisos que se elijan (lector o editor), de la misma forma que en los demás documentos de Google Drive. Es útil para pedir ayuda o para trabajar en parejas.

## Funciones de inteligencia artificial (Gemini)

Colab integra funciones de [asistencia con IA](../i-introduccion-ciencia-datos-programacion/07-asistentes-ia.md) basadas en Gemini, como el autocompletado de código y un chat en el que se pueden pedir explicaciones o generación de código. Según la [documentación de Colab](https://research.google.com/colaboratory/faq.html), estas funciones requieren que la cuenta pertenezca a una persona mayor de 18 años; el uso básico de Colab no tiene esa restricción.

Estas funciones pueden ocultarse o mostrarse en *Herramientas > Configuración*, en la sección de asistencia de IA. Al igual que con las sugerencias de [GitHub Copilot](copilot.md) en Visual Studio Code, se recomienda mantenerlas desactivadas mientras se aprende un tema nuevo: primero intente resolver los ejercicios por su cuenta y use el asistente para pedir explicaciones o revisar su solución, según los lineamientos de uso de IA del curso (declarar el uso, comprender y verificar todo el código que entregue).

## Limitaciones

- Requiere conexión a Internet.
- Las sesiones se reinician tras un período de inactividad y se pierde el estado del kernel; basta con volver a ejecutar el cuaderno (*Entorno de ejecución > Ejecutar todas*).
- Los archivos cargados o generados en el entorno de ejecución (visibles en el panel de archivos, a la izquierda) también se pierden al reiniciarse la sesión, a diferencia de los cuadernos, que quedan guardados en Google Drive. Los archivos que deban conservarse tienen que descargarse o guardarse en Drive antes de cerrar la sesión.
- Las bibliotecas que no vienen preinstaladas deben instalarse en cada sesión (ej. `%pip install pygbif`).

## Teclas rápidas recomendadas

- Ejecutar la celda actual: `Ctrl + Enter`
- Ejecutar la celda y pasar a la siguiente: `Shift + Enter`
- Insertar una celda de código abajo: `Ctrl + M B` (arriba: `Ctrl + M A`)
- Convertir la celda en celda de texto: `Ctrl + M M`
- Convertir la celda en celda de código: `Ctrl + M Y`
- Borrar la celda actual: `Ctrl + M D`
- Ver todas las teclas rápidas: `Ctrl + M H`

Las combinaciones con prefijo `Ctrl + M` se ejecutan en dos pasos: primero `Ctrl + M` y luego la letra. En macOS, sustituya `Ctrl` por `Cmd`.

El contexto conceptual de los cuadernos de notas, el kernel y Colab se explica en la [lección de cuadernos de notas Jupyter](../i-introduccion-ciencia-datos-programacion/03-cuadernos-jupyter.md).
