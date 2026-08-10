# GF-0657 Programación en SIG — II ciclo lectivo 2026

Curso de la Escuela de Geografía de la Universidad de Costa Rica (UCR).

- Sitio web del curso: [https://gf0657-programacionsig.github.io/2026-ii/](https://gf0657-programacionsig.github.io/2026-ii/)
- Profesor: Manuel Vargas Del Valle

## Estructura del repositorio

- `myst.yml`, `index.md`, `contenidos/`, `estilos.css`: fuentes del sitio web del curso,
  construido con [MyST](https://mystmd.org/) y desplegado en GitHub Pages
  mediante GitHub Actions (`.github/workflows/deploy.yml`).
- `traducir-sitio.py`: traduce al español las etiquetas de la interfaz del
  sitio generado (MyST aún no tiene internacionalización); se ejecuta después
  de `myst build --html`, localmente y en el workflow de despliegue.
- `environment.yml`: ambiente conda del curso, compartido por estudiantes
  (`conda env create -f environment.yml`, crea el ambiente `geopython`) y
  profesor (mismo comando con `-n gf0657-programacionsig-2026-ii`).
- `programa/`: programa del curso.
  - `programa.md`: fuente de la verdad del contenido del programa.
  - `generar-referencia.py`: crea `referencia.docx` (plantilla oficial de la
    Escuela de Geografía + estilos requeridos por pandoc). Tanto la plantilla
    como `referencia.docx` son documentos internos: no se versionan y el
    script requiere la plantilla en `privado/documentos-recibidos/`.
  - `generar.sh`: genera el DOCX (pandoc, con `referencia.docx` como documento
    de referencia) y el PDF (LibreOffice) a partir de `programa.md`.
  - `postprocesar.py`: ajustes finales al DOCX (anchos de columnas).
- `privado/`: documentos no publicados (calificaciones, documentos
  administrativos recibidos). Excluido del repositorio mediante `.gitignore`.

Las convenciones de Git del repositorio (mensajes de commit, flujo de
trabajo, qué no se versiona) están documentadas en
[CONTRIBUTING.md](CONTRIBUTING.md).

## Flujo de trabajo del programa del curso

1. Editar `programa/programa.md`.
2. Ejecutar `programa/generar.sh`.
3. Revisar `programa/gf0657-programacionsig-g001-2026-ii.pdf`.

## Flujo de trabajo del sitio web

```bash
conda activate gf0657-programacionsig-2026-ii

# Construir el sitio HTML estático (salida en _build/html/)
# BASE_URL reproduce el build de GitHub Actions; sin esa variable, algunos
# comportamientos del tema (ej. la composición del <title>) difieren.
BASE_URL=/2026-ii myst build --html

# Traducir al español las etiquetas de la interfaz
python3 traducir-sitio.py

# Servidor de desarrollo local (puerto 3000)
myst start
```

Los push a `main` construyen y despliegan el sitio automáticamente en
GitHub Pages.
