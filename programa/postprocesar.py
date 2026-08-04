"""Posprocesa el DOCX generado por pandoc.

- Ajusta los anchos de columna de todas las tablas al ancho completo de la
  página: la tabla de contenidos queda 20/50/30 % y las tablas de
  evaluación 18/62/20 % (columna central ancha).
- Centra los párrafos que contienen imágenes (código QR).
- Centra el bloque de encabezado (del nombre del curso hasta el título
  "PROGRAMA DEL CURSO"), como en la plantilla oficial.
- En la tabla de contenidos, fusiona en una sola celda centrada las filas de
  título de sección (las que inician con numeración romana, ej. "I. …").
- Aplica espaciado sencillo (sin espacio entre párrafos) a las líneas desde
  "Profesor:" hasta "II ciclo lectivo 2026" y deja una línea en blanco antes
  de "PROGRAMA DEL CURSO".

Uso: python3 postprocesar.py <archivo.docx>
"""

import re
import sys
import zipfile

# Ancho útil de la página: 21.59 cm - 4 cm de márgenes ≈ 9970 twips.
ANCHOS_CONTENIDOS = [1994, 4985, 2991]   # 20 %, 50 %, 30 %
ANCHOS_EVALUACION = [1794, 6182, 1994]   # 18 %, 62 %, 20 %
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


def fusionar_filas_seccion(doc):
    """Fusiona las filas de título de sección de la tabla de contenidos."""
    ini = doc.index("<w:tbl>")
    fin = doc.index("</w:tbl>", ini) + len("</w:tbl>")
    tabla = doc[ini:fin]

    def fusionar(m):
        fila = m.group(0)
        celdas = re.findall(r"<w:tc>.*?</w:tc>", fila, re.S)
        if len(celdas) != 3:
            return fila
        texto = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", celdas[0]))
        if not re.match(r"[IVX]+\.\s", texto):
            return fila
        if any(re.search(r"<w:t[^>]*>[^<]", c) for c in celdas[1:]):
            return fila
        celda = celdas[0].replace(
            "<w:tcPr />", '<w:tcPr><w:gridSpan w:val="3" /></w:tcPr>', 1
        )
        celda = centrar_parrafo(celda)
        # Línea en blanco antes y después del título de sección.
        celda = celda.replace("</w:tcPr>", "</w:tcPr><w:p />", 1)
        celda = celda.replace("</w:tc>", "<w:p /></w:tc>")
        return "<w:tr>" + celda + "</w:tr>"

    tabla = re.sub(r"<w:tr>.*?</w:tr>", fusionar, tabla, flags=re.S)
    return doc[:ini] + tabla + doc[fin:]


def main(path):
    zin = zipfile.ZipFile(path)
    doc = zin.read("word/document.xml").decode()

    tabla_n = [0]

    def anchos_tabla(m):
        tabla_n[0] += 1
        anchos = ANCHOS_CONTENIDOS if tabla_n[0] == 1 else ANCHOS_EVALUACION
        grid = "".join(f'<w:gridCol w:w="{w}" />' for w in anchos)
        return f"<w:tblGrid>{grid}</w:tblGrid>"

    doc = re.sub(r"<w:tblGrid>.*?</w:tblGrid>", anchos_tabla, doc, flags=re.S)

    # Centra los párrafos que contienen imágenes (código QR).
    doc = re.sub(
        r"<w:p>(?:(?!</w:p>).)*?<w:drawing>.*?</w:p>",
        lambda m: centrar_parrafo(m.group(0)),
        doc,
        flags=re.S,
    )

    doc = procesar_encabezado(doc)
    doc = fusionar_filas_seccion(doc)

    datos = {item: zin.read(item) for item in zin.namelist()}
    datos["word/document.xml"] = doc.encode()
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zout:
        for item, data in datos.items():
            zout.writestr(item, data)
    print(f"{path} posprocesado")


if __name__ == "__main__":
    main(sys.argv[1])
