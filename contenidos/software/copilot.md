# GitHub Copilot

[GitHub Copilot](https://github.com/features/copilot) es el asistente de IA integrado en [Visual Studio Code](vscode.md): sugiere autocompletados de código mientras se escribe y ofrece un chat dentro del editor. Es uno de los asistentes presentados en la lección de [asistentes de programación basados en IA](../i-introduccion-ciencia-datos-programacion/07-asistentes-ia.md) y su uso en el curso comienza en la semana 5. Esta guía explica cómo activarlo y configurarlo; requiere VS Code instalado según su [guía](vscode.md) y la cuenta de GitHub creada en la lección de [Git, GitHub y GitHub Pages](../i-introduccion-ciencia-datos-programacion/05-git-github.md).

## Activación

### Instalación de la extensión

Haga clic en el ícono de Copilot en la barra de estado de VS Code (abajo a la derecha) y elija *Set up Copilot*: VS Code instala la extensión necesaria. Si prefiere hacerlo a mano, instale desde el panel de extensiones la extensión **GitHub Copilot Chat**, publicada por GitHub. Esa sola extensión incluye los autocompletados y el chat; la extensión **GitHub Copilot** (sin "Chat") quedó obsoleta y no hace falta instalarla, y las demás con nombre parecido (*for Azure*, *Nightly*, etc.) no se usan en el curso.

(copilot-inicio-sesion)=
### Inicio de sesión con la cuenta de GitHub

1. Haga clic en el ícono de Copilot en la barra de estado y elija *Sign in to use Copilot*. Otra vía es el ícono de *Accounts* (la silueta, abajo a la izquierda) y luego *Sign in with GitHub to use GitHub Copilot*.
2. VS Code abre el navegador en GitHub. Si no tiene la sesión iniciada, ingrese con su usuario, su contraseña y el segundo factor de autenticación, si lo tiene activado.
3. GitHub pide autorizar a *Visual Studio Code* para usar su cuenta. Haga clic en *Authorize* (o *Continue*).
4. El navegador pregunta si desea volver a VS Code. Acepte, y en VS Code confirme el aviso *Allow an extension to open this URI*.
5. Si es la primera vez y su cuenta no tiene plan de Copilot, VS Code ofrece activar el plan gratuito con un clic.

Si el navegador no logra devolverle a VS Code (ocurre a veces en Linux o cuando el navegador usa otro perfil), en el diálogo de inicio de sesión elija la opción de código de dispositivo: VS Code muestra un código de ocho caracteres; abra [github.com/login/device](https://github.com/login/device), ingrese el código y autorice.

### Verificación

Al terminar, el ícono de Copilot en la barra de estado deja de mostrar la marca de alerta y, al escribir código, aparecen sugerencias en gris que se aceptan con la tecla *Tab*. Para comprobar la cuenta conectada, haga clic en el ícono de *Accounts*: debe listar su usuario de GitHub. Si necesita cambiar de cuenta, elija ahí *Sign out* y repita el inicio de sesión.

Con el plan gratuito basta para comenzar; sus límites y la forma de ampliarlos se explican en la sección siguiente.

## Planes

El plan gratuito para cuentas personales (**Copilot Free**) tiene límites mensuales de uso: a octubre de 2026, 2000 autocompletados y un uso limitado del chat, con el modelo elegido automáticamente por Copilot. Son suficientes para los ejercicios del curso, pero ajustados para el proyecto final.

### Copilot Student gratuito con GitHub Education

[GitHub Education](https://github.com/education) ofrece gratis a estudiantes verificados el plan **Copilot Student**, que desde marzo de 2026 sustituye al Copilot Pro que antes recibían: autocompletados ilimitados y una asignación mensual de créditos de IA para el chat mayor que la del plan gratuito (aunque menor que la de Copilot Pro, el plan de pago), también con selección automática de modelo. **Se recomienda solicitar la verificación desde ya**: el proceso puede tardar varios días y conviene tenerla lista antes de la semana 5.

1. Agregue su correo institucional (`@ucr.ac.cr`) a su cuenta de GitHub (*Settings > Emails*).
2. En [GitHub Education](https://github.com/education), solicite los beneficios de estudiante (*Join GitHub Education*) con ese correo, y aporte la prueba de matrícula que se le pida (ej. una constancia o el carné).
3. Al aprobarse la solicitud, abra la [página de beneficios de GitHub Education](https://github.com/settings/education/benefits), elija *Learn more* bajo *Free GitHub developer resources for students and teachers* y siga las indicaciones para activar Copilot Student. El beneficio puede tardar varios días en aplicarse después de la verificación; si pasado ese tiempo la [página de configuración de Copilot](https://github.com/settings/copilot) sigue mostrando el plan gratuito, contacte al soporte de GitHub.

### Consultar el consumo

Cada plan incluye una asignación mensual que se reinicia el primer día de cada mes a las 00:00 UTC; lo que no se usa se pierde. En el plan gratuito la asignación se expresa en autocompletados y en un uso limitado del chat. En Copilot Student y Copilot Pro los autocompletados son ilimitados y el chat se mide en **créditos de IA**: cada mensaje descuenta créditos según el modelo que lo atiende y la cantidad de texto que procesa (a octubre de 2026, Copilot Pro incluye 1500 créditos al mes; GitHub no publica la cifra de Copilot Student). Conviene revisar el consumo de vez en cuando, sobre todo durante el proyecto final, para no quedarse sin asistente a mitad de una tarea. Hay dos vías:

- **En VS Code**: haga clic en el ícono de Copilot en la barra de estado (abajo a la derecha). El menú muestra las funciones incluidas en su plan, el porcentaje consumido de cada límite y la fecha en que se reinicia la asignación. Es la vía más rápida.
- **En GitHub**: abra la [página de facturación de su cuenta](https://github.com/settings/billing). La sección *Metered usage* muestra, junto al ícono de Copilot, lo consumido en el mes; el apartado de analítica de la barra lateral desglosa el uso por día y por modelo.

Si agota la asignación, los autocompletados y el chat se pausan hasta el siguiente mes, salvo que fije un presupuesto de pago en la misma página de facturación. Para el curso no hace falta: basta con usar el chat con criterio, por ejemplo con preguntas concretas sobre el fragmento de código en cuestión en vez de pegar archivos completos.

## Sugerencias automáticas y aprendizaje

Se recomienda mantener las sugerencias automáticas desactivadas mientras se aprende un tema nuevo: primero intente resolver los ejercicios por su cuenta y use el asistente para pedir explicaciones o revisar su solución, según los lineamientos de uso de IA del curso (declarar el uso, comprender y verificar todo el código que entregue). Desactivarlas no afecta al chat: el panel de chat y el chat en línea siguen funcionando, que es justo la combinación recomendada.

### Desactivar y reactivar las sugerencias

Desde el ícono de Copilot en la barra de estado de VS Code (abajo a la derecha):

- **Desactivar**: haga clic en el ícono y elija *Snooze* para pausarlas por unos minutos, o desmarque *Code completions* (en versiones anteriores, *Disable completions*). Ahí mismo puede desactivarlas solo para el lenguaje del archivo abierto, por ejemplo Python, y dejarlas activas para el resto.
- **Reactivar**: en el mismo menú, marque de nuevo *Code completions* (o *Enable completions*). Si usó *Snooze*, vuelven solas al terminar el tiempo, o antes con *Unsnooze*.

El ícono cambia de aspecto cuando están desactivadas (aparece tachado o con una marca), así que el estado se nota de un vistazo. También sirve la paleta de comandos (`Ctrl+Shift+P`) escribiendo *Copilot: Disable Completions* o *Copilot: Enable Completions*. La configuración permanente está en *File > Preferences > Settings*, buscando `github.copilot.enable`, donde puede fijar por lenguaje cuáles reciben sugerencias.

## Uso en el curso

El curso incorpora Copilot de forma paulatina, según el calendario de la lección de [asistentes de IA](../i-introduccion-ciencia-datos-programacion/07-asistentes-ia.md):

- **Semana 5**: el chat, para explicar código y mensajes de error y ayudar a depurar (con la estructura de prompts practicada en el cuaderno de [estructuras de datos y servicios web](../ii-lenguaje-programacion-python/11-estructuras-datos-apis.ipynb)).
- **Semana 7**: generación y verificación de código de análisis de datos.
- **Semana 15**: herramientas agénticas, revisión crítica del código generado y documentación de su uso.

En todas las etapas aplican los mismos lineamientos: el uso se declara en los trabajos, y todo el código que se entregue debe comprenderse y poder explicarse.

### Abrir el chat

Con la extensión instalada y la sesión de GitHub iniciada, el chat ya está activo; solo hay que abrirlo:

- **Panel de chat**: haga clic en el ícono de Copilot en la barra superior de VS Code (al centro, junto al cuadro de búsqueda) y elija *Open Chat*, o use el atajo `Ctrl+Alt+I` (`Ctrl+Cmd+I` en macOS). Se abre un panel lateral con el cuadro para escribir.
- **Chat en línea**: con el cursor sobre el código, o con líneas seleccionadas, presione `Ctrl+I`. Aparece un cuadro flotante para pedir una explicación o un cambio sobre ese fragmento.
- **Paleta de comandos**: `Ctrl+Shift+P` y escriba *Chat: Open Chat*.

Arriba del cuadro de texto está el selector de modo. Para la semana 5 conviene dejarlo en *Ask*, que solo responde sin modificar los archivos; los modos *Edit* y *Agent* corresponden a etapas posteriores del curso.

Si el ícono no aparece o el atajo no hace nada, revise en este orden:

1. **La extensión instalada es Copilot Chat**, no otra con nombre parecido. En el panel de extensiones (`Ctrl+Shift+X`) busque "GitHub Copilot Chat" y confirme que dice *Installed* y no *Disabled*.
2. **La sesión está iniciada**: el ícono de *Accounts*, abajo a la izquierda, debe listar su usuario de GitHub. Si no, siga los pasos de [inicio de sesión](#copilot-inicio-sesion).
3. **La cuenta tiene plan**: si es la primera vez, al abrir el chat VS Code ofrece activar el plan gratuito con un botón. Acéptelo. Si ya tiene Copilot Student por GitHub Education, no pide nada.
4. **VS Code está actualizado**: el chat requiere una versión reciente. Use *Help > Check for Updates* (o el gestor de paquetes, en Linux).
