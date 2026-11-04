from collections import deque

def bfs(grafo, origen, permitido=lambda v: True):
    """Devuelve los vertices alcanzables desde origen, del mas cercano al mas lejano."""
    visitados = {origen}
    cola = deque([origen])
    orden = []
    while cola:
        actual = cola.popleft()  # saca el PRIMERO que entro
        if actual is not origen:
            orden.append(actual)
        for vecino in grafo.adyacentes(actual):
            if vecino not in visitados and permitido(vecino):
                visitados.add(vecino)
                cola.append(vecino)
    return orden