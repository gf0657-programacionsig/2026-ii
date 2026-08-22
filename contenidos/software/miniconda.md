# Miniconda

[Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) es un instalador mínimo del sistema de gestión de paquetes y de ambientes virtuales [conda](https://docs.conda.io/). Es una versión reducida de [Anaconda](https://www.anaconda.com/) que incluye solamente conda, Python y unos pocos paquetes adicionales. Esta guía explica cómo instalarlo y cómo crear con él el ambiente de Python del curso, con el que se trabaja localmente a partir de la semana 3, como alternativa a [Google Colab](colab.md).

## Conda y los ambientes virtuales

Un **ambiente virtual** es un conjunto aislado de programas y bibliotecas, con versiones específicas, que se instala sin interferir con otros ambientes ni con el resto del sistema. Así, por ejemplo, pueden coexistir en la misma computadora un ambiente para este curso y otros con versiones diferentes de Python o de sus bibliotecas para otros proyectos. Conda administra estos ambientes: los crea, instala paquetes en ellos, los actualiza y los borra.

Un ambiente puede describirse en un archivo de texto que enumera sus paquetes y versiones. El del curso está definido en el archivo [environment.yml](https://github.com/gf0657-programacionsig/2026-ii/blob/main/environment.yml) del repositorio del curso: cualquier persona puede recrear con él un ambiente idéntico, otra aplicación de la [reproducibilidad](../i-introduccion-ciencia-datos-programacion/01-introduccion-ciencia-datos.md) estudiada en el curso, ahora aplicada al software.

## Instalación de Miniconda

1. Ingrese a la [página de descarga de Anaconda](https://www.anaconda.com/download/success) y descargue el instalador de **Miniconda** correspondiente a su sistema operativo.
2. Ejecute el instalador y siga las instrucciones. Se recomienda:
    - Elegir la opción **Just Me** (para que se instale en el directorio de la persona usuaria).
    - Aceptar las demás opciones que el instalador presenta por defecto.
3. Al finalizar la instalación, abra una terminal con conda habilitado:
    - **Windows**: abra **Anaconda Prompt** desde el menú Inicio (no use CMD ni PowerShell directamente, ya que no tienen conda habilitado por defecto).
    - **macOS / Linux**: abra la terminal del sistema.
4. Verifique la instalación:

```shell
conda --version
```

## Creación del ambiente del curso

1. Descargue el archivo [environment.yml](https://raw.githubusercontent.com/gf0657-programacionsig/2026-ii/main/environment.yml) del repositorio del curso (clic derecho sobre el enlace y *Guardar enlace como*) y colóquelo en la carpeta de trabajo del curso.
2. En la terminal con conda habilitado, muévase a esa carpeta con el comando `cd` (ej. `cd Documentos\gf0657`). También puede usar la [terminal integrada de Visual Studio Code](vscode.md) con la carpeta de trabajo abierta, que ya inicia ubicada en ella.
3. Cree el ambiente:

```shell
conda env create -f environment.yml
```

El comando crea un ambiente llamado `geopython` (el nombre está definido en el archivo) y descarga e instala todos los paquetes del curso, entre ellos Python, git, Jupyter, pandas y las bibliotecas geoespaciales. La descarga toma varios minutos.

4. Active el ambiente y verifique la versión de Python:

```shell
conda activate geopython
python --version
```

Al activarse el ambiente, su nombre aparece al inicio de la línea de la terminal: `(geopython)`. Los comandos que se ejecuten a partir de ese momento usan los programas del ambiente.

5. Al finalizar la sesión de trabajo, desactive el ambiente:

```shell
conda deactivate
```

## Actualización del ambiente

Si durante el curso se agregan paquetes, se anunciará un cambio en `environment.yml`. Para aplicarlo, descargue la versión nueva del archivo y ejecute:

```shell
conda env update -f environment.yml
```

No se recomienda instalar paquetes por su cuenta en `geopython` (ej. con `conda install`): el ambiente quedaría distinto al del resto del curso. Si necesita experimentar, cree un ambiente aparte.

## Uso del ambiente

- **Cuadernos de notas en VS Code**: abra el cuaderno y elija el ambiente `geopython` en **Select Kernel**, como se explica en la [guía de VS Code](vscode.md).
- **Jupyter en el navegador**: con el ambiente activado, ejecute `jupyter notebook` en la terminal; la aplicación se abre en el navegador y los cuadernos se guardan en la carpeta desde donde se ejecutó el comando.
- **Python interactivo**: con el ambiente activado, el comando `python` abre el interpretador en la terminal (se sale con `exit()`).

## Otros comandos de conda

```shell
# Información general sobre conda
conda info

# Lista de ambientes instalados
conda env list

# Lista de paquetes instalados en el ambiente activo
conda list

# Ayuda sobre un comando (ej. conda install)
conda install --help

# Borrado de un ambiente (que no esté activo)
conda env remove -n nombre-del-ambiente
```

La lista completa de comandos está en la [hoja de referencia de conda](https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html).
