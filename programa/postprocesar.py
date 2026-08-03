"""Posprocesa el DOCX generado por pandoc.

- Ajusta los anchos de columna de la tabla de contenidos (la primera tabla
  del documento): SEMANA 20 %, CONTENIDO 50 %, LECTURA OBLIGATORIA 30 %.
- Centra el bloque de encabezado (del nombre del curso hasta el título
  "PROGRAMA DEL CURSO"), como en la plantilla oficial.

Uso: python3 postprocesar.py <archivo.docx>
"""

import re
import sys
import zipfile

ANCHOS = [1584, 3960, 2376]  # 20 %, 50 %, 30 % de 7920 twips
FIN_ENCABEZADO = "PROGRAMA DEL CURSO"


def centrar_parrafo(parrafo):
    if "<w:jc " in parrafo:
        return parrafo
    if "<w:pPr>" in parrafo:
        return parrafo.replace("</w:pPr>", '<w:jc w:val="center" /></w:pPr>', 1)
    return parrafo.replace("<w:p>", '<w:p><w:pPr><w:jc w:val="center" /></w:pPr>', 1)


def centrar_encabezado(doc):
    """Centra los párrafos desde el inicio del cuerpo hasta FIN_ENCABEZADO."""
    resultado = []
    pos = 0
    for m in re.finditer(r"<w:p>.*?</w:p>", doc, re.S):
        resultado.append(doc[pos : m.start()])
        parrafo = centrar_parrafo(m.group(0))
        resultado.append(parrafo)
        pos = m.end()
        if FIN_ENCABEZADO in parrafo:
            break
    resultado.append(doc[pos:])
    return "".join(resultado)


def main(path):
    zin = zipfile.ZipFile(path)
    doc = zin.read("word/document.xml").decode()

    grid = "".join(f'<w:gridCol w:w="{w}" />' for w in ANCHOS)
    doc = re.sub(
        r"<w:tblGrid>.*?</w:tblGrid>",
        f"<w:tblGrid>{grid}</w:tblGrid>",
        doc,
        count=1,
        flags=re.S,
    )

    doc = centrar_encabezado(doc)

    datos = {item: zin.read(item) for item in zin.namelist()}
    datos["word/document.xml"] = doc.encode()
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zout:
        for item, data in datos.items():
            zout.writestr(item, data)
    print(f"{path} posprocesado")


if __name__ == "__main__":
    main(sys.argv[1])
