---
short_title: "pandas I: Series y DataFrames"
---

# Soluciones — pandas I: Series y DataFrames

Soluciones y pautas de respuesta de los ejercicios del cuaderno de notas [pandas I: Series y DataFrames](../iii-analisis-visualizacion-datos/12-pandas-series-dataframes.ipynb). Los ejercicios 1 y 3 a 7 tienen en el propio cuaderno una celda de verificación con `assert`, que comprueba automáticamente el resultado; para los demás se describen los elementos de una buena respuesta y los errores esperables.

## Ejercicio 1 (Series de áreas)

```python
areas = pd.Series(
    [4969.80, 9772.12, 3093.24, 2663.30, 10196.29, 11275.00, 9176.88],
    index=["San José", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limón"]
)

print(areas.sum())
print(areas.idxmax())
```

- Verificación: área total 51 146.63 km² y provincia más extensa
  Puntarenas.
- Errores esperables: omitir el `index` (la Series queda con posiciones
  0 a 6 y el segundo assert falla) y confundir `max()` (el valor, 11 275)
  con `idxmax()` (la etiqueta).

## Ejercicio 2 (predicción: corchetes simples y dobles)

- Respuesta esperada: `<class 'pandas.core.series.Series'>`,
  `<class 'pandas.core.frame.DataFrame'>` y `(82, 1)`. La explicación
  completa está en el desplegable del cuaderno.
- Predicción errónea típica: "los dos son DataFrame" o "la forma es
  (82,)". Conexión con la sección de selección de columnas.

## Ejercicio 3 (carga del archivo de distritos)

```python
distritos = pd.read_csv(
    "https://raw.githubusercontent.com/gf0657-programacionsig/2026-ii/main/datos/inec/distritos-2022.csv"
)

distritos.shape
distritos.info()
distritos.describe()

# Distritos por cantón (los primeros son los cantones con más distritos)
distritos["canton"].value_counts()
```

- Verificación: forma (487, 17). El cantón con más distritos es
  **Puntarenas (15)**, seguido de Alajuela y San Ramón (14) y de
  Desamparados y San Carlos (13); se lee en `value_counts().head()`.
  Recordar que la división es la de 2011: Monteverde y Puerto Jiménez
  aparecen como distritos de Puntarenas y de Golfito, respectivamente.
- Errores esperables: cargar de nuevo el archivo de cantones (el assert
  de la columna `distrito` lo detecta) y usar `value_counts()` sobre la
  columna `distrito`, que cuenta nombres de distritos repetidos (San
  Rafael, San Isidro, etc.) en lugar de distritos por cantón.

## Ejercicio 4 (cantones densos)

```python
cantones_densos = cantones.loc[cantones["densidad"] > 1000, ["provincia", "canton", "densidad"]]

cantones_densos["provincia"].value_counts()
```

- Verificación: 16 cantones: de San José (9), Heredia (5),
  Alajuela (Palmares) y Cartago (La Unión): el anillo urbano de la Gran
  Área Metropolitana.
- Errores esperables: `>=` en vez de `>` (no cambia el resultado con
  estos datos, pero conviene señalarlo), y seleccionar las columnas en
  otro orden o con corchetes simples (el tercer assert compara la lista
  de columnas). También es válido `cantones[cantones["densidad"] > 1000][["provincia", "canton", "densidad"]]`.

## Ejercicio 5 (cantones extensos de Guanacaste)

```python
guanacaste_extensos = cantones[(cantones["provincia"] == "Guanacaste") & (cantones["area_km2"] > 1000)]
```

- Verificación: Liberia, Nicoya, Santa Cruz, Bagaces y La Cruz.
- Errores esperables: usar `and` (ValueError de la clínica), omitir los
  paréntesis (TypeError por la precedencia de `&`), y usar la columna
  `densidad` en lugar de `area_km2`.

## Ejercicio 6 (cinco cantones más poblados)

```python
mas_poblados = cantones.sort_values("poblacion", ascending=False)["canton"].head(5).tolist()
```

- Verificación: `["San José", "Alajuela", "Desamparados", "San Carlos", "Cartago"]`.
- Errores esperables: olvidar `ascending=False` (quedan los menos
  poblados), y dejar el resultado como Series o como `list(...)` de un
  DataFrame (el primer assert pide una lista; `list(df)` retorna los
  nombres de las columnas, un error instructivo). También es válido
  `cantones.nlargest(5, "poblacion")["canton"].tolist()`.

## Ejercicio 7 (porcentaje de viviendas desocupadas)

```python
cantones["porcentaje_desocupadas"] = cantones["viviendas_desocupadas"] / cantones["viviendas"] * 100

cantones.sort_values("porcentaje_desocupadas", ascending=False)[["canton", "provincia", "porcentaje_desocupadas"]].head()
```

- Verificación: máximo de 44,3 % en Garabito (Jacó). Le siguen otros
  cantones costeros y turísticos (Santa Cruz, Carrillo, Osa, Quepos).
- Elementos de una buena respuesta a la pregunta abierta: viviendas de
  recreo o de alquiler vacacional desocupadas en el momento del
  levantamiento, propias de zonas turísticas de playa; no es lo mismo
  que abandono.
- Errores esperables: dividir entre `viviendas_ocupadas` en lugar de
  `viviendas` (el valor máximo no coincide) y olvidar el `* 100`.

## Ejercicio 8 (cantones de la provincia propia, exportación)

Ejemplo con Cartago (depende de la provincia de cada estudiante):

```python
mi_provincia = cantones[cantones["provincia"] == "Cartago"] \
    .sort_values("densidad", ascending=False)[["canton", "poblacion", "area_km2", "densidad"]]

mi_provincia.to_csv("mi-provincia.csv", index=False)

pd.read_csv("mi-provincia.csv")
```

- Lo evaluable: filtro por provincia, ordenamiento descendente, selección
  de las cuatro columnas, `index=False` y la relectura.
- Errores esperables: omitir `index=False` (al releer aparece una columna
  `Unnamed: 0`, buen momento para explicar qué es el índice) y ordenar
  después de seleccionar columnas que no incluyen `densidad`.

## Ejercicio 9 (asistente de IA: el ValueError de la clínica)

Ejercicio abierto. Elementos de una buena respuesta:

- Prompt con los cuatro componentes (rol de tutor, contexto de aprendizaje
  de pandas, tarea de explicar y dar una pista, formato sin código
  corregido) y el mensaje de error completo.
- Resumen de la respuesta que mencione que `and` evalúa la verdad de un
  objeto completo, que una Series no tiene un único valor de verdad y que
  la solución son los operadores vectorizados `&` y `|` con paréntesis.
- Evaluación crítica: ¿el asistente dio directamente el código corregido
  a pesar de pedirse solo una pista? (frecuente); ¿mencionó los
  paréntesis? (a veces se omite y el estudiante se topa luego con el
  TypeError de precedencia).
- Declaración explícita del asistente usado.
