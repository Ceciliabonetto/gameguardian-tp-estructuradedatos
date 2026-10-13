# Conexión entre estructuras - GameGuardian

```mermaid
flowchart TD
    A[datos/videojuegos.json] --> B[Lista de objetos Videojuego]
    B --> C[ArbolAVL por título - implementado]
    B --> D[Heap por valoración - pendiente TP6]
    B --> E[Grafo de similitud - pendiente TP7]
    E --> F[BFS / DFS / camino mínimo - pendiente TP8-TP9]
    C --> G[Interfaz de terminal]
    D --> G
    F --> G
```

**Estado actual:** el JSON se carga como lista de `Videojuego`, y esa lista se
inserta en el AVL, que atiende las opciones de buscar y listar. El filtro por
clasificación recorre la lista directamente.
Este documento se completa a medida que se suman el heap y el grafo.