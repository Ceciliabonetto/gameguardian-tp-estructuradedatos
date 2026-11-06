# TP5 - Jerarquía de categorías

## Qué jerarquía armamos

Armamos una jerarquía de 4 niveles:

- Nivel 0: la raíz, que es todo el catálogo ("Videojuegos").
- Nivel 1: la clasificación ESRB (E, E10+, T, M).
- Nivel 2: el género del juego (Sandbox, Shooter, etc.).
- Nivel 3: el videojuego (Minecraft, Fortnite, etc.).

Los niveles 0, 1 y 2 son categorías que solo sirven para agrupar. Los
videojuegos son las hojas del árbol.

## Por qué la armamos así

El usuario de GameGuardian es un padre que primero necesita saber qué juegos
son aptos para la edad de su hijo y después busca un tipo de juego. Por eso
la clasificación va primero y el género después.

Usamos un árbol general porque cada categoría tiene una cantidad distinta de
hijos, y un árbol binario no lo permite.

## Cómo funciona en el menú

La opción 4 muestra primero solo las categorías. El usuario escribe una (por
ejemplo T) y el programa muestra los juegos de esa categoría.

## Recorridos

- mostrar_categorias(): recorre el árbol en preorden (primero el nodo y
  después sus hijos) y muestra solo las categorías.
- juegos_de(nodo): recorre en profundidad y junta los videojuegos de una
  categoría.

## Complejidad

Buscar una categoría es O(n) en el peor caso, porque hay que recorrer los
nodos. Para buscar por título se sigue usando el AVL, que es O(log n).

## Limitación

Algunos géneros se repiten en distintas franjas (por ejemplo Sandbox está
en E10+ y en T). La búsqueda devuelve la primera que encuentra. Con E, E10+,
T y M no hay problema porque esos nombres no se repiten.