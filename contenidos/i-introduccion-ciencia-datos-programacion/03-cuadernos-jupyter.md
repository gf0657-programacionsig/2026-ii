# Cuadernos de notas Jupyter

## Trabajo previo

### Lecturas

Antes de la clase, revise las siguientes lecturas. La primera es el cuaderno interactivo de bienvenida a Google Colab, el servicio en el que se trabajará durante las primeras semanas del curso; la segunda, en inglés, presenta Jupyter y sus fundamentos (interesa especialmente la sección 2.2). Además, asegúrese de contar con una cuenta de Google antes de la clase; los requisitos se explican en la guía de [Google Colab](../software/colab.md) de la sección de software.

Google. (s. f.). *Te damos la bienvenida a Colab* [cuaderno de notas]. Google Colab. Recuperado el 9 de agosto de 2026, de https://colab.research.google.com/
\
\
McKinney, W. (2022). Python language basics, IPython, and Jupyter notebooks. En *Python for data analysis: Data wrangling with pandas, NumPy, and Jupyter* (3.ª ed.). O'Reilly Media. https://wesmckinney.com/book/python-basics

## Introducción

Los cuadernos de notas de [Jupyter](https://jupyter.org/) se presentaron en la lección de [introducción a la ciencia de datos](01-introduccion-ciencia-datos.md) como una de las herramientas del curso, y el [cuaderno de ejemplo](02-ejemplo-procesos-ciencia-datos.ipynb) mostró cómo implementan los procesos de la ciencia de datos. Este capítulo los estudia con más detalle: la estructura de celdas que los compone, el kernel que ejecuta su código y Google Colab, el servicio en la nube con el que se trabajará mientras se instalan las herramientas locales.

## Estructura de un cuaderno

Un cuaderno de notas es un documento interactivo compuesto por una secuencia de **celdas**, de dos tipos principales:

- **Celdas de código**: contienen código —en este curso, de Python— que puede ejecutarse. El resultado (un valor, una tabla, un gráfico, un mapa o un mensaje de error) se muestra inmediatamente debajo de la celda, como su **salida** (*output*).
- **Celdas de texto**: contienen texto con formato escrito en [Markdown](https://es.wikipedia.org/wiki/Markdown): títulos, párrafos, listas, enlaces, imágenes y fórmulas que documentan el análisis.

La figura 1 ilustra la relación entre estos elementos.

```{mermaid}
flowchart LR
  C([Cuaderno de notas]) --> CT([Celdas de texto<br>en Markdown])
  C --> CC([Celdas de código<br>en Python])
  CC --> K([Kernel])
  K --> S([Salidas: valores, tablas,<br>gráficos, mapas])
```

<p style="text-align: center;"><strong>Figura 1</strong>. Elementos de un cuaderno de notas. Elaboración propia.</p>

Esta organización divide el análisis en pasos pequeños que pueden ejecutarse y corregirse de forma independiente, documentados junto a sus resultados. Por eso los cuadernos son idóneos para la ciencia de datos reproducible y para la comunicación de resultados (Kluyver et al., 2016): el documento completo —código, explicación y salidas— puede compartirse, versionarse con Git y publicarse, como hace este sitio web con el cuaderno de ejemplo.

Los cuadernos se guardan en archivos con la extensión `.ipynb`, un formato abierto basado en [JSON](https://es.wikipedia.org/wiki/JSON) que plataformas como GitHub muestran ya renderizado. Aunque surgieron en el ecosistema de Python, soportan muchos otros lenguajes de programación: el nombre Jupyter proviene de tres de los más usados en ciencia de datos —Julia, Python y R—.

*Ejercicios de esta sección: [ejercicios sobre la estructura de un cuaderno](#ejercicios-estructura).*

## El kernel

Detrás de cada cuaderno hay un **kernel**: el proceso que ejecuta el código de las celdas y conserva en memoria el **estado**, es decir, las variables y los datos definidos hasta el momento (McKinney, 2022). De esto se derivan dos consecuencias prácticas:

- Las celdas comparten el estado: una variable definida al ejecutar una celda puede usarse en las celdas que se ejecuten después.
- El estado depende del **orden de ejecución** y no del orden en el que las celdas aparecen en el documento. El número entre corchetes que acompaña a cada celda de código (ej. `[3]`) indica en qué orden se ejecutó.

Ejecutar celdas fuera de orden es una fuente frecuente de confusión y de resultados no reproducibles: un cuaderno puede "funcionar" gracias a variables que quedaron en memoria, pero fallar cuando otra persona lo ejecuta desde el inicio. Por eso, antes de compartir un cuaderno conviene reiniciar el kernel y ejecutarlo completo, de arriba abajo (en Colab: *Entorno de ejecución > Reiniciar y ejecutar todo*), tal como se hace con los cuadernos de este curso.

*Ejercicios de esta sección: [ejercicios sobre el kernel](#ejercicios-kernel).*

## Jupyter

[Jupyter](https://jupyter.org/) es el proyecto de código abierto que desarrolla el formato de los cuadernos y las aplicaciones para trabajar con ellos en la computadora local, como Jupyter Notebook y [JupyterLab](https://jupyterlab.readthedocs.io/). El ambiente conda del curso incluye Jupyter; su instalación local se realiza junto con la de Python, siguiendo la [guía de Miniconda](../software/miniconda.md). Los archivos `.ipynb` también pueden abrirse y ejecutarse en editores de código como [Visual Studio Code](../software/vscode.md), que se estudiará más adelante en el curso.

## Google Colab

[Google Colab](https://colab.research.google.com/) es un servicio gratuito que permite crear y ejecutar cuadernos de notas directamente en la nube. Entre sus ventajas pueden mencionarse:

- **Entorno preconfigurado**: no requiere instalar ni configurar nada en la computadora local; por eso el curso lo utiliza desde la primera semana.
- **Integración con Google Drive**: los cuadernos y sus datos se guardan en la nube (*Archivo > Guardar una copia en Drive*).
- **Colaboración**: un cuaderno puede compartirse para que varias personas lo lean o editen.
- **Aceleradores de hardware**: ofrece acceso limitado y gratuito a GPU y TPU, útiles en aprendizaje automático.

También tiene limitaciones que conviene conocer: requiere una [cuenta de Google](../software/colab.md) y conexión a Internet; las sesiones se reinician tras un período de inactividad, con lo que se pierde el estado del kernel; y las bibliotecas que no vienen preinstaladas deben instalarse en cada sesión, como hace el cuaderno de ejemplo con pygbif.

*Ejercicios de esta sección: [ejercicios sobre Google Colab](#ejercicios-colab).*

## Resumen

- Un **cuaderno de notas** combina, en un solo documento, celdas de código, celdas de texto en Markdown y las salidas del código: la unidad básica de trabajo de la ciencia de datos reproducible.
- El **kernel** ejecuta el código y conserva el estado, que depende del orden de ejecución de las celdas; reiniciar el kernel y ejecutar todo, de arriba abajo, es la prueba de que un cuaderno es reproducible.
- Los cuadernos se guardan en archivos `.ipynb`, un formato abierto basado en JSON que puede versionarse con Git y que GitHub muestra renderizado.
- **Google Colab** permite trabajar con cuadernos en la nube sin instalar nada; **Jupyter** ofrece las aplicaciones para trabajar localmente, con el ambiente conda del curso.

## Ejercicios

Los ejercicios se agrupan según la sección del capítulo a la que corresponden; se recomienda realizarlos al concluir la sección respectiva. La sintaxis de Markdown y el lenguaje Python se estudiarán en las próximas semanas: en estos ejercicios basta con copiar el texto y el código que se indican, pues su objetivo es el manejo del cuaderno y no la sintaxis. Las [soluciones de estos ejercicios](../soluciones/03-soluciones-cuadernos-jupyter.md) se publican después de la clase correspondiente.

(ejercicios-estructura)=
### Estructura de un cuaderno

1. Cree un cuaderno nuevo en [Google Colab](https://colab.research.google.com/) y construya en él un ejemplo mínimo con ambos tipos de celda:
    - Agregue una celda de texto (botón *+ Texto*) y copie en ella el siguiente contenido en Markdown:

      ```
      # Mi primer cuaderno

      Este cuaderno practica los dos tipos de celda:

      - celdas de texto
      - celdas de código
      ```

    - Agregue una celda de código (botón *+ Código*), copie en ella el siguiente código y ejecútela:

      ```python
      dias = 7
      horas = dias * 24
      print(horas)
      ```

    - Observe la diferencia entre ambos tipos de celda y dónde aparece la salida del código.

(ejercicios-kernel)=
### El kernel

2. En el cuaderno del ejercicio anterior, experimente con el estado del kernel:
    - Agregue una celda de código con `print(minutos)` y ejecútela: observe el error, pues esa variable no ha sido definida.
    - Agregue después otra celda de código con `minutos = horas * 60`, ejecútela y vuelva a ejecutar la celda de `print(minutos)`: observe que ahora funciona, aunque la definición aparece después en el documento (y que usa la variable `horas` del ejercicio anterior: las celdas comparten el estado).
    - Revise los números entre corchetes de las celdas y explique en una celda de texto, con sus palabras, por qué el cuaderno «funciona» a pesar de estar en desorden.

(ejercicios-colab)=
### Google Colab

3. Con el cuaderno en desorden del ejercicio anterior, use *Entorno de ejecución > Reiniciar y ejecutar todo* y observe qué sucede. Reordene las celdas (o corrija el código) hasta que el cuaderno completo se ejecute sin errores de arriba abajo, y guarde su copia en Drive.
4. Descargue el cuaderno como archivo (*Archivo > Descargar > Descargar .ipynb*) y ábralo con un editor de texto simple. Identifique en el JSON las celdas de código, las celdas de texto y las salidas, y compare lo que ve con la versión renderizada en Colab.

## Referencias bibliográficas

Google. (s. f.). *Te damos la bienvenida a Colab* [cuaderno de notas]. Google Colab. Recuperado el 9 de agosto de 2026, de https://colab.research.google.com/
\
\
Kluyver, T., Ragan-Kelley, B., Pérez, F., Granger, B., Bussonnier, M., Frederic, J., Kelley, K., Hamrick, J., Grout, J., Corlay, S., Ivanov, P., Avila, D., Abdalla, S. y Willing, C. (2016). Jupyter Notebooks—a publishing format for reproducible computational workflows. En F. Loizides y B. Schmidt (eds.), *Positioning and power in academic publishing: Players, agents and agendas* (pp. 87–90). IOS Press. https://eprints.soton.ac.uk/403913/
\
\
McKinney, W. (2022). Python language basics, IPython, and Jupyter notebooks. En *Python for data analysis: Data wrangling with pandas, NumPy, and Jupyter* (3.ª ed.). O'Reilly Media. https://wesmckinney.com/book/python-basics
