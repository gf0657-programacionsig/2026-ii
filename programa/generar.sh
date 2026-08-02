#!/bin/bash
# Genera el programa del curso en DOCX y PDF a partir de programa.md.
#
# Flujo: programa.md (fuente de la verdad)
#   1. pandoc (gfm -> html): resuelve las tablas con <br> en las celdas.
#   2. pandoc (html -> docx) con la plantilla oficial de la Escuela de
#      Geografía como documento de referencia (estilos, márgenes, logos).
#   3. LibreOffice (docx -> pdf).
#
# Uso: ./generar.sh

set -euo pipefail
cd "$(dirname "$0")"

PANDOC="${PANDOC:-$HOME/miniconda3/bin/pandoc}"
PLANTILLA="../privado/documentos-recibidos/PLANTILLA DE CURSOS II CICLO 2026.docx"
REFERENCIA="referencia.docx"   # copia de la plantilla con estilos ajustados (si existe)
SALIDA="gf0657-programacionsig-g001-2026-ii"

REF="$PLANTILLA"
[ -f "$REFERENCIA" ] && REF="$REFERENCIA"

"$PANDOC" programa.md -f gfm -t html -o /tmp/programa-tmp.html
"$PANDOC" /tmp/programa-tmp.html -f html -o "$SALIDA.docx" --reference-doc="$REF"
python3 postprocesar.py "$SALIDA.docx"

libreoffice --headless --convert-to pdf --outdir . "$SALIDA.docx" > /dev/null

echo "Generados: $SALIDA.docx y $SALIDA.pdf"
