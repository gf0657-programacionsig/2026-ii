# Asistentes de programación basados en inteligencia artificial

## Trabajo previo

### Lecturas

Antes de la clase, revise las siguientes lecturas. De la primera, en inglés, interesa la descripción general (*Overview*): presenta cómo los modelos de lenguaje están transformando el desarrollo de software, tema que este curso retoma en varias de sus semanas. La segunda, en español, es una guía introductoria breve sobre la inteligencia artificial generativa en la educación superior.

Stanford University. (2025). *CS146S: The modern software developer*. Recuperado el 16 de agosto de 2026, de https://themodernsoftware.dev/
\
\
UNESCO IESALC. (2023). *ChatGPT e inteligencia artificial en la educación superior: Guía de inicio rápido*. UNESCO. https://unesdoc.unesco.org/ark:/48223/pf0000385146_spa

### Videos

El siguiente video (en inglés, con subtítulos en español) explica en ocho minutos cómo funcionan los modelos de lenguaje en los que se basan los asistentes de programación.

3Blue1Brown. (2024). *Large language models explained briefly* [video]. YouTube. https://www.youtube.com/watch?v=LPZh9BOjkQs

## Introducción

El capítulo anterior mostró que un programa expresa un algoritmo en un lenguaje de programación. Desde hace pocos años existen herramientas capaces de generar esos programas a partir de instrucciones en lenguaje natural: los **asistentes de programación basados en inteligencia artificial (IA)**. Estas herramientas también explican y corrigen código, redactan documentación y responden preguntas técnicas, por lo que están cambiando la forma en que se desarrolla software (Stanford University, 2025) y, a la vez, plantean preguntas nuevas sobre cómo se aprende a programar.

Este curso incorpora los asistentes de IA de manera paulatina y crítica, como establece su programa: el objetivo es emplearlos de forma responsable y transparente como apoyo, no como sustituto, del razonamiento propio. Este capítulo presenta el panorama de estas herramientas, explica su funcionamiento y sus riesgos, y establece los lineamientos que rigen su uso en el curso.

## Modelos de lenguaje de gran tamaño

Los asistentes de IA actuales se basan en **modelos de lenguaje de gran tamaño** (LLM, por sus siglas en inglés: *large language models*): programas entrenados con volúmenes enormes de texto y de código, de los que aprenden patrones estadísticos del lenguaje. Con base en esos patrones, un LLM genera sus respuestas prediciendo, palabra por palabra, la continuación más probable del texto que recibe (3Blue1Brown, 2024). La instrucción o pregunta que la persona usuaria escribe se denomina **prompt** y, junto con el resto de la conversación, forma el **contexto** que el modelo utiliza para generar la respuesta siguiente, como ilustra la figura 1.

```{mermaid}
flowchart LR
  C([Grandes volúmenes<br>de texto y código]) -- entrenamiento --> M([Modelo de lenguaje<br>de gran tamaño])
  P([Prompt]) --> M
  M --> R([Respuesta])
  R -. se agrega al contexto<br>de la conversación .-> P
```

<p style="text-align: center;"><strong>Figura 1</strong>. Funcionamiento básico de un modelo de lenguaje de gran tamaño. Elaboración propia con base en 3Blue1Brown (2024).</p>

Esta naturaleza estadística explica tanto las capacidades de los LLM como sus limitaciones principales:

- **Alucinaciones**: las respuestas de un LLM son *verosímiles*, pero no necesariamente *verdaderas*. Un modelo puede inventar datos, referencias bibliográficas o funciones de una biblioteca de Python que no existen, y presentarlos con total seguridad. Por eso toda salida debe verificarse antes de utilizarse.
- **Sesgos**: los modelos reproducen, y pueden amplificar, los sesgos presentes en sus datos de entrenamiento, como subrepresentar regiones, idiomas o puntos de vista.
- **Adulación**: los asistentes conversacionales tienden a complacer a la persona usuaria y a darle la razón, en lugar de contradecirla cuando se equivoca. Que un asistente "confirme" una idea no es evidencia de que sea correcta.
- **Corte de conocimiento**: el entrenamiento tiene una fecha límite, por lo que el modelo puede desconocer versiones recientes de las bibliotecas y herramientas, o eventos posteriores a esa fecha.
- **Privacidad**: en varias herramientas, especialmente en sus versiones gratuitas, las conversaciones pueden utilizarse para entrenar los modelos. No debe ingresarse en ellas información personal, datos sensibles ni credenciales de acceso.

*Ejercicios de esta sección: [ejercicios sobre modelos de lenguaje](#ejercicios-llm).*

## Panorama de asistentes de programación

Los asistentes de programación se presentan en tres modalidades principales, que se diferencian por el grado de integración con el entorno de trabajo y por el grado de autonomía con que operan, como resume la tabla 1.

<figure style="text-align: center; margin: 20px 0;">
    <figcaption><strong>Tabla 1</strong>. Modalidades de asistentes de programación basados en IA. Elaboración propia con base en Stanford University (2025).</figcaption>
    <table class="table table-bordered table-striped" style="margin: 0 auto;">
    <thead>
      <tr>
        <th>Modalidad</th>
        <th>Ejemplos</th>
        <th>Uso típico</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Asistentes conversacionales</td>
        <td><a href="https://chatgpt.com/">ChatGPT</a>, <a href="https://gemini.google.com/">Gemini</a>, <a href="https://claude.ai/">Claude</a>, <a href="https://copilot.microsoft.com/">Copilot</a></td>
        <td>Conversación en el navegador o en una aplicación: explicar conceptos y código, depurar errores, generar ejemplos y borradores.</td>
      </tr>
      <tr>
        <td>Asistentes integrados en editores de código</td>
        <td><a href="https://github.com/features/copilot">GitHub Copilot</a> en Visual Studio Code, Gemini en Google Colab</td>
        <td>Autocompletado y chat dentro del editor, con acceso al código en el que se trabaja.</td>
      </tr>
      <tr>
        <td>Herramientas agénticas</td>
        <td><a href="https://claude.com/claude-code">Claude Code</a>, <a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a>, modo agente de GitHub Copilot</td>
        <td>Ejecutan tareas de varios pasos (ej. modificar archivos, ejecutar programas y pruebas) bajo supervisión humana.</td>
      </tr>
    </tbody>
    </table>
</figure>

Casi todas estas herramientas ofrecen versiones gratuitas con límites de uso, suficientes para este curso. Conviene tener presentes dos aspectos: las funciones de IA integradas en Google Colab requieren una cuenta personal de Google y ser mayor de 18 años, y cada herramienta tiene sus propias políticas sobre el uso que hace de los datos de las personas usuarias, que conviene revisar antes de utilizarla.

El uso de estas modalidades se distribuye a lo largo del curso, en paralelo con el avance de los contenidos de programación:

- **Semana 2**: panorama de los asistentes y lineamientos de uso (este capítulo).
- **Semana 5**: uso de asistentes para explicar y depurar código.
- **Semana 7**: uso de asistentes para generación y verificación de código de análisis de datos.
- **Semana 15**: herramientas agénticas, revisión crítica del código generado y documentación de su uso.

*Ejercicios de esta sección: [ejercicios sobre el panorama de asistentes](#ejercicios-panorama).*

## Posibilidades y riesgos en el aprendizaje

Bien utilizados, los asistentes de IA pueden apoyar el aprendizaje de la programación de varias maneras: explican línea por línea un fragmento de código ajeno, ayudan a interpretar mensajes de error, generan ejemplos y ejercicios adicionales sobre un tema y responden preguntas a cualquier hora, como una especie de tutoría siempre disponible. Para una persona que aprende a programar, poder preguntar "¿por qué falla este código?" o "¿qué hace esta línea?" y recibir una explicación inmediata es una posibilidad valiosa.

El riesgo central es la **dependencia**: si el asistente resuelve las tareas, la persona estudiante se salta precisamente el proceso que desarrolla su capacidad de programar. La evidencia disponible señala que el uso excesivo de estas herramientas puede disminuir el esfuerzo intelectual, la exploración autónoma y el pensamiento crítico (Del Cisne Loján et al., 2024). En programación el problema es tangible: quien entrega código generado que no comprende no puede corregirlo cuando falla, ni adaptarlo a un problema nuevo, ni defenderlo. A esto se suman las limitaciones de la sección anterior: el código generado puede contener errores sutiles, usar funciones inexistentes o basarse en versiones desactualizadas de las bibliotecas.

La legitimidad de usar un asistente depende, entonces, del objetivo de cada actividad. Cuando el objetivo es el producto (ej. redactar más rápido un texto cuyo contenido ya se domina), el asistente es una herramienta legítima de productividad. Cuando el objetivo es el aprendizaje —como ocurre en este curso con la programación—, delegar la tarea en el asistente vacía la actividad de sentido, de la misma forma en que pedirle a otra persona que haga el ejercicio por uno no es hacer el ejercicio. La recomendación general del curso es usar los asistentes **para aprender** (pedir explicaciones, ejemplos, pistas) más que **para resolver** (pedir la solución completa).

Cabe agregar que los detectores automáticos de texto y código generados por IA producen falsos positivos y falsos negativos, por lo que no constituyen una base confiable para evaluar la honestidad académica. Por esa razón, este curso no se apoya en detectores, sino en la transparencia: la declaración del uso y la capacidad de explicar el trabajo propio, como se detalla en la siguiente sección.

*Ejercicios de esta sección: [ejercicios sobre posibilidades y riesgos](#ejercicios-posibilidades-riesgos).*

## Lineamientos de uso en el curso

La Universidad de Costa Rica cuenta desde marzo de 2026 con un [Marco de gobernanza y gestión de la inteligencia artificial](https://ci.ucr.ac.cr/marco-gobernanza-gestion-ia), que orienta la integración ética, crítica y humanista de la IA en la docencia, la investigación, la acción social y la gestión (Universidad de Costa Rica, 2026). Entre sus principios, la **integridad académica** y la **honestidad intelectual** piden declarar de forma transparente el uso de la IA, verificar y contrastar sus salidas, y mantener la responsabilidad personal sobre el trabajo que se firma: la IA puede ser un apoyo, pero no un sustituto del pensamiento crítico. En la misma línea, la UNESCO (2025) define las competencias en materia de IA que el estudiantado debe desarrollar, empezando por una mentalidad centrada en el ser humano y el juicio crítico sobre estas tecnologías, y Costa Rica oficializó en 2026 la norma técnica INTE/ISO/IEC 42001 de gestión de sistemas de IA, elaborada por [INTECO](https://www.inteco.org/), lo que ilustra que el uso responsable de la IA es también una competencia profesional demandada en el país.

En concordancia con ese marco, el uso de asistentes de IA en este curso se rige por los siguientes lineamientos, establecidos en el programa del curso:

1. **Dónde se permite**: en las tareas programadas, en el proyecto final y en los ejercicios de clase. En los exámenes cortos, que son presenciales, no se permite el uso de herramientas de IA.
2. **Transparencia**: todo trabajo que haya utilizado asistentes de IA debe declararlo explícitamente: cuál herramienta se usó, con qué propósito y en cuáles partes del trabajo.
3. **Comprensión**: cada estudiante debe comprender y ser capaz de explicar todo el código y el texto que entregue, incluido el elaborado con asistencia de IA. Puede solicitarse una explicación o defensa oral de cualquier trabajo.
4. **Verificación**: los resultados generados deben verificarse antes de incorporarse al trabajo: ejecutar el código, contrastar las afirmaciones con la [documentación oficial](https://docs.python.org/es/3/) de las bibliotecas y comprobar que las referencias citadas existan.
5. **Privacidad**: no debe ingresarse en estas herramientas información personal propia ni de terceros, datos sensibles, contraseñas ni claves de acceso a servicios (como las claves de API que se usarán más adelante en el curso).
6. **Derechos de autor**: debe respetarse la licencia del código y de los materiales de terceros, y citarse las fuentes utilizadas, según las prácticas de citación del curso.

La declaración de uso puede ser breve. Por ejemplo, al final de un cuaderno de notas o documento:

```
Declaración de uso de IA: se utilizó [herramienta] para [propósito, ej.
generar una primera versión de la función de descarga de datos y explicar
el mensaje de error de la sección 3]. Los resultados fueron revisados,
verificados y adaptados por la persona autora.
```

Este mismo repositorio ofrece un ejemplo real: los mensajes de los *commits* del sitio web del curso declaran la asistencia de IA mediante una línea final (`Co-Authored-By`), visible en el [historial de confirmaciones](https://github.com/gf0657-programacionsig/2026-ii/commits/).

El uso no declarado de herramientas de IA, así como la incapacidad de explicar el trabajo propio, se considera una falta a la honestidad académica, según lo establecido en el [Reglamento de Orden y Disciplina de los Estudiantes de la Universidad de Costa Rica](https://www.cu.ucr.ac.cr/normativ/orden_y_disciplina.pdf). El espíritu de estos lineamientos no es punitivo: es aprender a usar herramientas poderosas de una forma que fortalezca, en lugar de debilitar, el aprendizaje y la integridad del trabajo académico.

*Ejercicios de esta sección: [ejercicios sobre los lineamientos](#ejercicios-lineamientos).*

## Resumen

- Los **asistentes de programación basados en IA** generan, explican, corrigen y documentan código a partir de instrucciones en lenguaje natural denominadas **prompts**.
- Se basan en **modelos de lenguaje de gran tamaño (LLM)**, que aprenden patrones estadísticos de grandes volúmenes de texto y código, y generan respuestas prediciendo la continuación más probable. Por eso sus salidas son verosímiles pero no necesariamente verdaderas: presentan **alucinaciones**, **sesgos**, **adulación** y un **corte de conocimiento**, y deben verificarse siempre.
- Existen tres modalidades: **asistentes conversacionales**, **asistentes integrados en editores de código** y **herramientas agénticas**; el curso las incorpora paulatinamente en las semanas 2, 5, 7 y 15.
- El riesgo central para el aprendizaje es la **dependencia**: código que no se comprende no se puede corregir, adaptar ni defender. La recomendación del curso es usar los asistentes para aprender más que para resolver.
- Los **lineamientos del curso**, alineados con el Marco de gobernanza de la IA de la UCR, son: uso permitido excepto en exámenes cortos, **declaración explícita** del uso, **comprensión** demostrable del trabajo entregado, **verificación** de los resultados, protección de la **privacidad** y respeto a los **derechos de autor**.

## Ejercicios

Los ejercicios se agrupan según la sección del capítulo a la que corresponden; se recomienda realizarlos al concluir la sección respectiva. Para realizarlos se requiere una cuenta en al menos un asistente conversacional de la tabla 1; puede usarse la versión gratuita de cualquiera de ellos.

(ejercicios-llm)=
### Modelos de lenguaje

1. Pida a un asistente conversacional que explique qué es un modelo de lenguaje de gran tamaño y que incluya tres referencias bibliográficas. Luego verifique si las referencias existen, buscándolas en la Web.
    - ¿Encontró todas las referencias? Si alguna no existe, acaba de observar una alucinación.
    - Compare la explicación con la del video de 3Blue1Brown (2024): ¿hay diferencias o contradicciones?
2. Formule a dos asistentes distintos una misma pregunta sobre un tema geográfico de Costa Rica que conozca bien (ej. sobre su cantón, una cuenca o un área protegida). Compare las respuestas: ¿en qué coinciden y en qué difieren? Verifique al menos un dato de cada respuesta en una fuente oficial e indique cuál fuente usó.

(ejercicios-panorama)=
### Panorama de asistentes

3. Explore un asistente conversacional de la tabla 1 que no haya utilizado antes y busque en su sitio web la respuesta a dos preguntas: ¿la versión gratuita utiliza las conversaciones para entrenar los modelos? ¿Puede desactivarse ese uso? Anote lo que encuentre y lo que no logre encontrar; la dificultad para hallar esta información también es un resultado relevante.

(ejercicios-posibilidades-riesgos)=
### Posibilidades y riesgos

4. Este ejercicio practica el ciclo completo de uso responsable: generar, comprender, verificar y criticar.
    - Pida a un asistente un programa en Python que calcule la densidad de población de un cantón a partir de las variables `poblacion` y `area`, como el que usted escribió en el ejercicio 5 del capítulo [Introducción a la programación de computadoras](06-introduccion-programacion.md).
    - Ejecute el programa generado en [Google Colab](https://colab.research.google.com/) y verifique que produce el resultado correcto.
    - Pida al asistente que explique el programa línea por línea y compare la versión generada con la suya: ¿qué hace diferente? ¿Cuál de las dos comprende mejor?
    - Pregunte al asistente si su programa tiene errores o limitaciones (ej. ¿qué sucede si `area` es cero?) y evalúe críticamente la respuesta.

(ejercicios-lineamientos)=
### Lineamientos

5. Redacte la declaración de uso de IA que correspondería al ejercicio 4, siguiendo el formato de ejemplo de la sección de lineamientos: herramienta, propósito, partes del trabajo y revisión realizada.
6. Escriba cinco normas personales para su propio uso de asistentes de IA durante este curso, en forma de decálogo breve. Compárelas con los lineamientos del curso: ¿cuáles coinciden? ¿Agregó alguna que no está en los lineamientos?

## Referencias bibliográficas

3Blue1Brown. (2024). *Large language models explained briefly* [video]. YouTube. https://www.youtube.com/watch?v=LPZh9BOjkQs
\
\
Del Cisne Loján, M., Antonio Romero, J., Sancho Aguilera, D. y Yajaira Romero, A. (2024). Consecuencias de la dependencia de la inteligencia artificial en habilidades críticas y aprendizaje autónomo en los estudiantes. *Ciencia Latina Revista Científica Multidisciplinar*, *8*(2), 2368–2382. https://ciencialatina.org/index.php/cienciala/article/view/10678
\
\
Stanford University. (2025). *CS146S: The modern software developer*. Recuperado el 16 de agosto de 2026, de https://themodernsoftware.dev/
\
\
UNESCO. (2025). *Marco de competencias para estudiantes en materia de IA*. https://unesdoc.unesco.org/ark:/48223/pf0000393812 (Obra original publicada en 2024)
\
\
UNESCO IESALC. (2023). *ChatGPT e inteligencia artificial en la educación superior: Guía de inicio rápido*. UNESCO. https://unesdoc.unesco.org/ark:/48223/pf0000385146_spa
\
\
Universidad de Costa Rica. (2026). *Marco de gobernanza y gestión de la inteligencia artificial en la Universidad de Costa Rica*. https://ci.ucr.ac.cr/marco-gobernanza-gestion-ia
