# Google Colab

[Google Colab](https://colab.research.google.com/) es el servicio en la nube con el que se trabaja con [cuadernos de notas](../i-introduccion-ciencia-datos-programacion/03-cuadernos-jupyter.md) durante las primeras semanas del curso, sin instalar nada en la computadora local. Esta guía explica lo necesario para usarlo.

## Cuenta de Google

Para usar Colab se requiere una cuenta de Google, ya que los cuadernos se guardan en Google Drive. Una cuenta personal (ej. Gmail) funciona de inmediato, sin configuración adicional; si no tiene una, [créela](https://accounts.google.com/signup) antes de la primera clase.

Según la [documentación de Colab](https://research.google.com/colaboratory/faq.html), las funciones de inteligencia artificial integradas requieren que la cuenta pertenezca a una persona mayor de 18 años; el uso básico de Colab, el de este curso, no tiene esa restricción.

## Acceso

1. Ingrese a [colab.research.google.com](https://colab.research.google.com/) con su cuenta de Google. Se mostrará el cuaderno de bienvenida, que puede recorrer como introducción al servicio.
2. Los cuadernos del curso se abren con la insignia "*Open in Colab*" que aparece al inicio de cada uno, en el sitio web del curso.
3. Para crear un cuaderno propio, use *Archivo > Nuevo cuaderno en Drive*. También es posible crearlo desde Google Drive (*Nuevo > Más > Google Colaboratory*), aunque si la opción no aparece en el menú es necesario conectar primero la aplicación (*Nuevo > Más > Conectar más aplicaciones*); por simplicidad, se recomienda ingresar siempre por [colab.research.google.com](https://colab.research.google.com/).

## Guardado del trabajo

Los cuadernos del curso se abren desde GitHub en modo de solo lectura: los cambios no se guardan hasta crear una copia propia con *Archivo > Guardar una copia en Drive*. Las copias quedan en la carpeta *Colab Notebooks* del Google Drive de la cuenta.

## Limitaciones

- Requiere conexión a Internet.
- Las sesiones se reinician tras un período de inactividad y se pierde el estado del kernel; basta con volver a ejecutar el cuaderno (*Entorno de ejecución > Ejecutar todas*).
- Las bibliotecas que no vienen preinstaladas deben instalarse en cada sesión (ej. `%pip install pygbif`).

El contexto conceptual de los cuadernos de notas, el kernel y Colab se explica en la [lección de cuadernos de notas Jupyter](../i-introduccion-ciencia-datos-programacion/03-cuadernos-jupyter.md).
