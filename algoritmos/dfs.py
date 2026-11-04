def dfs(grafo, origen, permitido=lambda v: True):
    """Recorre en profundidad desde origen, usando una pila."""
    visitados = {origen}
    pila = [origen]
    orden = []
    while pila:
        actual = pila.pop()  # saca el ULTIMO que entro
        if actual is not origen:
            orden.append(actual)
        for vecino in grafo.adyacentes(actual):
            if vecino not in visitados and permitido(vecino):
                visitados.add(vecino)
                pila.append(vecino)
    return orden