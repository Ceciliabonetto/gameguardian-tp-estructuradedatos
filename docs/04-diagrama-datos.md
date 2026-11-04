# Conexión entre estructuras - GameGuardian

```mermaid
flowchart TD
    A[datos/videojuegos.json] --> B[Lista de objetos Videojuego]
    B --> C[ArbolAVL por título - implementado]
    B --> H[ArbolGeneral por categorías - implementado]
    B --> D[HeapMaximo por rating - implementado]
    B --> E[Grafo de similitud - implementado]
    E --> F[BFS / DFS / camino mínimo - pendiente TP8-TP9]
    C --> G[Interfaz de terminal]
    H --> G
    D --> G
    E --> G
    F --> G
```

**Estado actual:** el JSON se carga como lista de `Videojuego`, y esa lista
alimenta cuatro estructuras:

- **ArbolAVL**, ordenado por título: atiende las opciones de buscar y listar.
- **ArbolGeneral**, con la jerarquía clasificación → género → videojuego:
  atiende "Explorar categorías".
- **HeapMaximo**, ordenado por rating: atiende el Top 10 por clasificación.
  Se arma en cada consulta con los juegos de la clasificación elegida.
- **Grafo** de similitud (no dirigido, sin pesos, lista de adyacencia): atiende
  "Ver juegos conectados a uno". Va a alimentar BFS, DFS y el camino mínimo.

El filtro por clasificación recorre la lista directamente.
Este documento se completa a medida que se suman las etapas siguientes.