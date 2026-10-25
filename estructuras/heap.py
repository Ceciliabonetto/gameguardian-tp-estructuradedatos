class HeapMaximo:
    """Heap maximal guardado en una lista. El elemento con mayor 'clave' esta en la raiz."""

    def __init__(self, clave):
        self._datos = []
        self._clave = clave  # funcion que devuelve la prioridad de un elemento

    def vacio(self):
        return len(self._datos) == 0

    def tamanio(self):
        return len(self._datos)

    def ver_maximo(self):
        return self._datos[0] if self._datos else None  # O(1)

    def insertar(self, elemento):
        self._datos.append(elemento)
        self._subir(len(self._datos) - 1)  # O(log n)

    def extraer_maximo(self):
        if not self._datos:
            return None
        maximo = self._datos[0]
        ultimo = self._datos.pop()
        if self._datos:
            self._datos[0] = ultimo  # el ultimo pasa a ser la raiz
            self._bajar(0)           # y baja hasta su lugar
        return maximo  # O(log n)

    def construir(self, elementos):
        """Heapify: ordena una lista completa como heap."""
        self._datos = list(elementos)
        for i in range(len(self._datos) // 2 - 1, -1, -1):
            self._bajar(i)

    def _subir(self, i):
        # sift up: sube mientras sea mayor que su padre
        while i > 0:
            padre = (i - 1) // 2
            if self._clave(self._datos[i]) > self._clave(self._datos[padre]):
                self._datos[i], self._datos[padre] = self._datos[padre], self._datos[i]
                i = padre
            else:
                break

    def _bajar(self, i):
        # sift down: baja intercambiando con el hijo mayor
        n = len(self._datos)
        while True:
            izquierdo = 2 * i + 1
            derecho = 2 * i + 2
            mayor = i
            if izquierdo < n and self._clave(self._datos[izquierdo]) > self._clave(self._datos[mayor]):
                mayor = izquierdo
            if derecho < n and self._clave(self._datos[derecho]) > self._clave(self._datos[mayor]):
                mayor = derecho
            if mayor == i:
                break
            self._datos[i], self._datos[mayor] = self._datos[mayor], self._datos[i]
            i = mayor