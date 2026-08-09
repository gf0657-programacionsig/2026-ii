#!/usr/bin/env python3
"""Traduce al español las etiquetas de la interfaz del sitio generado por MyST.

El tema book-theme no tiene soporte de internacionalización
(https://github.com/jupyter-book/mystmd/issues/166), por lo que este script
reemplaza las cadenas en inglés en la salida de `myst build --html`, tanto en
el HTML estático como en los bundles de JavaScript del tema (React rehidrata
la página desde ellos, así que reemplazar solo el HTML no basta).

Se ejecuta después de `myst build --html`, localmente y en el workflow de
despliegue:

    myst build --html
    python3 traducir-sitio.py

Los reemplazos incluyen sus delimitadores (comillas, `>`...`<`) para no
alterar identificadores del código. Si una actualización del tema cambia una
cadena, el reemplazo deja de aplicar y la etiqueta vuelve a aparecer en
inglés: el script lo reporta como "0 reemplazos" pero no falla el build.
No se tocan los bundles de thebe (*.thebe-*.js), que son código de Jupyter.
"""

import sys
from pathlib import Path

RAIZ = Path(__file__).parent / "_build" / "html"

# (patrón exacto en inglés, reemplazo en español)
REEMPLAZOS = [
    # Pie de página
    ('"Made with MyST"', '"Hecho con MyST"'),
    (">Made with MyST<", ">Hecho con MyST<"),
    # Búsqueda
    ('children:"Search"', 'children:"Buscar"'),
    ('placeholder:"Search"', 'placeholder:"Buscar"'),
    (">Search<", ">Buscar<"),
    ('"No results found."', '"No se encontraron resultados."'),
    # Esquema del documento (margen derecho)
    ('="Contents"', '="Contenido"'),
    ('"Open Contents"', '"Abrir contenido"'),
    # Navegación y accesibilidad
    ('"Table of Contents"', '"Tabla de contenidos"'),
    ('"Skip to article content"', '"Ir al contenido del artículo"'),
    ('"Skip to article frontmatter"', '"Ir al encabezado del artículo"'),
    (">Skip to article content<", ">Ir al contenido del artículo<"),
    (">Skip to article frontmatter<", ">Ir al encabezado del artículo<"),
    ('"Previous: "', '"Anterior: "'),
    ('"Next: "', '"Siguiente: "'),
    ('aria-label="Previous: ', 'aria-label="Anterior: '),
    ('aria-label="Next: ', 'aria-label="Siguiente: '),
    ('"Open Folder"', '"Abrir carpeta"'),
    ('"Link to this Section"', '"Enlace a esta sección"'),
    # Selector de tema claro/oscuro
    (
        '"Toggle theme between light and dark mode"',
        '"Cambiar entre tema claro y tema oscuro"',
    ),
]


def archivos_a_procesar():
    """HTML de todo el sitio y JavaScript del tema (build/), sin thebe."""
    yield from RAIZ.rglob("*.html")
    yield from (RAIZ / "build").rglob("*.js")


def main():
    if not RAIZ.is_dir():
        sys.exit(f"No existe {RAIZ}; ejecute antes `myst build --html`.")

    conteos = {ingles: 0 for ingles, _ in REEMPLAZOS}
    for archivo in archivos_a_procesar():
        texto = archivo.read_text(encoding="utf-8")
        original = texto
        for ingles, espanol in REEMPLAZOS:
            apariciones = texto.count(ingles)
            if apariciones:
                texto = texto.replace(ingles, espanol)
                conteos[ingles] += apariciones
        if texto != original:
            archivo.write_text(texto, encoding="utf-8")

    for ingles, total in conteos.items():
        marca = "✔" if total else "–"
        print(f"{marca} {ingles}: {total} reemplazos")


if __name__ == "__main__":
    main()
