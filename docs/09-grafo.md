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

Lista de adyacencia: cada videojuego guarda la lista de los juegos con los que
está conectado.

El grafo tiene 42 vértices y 69 aristas. Según la definición vista en clase
(más aristas que vértices) ya es denso, pero la mayoría de los pares posibles
no están conectados: hay 861 pares y solo 69 aristas (8%). Con una matriz de
adyacencia tendríamos 42 x 42 = 1.764 casilleros y solo 138 ocupados. Con la
lista guardamos únicamente las conexiones que existen.

## Limitación

6 de los 42 juegos no tienen ninguna conexión (Resident Evil 4, Hollow Knight,
It Takes Two, Among Us, Portal 2 y Hades), porque son los únicos de su género y
de su desarrollador. Una mejora posible es agregar etiquetas de mecánicas y
conectar los juegos que compartan alguna.