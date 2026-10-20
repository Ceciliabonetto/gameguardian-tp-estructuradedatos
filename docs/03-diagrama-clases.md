# Diagrama de clases - GameGuardian

```mermaid
classDiagram
    class Videojuego {
        -titulo
        -genero
        -desarrollador
        -clasificacion_esrb
        +get_titulo()
        +get_genero()
        +get_clasificacion_esrb()
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
    ArbolBST --> Videojuego : almacena
    ArbolAVL --> Videojuego : almacena
```

**Implementado:** `Videojuego`, `ArbolBST` (TP3), `ArbolAVL` (TP4).
**Pendiente:** `Usuario`, `Voto`, `Heap` (TP6), `Grafo` (TP7) y `Recomendador`.

El menú (`ui/terminal.py`) usa `ArbolAVL`. `ArbolBST` se conserva como punto de
comparación en el experimento de TP4.