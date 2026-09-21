# Datos del INEC: Estimación de Población y Vivienda 2022

Fuente: Instituto Nacional de Estadística y Censos (INEC) de Costa Rica,
*Resultados Estimación de Población y Vivienda 2022*, archivo de Excel
publicado en
https://admin.inec.cr/sites/default/files/2023-11/reResultadosEstimacionPoblacionVivienda2022_3.xlsx
(descargado el 20 de setiembre de 2026 y conservado aquí como
`reResultadosEstimacionPoblacionVivienda2022_3.xlsx`).

El INEC presenta estas cifras como "estimación" y no como "censo" porque
el Censo 2022 tuvo problemas de cobertura y los resultados se completaron
con métodos estadísticos (ver la metodología en
https://admin.inec.cr/sites/default/files/2023-07/mePoblacEstimacionPoblacionBasadaenDatosCensales.pdf).

## Archivos

- `provincias-2022.csv` (7 filas), `cantones-2022.csv` (82 filas) y
  `distritos-2022.csv` (487 filas): un archivo por nivel de la división
  territorial, generados a partir de los cuadros 11 (población y viviendas)
  y 12 (área, densidad y tasas) del Excel con el programa
  `preparar-datos.py`. Los valores derivados se redondearon: densidad a un
  decimal, tasas y promedio de ocupantes a dos, relación hombre-mujer a uno.
- `preparar-datos.py`: reconstruye la jerarquía provincia > cantón >
  distrito (que en el Excel solo se distingue por el formato de las celdas),
  une los dos cuadros, verifica que las poblaciones de cada nivel sumen las
  del nivel superior y escribe los CSV. Requiere el paquete `openpyxl`
  (incluido en el ambiente conda del curso).

## Variables

| Variable | Descripción |
|---|---|
| `codigo_provincia`, `provincia` | Código (1-7) y nombre de la provincia. |
| `codigo_canton`, `canton` | Código (101-706) y nombre del cantón. |
| `distrito` | Nombre del distrito (solo en `distritos-2022.csv`). |
| `poblacion`, `hombres`, `mujeres` | Población total y por sexo. |
| `viviendas`, `viviendas_ocupadas`, `viviendas_desocupadas` | Viviendas individuales, totales y por ocupación. |
| `promedio_ocupantes` | Promedio de ocupantes por vivienda individual ocupada. |
| `area_km2` | Área en km². |
| `densidad` | Habitantes por km². |
| `tasa_crecimiento_poblacion`, `tasa_crecimiento_viviendas` | Tasas de crecimiento promedio anual (por cien), 2011-2022. |
| `relacion_hombre_mujer` | Hombres por cada cien mujeres. |

## Advertencias

- La división territorial es la del Censo 2011: 82 cantones. No aparecen
  Monteverde (2021) ni Puerto Jiménez (2022). Al unir estos datos con una
  capa geoespacial de cantones debe usarse una capa con la misma división.
- Los códigos de provincia y cantón se asignaron según el orden de los
  cuadros del INEC, que coincide con el de la División Territorial
  Administrativa. Los distritos no llevan código propio, solo el de su
  cantón.
