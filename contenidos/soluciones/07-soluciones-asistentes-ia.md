---
short_title: "Asistentes de programación basados en inteligencia artificial"
---

# Soluciones — Asistentes de programación basados en inteligencia artificial

Soluciones y pautas de respuesta de los ejercicios de la lección [Asistentes de programación basados en inteligencia artificial](../i-introduccion-ciencia-datos-programacion/07-asistentes-ia.md). La mayoría de los ejercicios son abiertos: para cada uno se describen los elementos que debe incluir una buena respuesta y los errores esperables.

## Ejercicio 1 (abierto — explicación de un LLM y verificación de referencias)

No hay una única respuesta: depende del asistente y del momento. Elementos de una buena respuesta:

- La explicación obtenida menciona el entrenamiento con grandes volúmenes de texto y la predicción de la continuación más probable (coherente con la lección y con 3Blue1Brown).
- La verificación de las referencias es el corazón del ejercicio: cada referencia se busca en la Web (título entre comillas, autores). Resultados esperables: algunas referencias existen, otras son parcialmente correctas (autores reales con título inexistente, año equivocado, DOI que no resuelve) y otras son completamente inventadas. Cualquiera de los dos últimos casos es una alucinación observada de primera mano.
- Es esperable (y vale discutirlo) que los asistentes más recientes citen fuentes reales con más frecuencia, especialmente si usan búsqueda web; eso no elimina la obligación de verificar.
- Error frecuente: dar por verificada una referencia porque "suena" real o porque el asistente insiste en que existe. La verificación es externa (buscador, Google Scholar, DOI), nunca preguntándole al propio asistente.

## Ejercicio 2 (abierto — comparación de dos asistentes en un tema geográfico)

Respuesta personal. Elementos de una buena respuesta:

- Una misma pregunta formulada a dos asistentes distintos (captura o transcripción).
- Identificación de coincidencias y diferencias concretas (datos numéricos, nombres, énfasis, nivel de detalle, errores).
- Al menos un dato de cada respuesta verificado contra una fuente oficial nombrada (ej. INEC, IGN/SNIT, SINAC, municipalidad). Es común que los asistentes den cifras desactualizadas (censos viejos, áreas imprecisas) — conectar con el corte de conocimiento.
- Puntos de discusión: las respuestas suelen ser más débiles en temas locales y en español que en temas globales y en inglés (sesgos de los datos de entrenamiento); dos asistentes pueden dar datos contradictorios con igual seguridad.

## Ejercicio 3 (abierto — políticas de datos de un asistente)

Depende de la herramienta y de la fecha de consulta; las políticas cambian con frecuencia. Criterios de éxito:

- Identificar si la versión gratuita usa las conversaciones para entrenar y si existe una opción para desactivarlo (en varios asistentes existe, pero está poco visible en la configuración).
- Documentar dónde se encontró la información (página de privacidad, términos de servicio, centro de ayuda) o el hecho de no encontrarla: la opacidad es un hallazgo válido y esperado en algunos casos.
- Punto de discusión: la información suele estar en inglés, dispersa entre varios documentos legales y redactada de forma poco clara para personas no especialistas — esto ilustra por qué el lineamiento de privacidad del curso pide cautela con lo que se ingresa en estas herramientas.

## Ejercicio 4 (ciclo generar–comprender–verificar–criticar)

- El programa generado será similar a:

  ```python
  poblacion = 165000
  area = 267.71
  densidad = poblacion / area
  print(densidad)
  ```

  con variantes esperables: uso de `f-strings` en el `print()`, redondeo con `round()`, comentarios, o incluso una función `def densidad(poblacion, area):` — más elaboradas que la versión del ejercicio 5 de la lección 06, lo cual alimenta la comparación.
- La ejecución en Colab debe producir el valor correcto (verificable con una calculadora).
- En la comparación, el criterio no es cuál versión es "mejor", sino cuál se comprende: es esperable que la versión propia, más simple, se entienda por completo, y que la generada incluya construcciones aún no estudiadas (funciones, formato de hileras, manejo de errores). Ese contraste es el punto pedagógico: código más sofisticado que no se comprende vale menos, en este curso, que código simple que sí.
- Ante la pregunta por errores o limitaciones, una buena respuesta del asistente mencionará la división entre cero (si `area` es 0, Python produce `ZeroDivisionError`) y quizás valores negativos o tipos incorrectos. Evaluar críticamente: ¿la respuesta es correcta? ¿propone soluciones desproporcionadas para el nivel del curso? La adulación puede aparecer aquí: si se le insiste en que el programa está perfecto, es probable que el asistente termine dándole la razón.

## Ejercicio 5 (declaración de uso de IA)

Respuesta personal siguiendo el formato de la lección. Una buena declaración indica: la herramienta (con su versión o fecha si se conoce), el propósito específico (generar el programa de densidad, explicarlo línea por línea, identificar limitaciones), las partes del trabajo donde se usó y la revisión realizada (ejecución en Colab, comparación con la versión propia). Ejemplo:

```
Declaración de uso de IA: se utilizó Gemini (agosto de 2026) para generar
un programa de cálculo de densidad de población, pedir su explicación
línea por línea y consultar sus limitaciones (ejercicio 4). El programa
fue ejecutado y verificado en Google Colab y comparado con una versión
propia; las conclusiones del ejercicio son de la persona autora.
```

Errores esperables: declaraciones vagas ("se usó IA de apoyo") que no dicen herramienta, propósito ni partes; o declaraciones que omiten la revisión/verificación.

## Ejercicio 6 (abierto — decálogo personal)

Respuesta personal. Elementos de una buena respuesta:

- Cinco normas propias, formuladas en primera persona y accionables ("pediré explicaciones antes que soluciones", "verificaré toda referencia antes de citarla"), no repeticiones literales de los lineamientos.
- Comparación explícita con los lineamientos del curso: cuáles coinciden (transparencia, comprensión, verificación...) y cuáles agregan una dimensión nueva. Adiciones valiosas y esperables: límites de tiempo o momento de uso ("primero intento resolverlo sin IA"), bienestar ("no usarla para todo"), sostenibilidad ambiental, contraste entre asistentes, no usar IA para comunicaciones personales.
- Este ejercicio conecta con la práctica docente recomendada de construir normas de uso con el estudiantado; en clase puede hacerse una puesta en común para consolidar un decálogo del grupo.
