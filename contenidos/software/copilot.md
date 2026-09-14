# GitHub Copilot

[GitHub Copilot](https://github.com/features/copilot) es el asistente de IA integrado en [Visual Studio Code](vscode.md): sugiere autocompletados de código mientras se escribe y ofrece un chat dentro del editor. Es uno de los asistentes presentados en la lección de [asistentes de programación basados en IA](../i-introduccion-ciencia-datos-programacion/07-asistentes-ia.md) y su uso en el curso comienza en la semana 5. Esta guía explica cómo activarlo y configurarlo; requiere VS Code instalado según su [guía](vscode.md) y la cuenta de GitHub creada en la lección de [Git, GitHub y GitHub Pages](../i-introduccion-ciencia-datos-programacion/05-git-github.md).

## Activación

### Instalación de la extensión

Haga clic en el ícono de Copilot en la barra de estado de VS Code (abajo a la derecha) y elija *Set up Copilot*: VS Code instala la extensión necesaria. Si prefiere hacerlo a mano, instale desde el panel de extensiones la extensión **GitHub Copilot Chat**, publicada por GitHub. Esa sola extensión incluye los autocompletados y el chat; la extensión **GitHub Copilot** (sin "Chat") quedó obsoleta y no hace falta instalarla, y las demás con nombre parecido (*for Azure*, *Nightly*, etc.) no se usan en el curso.

### Inicio de sesión con la cuenta de GitHub

1. Haga clic en el ícono de Copilot en la barra de estado y elija *Sign in to use Copilot*. Otra vía es el ícono de *Accounts* (la silueta, abajo a la izquierda) y luego *Sign in with GitHub to use GitHub Copilot*.
2. VS Code abre el navegador en GitHub. Si no tiene la sesión iniciada, ingrese con su usuario, su contraseña y el segundo factor de autenticación, si lo tiene activado.
3. GitHub pide autorizar a *Visual Studio Code* para usar su cuenta. Haga clic en *Authorize* (o *Continue*).
4. El navegador pregunta si desea volver a VS Code. Acepte, y en VS Code confirme el aviso *Allow an extension to open this URI*.
5. Si es la primera vez y su cuenta no tiene plan de Copilot, VS Code ofrece activar el plan gratuito con un clic.

Si el navegador no logra devolverle a VS Code (ocurre a veces en Linux o cuando el navegador usa otro perfil), en el diálogo de inicio de sesión elija la opción de código de dispositivo: VS Code muestra un código de ocho caracteres; abra [github.com/login/device](https://github.com/login/device), ingrese el código y autorice.

### Verificación

Al terminar, el ícono de Copilot en la barra de estado deja de mostrar la marca de alerta y, al escribir código, aparecen sugerencias en gris que se aceptan con la tecla *Tab*. Para comprobar la cuenta conectada, haga clic en el ícono de *Accounts*: debe listar su usuario de GitHub. Si necesita cambiar de cuenta, elija ahí *Sign out* y repita el inicio de sesión.

Con el plan gratuito basta para comenzar; sus límites y la forma de eliminarlos se explican en la sección siguiente.

## Planes

El plan gratuito para cuentas personales tiene límites mensuales de uso (a agosto de 2026, 2000 autocompletados y 50 mensajes de chat): suficientes para los ejercicios del curso, pero ajustados para el proyecto final.

### Copilot Pro gratuito con GitHub Education

[GitHub Education](https://github.com/education) ofrece el plan Copilot Pro —sin los límites anteriores— gratis a estudiantes verificados. **Se recomienda solicitar la verificación desde ya**: el proceso puede tardar varios días y conviene tenerla lista antes de la semana 5.

1. Agregue su correo institucional (`@ucr.ac.cr`) a su cuenta de GitHub (*Settings > Emails*).
2. En [GitHub Education](https://github.com/education), solicite los beneficios de estudiante (*Join GitHub Education*) con ese correo, y aporte la prueba de matrícula que se le pida (ej. una constancia o el carné).
3. Al aprobarse la solicitud, active Copilot Pro desde la [página de configuración de Copilot](https://github.com/settings/copilot).

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
