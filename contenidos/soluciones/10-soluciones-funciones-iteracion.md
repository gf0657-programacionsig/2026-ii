# Soluciones — Fundamentos de Python II: funciones e iteración

Soluciones y pautas de respuesta de los ejercicios del cuaderno de notas [Fundamentos de Python II: funciones e iteración](../ii-lenguaje-programacion-python/10-funciones-iteracion.ipynb). Los ejercicios 1, 2 y 4 a 6 tienen en el propio cuaderno una celda de verificación con `assert`, que comprueba automáticamente el resultado; para los demás se describen los elementos de una buena respuesta y los errores esperables.

## Ejercicio 1 (función gms_a_decimales)

```python
def gms_a_decimales(grados, minutos, segundos):
    """Retorna el equivalente en grados decimales de una
    coordenada expresada en grados, minutos y segundos."""
    return grados + minutos / 60 + segundos / 3600
```

- Verificación: 84° 4' 48" → 84.08 y 9° 55' 48" → 9.93 (la celda de
  asserts lo comprueba). Para el oeste: `-gms_a_decimales(84, 4, 48)`.
- Errores esperables: incluir el signo dentro de la función restando
  mal los minutos/segundos (si los grados son negativos, la fórmula
  simple suma mal — por eso el enunciado pide anteponer el signo al
  resultado), y olvidar el `return` (la celda de verificación falla
  con un TypeError sobre None — conexión con el ejercicio 3).

## Ejercicio 2 (función categoria_ciclon)

```python
def categoria_ciclon(velocidad):
    """Retorna la categoría de un ciclón tropical según la
    velocidad sostenida del viento en km/h (escala Saffir-Simpson)."""
    if velocidad < 63:
        return "depresión tropical"
    elif velocidad < 119:
        return "tormenta tropical"
    elif velocidad < 154:
        return "huracán categoría 1"
    elif velocidad < 178:
        return "huracán categoría 2"
    elif velocidad < 209:
        return "huracán categoría 3"
    elif velocidad < 252:
        return "huracán categoría 4"
    else:
        return "huracán categoría 5"
```

- Nótese el patrón `return` en cada rama (no hace falta variable
  intermedia ni `print`): un `return` termina la función de inmediato.
- Errores esperables: retornar hileras que no coinciden exactamente
  (mayúsculas, sin tilde en "categoría", "huracan") — los asserts lo
  detectan y es buena ocasión para hablar de exactitud en hileras;
  usar `print` en vez de `return` (los asserts fallan con None).

## Ejercicio 3 (predicción: print vs return)

- Respuesta esperada: imprime `20` y luego `None`. La explicación está
  en el propio desplegable del cuaderno; lo evaluable es que la
  predicción se haga ANTES de ejecutar y que la explicación propia
  mencione que la función no retorna nada (retorna None).
- Predicción errónea típica: "imprime 20 y 20".

## Ejercicio 4 (promedio con acumulador)

```python
suma = 0
conteo = 0

for i in range(len(provincias)):
    densidad = calcular_densidad(poblaciones[i], areas[i])
    suma = suma + densidad
    conteo = conteo + 1

promedio = suma / conteo
print(f"Promedio de densidades provinciales: {promedio:.1f} hab/km2")
```

- Verificación: 131.4 (el assert lo comprueba). Densidades: San José
  322.4, Alajuela 106.1, Cartago 174.4, Heredia 180.3, Guanacaste
  40.7, Puntarenas 44.4, Limón 51.2.
- Punto de discusión: este promedio de densidades provinciales NO es
  la densidad del país (98.7 = población total / área total) — buen
  ejemplo de que agregar promedios requiere cuidado.
- Errores esperables: usar sum()/len() (el enunciado lo excluye),
  inicializar los acumuladores dentro del ciclo, y dividir dentro del
  ciclo en cada iteración.

## Ejercicio 5 (Parsons: provincia con mayor densidad)

Orden correcto:

```python
densidad_max = calcular_densidad(poblaciones[0], areas[0])
provincia_max = provincias[0]
for i in range(len(provincias)):
    densidad = calcular_densidad(poblaciones[i], areas[i])
    if densidad > densidad_max:
        densidad_max = densidad
        provincia_max = provincias[i]
print(f"La provincia más densamente poblada es {provincia_max}.")
```

- Verificación: San José (el assert lo comprueba).
- Puntos que el reordenamiento obliga a razonar: las inicializaciones
  van ANTES del ciclo; la actualización de `densidad_max` y
  `provincia_max` va DENTRO del if (dos líneas al mismo nivel); el
  print va fuera de todo. Error esperable: dejar el print dentro del
  ciclo (imprime siete veces; el assert pasa igual — detectarlo
  visualmente).

## Ejercicio 6 (conteo con umbral)

```python
conteo_densas = 0

for i in range(len(provincias)):
    if calcular_densidad(poblaciones[i], areas[i]) > 100:
        conteo_densas = conteo_densas + 1

print(f"Provincias con más de 100 hab/km2: {conteo_densas}")
```

- Verificación: 4 (San José, Alajuela, Cartago, Heredia).
- Error esperable: acumular la densidad en vez de contar (confundir
  los dos usos del acumulador).

## Ejercicio 7 (clínica de errores)

- (a) `calcular_densidad("352381", 44.6)` → `TypeError: unsupported
  operand type(s) for /: 'str' and 'float'`. Comparación esperada: el
  TypeError de la clínica era por un argumento FALTANTE; este es por
  tipos INCOMPATIBLES — mismo tipo de error, causas distintas; la
  última línea del mensaje lo distingue.
- (b) `calcular_densidades(1, 2)` → `NameError: name
  'calcular_densidades' is not defined`. Python sugiere nombres
  parecidos ("Did you mean: 'calcular_densidad'?") — vale la pena
  hacerlo notar.
- (c) for sin indentar → `IndentationError: expected an indented
  block after 'for' statement...`.
- Lo evaluable: anotar la última línea de cada mensaje y explicarla
  con palabras propias. Las anotaciones se retoman en la semana 5
  (asistentes de IA explicando errores).
