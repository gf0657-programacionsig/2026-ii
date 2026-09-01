---
short_title: "Fundamentos de Python I: tipos de datos, variables y condicionales"
---

# Soluciones — Fundamentos de Python I: tipos de datos, variables y condicionales

Soluciones y pautas de respuesta de los ejercicios del cuaderno de notas [Fundamentos de Python I: tipos de datos, variables y condicionales](../ii-lenguaje-programacion-python/09-fundamentos-python.ipynb). Los ejercicios 1, 2, 3, 5 y 6 tienen en el propio cuaderno una celda de verificación con `assert`, que comprueba automáticamente el resultado; para los demás se describen los elementos de una buena respuesta y los errores esperables.

## Ejercicio 1 (variables de un cantón)

Ejemplo de respuesta con datos reales (cantón de Puntarenas):

```python
# Datos del cantón de Puntarenas
# Fuentes: INEC (Censo 2022), Instituto Geográfico Nacional
nombre_canton = "Puntarenas"
poblacion_canton = 119832     # habitantes
area_canton = 1842.3          # km2
tiene_costa = True
```

- Vale cualquier cantón con valores citables y coherentes (los valores
  exactos dependen de la fuente; lo evaluable es la correspondencia
  tipo–dato y la cita en el comentario). La celda de verificación
  revisa los cuatro tipos y la positividad.
- Errores esperables (los detectan los asserts): población como hilera
  (`"119832"`), área sin punto decimal (int), booleano como hilera
  (`"True"`). Recordar que estas variables se reutilizan en la parte
  III (diccionario del cantón).
- Fuente directa para verificar en clase: el archivo de resultados de
  población y vivienda 2022 del INEC (XLSX enlazado en el ejercicio)
  trae la población (cuadro por provincia, cantón y distrito) y la
  extensión territorial con la densidad (otro cuadro) de cada cantón.

## Ejercicio 2 (densidad con f-string)

```python
densidad_canton = poblacion_canton / area_canton
print(f"La densidad de población del cantón de {nombre_canton} es {densidad_canton:.1f} hab/km2.")
```

- Con los datos del ejemplo: ≈ 65.0 hab/km2. El assert de coherencia
  comprueba que la densidad venga de las variables del ejercicio 1.
- Errores esperables: olvidar la `f` inicial (imprime las llaves
  literales), invertir la división y calcular con números "a mano" en
  vez de con las variables (el assert de coherencia lo detecta).

## Ejercicio 3 (punto dentro del rectángulo de Costa Rica)

```python
latitud = 9.93
longitud = -84.08

dentro_cr = (latitud >= 8) and (latitud <= 11.3) and (longitud >= -86) and (longitud <= -82.5)
dentro_cr
```

- Con San José: `True` (el assert lo comprueba); con cualquier ciudad
  fuera del rectángulo (ej. Bogotá: 4.71, -74.07): `False`.
- Debe ser UNA expresión con `and` (encadenar comparaciones tipo
  `8 <= latitud <= 11.3` es válido en Python y puede aceptarse y
  comentarse como *idiom*).
- Errores esperables: usar `or` (casi todo da True), olvidar los
  signos negativos de las longitudes o invertir los límites
  oeste/este (-86 es el límite oeste: es MENOR que -82.5).

## Ejercicio 4 (predicción: concatenación vs suma)

- Respuesta esperada: imprime `55` y luego `10`. La explicación está
  en el desplegable del cuaderno; lo evaluable es que la predicción
  se haga ANTES de ejecutar y que la explicación propia mencione que
  el tipo de los operandos determina la operación de `+`.
- Predicción errónea típica: "10 y 10" (asumir que "5" se convierte
  solo). Rematar con la pregunta del desplegable: `"5" + 5` produce
  TypeError (clínica de errores).

## Ejercicio 5 (clasificación de ciclones tropicales)

```python
# ENTRADA
velocidad = 185  # velocidad sostenida del viento en km/h

# PROCESAMIENTO
if velocidad < 63:
    categoria = "depresión tropical"
elif velocidad < 119:
    categoria = "tormenta tropical"
elif velocidad < 154:
    categoria = "huracán categoría 1"
elif velocidad < 178:
    categoria = "huracán categoría 2"
elif velocidad < 209:
    categoria = "huracán categoría 3"
elif velocidad < 252:
    categoria = "huracán categoría 4"
else:
    categoria = "huracán categoría 5"

# SALIDA
print(f"Con vientos de {velocidad} km/h, el ciclón se clasifica como {categoria}.")
```

- Los `elif` con límites "menor que" reproducen exactamente la tabla 5
  (63, 119, 154, 178, 209, 252 como cotas). Probar los valores límite:
  62 → depresión, 63 → tormenta, 118 → tormenta, 119 → categoría 1,
  251 → categoría 4, 252 → categoría 5. Con 185 (estado final que
  piden los asserts): huracán categoría 3.
- Errores esperables: hileras que no coinciden exactamente
  (mayúsculas, tildes — los asserts lo detectan), usar `<=` y `>=`
  mezclados dejando "huecos" en los límites, condiciones redundantes
  tipo `velocidad >= 63 and velocidad < 119` (válidas pero
  innecesarias tras un `elif`) y desordenar las categorías (el orden
  de los `elif` importa).

## Ejercicio 6 (grados, minutos y segundos a grados decimales)

```python
# ENTRADA (longitud de San José: 84° 4' 48" oeste)
grados = 84
minutos = 4
segundos = 48

# PROCESAMIENTO
grados_decimales = grados + minutos / 60 + segundos / 3600
grados_decimales = -grados_decimales  # oeste: negativa

# SALIDA
print(f"La coordenada equivale a {grados_decimales:.4f} grados decimales.")
```

- Resultado: -84.0800 (el assert comprueba -84.08 con el signo). El
  signo puede aplicarse al final (como aquí) o definiendo los grados
  negativos desde la entrada (discutir: en ese caso los minutos y
  segundos deben restarse, no sumarse; el error es común).
- Errores esperables: dividir entre 100 en vez de 60/3600 y olvidar
  el signo (el assert lo detecta).

## Ejercicio 7 (clínica de errores)

Abierto; lista de verificación:

- Tres celdas con variantes propias: NameError (ej. `pobalcion`,
  `Densidad`), TypeError entre tipos incompatibles distinto de
  `"5" + 5` (ej. `"44.6" / 2`, `True + "a"`) y SyntaxError por dos
  puntos faltantes en otro condicional.
- Lo evaluable: anotar la última línea de cada mensaje y explicarla
  con palabras propias; notar la sugerencia "Did you mean..." del
  NameError cuando aplique.
- Las anotaciones se retoman en la parte III (ejercicio 7: explicar
  errores con un asistente de IA).

## Ejercicio 8 (ciclones con input y excepciones)

```python
# ENTRADA
velocidad_hilera = input("Ingrese la velocidad sostenida del viento en km/h: ")

try:
    velocidad = float(velocidad_hilera)

    # PROCESAMIENTO (igual al ejercicio 5)
    if velocidad < 63:
        categoria = "depresión tropical"
    elif velocidad < 119:
        categoria = "tormenta tropical"
    elif velocidad < 154:
        categoria = "huracán categoría 1"
    elif velocidad < 178:
        categoria = "huracán categoría 2"
    elif velocidad < 209:
        categoria = "huracán categoría 3"
    elif velocidad < 252:
        categoria = "huracán categoría 4"
    else:
        categoria = "huracán categoría 5"

    # SALIDA
    print(f"Con vientos de {velocidad} km/h, el ciclón se clasifica como {categoria}.")
except:
    print("Por favor ingrese un número (con punto decimal).")
```

- Probar con un número válido, con una hilera no numérica y con un
  número con coma decimal ("185,5" — cae en el except: conexión con el
  ejemplo del cuaderno).
- Variante aceptable: solo la conversión dentro del `try` y la
  clasificación después (más fina; puede comentarse como mejor
  práctica). Error esperable: dejar el `input()` dentro del `try`
  pensando que valida (input nunca falla; lo que falla es `float()`).
