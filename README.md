# GameGuardian

Sistema de recomendación de videojuegos por clasificación de edad (ESRB), hecho
en Python y con interfaz de terminal. Proyecto integrador de Estructuras de
Datos (UNaB), grupo 6.

## Problema que resuelve

Un padre quiere comprarle un videojuego a su hijo de 10 años y no tiene una forma
simple de saber qué juegos son aptos para esa edad ni de encontrar otros
parecidos. GameGuardian organiza un catálogo por clasificación de edad y permite
buscar, explorar, rankear, relacionar y votar juegos.

## Integrantes

- Cecilia Bonetto (@Ceciliabonetto)
- Leonel Rodriguez (@LeoDevSQL)

## Cómo ejecutarlo

Requisitos: Python 3.10 o superior. No hay librerías externas.

```
git clone https://github.com/Ceciliabonetto/gameguardian-tp-estructuradedatos.git
cd gameguardian-tp-estructuradedatos
python main.py
```

Ejecutarlo siempre desde la raíz del proyecto. Para correr los experimentos:

```
python -m algoritmos.experimento
python -m algoritmos.experimento_avl
```

## Menú

| Opción | Qué hace | Estructura |
|---|---|---|
| 1 | Buscar un videojuego por título | Árbol AVL |
| 2 | Listar todos, ordenados alfabéticamente | Árbol AVL (inorder) |
| 3 | Filtrar por clasificación ESRB | Lista |
| 4 | Explorar categorías (clasificación → género) | Árbol general |
| 5 | Top 10 por clasificación, según rating | Heap |
| 6 | Ver juegos conectados a uno | Grafo |
| 7 | Relacionados, del más cercano al más lejano | BFS |
| 8 | Explorar toda la red de relacionados | DFS |
| 9 | Votar la clasificación de un juego | Registro de votos |

En las opciones 7 y 8 nunca se muestran juegos con clasificación más
restrictiva que la del juego original.

## Estructura del repositorio

```
modelos/       clase Videojuego
estructuras/   arbol.py (BST), avl.py, arbol_general.py, heap.py, grafo.py
algoritmos/    busqueda.py, bfs.py, dfs.py, ranking.py y experimentos
servicios/     votos.py (votación de la comunidad)
ui/            terminal.py (menú)
datos/         videojuegos.json (catálogo de prueba)
docs/          documentación del proyecto
main.py        punto de entrada
```

## Documentación

- [Requerimientos](docs/01-requerimientos.md)
- [Casos de uso](docs/02-casos_de_uso.md)
- [Diagrama de clases](docs/03-diagrama_clases.md)
- [Conexión entre estructuras](docs/04-diagrama_datos.md)
- [Gestión de proyecto](docs/05-gestion_proyecto.md) (tablero Trello)
- [Análisis AVL](docs/06-analisis_avl.md)
- [Jerarquía de categorías](docs/07-jerarquia_categorias.md)
- [Ranking con heap](docs/08-heap_ranking.md)
- [Grafo de similitud](docs/09-grafo.md)
- [Recorridos BFS y DFS](docs/10-recorridos.md)

## Estado del proyecto

Implementado: TP0 a TP8 y la votación de la comunidad. El camino mínimo (TP9) no
se implementó.

Limitaciones conocidas: el catálogo es de 42 juegos y los ratings son valores de
ejemplo; el grafo une juegos solo por género o desarrollador, por lo que algunos
quedan sin conexiones; los votos se identifican por nickname, sin autenticación.