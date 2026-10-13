import sys
import time
from modelos.videojuego import Videojuego
from estructuras.arbol import ArbolBST
from estructuras.avl import ArbolAVL

# TP 4
sys.setrecursionlimit(20000)

def generar_ordenado(n):
    """Titulos ya ordenados alfabeticamente: el peor caso para un BST."""
    return [Videojuego(f"Juego{i:05d}", "Accion", "Estudio", "E") for i in range(n)]

def medir_busqueda(arbol, titulo, repeticiones=100):
    inicio = time.perf_counter()
    for _ in range(repeticiones):
        arbol.buscar(titulo)
    fin = time.perf_counter()
    return (fin - inicio) / repeticiones * 1000  # ms por busqueda

def ejecutar():
    print(f"{'N':<8}{'Altura BST':<14}{'Altura AVL':<14}{'Busq BST (ms)':<16}{'Busq AVL (ms)':<14}")
    print("-" * 66)

    for n in [100, 500, 1000, 5000]:
        juegos = generar_ordenado(n)
        bst, avl = ArbolBST(), ArbolAVL()
        for j in juegos:
            bst.insertar(j)
            avl.insertar(j)

        ultimo = f"Juego{n-1:05d}"
        print(f"{n:<8}{bst.altura():<14}{avl.altura():<14}"
              f"{medir_busqueda(bst, ultimo):<16.5f}{medir_busqueda(avl, ultimo):<14.5f}")

if __name__ == "__main__":
    ejecutar()