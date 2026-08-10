# Google Colab

[Google Colab](https://colab.research.google.com/) es el servicio en la nube con el que se trabaja con [cuadernos de notas](../i-introduccion-ciencia-datos-programacion/03-cuadernos-jupyter.md) durante las primeras semanas del curso, sin instalar nada en la computadora local. Esta guía explica lo necesario para usarlo.

## Cuenta de Google

Para usar Colab se requiere una cuenta de Google, ya que los cuadernos se guardan en Google Drive.

- **Cuenta personal** (ej. Gmail): funciona de inmediato, sin configuración adicional. Si no tiene una, [créela](https://accounts.google.com/signup) antes de la primera clase.
- **Cuenta institucional de la UCR**: en las cuentas de Google Workspace, el acceso a Colab depende de que la organización tenga habilitado el servicio. Si al intentar abrir Colab con la cuenta institucional aparece un mensaje de que el servicio no está disponible, use una cuenta personal.

Según la [documentación de Colab](https://research.google.com/colaboratory/faq.html), las funciones de inteligencia artificial integradas requieren que la cuenta pertenezca a una persona mayor de 18 años; el uso básico de Colab, el de este curso, no tiene esa restricción.

## Acceso

1. Ingrese a [colab.research.google.com](https://colab.research.google.com/) con su cuenta de Google. Se mostrará el cuaderno de bienvenida, que puede recorrer como introducción al servicio.
2. Los cuadernos del curso se abren con la insignia "*Open in Colab*" que aparece al inicio de cada uno, en el sitio web del curso.
3. Para crear un cuaderno propio, use *Archivo > Nuevo cuaderno en Drive*.

## Guardado del trabajo

Los cuadernos del curso se abren desde GitHub en modo de solo lectura: los cambios no se guardan hasta crear una copia propia con *Archivo > Guardar una copia en Drive*. Las copias quedan en la carpeta *Colab Notebooks* del Google Drive de la cuenta.

## Limitaciones

- Requiere conexión a Internet.
- Las sesiones se reinician tras un período de inactividad y se pierde el estado del kernel; basta con volver a ejecutar el cuaderno (*Entorno de ejecución > Ejecutar todas*).
- Las bibliotecas que no vienen preinstaladas deben instalarse en cada sesión (ej. `%pip install pygbif`).

El contexto conceptual de los cuadernos de notas, el kernel y Colab se explica en la [lección de cuadernos de notas Jupyter](../i-introduccion-ciencia-datos-programacion/03-cuadernos-jupyter.md).
