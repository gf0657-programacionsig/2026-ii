---
short_title: "Git, GitHub y GitHub Pages"
---

# Soluciones — Git, GitHub y GitHub Pages

Soluciones y pautas de respuesta de los ejercicios de la lección [Git, GitHub y GitHub Pages](../i-introduccion-ciencia-datos-programacion/05-git-github.md). Los ejercicios son operativos o exploratorios; en cada caso se indican los elementos que deben encontrarse o verificarse y los errores esperables.

## Ejercicio 1 (repositorio con README)

Operativo; lista de verificación:

- Repositorio **público** llamado `practica-markdown` con *Add a README
  file* marcado (si no lo marcaron, el repo queda vacío y la interfaz
  cambia: puede crearse el archivo con *creating a new file*).
- El README debe quedar con el documento de la lección 4 y renderizado
  en la página principal.
- El mensaje de *commit* debe describir el cambio ("Agrega el documento
  sobre X", no el "Update README.md" que GitHub sugiere por defecto —
  vale la pena señalarlo en clase).
- Errores esperables: crear el repo privado (Pages no funcionará luego
  en cuentas gratuitas; conviene detectarlo aquí) y pegar el Markdown
  en el campo del mensaje de *commit*.

## Ejercicio 2 (historial y comparación de versiones)

- En *History* deben verse (al menos) tres *commits*: el inicial de
  GitHub, el del ejercicio 1 y el nuevo.
- En el diff, líneas agregadas en verde con `+` y eliminadas en rojo
  con `-`; una línea modificada aparece como eliminada + agregada
  (conviene hacerlo notar: Git registra líneas, no ediciones).
- En *Raw* se ve la fuente sin renderizar — refuerza la distinción
  fuente/salida de la lección 4.

## Ejercicio 3 (Git "en producción" en el repositorio del curso)

Exploratorio; elementos que deben encontrar:

- En *History* de `05-git-github.md`: varios *commits* con títulos en
  tercera persona del presente ("Agrega…", "Refina…"), como pide
  CONTRIBUTING; el diff de un *commit* muestra líneas `+`/`-` igual que
  en su propio repositorio — la mecánica es la misma a cualquier escala.
- En *Pull requests > Closed*: una PR fusionada (ej. #18) muestra la
  rama de origen (`sitio-leccion-04-mejoras`), la pestaña *Commits* con
  los *commits* que la componen y el evento "merged" con fecha.
- Conexión esperada con la lección: la rama + PR es el mecanismo de la
  figura 2 y de la sección GitHub; conviene hacer notar el trailer
  `Co-Authored-By` de los *commits* asistidos por IA, que enlaza con la
  política de IA del curso.
- Error esperable: buscar en *Pull requests* sin el filtro *Closed* y
  concluir que "no hay ninguna".

## Ejercicio 4 (GitHub Pages)

- *Settings > Pages > Deploy from a branch > main > / (root) > Save*.
- En *Actions* aparece el flujo "pages build and deployment"; la URL
  queda en `https://usuario.github.io/practica-markdown/`.
- La comparación esperada: mismo contenido, presentación distinta
  (Jekyll aplica su propio tema; no se ve la interfaz de GitHub).
- Errores esperables: visitar la URL antes de que termine el
  despliegue (404 transitorio; revisar *Actions*), repositorio privado
  (Pages deshabilitado en cuentas gratuitas) y esperar que la página
  se llame como el archivo (`README.md` se sirve como página inicial
  por ausencia de `index.md`).

## Ejercicio 5 (reflexión sobre reproducibilidad)

Elementos de una buena respuesta:

- Ubicación en el espectro de Peng (lección 1): un repositorio público
  con código, datos y documentación está cerca del extremo de
  reproducibilidad total ("código y datos enlazados y ejecutables");
  publicar solo el documento (como en este ejercicio) queda más cerca
  de "solo la publicación".
- Aporte del historial: procedencia (quién, qué, cuándo), posibilidad
  de reproducir versiones anteriores del análisis, no solo la final, y
  transparencia sobre cómo evolucionó.
- Respuesta débil esperable: "es reproducible porque está en Internet"
  — disponibilidad no basta; el espectro valora qué está disponible.
