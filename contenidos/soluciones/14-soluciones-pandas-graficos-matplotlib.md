---
short_title: "pandas III: gráficos con matplotlib"
---

# Soluciones — pandas III: gráficos con matplotlib

Soluciones y pautas de respuesta de los ejercicios del cuaderno de notas [pandas III: gráficos con matplotlib](../iii-analisis-visualizacion-datos/14-pandas-graficos-matplotlib.ipynb). Los ejercicios 1 a 7 tienen en el propio cuaderno una celda de verificación con `assert`, que examina la figura y los ejes creados; para los demás se describen los elementos de una buena respuesta y los errores esperables. Todas las soluciones suponen ejecutada la celda de carga de datos del cuaderno (`provincias`, `cantones`, `distritos`, `censos`, `cantones_covid`, `AZUL`, `NARANJA`) y la importación de `StrMethodFormatter`.

## Ejercicio 1 (barras horizontales: los diez cantones más densos)

```python
top_densos = cantones.sort_values("densidad", ascending=False).head(10)

fig_1, ax_1 = plt.subplots(figsize=(8, 4.5))

top_densos.sort_values("densidad").plot(
    x="canton", y="densidad", kind="barh", ax=ax_1, color=AZUL, legend=False
)

ax_1.set_title("Los diez cantones más densamente poblados de Costa Rica, 2022")
ax_1.set_xlabel("Habitantes por km²")
ax_1.set_ylabel("")
ax_1.bar_label(ax_1.containers[0], fmt="{:,.0f}", padding=3, fontsize=9)
ax_1.set_xlim(0, 10000)

plt.show()
```

- Verificación: 10 barras, título, etiqueta del eje horizontal y la barra
  más larga arriba (Tibás, 9019.6 hab/km²).
- Siete de los diez están en San José (Tibás, San José, Curridabat,
  Goicoechea, Alajuelita, Montes de Oca y Escazú); los otros son San Pablo
  y Flores (Heredia) y La Unión (Cartago): todos del área metropolitana.
- Errores esperables: ordenar de forma descendente (el más denso queda
  abajo), olvidar `legend=False`, dejar la etiqueta `canton` en el eje
  vertical.

## Ejercicio 2 (barras agrupadas: viviendas ocupadas y desocupadas)

```python
fig_2, ax_2 = plt.subplots(figsize=(8, 4))

provincias.sort_values("viviendas", ascending=False).plot(
    x="provincia", y=["viviendas_ocupadas", "viviendas_desocupadas"], kind="bar", ax=ax_2,
    color=[AZUL, NARANJA], label=["Ocupadas", "Desocupadas"]
)

ax_2.set_title("Viviendas ocupadas y desocupadas por provincia, 2022")
ax_2.set_xlabel("")
ax_2.set_ylabel("Viviendas")
ax_2.tick_params(axis="x", rotation=0)
ax_2.yaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))
ax_2.legend(title="")

plt.show()
```

- Verificación: 14 barras, leyenda y título.
- La proporción de viviendas desocupadas es mayor en Guanacaste (19.4 %) y
  Puntarenas (19.3 %), seguidas de Limón (14.5 %); en las provincias del
  Valle Central ronda el 8 %. Explicación esperada: viviendas de recreo y
  segundas residencias en las zonas costeras, además de la migración
  laboral estacional.
- Nota: el gráfico muestra cantidades absolutas; para responder la
  pregunta con rigor conviene calcular el porcentaje (como en el
  ejercicio 5), porque San José tiene más viviendas desocupadas que
  Guanacaste en número, pero no en proporción.

## Ejercicio 3 (líneas: hombres y mujeres en los censos)

```python
fig_3, ax_3 = plt.subplots(figsize=(8, 4))

censos.plot(
    x="anio", y=["hombres", "mujeres"], kind="line", ax=ax_3,
    color=[AZUL, NARANJA], marker="o", label=["Hombres", "Mujeres"]
)

ax_3.set_title("Población por sexo de Costa Rica en los censos, 1864-2022")
ax_3.set_xlabel("Año del censo")
ax_3.set_ylabel("Habitantes")
ax_3.yaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))
ax_3.grid(axis="y", alpha=0.3)

plt.show()
```

- Verificación: dos líneas, leyenda y título.
- Las líneas casi se superponen durante todo el período: las diferencias
  son pequeñas y cambian de signo varias veces (más mujeres en 1864, 1883,
  1950, 1984 y desde 2000; más hombres en 1892, 1927, 1963 y 1973). La
  separación solo se aprecia en 2011 (89 586 mujeres más). Una respuesta
  correcta reconoce que el gráfico de líneas, con esta escala, no permite
  ver bien los cruces, y que un gráfico de la **diferencia** (o de la
  relación hombre-mujer) sería más informativo.

## Ejercicio 4 (histograma de la densidad de los cantones)

```python
fig_4, ax_4 = plt.subplots(figsize=(8, 4))

cantones["densidad"].plot(kind="hist", bins=20, ax=ax_4, color=AZUL, edgecolor="white")

ax_4.set_title("Distribución de la densidad de población de los cantones, 2022")
ax_4.set_xlabel("Habitantes por km²")
ax_4.set_ylabel("Cantidad de cantones")

plt.show()

print(cantones["densidad"].mean(), cantones["densidad"].median())
```

- Verificación: 20 barras y etiquetas en ambos ejes.
- Distribución fuertemente asimétrica a la derecha: la mayoría de los
  cantones tiene menos de 500 hab/km² y unos pocos del área metropolitana
  superan los 3000. Promedio 792.8 frente a mediana 83.5: el promedio es
  casi diez veces la mediana, arrastrado por Tibás, San José y los demás
  cantones densos.
- Con `bins=5`, toda la información queda en la primera barra (se pierde
  la forma de la cola); con `bins=80`, muchos intervalos vacíos y barras
  de uno o dos cantones (ruido). Extensión posible, no exigida: el
  histograma del logaritmo de la densidad (`np.log10(cantones["densidad"])`)
  muestra una distribución mucho más simétrica.

## Ejercicio 5 (dispersión: densidad y viviendas desocupadas)

```python
cantones["porcentaje_desocupadas"] = (
    cantones["viviendas_desocupadas"] / cantones["viviendas"] * 100
).round(1)

fig_5, ax_5 = plt.subplots(figsize=(8, 5))

cantones.plot(x="densidad", y="porcentaje_desocupadas", kind="scatter", ax=ax_5, color=AZUL, alpha=0.7)

ax_5.set_title("Densidad de población y viviendas desocupadas en los cantones, 2022")
ax_5.set_xlabel("Densidad de población (habitantes por km²), escala logarítmica")
ax_5.set_ylabel("Viviendas desocupadas (%)")
ax_5.set_xscale("log")
ax_5.xaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))
ax_5.grid(alpha=0.3)

for indice in cantones["porcentaje_desocupadas"].nlargest(2).index:
    fila = cantones.loc[indice]
    ax_5.annotate(fila["canton"], (fila["densidad"], fila["porcentaje_desocupadas"]),
                  xytext=(6, 4), textcoords="offset points", fontsize=9)

plt.show()
```

- Verificación: columna entre 0 y 100, un gráfico de dispersión y eje
  horizontal logarítmico.
- Relación negativa moderada (correlación -0.39): los cantones menos
  densos tienen mayor proporción de viviendas desocupadas. Los dos
  cantones anotados son Garabito (44.3 %, Jacó) y San Mateo (40.3 %).
  Explicación geográfica esperada: viviendas de recreo, condominios de
  playa y segundas residencias en las costas del Pacífico y en zonas
  rurales cercanas a la capital; en los cantones densos del Valle Central
  la vivienda es residencia habitual.
- Errores esperables: dividir por `viviendas_ocupadas` en vez de por el
  total; no usar la escala logarítmica (los puntos se amontonan a la
  izquierda); `idxmax()` en lugar de `nlargest(2)` (solo un cantón).

## Ejercicio 6 (dos gráficos: tasas de crecimiento)

```python
fig_6, (ax_a, ax_b) = plt.subplots(nrows=1, ncols=2, figsize=(11, 4))

ordenadas = provincias.sort_values("tasa_crecimiento_poblacion", ascending=False)

ordenadas.plot(x="provincia", y="tasa_crecimiento_poblacion", kind="bar", ax=ax_a, color=AZUL, legend=False)
ax_a.set_title("Población")
ax_a.set_xlabel("")
ax_a.set_ylabel("Crecimiento anual (%)")

ordenadas.plot(x="provincia", y="tasa_crecimiento_viviendas", kind="bar", ax=ax_b, color=AZUL, legend=False)
ax_b.set_title("Viviendas")
ax_b.set_xlabel("")
ax_b.set_ylabel("Crecimiento anual (%)")

for ax in (ax_a, ax_b):
    ax.tick_params(axis="x", rotation=45)

fig_6.suptitle("Tasas de crecimiento anual por provincia, 2011-2022", fontsize=13)
fig_6.tight_layout()

plt.show()
```

- Verificación: exactamente dos ejes en la figura y `suptitle`.
- Sí: en las siete provincias las viviendas crecen más rápido que la
  población (entre 1.1 y 1.4 puntos porcentuales más por año); la mayor
  brecha está en Puntarenas (1.79 frente a 3.26) y Cartago (0.95 frente a
  2.35). Interpretación esperada: hogares más pequeños (menos ocupantes
  por vivienda, como muestra la columna `promedio_ocupantes`) y viviendas
  desocupadas o de recreo.
- Errores esperables: distinto orden de las provincias en los dos
  gráficos; mismo eje vertical implícito (los dos gráficos tienen escalas
  parecidas aquí, pero no tienen por qué compartirlas); olvidar
  `tight_layout()` (los nombres girados se traslapan con el otro gráfico).

## Ejercicio 7 (guardar la figura)

```python
fig_6.savefig("tasas-provincias.png", dpi=200, bbox_inches="tight")
```

- Verificación: el archivo existe en el directorio de trabajo.
- Error esperable: llamar a `savefig()` en una celda posterior a la del
  gráfico con `plt.savefig()`: guarda una figura vacía (la misma trampa de
  la clínica). Con `fig_6.savefig()`, la referencia a la figura se
  conserva y funciona desde cualquier celda.

## Ejercicio 8 (tabla con formato: tasas de COVID-19)

```python
tabla_covid = cantones_covid.sort_values("tasa_100k", ascending=False).head(5)[
    ["provincia", "canton", "poblacion", "positivos", "tasa_100k"]
]

tabla_covid.style.format({
    "poblacion": "{:,.0f}",
    "positivos": "{:,.0f}",
    "tasa_100k": "{:,.0f}"
}).hide(axis="index")
```

- Resultado: Santa Ana (26 539), Flores (26 519), Belén (25 153), Garabito
  (24 321) y Heredia (24 090) casos por 100 000 habitantes.
- Errores esperables: aplicar `format()` a las columnas de texto;
  intentar seguir calculando con el `Styler`; olvidar `hide(axis="index")`.

## Ejercicio 9 (predicción: `plot(y="poblacion")` sin `x`)

- Predicción esperada: un gráfico de líneas con el índice (0 a 81) en el
  eje horizontal y la población en el vertical, con picos en el primer
  cantón de cada provincia (San José, Alajuela, Cartago, Heredia,
  Liberia, Puntarenas y Limón, que son los códigos x01).
- La explicación está en el propio cuaderno (bloque desplegable). Lo
  importante es que el estudiante identifique que la línea sugiere una
  continuidad inexistente entre categorías y que el gráfico adecuado es de
  barras (de un subconjunto).

## Ejercicio 10 (IA: generar el gráfico de los diez cantones más densos)

- Elementos de una buena respuesta: el prompt con la estructura de rol,
  contexto, tarea y formato; el código generado; la comparación con el
  gráfico del ejercicio 1 (mismo contenido, posiblemente distinto estilo:
  colores, tamaño, `invert_yaxis()` en lugar de ordenar de forma
  ascendente, `ax.barh()` de matplotlib en lugar de `plot()` de pandas);
  la lista de opciones desconocidas con su explicación; el resultado de
  las cuatro comprobaciones (código leído, gráfico revisado contra la
  lista de errores de diseño, valores comparados con la tabla,
  pertinencia).
- Errores esperables: entregar el código sin ejecutarlo; no comparar los
  valores con `sort_values("densidad", ascending=False).head(10)`; código
  que usa `plt.` en varias celdas.
- La declaración de uso de IA debe indicar asistente, propósito y partes.

## Ejercicio 11 (preguntas y gráficos para la tarea 2)

- Elementos de una buena respuesta: tres preguntas concretas sobre los
  datos de la tarea 1, cada una con el tipo de gráfico justificado con la
  tabla 1 (comparación entre categorías → barras; cambio en el tiempo →
  líneas; distribución → histograma; relación entre dos variables →
  dispersión) y con la identificación de las variables y sus tipos.
- Errores esperables: preguntas que no se responden con los datos
  disponibles; tres gráficos del mismo tipo; gráficos de pastel con
  muchas categorías; dos ejes verticales.
