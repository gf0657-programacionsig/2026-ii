"""Posprocesa el DOCX generado por pandoc.

- Ajusta los anchos de columna de la tabla de contenidos (la primera tabla
  del documento): SEMANA 20 %, CONTENIDO 50 %, LECTURA OBLIGATORIA 30 %.
- Centra el bloque de encabezado (del nombre del curso hasta el título
  "PROGRAMA DEL CURSO"), como en la plantilla oficial.
- Aplica espaciado sencillo (sin espacio entre párrafos) a las líneas desde
  "Profesor:" hasta "II ciclo lectivo 2026" y deja una línea en blanco antes
  de "PROGRAMA DEL CURSO".

Uso: python3 postprocesar.py <archivo.docx>
"""

import re
import sys
import zipfile

ANCHOS = [1584, 3960, 2376]  # 20 %, 50 %, 30 % de 7920 twips
FIN_ENCABEZADO = "PROGRAMA DEL CURSO"
INICIO_COMPACTO = "Profesor:"
FIN_COMPACTO = "II ciclo lectivo 2026"
ESPACIADO_SENCILLO = '<w:spacing w:after="0" w:line="240" w:lineRule="auto" />'


def agregar_a_ppr(parrafo, xml):
    if "<w:pPr>" in parrafo:
        return parrafo.replace("</w:pPr>", xml + "</w:pPr>", 1)
    return parrafo.replace("<w:p>", "<w:p><w:pPr>" + xml + "</w:pPr>", 1)


def centrar_parrafo(parrafo):
    if "<w:jc " in parrafo:
        return parrafo
    return agregar_a_ppr(parrafo, '<w:jc w:val="center" />')


def procesar_encabezado(doc):
    """Centra y compacta los párrafos del bloque de encabezado del programa."""
    resultado = []
    pos = 0
    compacto = False
    for m in re.finditer(r"<w:p>.*?</w:p>", doc, re.S):
        resultado.append(doc[pos : m.start()])
        parrafo = m.group(0)
        pos = m.end()
        texto = re.sub(r"<[^>]+>", "", parrafo)
        if FIN_ENCABEZADO in texto:
            resultado.append("<w:p />")  # línea en blanco de separación
            resultado.append(centrar_parrafo(parrafo))
            break
        if INICIO_COMPACTO in texto:
            compacto = True
        if compacto:
            parrafo = agregar_a_ppr(parrafo, ESPACIADO_SENCILLO)
        if FIN_COMPACTO in texto:
            compacto = False
        resultado.append(centrar_parrafo(parrafo))
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

    doc = procesar_encabezado(doc)

    datos = {item: zin.read(item) for item in zin.namelist()}
    datos["word/document.xml"] = doc.encode()
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zout:
        for item, data in datos.items():
            zout.writestr(item, data)
    print(f"{path} posprocesado")


if __name__ == "__main__":
    main(sys.argv[1])
