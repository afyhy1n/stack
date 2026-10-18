`Prefijo` - $1+2\ast3-(4+5)\ast6/2$

Se deberán de crear dos listas en las que se guardaran números y operadores, siendo:

- `exit=[]` - usada para la creación del `postfijo`, entran principalmente números y los operadores entraran una vez que un peso sea menor a otro
- `stack=[]` - usada únicamente para la entrada de operadores

## CREACIÓN DEL POSTFIJO

1.- Se leerá la operación $1+2\ast3-(4+5)\ast6/2$ y entrara el 1 a `exit`

${\color{cyan}1}+2\ast3-(4+5)\ast6/2$

| exit | stack |
| ---- | ----- |
| 1    |       |

2.- Se leerá el + y entrara a `stack`

${\color{red}1}{\color{cyan}+}2\ast3-(4+5)\ast6/2$

| exit | stack |
| ---- | ----- |
| 1    | `+`   |

3.- Se leerá el 2 y entrara a `exit`

${\color{red}1+}{\color{cyan}2}\ast3-(4+5)\ast6/2$

| exit | stack |
| ---- | ----- |
| 1    | `+`   |
| 2    |       |

4.- Se leerá \* y entrara a `stack`

${\color{red}1+2}{\color{cyan}\ast}3-(4+5)\ast6/2$

| exit | stack |
| ---- | ----- |
| 1    | `+`   |
| 2    | `*`   |

5.- Se leerá el 3 y entrara a `exit`

${\color{red}1+2\ast}{\color{cyan}3}-(4+5)\ast6/2$

| exit | stack |
| ---- | ----- |
| 1    | `+`   |
| 2    | `*`   |
| 3    |       |

6.- Se leerá - y entrara a `stack`, pero al ser <= que los anteriores signos primero se sacaran los operadores de stack y entraran a `exit`, despues entrara -

${\color{red}1+2\ast3}{\color{cyan}-}(4+5)\ast6/2$

| exit | stack |
| ---- | ----- |
| 1    | `-`   |
| 2    |       |
| 3    |       |
| `*`  |       |
| `+`  |       |

7.- Se leerá ( y entrara a `stack`

${\color{red}1+2\ast3-}{\color{cyan}(}4+5)\ast6/2$

| exit | stack |
| ---- | ----- |
| 1    | `-`   |
| 2    | `(`   |
| 3    |       |
| `*`  |       |
| `+`  |       |

8.- Se leerá 4 y entrara a `exit`

${\color{red}1+2\ast3-(}{\color{cyan}4}+5)\ast6/2$

| exit | stack |
| ---- | ----- |
| 1    | `-`   |
| 2    | `(`   |
| 3    |       |
| `*`  |       |
| `+`  |       |
| 4    |       |

9.- Se leerá + y entrara a `stack`

${\color{red}1+2\ast3-(4}{\color{cyan}+}5)\ast6/2$

| exit | stack |
| ---- | ----- |
| 1    | `-`   |
| 2    | `(`   |
| 3    | `+`   |
| `*`  |       |
| `+`  |       |
| 4    |       |

10.- Se leerá 5 y entrara a `exit`

${\color{red}1+2\ast3-(4+}{\color{cyan}5})\ast6/2$

| exit | stack |
| ---- | ----- |
| 1    | `-`   |
| 2    | `(`   |
| 3    | `+`   |
| `*`  |       |
| `+`  |       |
| 4    |       |
| 5    |       |

11.- Se leerá ) y entrara a `stack`, pero sacara primero todos los operadores hasta llegar a (, en este caso solamente +

${\color{red}1+2\ast3-(4+5}{\color{cyan})}\ast6/2$

| exit | stack |
| ---- | ----- |
| 1    | `-`   |
| 2    |       |
| 3    |       |
| `*`  |       |
| `+`  |       |
| 4    |       |
| 5    |       |
| `+`  |       |

12.- Se leerá \* y entrara a `stack`

${\color{red}1+2\ast3-(4+5)}{\color{cyan}\ast}6/2$

| exit | stack |
| ---- | ----- |
| 1    | `-`   |
| 2    | `*`   |
| 3    |       |
| `*`  |       |
| `+`  |       |
| 4    |       |
| 5    |       |
| `+`  |       |

13.- Se leerá 6 y entrara a `exit`

${\color{red}1+2\ast3-(4+5)\ast}{\color{cyan}6}/2$

| exit | stack |
| ---- | ----- |
| 1    | `-`   |
| 2    | `*`   |
| 3    |       |
| `*`  |       |
| `+`  |       |
| 4    |       |
| 5    |       |
| `+`  |       |
| 6    |       |

14.- Se leerá / y entrara a `stack`, pero sacara de `stack` todos los operadores que sean <= a el, en este caso solo sacara a \*

${\color{red}1+2\ast3-(4+5)\ast6}{\color{cyan}/}2$

| exit | stack |
| ---- | ----- |
| 1    | `-`   |
| 2    | `/`   |
| 3    |       |
| `*`  |       |
| `+`  |       |
| 4    |       |
| 5    |       |
| `+`  |       |
| 6    |       |
| `*`  |       |

15.- Se leerá 2 y entrara a `exit`

${\color{red}1+2\ast3-(4+5)\ast6/}{\color{cyan}2}$

| exit | stack |
| ---- | ----- |
| 1    | `-`   |
| 2    | `/`   |
| 3    |       |
| `*`  |       |
| `+`  |       |
| 4    |       |
| 5    |       |
| `+`  |       |
| 6    |       |
| `*`  |       |
| 2    |       |

16.- Al ya no haber nada más en el `Prefijo` se sacaran todos los elementos de la lista `stack` y se añadiran a `exit`

${\color{red}1+2\ast3-(4+5)\ast6/2}$

| exit | stack |
| ---- | ----- |
| 1    |       |
| 2    |       |
| 3    |       |
| `*`  |       |
| `+`  |       |
| 4    |       |
| 5    |       |
| `+`  |       |
| 6    |       |
| `*`  |       |
| 2    |       |
| `/`  |       |
| `-`  |       |

17.- La lista final de `exit` quedara como:

`exit=[ 1, 2, 3, *, +, 4, 5, +, 6, *, 2, /, - ]`

Este mismo sera el `Postfijo`: **`1 2 3 * + 4 5 + 6 * 2 / -`**

## TRADUCCIÓN DEL POSTFIJO

Cuando tenemos el `Postfijo`, ahora ya podemos resolver la ecuación matemática:

**`1 2 3 * + 4 5 + 6 * 2 / -`**

1.- Desde el operador `*` multiplicaremos los elementos ${\color{lime}a}$ y ${\color{cyan}b}$:

$$1\ {\color{lime}2}\ {\color{cyan}3}\ {\color{red}\ast}\ +\ 4\ 5\ +\ 6\ \ast\ 2\ /\ -$$

Dando como resultado:

$$1\ {\color{red}6}\ +\ 4\ 5\ +\ 6\ \ast\ 2\ /\ -$$

___

2.- Desde el operador `+` sumaremos los elementos ${\color{lime}1}$ y ${\color{cyan}6}$:

$${\color{lime}1}\ {\color{cyan}6}\ {\color{red}+}\ 4\ 5\ +\ 6\ \ast\ 2\ /\ -$$

Dando como resultado:

$${\color{red}7}\ 4\ 5\ +\ 6\ \ast\ 2\ /\ -$$

___

3.- Desde el operador `+` sumaremos los elementos ${\color{lime}4}$ y ${\color{cyan}5}$:

$$7\ {\color{lime}4}\ {\color{cyan}5}\ {\color{red}+}\ 6\ \ast\ 2\ /\ -$$

Dando como resultado:

$$7\ {\color{red}9}\ 6\ \ast\ 2\ /\ -$$

___

4.- Desde el operador `*` multiplicaremos los elementos ${\color{lime}9}$ y ${\color{cyan}6}$:

$$7\ {\color{lime}9}\ {\color{cyan}6}\ {\color{red}\ast}\ 2\ /\ -$$

Dando como resultado:

$$7\ {\color{red}54}\ 2\ /\ -$$

___

5.- Desde el operador `/` multiplicaremos los elementos ${\color{lime}54}$ y ${\color{cyan}2}$:

$$7\ {\color{lime}54}\ {\color{cyan}2}\ {\color{red}/}\ -$$

Dando como resultado:

$$7\ {\color{red}27}\ -$$

___

6.- Desde el operador `-` multiplicaremos los elementos ${\color{lime}7}$ y ${\color{cyan}27}$:

$${\color{lime}7}\ {\color{cyan}27}\ {\color{red}-}$$

Dando como resultado:

$${\color{red}-20}$$

Siendo este **-20** el resultado final.