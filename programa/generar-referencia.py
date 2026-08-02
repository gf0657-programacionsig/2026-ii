"""Genera referencia.docx: la plantilla oficial de la Escuela de Geografía
con los estilos que pandoc necesita inyectados en styles.xml.

La plantilla (creada en LibreOffice) no define los estilos que pandoc usa
(Compact, Table, Heading1, etc.). Sin ellos, las listas pierden la numeración
y las tablas los bordes. Este script:
  1. Extrae los estilos del documento de referencia por defecto de pandoc.
  2. Inyecta en la plantilla los que falten (por styleId).
  3. Ajusta los estilos de encabezados (color negro, fuente heredada).
  4. Ajusta el estilo de tabla para que tenga bordes completos.

Uso: python3 generar-referencia.py
"""

import os
import re
import subprocess
import zipfile

PANDOC = os.environ.get("PANDOC", os.path.expanduser("~/miniconda3/bin/pandoc"))
PLANTILLA = "../privado/documentos-recibidos/PLANTILLA DE CURSOS II CICLO 2026.docx"
SALIDA = "referencia.docx"
REF_PANDOC = "/tmp/pandoc-default-reference.docx"

BORDES_TABLA = (
    '<w:tblBorders>'
    '<w:top w:val="single" w:sz="4" w:space="0" w:color="000000" />'
    '<w:left w:val="single" w:sz="4" w:space="0" w:color="000000" />'
    '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000" />'
    '<w:right w:val="single" w:sz="4" w:space="0" w:color="000000" />'
    '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="000000" />'
    '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="000000" />'
    '</w:tblBorders>'
)


def leer_styles(path):
    return zipfile.ZipFile(path).read("word/styles.xml").decode()


def main():
    subprocess.run(
        [PANDOC, "-o", REF_PANDOC, "--print-default-data-file", "reference.docx"],
        check=True,
    )

    plantilla_xml = leer_styles(PLANTILLA)
    pandoc_xml = leer_styles(REF_PANDOC)

    ids_plantilla = set(re.findall(r'w:styleId="([^"]+)"', plantilla_xml))
    inyectados = []
    for estilo in re.findall(r"<w:style [^>]*>.*?</w:style>", pandoc_xml, re.S):
        sid = re.search(r'w:styleId="([^"]+)"', estilo).group(1)
        if sid in ids_plantilla:
            continue
        if sid.startswith("Heading"):
            # Heredar fuente y color de la plantilla (negro, no azul).
            estilo = re.sub(r"<w:color [^/]*/>", "", estilo)
            estilo = re.sub(r"<w:rFonts [^/]*/>", "", estilo)
        if sid == "Table":
            # El estilo por defecto de pandoc no define bordes; se insertan.
            estilo = re.sub(r"<w:tblBorders>.*?</w:tblBorders>", "", estilo, flags=re.S)
            estilo = estilo.replace("<w:tblPr>", "<w:tblPr>" + BORDES_TABLA, 1)
        inyectados.append((sid, estilo))

    nuevo_xml = plantilla_xml.replace(
        "</w:styles>", "".join(e for _, e in inyectados) + "</w:styles>"
    )

    zin = zipfile.ZipFile(PLANTILLA)
    with zipfile.ZipFile(SALIDA, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.namelist():
            data = zin.read(item)
            if item == "word/styles.xml":
                data = nuevo_xml.encode()
            zout.writestr(item, data)

    print(f"{SALIDA} creado ({len(inyectados)} estilos inyectados)")


if __name__ == "__main__":
    main()
