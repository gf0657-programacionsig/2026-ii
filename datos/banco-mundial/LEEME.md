# Datos del Banco Mundial

Fuente: Banco Mundial, base de datos [Indicadores del desarrollo
mundial](https://datos.bancomundial.org/), consultada mediante su API
(https://api.worldbank.org/v2/) el 4 de octubre de 2026 con el programa
`preparar-datos.py` (requiere pandas). Los datos del Banco Mundial se
publican con licencia CC BY 4.0.

## Archivos

- `indicadores-2022.csv` (217 filas): una fila por país o territorio (se
  excluyen los agregados regionales y por ingreso), con `codigo` (ISO
  3166-1 alfa-3, con las variantes del Banco Mundial: `XKX` para Kosovo),
  `pais` (nombre en español), `region`, `grupo_ingreso` y los indicadores
  de 2022 de la tabla siguiente. Las celdas vacías son valores que el
  Banco Mundial no publica para ese país.
- `poblacion-1960-2023.csv` (13 858 filas): población total por país y
  año, en formato largo (`codigo`, `anio`, `poblacion`).

| Variable | Indicador | Descripción |
|---|---|---|
| `poblacion` | SP.POP.TOTL | Población total |
| `crecimiento_poblacion` | SP.POP.GROW | Crecimiento de la población (% anual) |
| `area_km2` | AG.LND.TOTL.K2 | Superficie terrestre (km²), sin aguas interiores |
| `pib_per_capita` | NY.GDP.PCAP.CD | PIB per cápita (US$ a precios actuales) |
| `esperanza_vida` | SP.DYN.LE00.IN | Esperanza de vida al nacer (años) |
| `poblacion_urbana_pct` | SP.URB.TOTL.IN.ZS | Población urbana (% del total) |
| `usuarios_internet_pct` | IT.NET.USER.ZS | Personas que usan Internet (% de la población) |
