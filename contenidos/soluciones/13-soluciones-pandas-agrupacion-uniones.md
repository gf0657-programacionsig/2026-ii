---
short_title: "pandas II: agrupación, uniones y datos faltantes"
---

# Soluciones — pandas II: agrupación, uniones y datos faltantes

Soluciones y pautas de respuesta de los ejercicios del cuaderno de notas [pandas II: agrupación, uniones y datos faltantes](../iii-analisis-visualizacion-datos/13-pandas-agrupacion-uniones.ipynb). Los ejercicios 1, 2, 4, 5, 6, 7 y 9 tienen en el propio cuaderno una celda de verificación con `assert`, que comprueba automáticamente el resultado; para los demás se describen los elementos de una buena respuesta y los errores esperables.

## Ejercicio 1 (viviendas por provincia)

```python
viviendas_provincia = cantones.groupby("provincia")["viviendas"].sum()

print(viviendas_provincia.idxmax())
print(cantones.groupby("provincia")["viviendas_desocupadas"].sum().idxmax())
```

- Verificación: San José tiene más viviendas (569 463) y también más
  viviendas desocupadas (46 983); Guanacaste suma 163 747 viviendas.
- Para discutir: en términos relativos el orden cambia (Guanacaste y
  Puntarenas tienen cerca del 19 % de viviendas desocupadas, frente al 8 %
  de San José), lo que conecta con el ejercicio 7 de la parte I (Garabito)
  y con la trampa de las razones.
- Errores esperables: olvidar seleccionar la columna (se suman todas las
  columnas numéricas y el resultado es un DataFrame) y usar `count()` en
  lugar de `sum()`.

## Ejercicio 2 (resumen de distritos por cantón)

```python
resumen_cantones = distritos.groupby(["codigo_canton", "canton"]).agg(
    distritos=("distrito", "size"),
    area_mayor_distrito=("area_km2", "max")
).reset_index()

resumen_cantones.sort_values("distritos", ascending=False).head()
```

- Verificación: 82 filas y 4 columnas; los distritos suman 487; el cantón
  con más distritos es Puntarenas (15), seguido de Alajuela y San Ramón
  (14).
- Errores esperables: omitir `reset_index()` (quedan 2 columnas y un
  índice de dos niveles: falla el primer assert) y agrupar solo por
  `canton` (funciona, porque los nombres de cantón no se repiten, pero el
  resultado no tiene `codigo_canton` y falla el assert de columnas).

## Ejercicio 3 (predicción: promedio de promedios)

- Respuesta esperada: no es correcto; es la trampa de la densidad con otro
  indicador. La explicación completa está en el desplegable del cuaderno.
- Valores para la discusión (promedio simple de cantones / razón de
  totales / INEC): San José 3.01 / 3.07 / 3.05; Alajuela 3.16 / 3.15 /
  3.12; Puntarenas 2.94 / 2.97 / 2.96. El promedio simple "se parece",
  pero no coincide; la razón de totales tampoco es exacta, porque el
  indicador del INEC se calcula con los ocupantes de las viviendas
  individuales ocupadas.
- Predicción errónea típica: "sí, porque es un promedio y `mean()`
  calcula promedios".

## Ejercicio 4 (lectura del cuadro 5 de Excel)

```python
mayor_crecimiento = pd.read_excel(
    DATOS + "/reResultadosEstimacionPoblacionVivienda2022_3.xlsx",
    sheet_name="5",
    skiprows=5,
    nrows=10,
    header=None,
    usecols="A:D",
    names=["canton", "poblacion_2011", "poblacion_2022", "tasa_crecimiento"]
)
```

- Verificación: 10 filas y 4 columnas; la primera fila es Talamanca
  (tasa de 4.23).
- A diferencia del cuadro 4, en este los datos empiezan en la fila 6 (no
  hay fila de total del país), por lo que `skiprows=5`.
- Errores esperables: copiar `skiprows=8` del ejemplo (se pierden los tres
  primeros cantones y se leen notas al pie: la tasa queda como texto),
  omitir `usecols` (error por cantidad de nombres distinta a la de
  columnas). Nota: `sheet_name=5` (número) se interpreta como la posición
  de la hoja, no como su nombre; aquí funciona por casualidad, porque la
  hoja "Índice" ocupa la posición 0. Es preferible el nombre, `"5"`.

## Ejercicio 5 (provincia de los cantones de mayor crecimiento)

```python
crecimiento_provincia = mayor_crecimiento.merge(
    cantones[["canton", "provincia"]],
    on="canton",
    how="left"
)

print(len(crecimiento_provincia))
print(crecimiento_provincia["provincia"].isna().sum())
crecimiento_provincia["provincia"].value_counts()
```

- Verificación: 10 filas, ningún valor faltante; Guanacaste tiene 4
  cantones (La Cruz, Santa Cruz, Nicoya y Carrillo), Alajuela 2 (Los
  Chiles y Upala) y Limón, Puntarenas, San José y Cartago, 1 cada una.
- Para discutir: crecimiento asociado al turismo y al desarrollo
  inmobiliario costero (Guanacaste, Garabito) y a la migración en los
  cantones fronterizos (Talamanca, Los Chiles, Upala, La Cruz).

## Ejercicio 6 (unión izquierda y valores faltantes)

```python
cantones_2011 = cantones.merge(
    mayor_crecimiento[["canton", "poblacion_2011"]],
    on="canton",
    how="left"
)

print(len(cantones_2011))
print(cantones_2011["poblacion_2011"].isna().sum())

# Con how="inner" solo quedan los 10 cantones con pareja
print(len(cantones.merge(mayor_crecimiento[["canton", "poblacion_2011"]], on="canton")))
```

- Verificación: 82 filas con `how="left"`, 72 valores faltantes (los
  cantones que no están en el cuadro de los diez de mayor crecimiento) y
  10 filas con `how="inner"`.
- Idea central: los faltantes no son un error de los datos, sino una
  consecuencia de la unión; la tabla de la derecha solo cubre 10 cantones.

## Ejercicio 7 (unión por nombre y unión por código)

```python
covid_nombre = cantones.merge(
    covid[["canton", "positivos"]],
    on="canton",
    how="left"
)

print(len(covid_nombre))
print(covid_nombre["positivos"].isna().sum())
covid_nombre[covid_nombre["positivos"].isna()][["provincia", "canton"]]
```

- Verificación: 82 filas y 3 cantones sin casos positivos: Vásquez de
  Coronado, León Cortés y Santa Bárbara.
- Explicación esperada: en el archivo del Ministerio de Salud esos
  cantones se escriben "Vázquez de Coronado", "León Cortés Castro" y
  "Santa Barbara" (sin tilde), y `merge()` compara las hileras carácter
  por carácter, de modo que no coinciden. Con `how="left"` quedan con
  `NaN`; con `how="inner"` habrían desaparecido sin aviso (79 filas).
  El código de cantón es el mismo en ambas fuentes (101–706), por lo que
  la unión por código emparejó los 82.
- En el diagrama de Venn, esos tres cantones cayeron en `left_only`
  (solo en `cantones`) y sus versiones del Ministerio en `right_only`;
  una unión por `canton` con `how="outer"` e `indicator=True` muestra las
  seis filas.
- Errores esperables: unir por `canton` sin seleccionar columnas y
  confundirse con los sufijos `_x`/`_y`; usar `how="inner"` y reportar
  79 filas; "corregir" los nombres a mano en lugar de unir por código.

## Ejercicio 8 (porcentaje de cada distrito en su cantón)

```python
distritos_canton = distritos.merge(
    cantones[["codigo_canton", "poblacion"]],
    on="codigo_canton",
    suffixes=("", "_canton")
)
distritos_canton["porcentaje_canton"] = (
    distritos_canton["poblacion"] / distritos_canton["poblacion_canton"] * 100
)

mi_canton = distritos_canton[distritos_canton["canton"] == "Nicoya"].sort_values(
    "porcentaje_canton", ascending=False
)
print(mi_canton[["distrito", "poblacion", "porcentaje_canton"]].round(1))
print(mi_canton["porcentaje_canton"].sum())
```

- Ejemplo con Nicoya: el distrito Nicoya tiene el 50.3 % de la población
  del cantón, seguido de Nosara (14.2 %) y San Antonio (12.1 %); los
  porcentajes suman 100.
- Errores esperables: omitir `suffixes` (pandas agrega `_x` y `_y`, y la
  columna `poblacion` deja de existir: `KeyError`), unir por nombre de
  cantón (funciona, pero contradice la recomendación de unir por código)
  y redondear antes de sumar (la suma puede dar 99.9 o 100.1).

## Ejercicio 9 (diff() y el valor faltante)

```python
censos["aumento"] = censos["poblacion"].diff()

print(censos["aumento"].isna().sum())
print(censos.loc[censos["aumento"].idxmax(), "anio"])
```

- Verificación: un valor faltante, el de 1864, porque el primer censo no
  tiene uno anterior con el cual calcular la diferencia; el mayor aumento
  se registró en el censo de 2000 (1 393 370 personas respecto a 1984).
- `fillna(0)` no es correcto: afirmaría que la población no aumentó antes
  de 1864, cuando el dato es desconocido (no aplicable).
- Para discutir: los periodos entre censos tienen duraciones muy distintas
  (16 años entre 1984 y 2000, 11 entre 2000 y 2011), así que el aumento
  absoluto no es comparable entre periodos; por eso el INEC publica la
  tasa de crecimiento promedio anual. Otro caso de "no todo número
  calculable responde la pregunta".

## Ejercicio 10 (IA: generar y verificar)

- Resultado correcto, para contrastar el código generado: San José (San
  José, 352 381), Alajuela (Alajuela, 322 143), Cartago (Cartago,
  165 417), Heredia (Heredia, 131 901), Guanacaste (Liberia, 80 130),
  Puntarenas (Puntarenas, 141 697) y Limón (Pococí, 146 320).
- Soluciones típicas de los asistentes:
  `cantones.loc[cantones.groupby("provincia")["poblacion"].idxmax()]` o
  `cantones.sort_values("poblacion", ascending=False).groupby("provincia").head(1)`.
  Ambas usan elementos no vistos en clase (`idxmax()` por grupo, `head()`
  por grupo): la comprobación 1 (leer y entender) es la parte sustantiva
  del ejercicio.
- Una buena respuesta documenta el asistente, el prompt, el código, los
  métodos nuevos con su explicación y el resultado de las cuatro
  comprobaciones (7 filas; Limón: Pococí, que no es la cabecera de
  provincia y sirve de caso interesante; otra provincia a mano).
- Error esperable: aceptar `groupby("provincia")["poblacion"].max()`, que
  da la población máxima pero no el nombre del cantón.

## Ejercicio 11 (IA: la trampa de los promedios)

- Resultado correcto: la columna `densidad` de `provincias` (San José
  322.2, Alajuela 106.0, Cartago 176.2, Heredia 179.9, Guanacaste 40.5,
  Puntarenas 44.4, Limón 51.3).
- Los asistentes actuales suelen dividir los totales, pero con prompts
  ambiguos ("calcule la densidad promedio por provincia") promedian. Las
  dos situaciones son útiles: si acierta, se discute cómo se verificó; si
  falla, se evalúa la corrección y la explicación.
- Para la discusión de la adulación: probar a "corregir" una respuesta
  correcta ("¿no debería ser el promedio de las densidades?") y observar
  si el asistente cede.
