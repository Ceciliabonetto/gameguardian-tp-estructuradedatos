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
    ArbolBST --> Videojuego : almacena
    ArbolAVL --> Videojuego : almacena
    ArbolGeneral --> Videojuego : hojas
    HeapMaximo --> Videojuego : ordena por rating
```

**Implementado:** `Videojuego`, `ArbolBST` (TP3), `ArbolAVL` (TP4), `ArbolGeneral` (TP5), `HeapMaximo` (TP6).
**Pendiente:** `Usuario`, `Voto`, `Grafo` (TP7) y `Recomendador`.

El menú (`ui/terminal.py`) usa `ArbolAVL` (buscar y listar), `ArbolGeneral`
(categorías) y `HeapMaximo` (Top 10). `ArbolBST` se conserva como punto de
comparación en el experimento de TP4.