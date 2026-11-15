# Herramientas agénticas de inteligencia artificial para programación

## Trabajo previo

### Lecturas

Antes de la clase, revise las siguientes lecturas. De la primera, en inglés, interesa la descripción general del curso (*Overview*), que ya se leyó en la semana 2: vuelva a ella con la experiencia de este semestre y observe cuánto de su temario trata sobre agentes. La segunda es la página de la documentación de GitHub, en español, que describe el uso de Copilot CLI, una de las dos herramientas agénticas que se usan en esta lección.

Stanford University. (2025). *CS146S: The modern software developer*. Recuperado el 15 de noviembre de 2026, de https://themodernsoftware.dev/
\
\
GitHub. (s. f.). *Uso de la CLI de GitHub Copilot*. GitHub Docs. Recuperado el 15 de noviembre de 2026, de https://docs.github.com/es/copilot/how-tos/use-copilot-agents/use-copilot-cli

### Software

Instale Copilot CLI según la sección [Copilot CLI](../software/copilot.md#copilot-cli) de la guía de GitHub Copilot y compruebe que el chat de Copilot funciona en Visual Studio Code. Tenga a mano, en su computadora, la carpeta del repositorio de su proyecto final, con la aplicación en el estado en que la dejó la semana anterior.

## Introducción

La lección de [asistentes de programación basados en inteligencia artificial](../i-introduccion-ciencia-datos-programacion/07-asistentes-ia.md) presentó tres modalidades de asistentes. Las dos primeras ya se usaron en el curso: los asistentes conversacionales y el chat integrado en el editor, para explicar y depurar código (semana 5) y para generarlo y verificarlo (semana 7). En ambas, la persona que programa es quien ejecuta: copia el código que el asistente propone, lo pega, lo corre y regresa con el resultado.

Las **herramientas agénticas** eliminan ese ir y venir: leen los archivos del proyecto, los modifican y ejecutan comandos por su cuenta, en varios pasos encadenados, hasta completar la tarea que se les encargó. Esto las hace mucho más productivas y también cambia el trabajo de quien las usa, que pasa de escribir código a **delegar** tareas, **supervisar** acciones y **revisar** resultados. Esta lección explica cómo funcionan, propone un flujo de trabajo para usarlas con seguridad en la aplicación del [proyecto final](../evaluaciones/proyecto-final.md), y desarrolla las dos habilidades que el programa del curso pide para esta etapa: la revisión crítica del código generado y la documentación de su uso.

## Qué es un agente

Un **agente** es un modelo de lenguaje de gran tamaño (LLM) conectado a un conjunto de **herramientas** que puede invocar: leer un archivo, buscar un texto en una carpeta, editar un archivo, ejecutar un comando en la terminal o consultar una página web. El modelo sigue haciendo lo mismo que en un chat, predecir texto, pero parte de ese texto son solicitudes de uso de una herramienta. El programa que rodea al modelo ejecuta la solicitud, le devuelve el resultado, y el modelo decide el paso siguiente. Ese **ciclo del agente** se repite hasta que el modelo considera terminada la tarea, como muestra la figura 1.

```{mermaid}
flowchart LR
  T([Tarea en<br>lenguaje natural]) --> M([Modelo de lenguaje])
  M -- solicita una acción --> A{¿Aprobada por<br>la persona?}
  A -- sí --> H([Herramienta:<br>leer, editar, ejecutar])
  A -- no --> M
  H -- resultado --> M
  M -- tarea terminada --> R([Resumen y<br>cambios por revisar])
```

<p style="text-align: center;"><strong>Figura 1</strong>. Ciclo de un agente de programación. Elaboración propia con base en GitHub (s. f.).</p>

Una tarea como "agregue a la aplicación un botón para descargar la tabla" puede tomar una decena de vueltas del ciclo: el agente lista los archivos de la carpeta, lee `app.py`, busca dónde se crea la tabla, edita el archivo, ejecuta la aplicación para comprobar que no falla y redacta un resumen de lo que hizo. La tabla 1 compara esta forma de trabajo con la del chat.

<figure style="text-align: center; margin: 20px 0;">
    <figcaption><strong>Tabla 1</strong>. Diferencias entre un asistente conversacional y una herramienta agéntica. Elaboración propia.</figcaption>
    <table class="table table-bordered table-striped" style="margin: 0 auto;">
    <thead>
      <tr>
        <th>Aspecto</th>
        <th>Chat</th>
        <th>Agente</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Qué ve</td>
        <td>Lo que la persona pega o adjunta en la conversación.</td>
        <td>Los archivos de la carpeta del proyecto, que lee por su cuenta.</td>
      </tr>
      <tr>
        <td>Qué produce</td>
        <td>Texto y código en la conversación.</td>
        <td>Cambios en los archivos y comandos ejecutados.</td>
      </tr>
      <tr>
        <td>Quién ejecuta</td>
        <td>La persona, que copia, pega y corre.</td>
        <td>El agente, con la aprobación de la persona.</td>
      </tr>
      <tr>
        <td>Unidad de trabajo</td>
        <td>Una pregunta y su respuesta.</td>
        <td>Una tarea de varios pasos.</td>
      </tr>
      <tr>
        <td>Papel de la persona</td>
        <td>Preguntar e integrar las respuestas.</td>
        <td>Delegar, supervisar las acciones y revisar los cambios.</td>
      </tr>
      <tr>
        <td>Riesgo principal</td>
        <td>Aceptar una respuesta equivocada.</td>
        <td>Además, que una acción dañe archivos o que un cambio pase sin revisión.</td>
      </tr>
    </tbody>
    </table>
</figure>

Todas las limitaciones de los LLM vistas en la semana 2 siguen presentes en un agente: alucina funciones que no existen, desconoce las versiones recientes de las bibliotecas y tiende a complacer. La diferencia es que ahora esas limitaciones se traducen en **acciones**, no solo en texto, y que los errores se acumulan: una suposición equivocada en el segundo paso se arrastra a los diez siguientes. Por eso el ciclo incluye a una persona que aprueba las acciones y, sobre todo, que revisa el resultado.

*Ejercicios de esta sección: [ejercicios sobre agentes](#ejercicios-agentes).*

## Herramientas agénticas del curso

Las herramientas agénticas se presentan en dos formas: integradas en el editor de código o como programas de la terminal. El curso usa una de cada forma, ambas de GitHub Copilot, porque funcionan con la misma cuenta y el mismo plan que ya se tienen configurados:

- **El agente del chat de Visual Studio Code.** En el cuadro de texto del chat hay un selector de agente: con *Agent* seleccionado, Copilot deja de limitarse a responder y puede editar los archivos de la carpeta abierta y ejecutar comandos en la terminal integrada. Junto a ese selector está el de permisos, que debe quedar en *Manual permissions*: cada comando pide aprobación (*Allow Once*) antes de ejecutarse. Los cambios en los archivos quedan marcados en el editor como pendientes de revisión, cada uno con los botones *Keep* (conservar) y *Undo* (deshacer). Además, el chat guarda un **punto de control** antes de cada solicitud: al pasar el cursor sobre un mensaje anterior, *Restore Checkpoint* devuelve los archivos al estado que tenían en ese momento (Microsoft, s. f.).
- **Copilot CLI.** Es un agente que se ejecuta en la terminal, dentro de la carpeta del proyecto, con el comando `copilot`. Antes de cada acción muestra lo que va a hacer y espera la aprobación. Su instalación, el primer uso y sus comandos se explican en la [guía de GitHub Copilot](../software/copilot.md#copilot-cli).

Los nombres de los botones y de los menús de estas herramientas cambian con frecuencia entre versiones; lo que se mantiene son los tres mecanismos de control que esta lección usa: la **aprobación** de cada acción, la **revisión** de los cambios y la posibilidad de **revertirlos**.

Existen otras herramientas de la misma familia, como [Claude Code](https://claude.com/claude-code), [Gemini CLI](https://github.com/google-gemini/gemini-cli) y [Codex](https://openai.com/codex/), que funcionan con el mismo ciclo y a las que se aplica todo lo que sigue.

Conviene tener presente el consumo: un agente lee archivos completos y encadena muchos pasos por cada instrucción, así que gasta bastante más de la asignación mensual que una pregunta en el chat. La guía explica [cómo consultar el consumo](../software/copilot.md#copilot-consumo); con tareas pequeñas y bien delimitadas, la asignación de Copilot Student alcanza para el proyecto.

*Ejercicios de esta sección: [ejercicios sobre las herramientas](#ejercicios-herramientas-agenticas).*

## Flujo de trabajo con un agente

Un agente es útil en la medida en que sus cambios puedan revisarse y, si no sirven, descartarse sin pérdidas. El flujo de trabajo que se propone, resumido en la figura 2, se apoya para ello en Git, que ya se usa en el proyecto.

```{mermaid}
flowchart LR
  A([1. Punto de partida<br>limpio: commit]) --> B([2. Tarea pequeña<br>y precisa])
  B --> C([3. Plan del agente])
  C --> D([4. Acciones<br>aprobadas una a una])
  D --> E([5. Revisión<br>del diff])
  E --> F([6. Verificación:<br>ejecutar y comprobar])
  F -- correcto --> G([7. Commit<br>con declaración])
  F -- incorrecto --> H([Corregir o revertir])
  H --> B
```

<p style="text-align: center;"><strong>Figura 2</strong>. Flujo de trabajo propuesto para delegar una tarea a un agente. Elaboración propia.</p>

### Punto de partida limpio

Antes de darle una tarea al agente, se confirman con un *commit* todos los cambios pendientes, de modo que `git status` indique que no hay nada por confirmar. Así, todo lo que cambie después es obra del agente, puede verse completo con `git diff` y puede descartarse de una vez. Sin este paso, los cambios del agente se mezclan con los propios y ya no es posible separarlos.

### Instrucciones del proyecto

Un agente no sabe nada del proyecto más allá de lo que lee en la carpeta. Lo que conviene que sepa siempre (qué es la aplicación, con cuáles versiones trabaja, qué convenciones sigue) se escribe una sola vez en un archivo de instrucciones que el agente lee al inicio de cada sesión. El formato más extendido es un archivo de texto en Markdown llamado [`AGENTS.md`](https://agents.md/), en la raíz del repositorio, que reconocen tanto el agente de VS Code como Copilot CLI. Por ejemplo:

```markdown
# Instrucciones para agentes

Aplicación de streamlit del proyecto final del curso GF-0657 (UCR).
Muestra <tema> con una tabla, un gráfico de plotly y un mapa de folium.

## Reglas
- Responda y comente el código en español.
- Versiones: streamlit 1.61 y streamlit-folium 0.27. No use funciones
  obsoletas (st.cache, use_container_width, folium_static).
- Los datos se cargan desde URL en funciones con @st.cache_data; nunca
  desde rutas locales absolutas.
- Las capas que van al mapa se reproyectan a WGS84 (EPSG:4326).
- No agregue bibliotecas nuevas sin preguntar; si agrega una, inclúyala
  en requirements.txt con su versión.
- Haga solo lo que pide la tarea: no reorganice ni reformatee el resto
  del código.
- Para comprobar un cambio, ejecute: streamlit run app.py
```

Las reglas más útiles son las que previenen los errores que ya se han visto: las de este ejemplo salen de la clínica de errores del [cuaderno de streamlit](22-streamlit-aplicaciones-web.ipynb). El archivo se confirma en el repositorio como cualquier otro y se amplía cuando el agente repite un error.

### Tareas pequeñas y precisas

La calidad del resultado depende de la tarea que se encarga. Una buena tarea tiene cuatro partes:

1. **Objetivo**: qué debe quedar hecho, en una oración.
2. **Contexto**: en cuáles archivos y con cuáles datos (nombres de las columnas, de las funciones y de los controles que ya existen).
3. **Restricciones**: qué no debe tocar y qué debe respetar.
4. **Criterio de terminado**: cómo se comprueba que quedó bien.

Compárense dos formas de pedir lo mismo. La primera, "mejore la aplicación", deja al agente decidir qué es mejorar, y lo usual es que reescriba medio archivo. La segunda delimita el cambio y lo hace revisable:

```text
En app.py, agregue en la barra lateral un deslizador "Densidad mínima"
(de 0 a 1000 hab/km², paso de 50, valor inicial 0) que filtre los
cantones por la columna densidad. El filtro debe aplicarse en la función
filtrar(), para que afecte a los indicadores, la tabla, el gráfico y el
mapa. No modifique las funciones de carga ni agregue bibliotecas. Al
terminar, la aplicación debe correr con streamlit run app.py sin errores
y, con la densidad mínima en 500 y todas las provincias, mostrar solo
los cantones de más de 500 hab/km².
```

Como regla práctica, una tarea tiene el tamaño adecuado si sus cambios pueden leerse completos en pocos minutos. Una funcionalidad grande se divide en varias tareas, cada una con su revisión y su *commit*.

### Plan antes de la acción

Antes de permitir que el agente modifique algo, se le pide que explique lo que piensa hacer. Copilot CLI tiene para ello un modo de planificación, que se alterna con `Shift+Tab`; en cualquier herramienta basta con terminar la tarea con la frase "antes de modificar archivos, presente el plan y espere mi aprobación". Leer el plan toma un minuto y es el momento más barato para corregir un malentendido: si el plan menciona un archivo que no debería tocarse o una biblioteca que no se pidió, se corrige ahí, antes de que exista una sola línea de código que revisar.

### Aprobación de las acciones

Durante la ejecución, cada acción se aprueba individualmente, después de leerla. Las opciones de aprobar "por el resto de la sesión" ahorran clics, pero convierten la supervisión en un trámite. Leer un archivo del proyecto o ejecutar `git status` no cambia nada y puede aprobarse sin más; un comando que instala, borra, mueve o publica algo merece leerse con atención, y si no se entiende lo que hace, se rechaza y se le pregunta al agente.

### Revisión, verificación y cierre

Cuando el agente termina, su resumen ("listo, agregué el deslizador y verifiqué que funciona") es una afirmación más del modelo, no una prueba. El trabajo de la persona empieza ahí:

1. **Revisar** todos los cambios con `git diff` en la terminal, con el panel *Source Control* de VS Code (al hacer clic en cada archivo modificado se abre la comparación) o con `/diff` en Copilot CLI. La sección siguiente dice qué buscar.
2. **Verificar** el comportamiento: ejecutar la aplicación con `streamlit run app.py`, probar el cambio con valores cuyo resultado se conoce de antemano, y probar también lo que no debía cambiar.
3. **Cerrar**: si todo está bien, confirmar con un *commit* que declare la asistencia; si no, pedir la corrección o descartar los cambios. `git restore .` devuelve los archivos modificados al estado del último *commit*, y `git status` muestra los archivos nuevos que el agente haya creado, que se borran a mano.

Un mensaje de *commit* puede declarar la asistencia con una línea final, como hace el [historial del repositorio de este curso](https://github.com/gf0657-programacionsig/2026-ii/commits/):

```text
Agrega el filtro de densidad mínima

Co-Authored-By: GitHub Copilot <noreply@github.com>
```

*Ejercicios de esta sección: [ejercicios sobre el flujo de trabajo](#ejercicios-flujo-agentes).*

## Revisión crítica del código generado

Revisar código ajeno es una habilidad distinta de escribirlo, y con los agentes pasa a ser la principal. Los cambios se leen en forma de **diff**: las líneas que empiezan con `-` son las que se eliminaron y las que empiezan con `+`, las que se agregaron. El siguiente fragmento, de una aplicación como la del cuaderno de streamlit, muestra un cambio típico de un agente:

```diff
 @st.cache_data
 def cargar_cantones():
-    cantones = gpd.read_file(f"{DATOS}/ign/cantones.gpkg").to_crs(4326)
+    cantones = gpd.read_file("datos/cantones.gpkg")
     poblacion = pd.read_csv(f"{DATOS}/inec/cantones-2022.csv")
```

El cambio parece inofensivo y la aplicación incluso puede abrir sin errores, pero tiene dos problemas: la capa ya no se carga desde la URL, sino desde un archivo que quizá solo existe en la computadora donde trabajó el agente, y se perdió la reproyección a WGS84, con lo que el mapa quedará vacío. Ninguno de los dos se habría detectado leyendo solo el resumen del agente. La tabla 2 reúne las preguntas con las que conviene leer cada diff.

<figure style="text-align: center; margin: 20px 0;">
    <figcaption><strong>Tabla 2</strong>. Lista de comprobación para revisar los cambios de un agente. Elaboración propia.</figcaption>
    <table class="table table-bordered table-striped" style="margin: 0 auto;">
    <thead>
      <tr>
        <th>Pregunta</th>
        <th>Qué buscar</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>¿Hizo lo que se pidió, y solo eso?</td>
        <td>Archivos o funciones modificados que la tarea no mencionaba; código reformateado o reorganizado sin motivo; funcionalidad que desapareció.</td>
      </tr>
      <tr>
        <td>¿Existen y están vigentes las funciones que usa?</td>
        <td>Funciones y argumentos inventados u obsoletos (<code>st.cache</code>, <code>use_container_width</code>, <code>folium_static</code>). Se contrastan con la documentación de la versión instalada.</td>
      </tr>
      <tr>
        <td>¿Son correctos los datos y los resultados?</td>
        <td>Rutas locales, nombres de columnas supuestos, SRC equivocado o ausente, datos de ejemplo inventados en lugar de los reales; cifras que no coinciden con las conocidas.</td>
      </tr>
      <tr>
        <td>¿Ocultó un problema en lugar de resolverlo?</td>
        <td>Bloques <code>try/except</code> que silencian un error, comprobaciones eliminadas o debilitadas, valores fijos puestos para que una prueba pase.</td>
      </tr>
      <tr>
        <td>¿Cambió las dependencias?</td>
        <td>Bibliotecas nuevas importadas; <code>requirements.txt</code> sin actualizar o con versiones cambiadas.</td>
      </tr>
      <tr>
        <td>¿Expone información que no debe publicarse?</td>
        <td>Claves de acceso, contraseñas o datos personales escritos en el código o en archivos nuevos.</td>
      </tr>
      <tr>
        <td>¿Puedo explicar cada línea?</td>
        <td>Código que funciona pero no se entiende. Se le pide al agente que lo explique o que lo simplifique; lo que no se logre comprender no se entrega.</td>
      </tr>
    </tbody>
    </table>
</figure>

Algunos errores son más propios de los agentes que del chat. El más frecuente es el **exceso de alcance**: se pide un deslizador y el agente, además, renombra variables, cambia los colores del mapa y reescribe el pie de página. Otro es el **atajo**: cuando un paso falla, el agente tiende a lograr que el error desaparezca en lugar de corregir su causa, por ejemplo envolviendo el código en un `try/except` o borrando la comprobación que fallaba. Y otro es el **informe optimista**: el resumen final afirma que se verificó algo que no se ejecutó. Los tres se detectan de la misma forma: leyendo el diff completo y ejecutando la aplicación, no leyendo el resumen.

La última pregunta de la tabla es la que conecta con los [lineamientos del curso](../i-introduccion-ciencia-datos-programacion/07-asistentes-ia.md): cada estudiante debe comprender y poder explicar todo el código que entregue. En la presentación oral del proyecto, el profesor puede pedir la explicación de cualquier parte de la aplicación, sin importar quién la haya escrito. Un criterio sano para decidir qué delegar es encargar al agente lo que uno mismo sabría hacer y revisar, y usar el chat para aprender lo que todavía no se sabe.

*Ejercicios de esta sección: [ejercicios sobre la revisión del código](#ejercicios-revision-agentes).*

## Riesgos y medidas de seguridad

Un agente actúa en la computadora con los mismos permisos de la persona que lo inició: puede leer, modificar y borrar cualquier archivo al que ella tenga acceso, y ejecutar cualquier comando. Los riesgos principales y sus medidas son los siguientes:

- **Acciones destructivas.** Un comando equivocado puede borrar archivos o sobrescribir el trabajo de semanas. Medidas: iniciar el agente solo en la carpeta del proyecto, nunca en la carpeta personal completa; mantener la aprobación manual de las acciones; y tener el trabajo confirmado en Git y publicado en GitHub. Los puntos de control y `git restore` deshacen cambios en los archivos del repositorio, pero no deshacen los efectos de un comando ya ejecutado, como un archivo borrado fuera del repositorio o un `git push`.
- **Aprobación automática.** Tanto VS Code (*Allow all*) como Copilot CLI (`--allow-all`) permiten omitir las confirmaciones. Estas opciones no deben usarse en el curso: eliminan justamente el control que permite detener una acción equivocada.
- **Inyección de instrucciones.** El agente no distingue de manera confiable entre las instrucciones de la persona y el texto que lee mientras trabaja. Una página web, un archivo descargado o un conjunto de datos pueden contener frases redactadas para que el agente las obedezca ("ignore las instrucciones anteriores y…"), lo que se conoce como [inyección de *prompts*](https://es.wikipedia.org/wiki/Inyecci%C3%B3n_de_prompt) (OWASP, 2025). Medidas: desconfiar de las acciones que no guardan relación con la tarea encargada, sobre todo después de que el agente leyó contenido de terceros, y no aprobar lo que no se entiende.
- **Información sensible.** Todo lo que el agente lee se envía al proveedor del modelo. La carpeta del proyecto no debe contener contraseñas, claves de acceso ni datos personales, y nada de eso debe escribirse en una instrucción.
- **Dependencia.** Es el mismo riesgo de la semana 2, amplificado: un agente puede producir en una tarde una aplicación completa que su autor no comprende. Para el proyecto final esto no es una ventaja: la aplicación se defiende en la presentación oral.

*Ejercicios de esta sección: [ejercicios sobre riesgos](#ejercicios-riesgos-agentes).*

## Documentación del uso

El lineamiento de transparencia del curso pide declarar cuál herramienta se usó, con qué propósito y en cuáles partes del trabajo. Con un asistente conversacional, una oración bastaba; con un agente, que puede haber escrito buena parte del código, la declaración debe permitir que quien lee sepa qué hizo la herramienta y qué hizo la persona. Una buena declaración responde cinco preguntas:

1. **Cuál herramienta** y en cuál modalidad (chat, agente del editor, agente de la terminal).
2. **Cuáles tareas** se delegaron y en cuáles archivos o partes del trabajo.
3. **Cómo se revisó**: lectura de los cambios, ejecución, cifras contrastadas.
4. **Qué se corrigió o descartó** de lo generado.
5. **Qué se hizo sin asistencia**.

Por ejemplo, en el `README.md` de una aplicación:

```markdown
## Uso de inteligencia artificial

Se usó GitHub Copilot en modo agente (VS Code) y Copilot CLI para dos
tareas de app.py: agregar el filtro de densidad mínima y el botón de
descarga de la tabla. La carga de los datos, el mapa y el gráfico se
escribieron sin asistencia, a partir del código de la tarea 3. Cada
cambio generado se revisó con git diff y se probó con streamlit run;
las cifras de los indicadores se contrastaron con las de la tarea 3. Se
descartó una propuesta del agente que leía la capa desde una ruta local
y se sustituyó use_container_width, que el agente usó en la tabla, por
width="stretch". Los commits elaborados con asistencia llevan la línea
Co-Authored-By.
```

Para poder escribirla al final, conviene registrar el uso mientras ocurre. Tres prácticas lo facilitan: un *commit* por cada tarea delegada, con la línea `Co-Authored-By`; una lista breve, en un archivo de notas, de las instrucciones principales que se dieron y de lo que hubo que corregir; y el archivo `AGENTS.md` en el repositorio, que documenta las reglas con que trabajó el agente.

El proyecto final pide esta declaración en tres lugares: en el `README.md` de la aplicación, en una sección del documento computacional y, de forma oral, en la parte de la presentación dedicada al proceso de desarrollo.

*Ejercicios de esta sección: [ejercicios sobre la documentación del uso](#ejercicios-documentacion-agentes).*

## Resumen

- Una **herramienta agéntica** es un modelo de lenguaje conectado a **herramientas** (leer, editar, ejecutar) que usa en un **ciclo** de varios pasos hasta completar una tarea. Conserva todas las limitaciones de los LLM, pero ahora se expresan en acciones.
- El curso usa el **agente del chat de VS Code** y **Copilot CLI**. En ambos, los mecanismos de control son la **aprobación** de cada acción, la **revisión** de los cambios y la posibilidad de **revertirlos**.
- El **flujo de trabajo** propuesto: partir de un *commit* limpio, dar instrucciones permanentes en `AGENTS.md`, encargar **tareas pequeñas y precisas** (objetivo, contexto, restricciones y criterio de terminado), pedir un **plan**, aprobar las acciones una a una, revisar el **diff**, verificar ejecutando y cerrar con un *commit* o con `git restore`.
- La **revisión crítica** lee el diff completo, no el resumen del agente: alcance, funciones vigentes, datos y resultados, problemas ocultados, dependencias, información sensible y comprensión de cada línea. Los errores típicos son el **exceso de alcance**, el **atajo** y el **informe optimista**.
- Un agente actúa con los permisos de quien lo inicia: se usa solo en la carpeta del proyecto, sin **aprobación automática**, con el trabajo respaldado en Git, y con desconfianza ante la **inyección de instrucciones**.
- La **documentación del uso** declara la herramienta y su modalidad, las tareas delegadas, la revisión hecha, lo corregido y lo realizado sin asistencia, en el `README.md`, en el documento y en la presentación del proyecto final.

## Ejercicios

Los ejercicios se agrupan según la sección del capítulo a la que corresponden y se realizan sobre el repositorio de la aplicación de su proyecto final. Quien todavía no lo tenga puede usar una copia de la aplicación de ejemplo del [cuaderno de streamlit](22-streamlit-aplicaciones-web.ipynb) (`apps/07-app-proyecto.py`, guardada como `app.py` en un repositorio propio).

(ejercicios-agentes)=
### Qué es un agente

1. Abra en VS Code la carpeta de su proyecto y, con el agente del chat seleccionado y los permisos en *Manual permissions*, escriba: "Sin modificar ningún archivo, explique qué hace esta aplicación, cuáles datos carga y cuáles controles tiene". Observe el ciclo de la figura 1 y anote:
    - Cuáles archivos leyó el agente y si pidió aprobación para alguna acción.
    - Una afirmación de la explicación que sea correcta y, si la hay, una que sea imprecisa o falsa.

(ejercicios-herramientas-agenticas)=
### Herramientas agénticas del curso

2. Instale Copilot CLI según la [guía](../software/copilot.md#copilot-cli), inícielo en la carpeta de su proyecto y repita la instrucción del ejercicio 1. Compare las dos herramientas: ¿leyeron los mismos archivos?, ¿coinciden las explicaciones? Termine la sesión con `/exit`.
3. Consulte su consumo de Copilot antes y después del ejercicio 4, según la sección [Consultar el consumo](../software/copilot.md#copilot-consumo) de la guía, y anote cuánto gastó una tarea delegada a un agente.

(ejercicios-flujo-agentes)=
### Flujo de trabajo

4. Escriba el archivo `AGENTS.md` de su proyecto, a partir del ejemplo de la lección: describa su aplicación en dos líneas, liste sus fuentes de datos y adapte las reglas. Confírmelo con un *commit*.
5. Delegue una tarea pequeña siguiendo el flujo de la figura 2. Elija una mejora que su aplicación necesite para cumplir el enunciado del proyecto (un segundo control, el mensaje de `st.warning()` cuando la selección queda vacía, el botón de descarga de la tabla o el formato de las columnas con `column_config`).
    - Compruebe con `git status` que no hay cambios pendientes.
    - Redacte la tarea con sus cuatro partes (objetivo, contexto, restricciones y criterio de terminado) y pida el plan antes de cualquier modificación.
    - Apruebe las acciones una a una, leyéndolas.
    - Revise el diff, ejecute la aplicación y compruebe el criterio de terminado.
    - Si el resultado es correcto, confírmelo con un *commit* que lleve la línea `Co-Authored-By`.
6. Practique la reversión. Pida al agente un cambio que no piense conservar (ej. "cambie el título de la aplicación y los colores del mapa"). Revise el diff y luego descarte los cambios de dos maneras: una vez con *Restore Checkpoint* o *Undo* en VS Code, y otra, repitiendo el cambio, con `git restore .` en la terminal. Compruebe con `git status` que el repositorio quedó como antes.

(ejercicios-revision-agentes)=
### Revisión crítica del código generado

7. A un agente se le encargó la tarea del deslizador de densidad mínima que aparece en la sección de flujo de trabajo, sobre la aplicación de ejemplo del cuaderno de streamlit. Este es el diff que produjo. Revíselo con la tabla 2 y liste todos los problemas que encuentre, indicando para cada uno a cuál pregunta de la tabla corresponde y cómo lo comprobaría.

    ```diff
     import plotly.express as px
    +import seaborn as sns
     import streamlit as st
    @@
     @st.cache_data
     def cargar_cantones():
    -    cantones = gpd.read_file(f"{DATOS}/ign/cantones.gpkg").to_crs(4326)
    +    cantones = gpd.read_file("C:/Users/ana/proyecto/datos/cantones.gpkg")
         poblacion = pd.read_csv(f"{DATOS}/inec/cantones-2022.csv")
    @@
    -def filtrar(provincia, poblacion_minima):
    +def filtrar(provincia, poblacion_minima, densidad_minima=0):
         cantones = cargar_cantones()
         seleccion = cantones if provincia == "Todas" else cantones[cantones["provincia"] == provincia]
    -    return seleccion[seleccion["poblacion"].fillna(0) >= poblacion_minima]
    +    try:
    +        seleccion = seleccion[seleccion["densidad_poblacion"] >= densidad_minima]
    +    except Exception:
    +        pass
    +    return seleccion[seleccion["poblacion"].fillna(0) >= poblacion_minima]
    @@
     poblacion_minima = st.sidebar.slider("Población mínima", 0, 100_000, 0, step=5_000)
    +densidad_minima = st.sidebar.slider("Densidad mínima", 0, 1000, 0, step=50)
    @@
    -seleccion = filtrar(provincia, poblacion_minima)
    +seleccion = filtrar(provincia, poblacion_minima, densidad_minima)
    @@
    -col3.metric("Densidad (hab/km²)", f"{seleccion['poblacion'].sum() / seleccion['area_km2'].sum():,.0f}" if seleccion["area_km2"].sum() else "—")
    +col3.metric("Densidad (hab/km²)", f"{seleccion['poblacion'].sum() / seleccion['area_km2'].sum():,.0f}")
    @@
    -    st.dataframe(tabla, hide_index=True, width="stretch",
    +    st.dataframe(tabla, hide_index=True, use_container_width=True,
    @@
    -        mapa = copy.deepcopy(crear_mapa(provincia, poblacion_minima, variable))
    +        mapa = copy.deepcopy(crear_mapa(provincia, poblacion_minima, variable))  # el mapa ya responde al nuevo filtro
    ```

8. Aplique la tabla 2 al diff de su propia tarea del ejercicio 5 (puede verlo de nuevo con `git show`). Anote, para cada pregunta, lo que comprobó y cómo. Si encuentra algo que corregir, corríjalo y confírmelo.
9. Pida al agente, sin que modifique archivos, que revise su aplicación contra los rubros de calificación de la aplicación del [enunciado del proyecto final](../evaluaciones/proyecto-final.md), pegándolos en la instrucción. Evalúe el informe: ¿cuáles observaciones son correctas?, ¿cuáles no?, ¿qué pasó por alto? Anote dos mejoras que decida hacer y una sugerencia que decida no seguir, con la razón.

(ejercicios-riesgos-agentes)=
### Riesgos y medidas de seguridad

10. Un agente pide aprobación para cada una de las siguientes acciones mientras trabaja en la tarea "agregue un gráfico de barras a la aplicación". Clasifíquelas en tres grupos (se aprueba sin más, se aprueba solo después de leerla con cuidado, se rechaza) y justifique cada decisión.
    - `git status`
    - Leer `app.py`.
    - `pip install plotly-express-extras`
    - Editar `app.py`.
    - `rm -rf datos/`
    - `streamlit run app.py`
    - Leer el archivo `.env` de la carpeta personal.
    - `git push --force`
    - Editar `requirements.txt` para quitar las versiones.

(ejercicios-documentacion-agentes)=
### Documentación del uso

11. Redacte la sección "Uso de inteligencia artificial" del `README.md` de su proyecto, de modo que responda las cinco preguntas de la sección de documentación con lo que realmente hizo en los ejercicios 5 a 9. Confírmela en el repositorio.

## Referencias bibliográficas

GitHub. (s. f.). *Uso de la CLI de GitHub Copilot*. GitHub Docs. Recuperado el 15 de noviembre de 2026, de https://docs.github.com/es/copilot/how-tos/use-copilot-agents/use-copilot-cli
\
\
Microsoft. (s. f.). *Build with AI in VS Code*. Visual Studio Code. Recuperado el 15 de noviembre de 2026, de https://code.visualstudio.com/docs/agents/overview
\
\
OWASP. (2025). *LLM01:2025 Prompt injection*. OWASP Gen AI Security Project. https://genai.owasp.org/llmrisk/llm01-prompt-injection/
\
\
Stanford University. (2025). *CS146S: The modern software developer*. Recuperado el 15 de noviembre de 2026, de https://themodernsoftware.dev/
