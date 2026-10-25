from estructuras.heap import HeapMaximo

def top_n(videojuegos, n=10):
    """Devuelve los n videojuegos con mejor rating, de mayor a menor."""
    heap = HeapMaximo(lambda juego: juego.get_rating())
    heap.construir(videojuegos)
    resultado = []
    while len(resultado) < n and not heap.vacio():
        resultado.append(heap.extraer_maximo())
    return resultado