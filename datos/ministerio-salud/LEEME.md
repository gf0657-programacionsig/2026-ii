# Datos del Ministerio de Salud: casos positivos de COVID-19 por cantón

Fuente: Ministerio de Salud de Costa Rica, *Situación Nacional COVID-19*,
archivo de datos abiertos `05_30_22_CSV_POSITIVOS.csv` con la cantidad
acumulada de casos positivos por cantón, del 15 de marzo de 2020 al 30 de
mayo de 2022 (última fecha publicada en este formato). Se conserva aquí
tal como se distribuyó, sin modificaciones.

## Estructura

- Separador de campos: punto y coma (`;`). Codificación: Windows-1252
  (`cp1252`), no UTF-8.
- Columnas `cod_provin`, `provincia`, `cod_canton` y `canton`, seguidas
  de una columna por fecha (`15/03/2020`, `16/03/2020`, ..., `30/05/2022`)
  con el acumulado de casos positivos a esa fecha.
- 84 filas: los 82 cantones de la división territorial de 2011, una fila
  `Otros` (código 999, casos sin cantón asignado) y una fila vacía al
  final.
- Los códigos de cantón son los mismos del INEC (101–706), por lo que el
  archivo puede unirse con `datos/inec/cantones-2022.csv`. Tres nombres de
  cantón difieren de los del INEC (Vázquez de Coronado, León Cortés Castro
  y Santa Barbara), lo que ilustra por qué se une por código y no por
  nombre.

Usado en el cuaderno *pandas II: agrupación, uniones y datos faltantes*.
