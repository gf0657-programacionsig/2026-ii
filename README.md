# GF-0657 Programación en SIG — II ciclo lectivo 2026

Curso de la Escuela de Geografía de la Universidad de Costa Rica (UCR).

- Sitio web del curso: [https://gf0657-programacionsig.github.io/2026-ii/](https://gf0657-programacionsig.github.io/2026-ii/)
- Profesor: Manuel Vargas Del Valle

## Estructura del repositorio

- `programa/`: programa del curso.
  - `programa.md`: fuente de la verdad del contenido del programa.
  - `generar-referencia.py`: crea `referencia.docx` (plantilla oficial de la
    Escuela de Geografía + estilos requeridos por pandoc).
  - `generar.sh`: genera el DOCX (pandoc, con `referencia.docx` como documento
    de referencia) y el PDF (LibreOffice) a partir de `programa.md`.
  - `postprocesar.py`: ajustes finales al DOCX (anchos de columnas).
- `privado/`: documentos no publicados (calificaciones, documentos
  administrativos recibidos). Excluido del repositorio mediante `.gitignore`.

## Flujo de trabajo del programa del curso

1. Editar `programa/programa.md`.
2. Ejecutar `programa/generar.sh`.
3. Revisar `programa/gf0657-programacionsig-g001-2026-ii.pdf`.
