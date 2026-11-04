class Grafo:
    """Grafo no dirigido, sin pesos, con lista de adyacencia."""

    def __init__(self):
        self._adyacentes = {}  # vertice -> lista de vecinos

    def agregar_vertice(self, vertice):
        self._adyacentes.setdefault(vertice, [])

    def agregar_arista(self, a, b):
        self._adyacentes[a].append(b)
        self._adyacentes[b].append(a)

    def adyacentes(self, vertice):
        return self._adyacentes[vertice]

    def vertices(self):
        return list(self._adyacentes)

    def cantidad_aristas(self):
        return sum(len(v) for v in self._adyacentes.values()) // 2