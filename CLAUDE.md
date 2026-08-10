# CLAUDE.md

Este archivo orienta a Claude Code (claude.ai/code) al trabajar con este
repositorio.

El idioma del proyecto es **español**: contenido, mensajes de commit y
comunicación.

## Descripción

Curso GF-0657 Programación en SIG (II ciclo 2026), Escuela de Geografía,
Universidad de Costa Rica. El repositorio contiene el programa del curso
(`programa/`) y las fuentes del sitio web (`myst.yml`, `index.md`,
`contenidos/`, `estilos.css`), construido con MyST (mystmd) y desplegado
en GitHub Pages mediante GitHub Actions.

## Comandos

```bash
# Ambiente conda (definido en environment.yml)
conda activate gf0657-programacionsig-2026-ii

# Construir el sitio como lo hace el CI y traducir la interfaz
BASE_URL=/2026-ii myst build --html
python3 traducir-sitio.py

# Ejecutar un notebook antes de confirmarlo
NUMEXPR_MAX_THREADS=16 jupyter nbconvert --to notebook --execute --inplace <archivo>.ipynb

# Regenerar el programa (DOCX y PDF)
bash programa/generar.sh
```

## Convenciones

Todas las convenciones — flujo de Git, estructura de capítulos, formato de
referencias, patrones de gráficos y mapas, negritas e hipervínculos —
están en [CONTRIBUTING.md](CONTRIBUTING.md) y son de cumplimiento
obligatorio para el contenido nuevo. El directorio `privado/` está fuera
del repositorio (.gitignore) y nunca debe publicarse.
