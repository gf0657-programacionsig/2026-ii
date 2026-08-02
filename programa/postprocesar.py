"""Posprocesa el DOCX generado por pandoc.

Ajusta los anchos de columna de la tabla de contenidos (la primera tabla del
documento): SEMANA 20 %, CONTENIDO 50 %, LECTURA OBLIGATORIA 30 %.

Uso: python3 postprocesar.py <archivo.docx>
"""

import re
import sys
import zipfile

ANCHOS = [1584, 3960, 2376]  # 20 %, 50 %, 30 % de 7920 twips


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

    datos = {item: zin.read(item) for item in zin.namelist()}
    datos["word/document.xml"] = doc.encode()
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zout:
        for item, data in datos.items():
            zout.writestr(item, data)
    print(f"{path} posprocesado")


if __name__ == "__main__":
    main(sys.argv[1])
