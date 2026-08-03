# Convenciones del repositorio

Este documento describe las convenciones de Git usadas en este repositorio.
Además de mantener el orden del proyecto, sirve como material de referencia
para el curso.

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

## Qué no se versiona

- El directorio `privado/` (calificaciones, documentos administrativos
  recibidos) está excluido mediante `.gitignore` y nunca debe publicarse.
- `programa/referencia.docx` se deriva de la plantilla interna de la Escuela
  de Geografía y se regenera localmente; tampoco se versiona.
- Antes de agregar archivos nuevos, verificar que no contengan datos
  personales de estudiantes ni documentos internos de la Escuela.
