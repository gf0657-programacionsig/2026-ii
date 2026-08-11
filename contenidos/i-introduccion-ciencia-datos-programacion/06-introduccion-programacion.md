# Introducción a la programación de computadoras

## Trabajo previo

### Lecturas

Antes de la clase, revise las siguientes lecturas, ambas en inglés: son los capítulos iniciales de los dos libros con los que se estudiará el lenguaje Python a partir de la próxima semana. La primera presenta la programación como una forma de pensar; la segunda explica por qué conviene aprender a programar y describe los componentes de una computadora. Como lectura complementaria breve, el artículo de Wing introduce el pensamiento computacional.

Downey, A. B. (2024). Programming as a way of thinking. En *Think Python: How to think like a computer scientist* (3.ª ed.). O'Reilly Media. https://allendowney.github.io/ThinkPython/chap01.html
\
\
Severance, C. R. (2016). Why should you learn to write programs? En *Python for everybody: Exploring data in Python 3* (S. Blumenberg y E. Hauser, eds.). CreateSpace Independent Publishing Platform. https://www.py4e.com/html3/01-intro
\
\
Wing, J. M. (2006). Computational thinking. *Communications of the ACM*, *49*(3), 33–35. [https://dl.acm.org/doi/10.1145/1118178.1118215](https://dl.acm.org/doi/10.1145%2F1118178.1118215)

### Videos

La primera lección del curso CS50 de la Universidad de Harvard (en inglés, con subtítulos) presenta de forma accesible varios de los conceptos de este capítulo, como los sistemas binarios y los algoritmos.

CS50. (2024). *CS50x 2024 – Lecture 0 – Scratch* [video]. YouTube. https://www.youtube.com/watch?v=3LPJfIKxwWc

## Introducción

Las semanas anteriores presentaron las herramientas del curso: los cuadernos de notas, Markdown y el control de versiones. Este capítulo se ocupa del fondo: qué es programar una computadora. Estudia qué pueden hacer las computadoras, qué es un algoritmo y cómo se convierte en un programa, recorre brevemente la historia y la arquitectura de las computadoras y concluye con los lenguajes de programación, como antesala del estudio de Python que comienza la próxima semana.

## Computadoras, algoritmos y programas

### Capacidades de las computadoras

Una **computadora** es una máquina que ejecuta secuencias de instrucciones, denominadas **programas**. Las instrucciones de los programas realizan operaciones de diversos tipos, entre las que pueden mencionarse:

- **Cálculos aritméticos**: sumar, restar, multiplicar, dividir.
- **Procesamiento de texto**: buscar, reemplazar, dividir y concatenar hileras de texto.
- **Operaciones lógicas**: determinar si un número es mayor que otro, si una hilera está contenida en otra o si un elemento está en una lista.
- **Manipulación de datos**: crear, leer, actualizar y eliminar datos en estructuras de datos (ej. listas, matrices) o en bases de datos.
- **Interacción**: recibir entradas (ej. del teclado o del ratón) y mostrar información (ej. en la pantalla o en la impresora).
- **Manejo de archivos**: leer, escribir y modificar archivos.
- **Comunicaciones en red**: enviar y recibir datos a través de una red local o de Internet (ej. páginas web, correos electrónicos).

La capacidad de ser programadas permite modificar el funcionamiento de las computadoras sin alterar sus componentes físicos, lo que las hace aptas para ayudar a resolver una gran variedad de problemas: por eso se dice que son máquinas de **propósito general**, a diferencia de las máquinas construidas para fines específicos. Severance (2016) argumenta que, precisamente por esa versatilidad, aprender a programar es valioso en cualquier disciplina: permite poner la computadora al servicio de las preguntas propias —en este curso, las de la geografía— sin depender de programas escritos por otras personas para otros fines.

### Algoritmos

Para que una computadora ayude a resolver un problema, es necesario expresarlo como un conjunto de pasos claramente definidos. Un **algoritmo** es un conjunto de instrucciones definidas, no ambiguas, ordenadas y finitas que permite solucionar un problema. Los algoritmos son fundamentales en la computación: son la base sobre la que se construyen los programas. Un algoritmo puede ser tan sencillo como una receta de cocina o tan complejo como los que se emplean en [aprendizaje automático](https://es.wikipedia.org/wiki/Aprendizaje_autom%C3%A1tico).

Un algoritmo debe cumplir ciertas características básicas:

1. **Recibir entradas**: los datos con los que trabaja.
2. **Generar salidas**: los resultados de las operaciones que ejecuta.
3. **Tener pasos claros**: la definición de cada paso debe ser precisa y sin ambigüedades.
4. **Ser finito**: debe terminar después de un número finito de pasos.

La habilidad de formular problemas y soluciones de manera que puedan expresarse como algoritmos se conoce como **pensamiento computacional** e incluye estrategias como la descomposición de problemas en partes, el reconocimiento de patrones y la abstracción. Wing (2006) sostiene que es una habilidad fundamental para todas las disciplinas, no solo para la computación.

Un algoritmo puede representarse mediante una descripción escrita, [pseudocódigo](https://es.wikipedia.org/wiki/Pseudoc%C3%B3digo) o un [diagrama de flujo](https://es.wikipedia.org/wiki/Diagrama_de_flujo), entre otras formas. Como ejemplo, se presenta la descripción de un algoritmo para obtener el valor máximo de una lista:

```text
Algoritmo para obtener el valor máximo de una lista
---------------------------------------------------

1. Lea la lista (del teclado, de un archivo o de alguna otra fuente).
2. Si la lista está vacía, despliegue la hilera de texto "Lista vacía"
   y concluya el algoritmo. Si no, continúe con el paso 3.
3. Designe el primer elemento de la lista como "máximo actual".
4. Recorra la lista y compare cada uno de los elementos con el máximo actual.
   4.1. Si un elemento comparado es mayor que el máximo actual,
        entonces desígnelo como el nuevo máximo actual.
5. Al finalizar el recorrido de la lista, imprima el máximo actual
   como valor máximo de la lista.
```

Seguidamente se muestra la aplicación del algoritmo a la lista `[29.6, -36.81, 31.85, 25.71, 90.2, 0.4]`. En cada paso del recorrido, el elemento en **negrita** es el máximo actual y el elemento en *itálica* es el que está siendo comparado:

1. Lista leída: [29.6, -36.81, 31.85, 25.71, 90.2, 0.4]
2. La lista no está vacía, por lo que se continúa con el paso 3.
3. Se designa el primer elemento, 29.6, como el máximo actual.
4. Se recorre la lista comparando cada elemento con el máximo actual:

    [**29.6**, *-36.81*, 31.85, 25.71, 90.2, 0.4]

    [**29.6**, -36.81, *31.85*, 25.71, 90.2, 0.4]

    [29.6, -36.81, **31.85**, *25.71*, 90.2, 0.4]

    [29.6, -36.81, **31.85**, 25.71, *90.2*, 0.4]

    [29.6, -36.81, 31.85, 25.71, **90.2**, *0.4*]

5. Al finalizar el recorrido, se imprime el máximo actual como valor máximo de la lista: 90.2.

Note que el algoritmo tiene un inicio claramente definido (la lectura de la lista) y una condición de finalización (que termine el recorrido), que cada paso intermedio está especificado con claridad —incluidas las condiciones para que se ejecute— y que comprende la lectura de entradas (la lista), su procesamiento (el recorrido y las comparaciones) y la generación de salidas (el valor máximo).

*Ejercicios de esta sección: [ejercicios sobre algoritmos](#ejercicios-algoritmos).*

### El modelo entrada–procesamiento–salida

El modelo **entrada–procesamiento–salida** (*input–process–output*, IPO) describe la estructura básica de un algoritmo o de un programa, como se aprecia en el ejemplo anterior: se reciben entradas, se procesan y se generan salidas. La figura 1 lo esquematiza.

```{mermaid}
flowchart LR
  E([Entrada]) --> P([Procesamiento])
  P --> S([Salida])
```

<p style="text-align: center;"><strong>Figura 1</strong>. Modelo entrada–procesamiento–salida. Elaboración propia.</p>

Sus componentes son:

- **Entrada**: los datos que recibe el algoritmo o programa. Pueden provenir del teclado, de un archivo o de un sensor, entre otras fuentes. La calidad de las entradas afecta directamente la calidad del resultado.
- **Procesamiento**: las operaciones que transforman las entradas —cálculos matemáticos, operaciones lógicas, transformaciones de datos— de acuerdo con un conjunto de instrucciones. Es donde se realiza el "trabajo" principal.
- **Salida**: el resultado del procesamiento, que puede presentarse en la pantalla, escribirse en un archivo o servir como entrada de otro algoritmo o programa.

Para ilustrar el modelo, considere el cálculo de la [densidad de población](https://es.wikipedia.org/wiki/Densidad_de_poblaci%C3%B3n), un indicador de uso constante en geografía. Requiere dos entradas: la población de un territorio y su área (en km²). El procesamiento aplica la fórmula $d = P/A$ y la salida es la densidad, en habitantes por km². Un posible algoritmo es:

```text
1. Lea la población y el área del territorio.
2. Calcule la densidad mediante la fórmula: densidad = población / área.
3. Imprima la densidad.
```

*Ejercicios de esta sección: [ejercicios sobre algoritmos](#ejercicios-algoritmos).*

### De los algoritmos a los programas

El diseño de un algoritmo puede verse como un paso previo a la escritura de un programa, y un mismo algoritmo puede implementarse en diferentes lenguajes de programación. Seguidamente se muestra la implementación del algoritmo del valor máximo en dos lenguajes de uso frecuente en ciencia de datos: [Python](https://www.python.org/) y [R](https://www.r-project.org/).

```python
# Python
# Obtención del valor máximo de una lista

# Entrada
lista = [29.6, -36.81, 31.85, 25.71, 90.2, 0.4]
print("Lista de entrada:", lista)

# Procesamiento
if len(lista) == 0:
    print("La lista está vacía")
else:
    maximo = lista[0]
    i = 0
    while i < len(lista):
        if lista[i] > maximo:
            maximo = lista[i]
        i = i + 1

    # Salida
    print("Valor máximo de la lista:", maximo)
```

```r
# R
# Obtención del valor máximo de una lista

# Entrada
lista <- c(29.6, -36.81, 31.85, 25.71, 90.2, 0.4)
cat("Lista de entrada:", lista, "\n")

# Procesamiento
if (length(lista) == 0) {
  cat("La lista está vacía", "\n")
} else {
  maximo <- lista[1]
  i <- 1
  while (i <= length(lista)) {
    if (lista[i] > maximo) {
      maximo <- lista[i]
    }
    i <- i + 1
  }

  # Salida
  cat("Valor máximo de la lista:", maximo, "\n")
}
```

Aunque la sintaxis difiere —se estudiará la de Python a partir de la próxima semana—, ambos programas siguen exactamente los mismos pasos del algoritmo, con las secciones de entrada, procesamiento y salida señaladas en comentarios. Cabe aclarar que tanto Python como R ya incluyen funciones que obtienen el máximo de una lista (`max()`); el ejemplo lo implementa paso a paso con fines didácticos.

*Ejercicios de esta sección: [ejercicios sobre programas](#ejercicios-programas).*

## Breve historia de las computadoras

### Calculadoras mecánicas

Durante el siglo XVII, varios matemáticos construyeron calculadoras mecánicas capaces de realizar operaciones aritméticas. Alrededor de 1645, el filósofo y matemático francés [Blaise Pascal](https://es.wikipedia.org/wiki/Blaise_Pascal) (1623–1662) inventó la [Pascalina](https://es.wikipedia.org/wiki/Pascalina), una calculadora de ruedas y engranajes que podía sumar y restar, creada para ayudar a su padre en cálculos de aritmética comercial. En 1672, el científico alemán [Gottfried Leibniz](https://es.wikipedia.org/wiki/Gottfried_Leibniz) (1646–1716) extendió las ideas de Pascal con la [máquina de Leibniz](https://es.wikipedia.org/wiki/Stepped_Reckoner) (*Stepped Reckoner*), que además podía multiplicar, dividir y calcular raíces cuadradas, basada en un tambor cilíndrico conocido como [rueda de Leibniz](https://es.wikipedia.org/wiki/Rueda_de_Leibniz). La figura 2 muestra una réplica.

<figure style="text-align: center;">
  <img
    src="img/maquina-leibniz.jpg"
    alt="Réplica de la máquina de Leibniz"
  >
  <figcaption><strong>Figura 2</strong>. Réplica de la máquina de Leibniz. Fuente: Kolossos, a través de <a href="https://commons.wikimedia.org/wiki/File:Leibnitzrechenmaschine.jpg">Wikimedia Commons</a>.</figcaption>
</figure>

El objetivo de Leibniz era realizar cálculos de manera "fácil, rápida y fiable", aunque las primeras versiones de su máquina fallaban con frecuencia por problemas mecánicos. Los derivados de estas calculadoras continuaron produciéndose durante tres siglos, hasta que sus equivalentes electrónicos se volvieron baratos y accesibles a inicios de la década de 1970.

### La máquina analítica de Babbage

En la primera mitad del siglo XIX, el matemático inglés [Charles Babbage](https://es.wikipedia.org/wiki/Charles_Babbage) (1791–1871) diseñó la [máquina analítica](https://es.wikipedia.org/wiki/M%C3%A1quina_anal%C3%ADtica), una computadora mecánica considerada la primera computadora programable de la historia, que incorporaba características de las computadoras modernas: usaba tarjetas perforadas para la entrada de datos, una unidad aritmética para las operaciones y una memoria capaz de almacenar 1000 números, y su lenguaje de programación —similar a los actuales [lenguajes ensambladores](https://es.wikipedia.org/wiki/Lenguaje_ensamblador)— admitía ciclos y condicionales. Nunca fue terminada, por limitaciones técnicas y económicas. La figura 3 muestra la parte construida.

<figure style="text-align: center;">
  <img
    src="img/maquina-analitica.jpg"
    alt="Máquina analítica de Babbage"
  >
  <figcaption><strong>Figura 3</strong>. Máquina analítica de Babbage. Fuente: Bruno Barral, a través de <a href="https://commons.wikimedia.org/wiki/File:AnalyticalMachine_Babbage_London.jpg">Wikimedia Commons</a>.</figcaption>
</figure>

En 1843, la matemática británica [Ada Lovelace](https://es.wikipedia.org/wiki/Ada_Lovelace) (1815–1852) tradujo al inglés una descripción de la máquina analítica escrita por el matemático italiano [Luigi Menabrea](https://es.wikipedia.org/wiki/Luigi_Menabrea). En las notas que agregó a la traducción —más extensas que el propio artículo— incluyó los pasos con los que la máquina podría calcular los [números de Bernoulli](https://es.wikipedia.org/wiki/N%C3%BAmero_de_Bernoulli), elaborados en colaboración con Babbage y considerados el primer programa de computadora publicado. El diagrama correspondiente se muestra en la figura 4.

<figure style="text-align: center;">
  <img
    src="img/programa-maquina-analitica.jpg"
    alt="Diagrama del algoritmo para el cálculo de los números de Bernoulli en la máquina analítica"
  >
  <figcaption><strong>Figura 4</strong>. Diagrama del algoritmo para el cálculo de los números de Bernoulli en la máquina analítica. Fuente: Ada Lovelace, a través de <a href="https://commons.wikimedia.org/wiki/File:Diagram_for_the_computation_of_Bernoulli_numbers.jpg">Wikimedia Commons</a>.</figcaption>
</figure>

El aporte de Lovelace fue fundamental porque fue la primera persona en reconocer que la capacidad de las máquinas podía ir más allá del cálculo numérico: anticipó que en el futuro podrían componer música o generar gráficos, y enfatizó la diferencia entre la máquina analítica —programable para problemas de complejidad arbitraria— y las calculadoras que la precedieron.

### La máquina de Turing

En 1936, el matemático británico [Alan Turing](https://es.wikipedia.org/wiki/Alan_Turing) (1912–1954) propuso la **máquina de Turing**, un modelo matemático —no un dispositivo físico— que manipula símbolos en una cinta según un conjunto de reglas. La figura 5 muestra una representación artística.

<figure style="text-align: center;">
  <img
    src="img/maquina-turing.png"
    alt="Representación artística de la máquina de Turing"
  >
  <figcaption><strong>Figura 5</strong>. Representación artística de la máquina de Turing. Fuente: Porao, a través de <a href="https://commons.wikimedia.org/wiki/File:Turing_Machine.png">Wikimedia Commons</a>.</figcaption>
</figure>

Una máquina de Turing se compone de:

1. **Una cinta**: actúa como memoria; se divide en celdas, cada una de las cuales puede contener un símbolo (ej. una letra, un número).
2. **Una cabeza lectora/escritora**: lee y escribe símbolos en la cinta.
3. **Un conjunto de estados**: entre los que la máquina cambia en respuesta a lo que lee; hay un estado inicial y uno o más estados de parada que indican que la computación terminó.
4. **Una tabla de acciones**: indica, para cada combinación de estado actual y símbolo leído, qué debe hacer la máquina: escribir un símbolo, mover la cabeza a la izquierda o a la derecha, o cambiar de estado.

Con este esquema tan simple, una máquina de Turing puede ejecutar cualquier algoritmo, si dispone del tiempo y los recursos necesarios. Un sistema capaz de resolver cualquier problema computable —como una computadora o un lenguaje de programación de propósito general— se dice [Turing-completo](https://es.wikipedia.org/wiki/Turing_completo); no todos los sistemas lo son, pues algunos se diseñan con restricciones para propósitos específicos. Turing es considerado uno de los padres de la computación moderna por sus contribuciones a la [teoría de la computación](https://es.wikipedia.org/wiki/Teor%C3%ADa_de_la_computaci%C3%B3n) y a la [inteligencia artificial](https://es.wikipedia.org/wiki/Inteligencia_artificial), campo en el que propuso la [prueba de Turing](https://es.wikipedia.org/wiki/Prueba_de_Turing) para evaluar si una máquina exhibe un comportamiento equivalente al de una persona.

### Primeras computadoras electrónicas

Durante la Segunda Guerra Mundial (1939–1945) se construyeron en el Reino Unido máquinas para descifrar mensajes codificados: la [Bombe](https://es.wikipedia.org/wiki/Bombe), un dispositivo electromecánico en cuyo diseño participó el propio Turing, y [Colossus](https://es.wikipedia.org/wiki/Colossus), considerada una de las primeras computadoras electrónicas digitales programables. Su programación, sin embargo, se realizaba mediante interruptores y conexiones de *hardware*, no con un programa almacenado en memoria. La figura 6 muestra una computadora Colossus.

<figure style="text-align: center;">
  <img
    src="img/colossus.jpg"
    alt="Computadora Colossus operada por integrantes del Women's Royal Naval Service (WRNS)"
  >
  <figcaption><strong>Figura 6</strong>. Computadora Colossus operada por integrantes del <em>Women's Royal Naval Service</em> (WRNS). Fuente: fotografía de autoría desconocida, a través de <a href="https://commons.wikimedia.org/wiki/File:Colossus.jpg">Wikimedia Commons</a>.</figcaption>
</figure>

En la misma época, el ejército de Estados Unidos construyó [ENIAC](https://es.wikipedia.org/wiki/ENIAC) (*Electronic Numerical Integrator and Computer*), terminada en 1945 para calcular tablas de tiro de artillería y considerada la primera computadora electrónica digital de propósito general: era Turing-completa. La figura 7 la muestra.

<figure style="text-align: center;">
  <img
    src="img/eniac.jpg"
    alt="Computadora ENIAC en Filadelfia, Estados Unidos"
  >
  <figcaption><strong>Figura 7</strong>. Computadora ENIAC en Filadelfia, Estados Unidos. Fuente: fotografía del Ejército de los Estados Unidos, a través de <a href="https://commons.wikimedia.org/wiki/File:Eniac.jpg">Wikimedia Commons</a>.</figcaption>
</figure>

## La computadora moderna

### La arquitectura de von Neumann

En 1945, el matemático húngaro-estadounidense [John von Neumann](https://es.wikipedia.org/wiki/John_von_Neumann) (1903–1957) propuso el concepto de [programa almacenado](https://es.wikipedia.org/wiki/Computador_de_programa_almacenado): los datos y los programas se guardan en una estructura llamada memoria, separada de los componentes que ejecutan las instrucciones, lo que hace a las computadoras mucho más fáciles de reprogramar. Este modelo, conocido como **arquitectura de von Neumann**, es la base de las computadoras actuales (Severance, 2016). Su esquema se muestra en la figura 8.

<figure style="text-align: center;">
  <img
    src="img/arquitectura-von-neumann.jpg"
    alt="Arquitectura de von Neumann"
  >
  <figcaption><strong>Figura 8</strong>. Arquitectura de von Neumann. Fuente: David Strigoi, a través de <a href="https://commons.wikimedia.org/wiki/File:Arquitecturaneumann.jpg">Wikimedia Commons</a>.</figcaption>
</figure>

Sus componentes principales son:

- **Memoria principal**: almacena las instrucciones de los programas y los datos que estos utilizan. Se le denomina RAM (*random access memory*, memoria de acceso aleatorio) porque acceder a cualquiera de sus posiciones toma el mismo tiempo; cada posición tiene una dirección que se usa para leerla o escribirla.
- **Unidad central de procesamiento** (CPU, *central processing unit*): ejecuta las instrucciones de los programas. Contiene memorias temporales de alta velocidad y poca capacidad, llamadas registros, y se compone de la **unidad de control**, que determina cuál es la siguiente instrucción a ejecutar, y la **unidad de aritmética y lógica** (ALU), que ejecuta las operaciones.
- **Sistemas de entrada y salida**: comunican la computadora con el mundo exterior; por ejemplo, el teclado y el ratón (entrada) y la pantalla y la impresora (salida).

### Sistemas binarios

Las computadoras modernas se construyen con [circuitos integrados](https://es.wikipedia.org/wiki/Circuito_integrado), también llamados *chips* o *microchips*, como el de la figura 9.

<figure style="text-align: center;">
  <img
    src="img/circuito-integrado.jpg"
    alt="Procesador Intel"
  >
  <figcaption><strong>Figura 9</strong>. Procesador Intel. Fuente: Slejven Djurakovic, a través de <a href="https://unsplash.com/s/photos/chip">Unsplash</a>.</figcaption>
</figure>

Los circuitos integrados procesan información digital, generalmente **binaria**: de dos valores, representados internamente con dos niveles de tensión eléctrica (bajo y alto) que se denotan con 0 y 1. Cada dígito binario se denomina **bit** (*binary digit*) y los bits se agrupan de ocho en ocho en [*bytes*](https://es.wikipedia.org/wiki/Byte) para representar información más compleja, como números grandes o caracteres de texto. Por ejemplo:

- El número decimal 14 se representa en binario como `1110`, pues `1110` = 2³×1 + 2²×1 + 2¹×1 + 2⁰×0 = 8 + 4 + 2 + 0 = 14.
- La palabra "bit" se representa en [código ASCII](https://es.wikipedia.org/wiki/ASCII) como `01100010 01101001 01110100`.

De manera similar se representan otras clases de información, como imágenes, sonidos o videos.

El uso de solo dos estados tiene ventajas: los circuitos que manejan señales binarias son más simples, confiables y baratos que los que tendrían que distinguir múltiples estados, y facilita aplicar dos herramientas matemáticas fundamentales: la [teoría de la información](https://es.wikipedia.org/wiki/Teor%C3%ADa_de_la_informaci%C3%B3n) —el estudio de la cuantificación, el almacenamiento y la comunicación de la información, propuesto por [Claude Shannon](https://es.wikipedia.org/wiki/Claude_Shannon) (1916–2001) en la década de 1940, con el bit como unidad fundamental— y el [álgebra de Boole](https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole) —introducida por [George Boole](https://es.wikipedia.org/wiki/George_Boole) (1815–1864) en 1847—, que opera con dos valores, verdadero (1) y falso (0), mediante operaciones lógicas como `AND` (y), `OR` (o) y `NOT` (no).

*Ejercicios de esta sección: [ejercicios sobre sistemas binarios](#ejercicios-binarios).*

### Código máquina

El **código máquina** es el conjunto de instrucciones binarias que la CPU de una computadora puede ejecutar directamente: es el único lenguaje que las computadoras "entienden". Las instrucciones disponibles varían según la arquitectura del procesador (ej. x86, ARM), pero en general comprenden operaciones aritméticas y lógicas, movimiento de datos entre la memoria y los registros, entrada/salida, comparaciones y control de flujo. La figura 10 muestra una instrucción en código máquina que suma los contenidos de los registros 1 y 2 de una CPU y almacena el resultado en el registro 6.

<figure style="text-align: center;">
  <img
    src="img/lenguaje-maquina.png"
    alt="Instrucción en código máquina"
  >
  <figcaption><strong>Figura 10</strong>. Instrucción en código máquina. Fuente: <a href="https://en.wikipedia.org/wiki/Machine_code">Wikipedia</a>.</figcaption>
</figure>

La figura 11 muestra el programa ["Hola mundo"](https://es.wikipedia.org/wiki/Hola_mundo) en código máquina. Este programa se limita a imprimir esa hilera de texto en la pantalla y es, tradicionalmente, el primer ejemplo con el que se estudia un lenguaje de programación.

<figure style="text-align: center;">
  <img
    src="img/lenguaje-maquina-hola-mundo.png"
    alt="Programa Hola mundo en código máquina"
  >
  <figcaption><strong>Figura 11</strong>. Programa <em>Hola mundo</em> en código máquina. Fuente: CS50 (2024).</figcaption>
</figure>

## Lenguajes de programación

Programar directamente en código máquina es lento y propenso a errores. Por eso, a partir de la década de 1950 comenzaron a crearse los **lenguajes de programación**: notaciones que expresan las instrucciones con palabras —usualmente en inglés— y símbolos, y que programas especiales traducen a código máquina. Como ejemplo, el programa "Hola mundo" se muestra a continuación en tres lenguajes: [C](https://es.wikipedia.org/wiki/C_(lenguaje_de_programaci%C3%B3n)), Python y R.

```c
/* Hola mundo en lenguaje C */

#include <stdio.h>

int main(void)
{
    printf("Hola mundo\n");
}
```

```python
# Hola mundo en lenguaje Python

print("Hola mundo")
```

```r
# Hola mundo en lenguaje R

cat("Hola mundo\n")
```

Existe una gran [variedad de lenguajes de programación](https://es.wikipedia.org/wiki/Anexo:Lenguajes_de_programaci%C3%B3n), creados con fines científicos, comerciales o educativos, entre otros; el sitio [The Hello World Collection](https://helloworldcollection.github.io/) reúne el programa "Hola mundo" en más de 600 de ellos. En este curso se estudia Python, cuya sintaxis, tipos de datos y estructuras se comienzan a ver en la próxima semana.

*Ejercicios de esta sección: [ejercicios sobre programas](#ejercicios-programas).*

## Resumen

- Una **computadora** es una máquina de **propósito general**: ejecuta programas que pueden cambiarse sin alterar sus componentes físicos. Aprender a programarla permite ponerla al servicio de las preguntas de la propia disciplina.
- Un **algoritmo** es un conjunto de pasos definidos, no ambiguos, ordenados y finitos que soluciona un problema; recibe entradas, las procesa y genera salidas (modelo **entrada–procesamiento–salida**). Formular problemas de esta manera es la esencia del **pensamiento computacional**.
- Un mismo algoritmo puede implementarse como **programa** en distintos lenguajes de programación.
- La historia de las computadoras va de las calculadoras mecánicas de Pascal y Leibniz, la máquina analítica de Babbage y las notas de Ada Lovelace, al modelo teórico de Turing y a las primeras computadoras electrónicas; las actuales siguen la **arquitectura de von Neumann**: memoria principal, CPU y sistemas de entrada y salida.
- Internamente, las computadoras representan la información en **sistemas binarios** (bits y bytes) y ejecutan **código máquina**; los **lenguajes de programación**, como Python, permiten escribir instrucciones legibles que se traducen a ese código.

## Ejercicios

Los ejercicios se agrupan según la sección del capítulo a la que corresponden; se recomienda realizarlos al concluir la sección respectiva.

(ejercicios-algoritmos)=
### Algoritmos

1. Escriba, en pasos numerados como los del ejemplo, un algoritmo para obtener el valor **mínimo** de una lista. Verifique que cumpla las cuatro características básicas (entradas, salidas, pasos claros, finitud) y aplíquelo manualmente a la lista `[8.5, 3.2, -4.7, 10.9, 0.6]`, mostrando el "mínimo actual" en cada paso del recorrido.
2. Elabore una hoja electrónica que calcule la densidad de población de los cantones de una provincia de Costa Rica (busque la población y el área de al menos cinco cantones en fuentes oficiales, como el [Instituto Nacional de Estadística y Censos](https://inec.cr/)). Identifique en la hoja los componentes de entrada, procesamiento y salida del modelo.

(ejercicios-programas)=
### Programas

3. Ejecute el programa del valor máximo en ambos lenguajes: el de Python en un cuaderno de [Google Colab](https://colab.research.google.com/) y el de R en un [ambiente de ejecución en línea](https://www.mycompiler.io/new/r). Solo debe copiar el código y ejecutarlo; compare las salidas.
4. Modifique el programa de Python para que obtenga el valor mínimo, implementando el algoritmo que diseñó en el ejercicio 1, y ejecútelo en Colab.
5. Escriba en Python un programa que calcule la densidad de población de un territorio, siguiendo el algoritmo de la sección del modelo entrada–procesamiento–salida: defina las variables `poblacion` y `area` con valores reales de un cantón, calcule la densidad e imprímala con `print()`.

(ejercicios-binarios)=
### Sistemas binarios

6. Siguiendo el ejemplo del número 14, represente en binario los números 21 y 64 y muestre la comprobación con las potencias de 2. Luego, con ayuda de la [tabla del código ASCII](https://es.wikipedia.org/wiki/ASCII), escriba la representación binaria de sus iniciales.

## Referencias bibliográficas

CS50. (2024). *CS50x 2024 – Lecture 0 – Scratch* [video]. YouTube. https://www.youtube.com/watch?v=3LPJfIKxwWc
\
\
Downey, A. B. (2024). Programming as a way of thinking. En *Think Python: How to think like a computer scientist* (3.ª ed.). O'Reilly Media. https://allendowney.github.io/ThinkPython/chap01.html
\
\
Severance, C. R. (2016). Why should you learn to write programs? En *Python for everybody: Exploring data in Python 3* (S. Blumenberg y E. Hauser, eds.). CreateSpace Independent Publishing Platform. https://www.py4e.com/html3/01-intro
\
\
Wing, J. M. (2006). Computational thinking. *Communications of the ACM*, *49*(3), 33–35. [https://dl.acm.org/doi/10.1145/1118178.1118215](https://dl.acm.org/doi/10.1145%2F1118178.1118215)
