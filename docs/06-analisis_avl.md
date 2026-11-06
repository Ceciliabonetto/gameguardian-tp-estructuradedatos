# TP4 - Balance del árbol: BST vs AVL

# Problema

En un BST común, el orden de inserción determina la forma del árbol. Si los
datos llegan ya ordenados, cada nodo nuevo va siempre al mismo lado y el
árbol degenera en una lista enlazada: altura = N.

# Resultados del experimento

Inserción de títulos ya ordenados alfabéticamente.

| N | Altura BST | Altura AVL | Búsqueda BST (ms) | Búsqueda AVL (ms) |
|---|---|---|---|---|
| 100 | 100 | 7 | 0.0203 | 0.0015 |
| 500 | 500 | 9 | 0.1792 | 0.0019 |
| 1000 | 1000 | 10 | 0.2970 | 0.0018 |

> **Nota:** los tiempos de búsqueda varían entre ejecuciones según la carga
> del equipo en ese momento, por eso se informan los de una sola corrida.
> Lo relevante es la tendencia: la altura y el tiempo del BST crecen con N,
> mientras que el AVL se mantiene casi constante. Las alturas no varían
> entre corridas.

## Por qué importa el balance

La búsqueda recorre, como máximo, tantos nodos como la altura del árbol. En
el BST degenerado la altura es N, así que buscar cuesta O(n). En el AVL la
altura se mantiene en O(log n) porque, después de cada inserción, si la
diferencia de alturas entre los subárboles supera 1, se rotan nodos para
recuperar el equilibrio. Por eso la búsqueda en el AVL es O(log n) sin
importar el orden de los datos.

## Decisión de diseño

GameGuardian usa AVL porque el catálogo podría cargarse ya ordenado (por
ejemplo, desde un archivo alfabético) y no queremos depender del orden de
entrada.