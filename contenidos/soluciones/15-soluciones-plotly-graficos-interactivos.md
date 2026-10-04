---
short_title: "plotly: gráficos interactivos"
---

# Soluciones — plotly: gráficos interactivos

Soluciones y pautas de respuesta de los ejercicios del cuaderno de notas [plotly: gráficos interactivos](../iii-analisis-visualizacion-datos/15-plotly-graficos-interactivos.ipynb). Los ejercicios 1 a 7 tienen en el propio cuaderno una celda de verificación con `assert`, que examina la figura creada; para los demás se describen los elementos de una buena respuesta y los errores esperables. Todas las soluciones suponen ejecutada la celda de carga de datos del cuaderno (`provincias`, `cantones`, `distritos`, `censos`, `cantones_covid`, la función `mostrar()` y la configuración de `px.defaults`).

## Ejercicio 1 (barras horizontales: los diez cantones más densos)

```python
top_densos = cantones.sort_values("densidad", ascending=False).head(10)

fig_1 = px.bar(
    top_densos.sort_values("densidad"),
    x="densidad",
    y="canton",
    orientation="h",
    title="Los diez cantones más densamente poblados de Costa Rica, 2022",
    labels={"densidad": "Habitantes por km²", "canton": "Cantón", "provincia": "Provincia"},
    hover_data=["provincia"],
    text_auto=",.0f"
)

fig_1.update_layout(yaxis_title="", xaxis_tickformat=",")

mostrar(fig_1)
```

- Verificación: traza de barras horizontal, 10 cantones y título.
- Errores esperables: ordenar de forma descendente (el más denso queda
  abajo); intercambiar `x` e `y` sin `orientation="h"`; olvidar
  `hover_data` (la provincia no aparece en la etiqueta emergente).

## Ejercicio 2 (barras agrupadas: viviendas ocupadas y desocupadas)

```python
fig_2 = px.bar(
    provincias.sort_values("viviendas", ascending=False),
    x="provincia",
    y=["viviendas_ocupadas", "viviendas_desocupadas"],
    barmode="group",
    title="Viviendas ocupadas y desocupadas por provincia, 2022",
    labels={"provincia": "Provincia", "value": "Viviendas", "variable": "Estado"}
)

nombres = {"viviendas_ocupadas": "Ocupadas", "viviendas_desocupadas": "Desocupadas"}
fig_2.for_each_trace(lambda traza: traza.update(name=nombres[traza.name]))
fig_2.update_layout(xaxis_title="", yaxis_tickformat=",", legend_title_text="")

mostrar(fig_2)
```

- Verificación: dos trazas, `barmode="group"` y nombres "Ocupadas" y
  "Desocupadas".
- Al ocultar "Ocupadas" en la leyenda, el eje vertical se reajusta a la
  escala de las desocupadas y se aprecia que Guanacaste y Puntarenas
  tienen casi tantas viviendas desocupadas como San José, con muchas
  menos viviendas en total.
- Errores esperables: omitir `barmode="group"` (barras apiladas);
  renombrar con `labels` en lugar de `for_each_trace()` (`labels` traduce
  los nombres de las columnas en los ejes y en la etiqueta emergente,
  pero no los nombres de las series en la leyenda cuando `y` es una
  lista).

## Ejercicio 3 (líneas: tasa de crecimiento entre censos)

```python
fig_3 = px.line(
    censos,
    x="anio",
    y="tasa_crecimiento",
    markers=True,
    title="Tasa de crecimiento anual de la población de Costa Rica entre censos",
    labels={"anio": "Año del censo", "tasa_crecimiento": "Crecimiento anual (%)"}
)

mostrar(fig_3)
```

- Verificación: traza de líneas con marcadores y título.
- El mayor crecimiento se registró entre los censos de 1950 y 1963 (3.94 %
  anual), como muestra la etiqueta emergente del punto de 1963. El primer
  censo no tiene tasa (`NaN`) y la línea empieza en 1883.

## Ejercicio 4 (histograma de la densidad de los cantones)

```python
fig_4 = px.histogram(
    cantones,
    x="densidad",
    nbins=20,
    title="Distribución de la densidad de población de los cantones, 2022",
    labels={"densidad": "Habitantes por km²"}
)

fig_4.update_layout(yaxis_title="Cantidad de cantones", bargap=0.05)

mostrar(fig_4)
```

- Verificación: traza de histograma y etiqueta del eje horizontal.
- Con `nbins=20`, plotly redondea los intervalos a valores "bonitos" (por
  ejemplo, de 500 en 500): la primera barra abarca los cantones con menos
  de 500 hab/km², que son 59 de los 82. Si el estudiante obtiene otro
  intervalo por usar otro `nbins`, la respuesta es válida mientras la
  lea de la etiqueta emergente. Dato de referencia: 44 cantones tienen
  menos de 100 hab/km².

## Ejercicio 5 (dispersión: densidad y viviendas desocupadas)

```python
cantones["porcentaje_desocupadas"] = (
    cantones["viviendas_desocupadas"] / cantones["viviendas"] * 100
).round(1)

fig_5 = px.scatter(
    cantones,
    x="densidad",
    y="porcentaje_desocupadas",
    color="provincia",
    size="viviendas",
    hover_name="canton",
    log_x=True,
    title="Densidad de población y viviendas desocupadas en los cantones, 2022",
    labels={
        "densidad": "Densidad de población (habitantes por km²)",
        "porcentaje_desocupadas": "Viviendas desocupadas (%)",
        "provincia": "Provincia",
        "viviendas": "Viviendas"
    }
)

mostrar(fig_5)
```

- Verificación: eje horizontal logarítmico, siete trazas (una por
  provincia) y nombre del cantón en la etiqueta emergente.
- Los tres cantones con mayor porcentaje son Garabito (44.3 %), San Mateo
  (40.3 %) y Parrita (33.2 %): costa del Pacífico central y sus
  alrededores, zona de viviendas de recreo.
- Errores esperables: `color` con la columna numérica (produce una escala
  continua, no una traza por provincia); `size` con el porcentaje en lugar
  de las viviendas; olvidar `log_x=True`.

## Ejercicio 6 (cajas: población de los distritos por provincia)

```python
fig_6 = px.box(
    distritos,
    x="provincia",
    y="poblacion",
    points="all",
    hover_name="distrito",
    log_y=True,
    title="Población de los distritos de Costa Rica, por provincia, 2022",
    labels={"provincia": "Provincia", "poblacion": "Habitantes (escala logarítmica)"}
)

fig_6.update_layout(xaxis_title="")

mostrar(fig_6)
```

- Verificación: traza de cajas y eje vertical logarítmico.
- La mediana más alta es la de Limón (11 974 habitantes por distrito):
  tiene pocos distritos (27) y grandes. El distrito más poblado del país
  es Pavas (cantón de San José, provincia de San José), con 83 573
  habitantes; se identifica con el cursor sobre el punto más alto.
- Errores esperables: `hover_name="canton"` en lugar de `"distrito"`;
  omitir la escala logarítmica (las cajas de casi todas las provincias
  quedan aplastadas contra el eje).

## Ejercicio 7 (guardar como página web)

```python
fig_5.write_html("cantones-desocupadas.html")
```

- Verificación: el archivo existe en el directorio de trabajo.
- El archivo pesa unos 4 MB porque incluye la biblioteca plotly.js
  completa; `write_html(..., include_plotlyjs="cdn")` produce un archivo
  pequeño que la carga desde Internet.

## Ejercicio 8 (predicción: barras apiladas por defecto)

- Predicción esperada: barras apiladas (no agrupadas), con la barra de
  San José de altura 1 601 167 (773 612 hombres + 827 555 mujeres), las
  provincias en el orden del archivo y "hombres" y "mujeres" en la
  leyenda. La explicación está en el bloque desplegable del cuaderno.
- Errores esperables: predecir barras agrupadas (confusión con el
  comportamiento por defecto de `plot()` de pandas, que sí agrupa).

## Ejercicio 9 (IA: dispersión de área contra población)

- Elementos de una buena respuesta: el prompt con la estructura de rol,
  contexto, tarea y formato; el código generado con `px.scatter(...,
  log_x=True, log_y=True, hover_name="canton", color="provincia",
  labels={...})`; las comprobaciones: código leído, gráfico revisado
  contra la lista de errores de diseño, tres etiquetas emergentes
  comparadas con las filas de `cantones` (por ejemplo, con
  `cantones[cantones["canton"] == "Tibás"]`) y evaluación de si el
  gráfico responde la pregunta (la relación entre área y población es
  débil: los cantones grandes no son los más poblados).
- Errores esperables: aceptar código con `fig.show()` en un cuaderno del
  sitio; etiquetas emergentes con columnas irrelevantes (códigos); no
  comparar los valores con la tabla.
- La declaración de uso de IA debe indicar asistente, propósito y partes.

## Ejercicio 10 (el mismo gráfico en matplotlib y en plotly)

- Elementos de una buena respuesta: dos versiones del mismo gráfico con
  los datos de la tarea 1, ambas con título, etiquetas y unidades; una
  comparación con los criterios de la tabla 1 (destino, información
  adicional en la etiqueta emergente, cantidad de código, peso) y una
  decisión justificada para la tarea 2. Cualquiera de las dos bibliotecas
  es aceptable; lo que se evalúa es la justificación.
- Errores esperables: comparar gráficos distintos; justificar la elección
  solo por estética; ignorar el destino del cuaderno (GitHub muestra las
  salidas de plotly solo si el cuaderno se guardó con ellas, y no siempre
  de forma interactiva: conviene mencionarlo como limitación).
