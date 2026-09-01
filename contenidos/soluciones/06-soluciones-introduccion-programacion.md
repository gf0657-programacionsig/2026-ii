---
short_title: "Introducción a la programación de computadoras"
---

# Soluciones — Introducción a la programación de computadoras

Soluciones y pautas de respuesta de los ejercicios de la lección [Introducción a la programación de computadoras](../i-introduccion-ciencia-datos-programacion/06-introduccion-programacion.md). Para los ejercicios sin una única respuesta correcta se describen los elementos que debe incluir una buena respuesta y los errores esperables.

## Ejercicio 1 (algoritmo del valor mínimo)

Solución esperada (espejo del ejemplo del máximo):

```text
1. Lea la lista.
2. Si la lista está vacía, despliegue "Lista vacía" y concluya.
   Si no, continúe con el paso 3.
3. Designe el primer elemento como "mínimo actual".
4. Recorra la lista y compare cada elemento con el mínimo actual.
   4.1. Si un elemento es menor que el mínimo actual, desígnelo
        como el nuevo mínimo actual.
5. Al finalizar el recorrido, imprima el mínimo actual.
```

Aplicación a `[8.5, 3.2, -4.7, 10.9, 0.6]`: mínimo actual 8.5 → 3.2 →
-4.7 → (10.9 y 0.6 no lo cambian) → resultado **-4.7**.

- Verificación de características: entradas (la lista), salidas (el
  mínimo), pasos claros (cada comparación definida), finitud (termina
  al acabar el recorrido).
- Error esperable: olvidar el caso de la lista vacía (la característica
  de "pasos claros" cubre también los casos límite).

## Ejercicio 2 (hoja electrónica de densidades)

- Estructura esperada: columnas de cantón, población y área
  (**entrada**), columna de densidad con la fórmula `=B2/C2`
  (**procesamiento**) y el valor resultante, quizá con formato o
  gráfico (**salida**).
- Datos de referencia (INEC, Censo 2022; con área oficial IGN): p. ej.
  San José ≈ 352 381 hab / 44.6 km² ≈ 7900 hab/km²; los valores exactos
  dependen de la fuente — lo evaluable es la coherencia y la
  identificación de los componentes del modelo, no el decimal.
- Error esperable: mezclar unidades (área en hectáreas o m²).

## Ejercicio 3 (ejecución en Colab y mycompiler)

- Operativo. Ambas salidas deben ser: lista de entrada y
  `Valor máximo de la lista: 90.2`.
- En R, la salida de `cat` no muestra el decimal de `90.2` de forma
  distinta; si alguien reporta diferencias de formato (espacios), es
  normal: `print`/`cat` formatean distinto — puede comentarse.

## Ejercicio 4 (programa del mínimo en Python)

```python
lista = [8.5, 3.2, -4.7, 10.9, 0.6]
print("Lista de entrada:", lista)

if len(lista) == 0:
    print("La lista está vacía")
else:
    minimo = lista[0]
    i = 0
    while i < len(lista):
        if lista[i] < minimo:
            minimo = lista[i]
        i = i + 1
    print("Valor mínimo de la lista:", minimo)
```

- Único cambio necesario: `>` por `<` (y los nombres). Error esperable:
  cambiar el nombre de la variable pero no el operador (devuelve el
  máximo) — buen ejemplo de que "corre sin errores" ≠ "es correcto".

## Ejercicio 5 (densidad de población en Python)

```python
# Entrada
poblacion = 352381   # cantón de San José, Censo 2022
area = 44.6          # km²

# Procesamiento
densidad = poblacion / area

# Salida
print("Densidad de población (hab/km²):", densidad)
```

- Salida ≈ 7901.4. Vale cualquier cantón con valores reales citables.
- Errores esperables: invertir la división (área/población) y no
  comentar/estructurar según entrada-procesamiento-salida (se pidió
  seguir el algoritmo de la lección).
