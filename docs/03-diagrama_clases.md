# Diagrama de clases - GameGuardian

```mermaid
classDiagram
    class Videojuego {
        -titulo
        -genero
        -desarrollador
        -clasificacion_esrb
        -rating
        +get_titulo()
        +get_genero()
        +get_desarrollador()
        +get_clasificacion_esrb()
        +get_rating()
        +desde_dict(datos)
    }
    class ArbolBST {
        +insertar(videojuego)
        +buscar(titulo)
        +inorder()
        +preorder()
        +postorder()
        +altura()
    }
    class ArbolAVL {
        +insertar(videojuego)
        +buscar(titulo)
        +inorder()
        +altura()
    }
    class ArbolGeneral {
        +insertar_juego(videojuego)
        +buscar_categoria(nombre)
        +juegos_de(nodo)
        +mostrar_categorias()
    }
    class HeapMaximo {
        +insertar(elemento)
        +extraer_maximo()
        +ver_maximo()
        +construir(elementos)
    }
    class Grafo {
        +agregar_vertice(vertice)
        +agregar_arista(a, b)
        +adyacentes(vertice)
        +vertices()
        +cantidad_aristas()
    }
        class RegistroVotos {
        +votar(nickname, juego, opinion)
        +ya_voto(nickname, juego)
        +resumen(juego)
    }
    RegistroVotos --> Videojuego : votos por juego

    ArbolBST --> Videojuego : almacena
    ArbolAVL --> Videojuego : almacena
    ArbolGeneral --> Videojuego : hojas
    HeapMaximo --> Videojuego : ordena por rating
    Grafo --> Videojuego : vertices
```

**Implementado:** `Videojuego`, `ArbolBST` (TP3), `ArbolAVL` (TP4), `ArbolGeneral` (TP5), `HeapMaximo` (TP6), `Grafo` (TP7), `RegistroVotos` (votación de la comunidad).
**Funciones de recorrido (TP8):** `bfs()` y `dfs()` en `algoritmos/`, que recorren el `Grafo`. La recomendación de juegos relacionados se resuelve con ellas, por eso no hay una clase `Recomendador`.
**Sin clases `Usuario` y `Voto`:** el usuario es su nickname y el voto es una de tres opiniones, así que alcanza con `RegistroVotos`.


El menú (`ui/terminal.py`) usa `ArbolAVL` (buscar y listar), `ArbolGeneral`
(categorías), `HeapMaximo` (Top 10), `Grafo` (juegos conectados) y, sobre el
grafo, `bfs()` y `dfs()` (relacionados, con filtro por edad). `ArbolBST`
se conserva como punto de comparación en el experimento de TP4.