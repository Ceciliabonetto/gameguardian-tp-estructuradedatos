# TP8 - Recorridos BFS y DFS

## Qué hacen

Los dos recorren el grafo desde un juego origen y marcan los visitados para no
dar vueltas infinitas. BFS usa una cola y explora por niveles: primero los
vecinos directos, después los vecinos de esos. DFS usa una pila y se va lo más
lejos posible por un camino antes de volver.

## Consulta con BFS

"¿Cuál es el juego relacionado más cercano a uno dado?" (opción 7). Usamos BFS
porque visita los juegos por distancia creciente al origen, así que el primero
que aparece es el más cercano.

## Consulta con DFS

"Explorar toda la red de relacionados" (opción 8). Usamos DFS porque sigue una
cadena de juegos hasta el final antes de pasar a otra.

## Filtro por edad

En las dos consultas solo se recorren juegos con una clasificación igual o
menos restrictiva que la del juego original. Así nunca se recomienda algo menos
apto para el chico, que es el objetivo de GameGuardian.

## Complejidad

Los dos son O(V + E): cada vértice se visita una vez y cada arista se mira una
vez. Con nuestro grafo son 42 vértices y 69 aristas.

## Diferencias

El código es igual salvo una línea: popleft() (cola) en BFS y pop() (pila) en
DFS. Con God of War Ragnarok, BFS muestra primero The Last of Us y DFS muestra
primero GTA V.

## Limitación

Muchos juegos no tienen conexiones, porque el grafo solo une por género o
desarrollador. Una mejora posible es agregar etiquetas de mecánicas.