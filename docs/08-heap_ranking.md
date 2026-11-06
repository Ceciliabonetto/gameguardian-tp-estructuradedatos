# TP6 - Ranking con heap

## Función de prioridad

La prioridad de cada videojuego es su rating (de 0 a 10). Elegimos solo el
rating porque es el dato que el usuario entiende para decidir qué juego
elegir. Más adelante se podría combinar con los votos de la comunidad.

## Estructura elegida

Heap maximal guardado en una lista. El juego con mejor rating siempre está
en la raíz. Lo implementamos a mano (sin heapq), con sift up al insertar y
sift down al extraer el máximo.

## Cómo se obtiene el Top 10

1. Se filtran los juegos de la clasificación elegida.
2. Se construye el heap con esos juegos (heapify).
3. Se extrae la raíz 10 veces (o hasta que se acaben los juegos).

## Complejidad

- Ver el máximo: O(1).
- Insertar: O(log n).
- Extraer el máximo: O(log n).
- Construir el heap con heapify: O(n).
- Top N completo: O(n + N log n).

## Por qué un heap y no ordenar todo cada vez

Ordenar todo el catálogo cuesta O(n log n) en cada consulta, aunque solo
necesitemos 10 juegos. Con el heap construimos la estructura en O(n) y
después solo pagamos por los N juegos que extraemos (N log n).

Además, un heap permite insertar un elemento nuevo en O(log n) sin reordenar
todo. En la versión actual el heap se arma en cada consulta, así que esa
ventaja todavía no se aprovecha. Una mejora posible es construirlo una vez al
iniciar y mantenerlo actualizado cuando lleguen votos o juegos nuevos.

## Limitación

Con un catálogo chico (18 juegos) la diferencia no se nota. Además, un heap
no permite actualizar eficientemente el rating de un juego que ya está
adentro, porque solo se accede a la raíz.