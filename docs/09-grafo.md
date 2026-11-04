# TP7 - Grafo de similitud entre videojuegos

## Vértices

Cada vértice es un videojuego (un objeto Videojuego). El grafo tiene 18
vértices, uno por cada juego del catálogo.

## Aristas

Dos videojuegos están conectados si comparten género o desarrollador. Por
ejemplo, Minecraft y Terraria están conectados porque los dos son Sandbox, y
Mario Kart 8 y Animal Crossing porque los dos son de Nintendo.

Elegimos estos dos criterios porque son los que un padre usaría para decir
"este juego se parece a aquel", y porque salen directo de los datos del JSON.

## Tipo de grafo

No dirigido y sin pesos.

- No dirigido: si A se parece a B, entonces B se parece a A. La relación
  es simétrica, así que una arista alcanza para los dos sentidos.
- Sin pesos: por ahora una conexión existe o no existe, no importa "cuánto"
  se parecen. Si en TP9 necesitamos un costo, se puede agregar un peso (por
  ejemplo, la cantidad de atributos que comparten).

## Representación

Lista de adyacencia: cada videojuego guarda la lista de los juegos con los
que está conectado.

Un grafo es denso cuando tiene más aristas que vértices. El nuestro tiene 18
vértices y solo 7 aristas, así que no es denso. Con una matriz de adyacencia
tendríamos 18 x 18 = 324 casilleros y casi todos serían ceros. Con la lista
solo guardamos las 7 conexiones que existen.

## Limitación

8 de los 18 juegos no tienen ninguna conexión (por ejemplo Fortnite o Celeste),
porque son los únicos de su género y desarrollador. Una mejora posible es
agregar etiquetas de mecánicas (crafteo, mundo abierto, cooperativo) y conectar
los juegos que compartan alguna.