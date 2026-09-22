def buscar_secuencial(catalogo, titulo):
    """Recorre todo el catalogo elemento por elemento. Complejidad: O(n)"""
    titulo = titulo.lower()
    for juego in catalogo:
        if juego.get_titulo().lower() == titulo:
            return juego
    return None


def buscar_binaria(catalogo_ordenado, titulo):
    """Requiere el catalogo ya ordenado por titulo. Complejidad: O(log n)"""
    titulo = titulo.lower()
    izq, der = 0, len(catalogo_ordenado) - 1

    while izq <= der:
        medio = (izq + der) // 2
        titulo_medio = catalogo_ordenado[medio].get_titulo().lower()

        if titulo_medio == titulo:
            return catalogo_ordenado[medio]
        elif titulo_medio < titulo:
            izq = medio + 1
        else:
            der = medio - 1

    return None