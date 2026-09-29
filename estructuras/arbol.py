class NodoArbol:
    def __init__(self, videojuego):
        self.videojuego = videojuego
        self.izquierda = None
        self.derecha = None


class ArbolBST:
    """Arbol binario de busqueda, ordenado por titulo del videojuego."""

    def __init__(self):
        self.raiz = None

    def insertar(self, videojuego):
        self.raiz = self._insertar_recursivo(self.raiz, videojuego)

    def _insertar_recursivo(self, nodo, videojuego):
        if nodo is None:
            return NodoArbol(videojuego)

        titulo_nuevo = videojuego.get_titulo().lower()
        titulo_actual = nodo.videojuego.get_titulo().lower()

        if titulo_nuevo < titulo_actual:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, videojuego)
        else:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, videojuego)

        return nodo

    def buscar(self, titulo):
        return self._buscar_recursivo(self.raiz, titulo.lower())

    def _buscar_recursivo(self, nodo, titulo):
        if nodo is None:
            return None

        titulo_actual = nodo.videojuego.get_titulo().lower()

        if titulo == titulo_actual:
            return nodo.videojuego
        elif titulo < titulo_actual:
            return self._buscar_recursivo(nodo.izquierda, titulo)
        else:
            return self._buscar_recursivo(nodo.derecha, titulo)

    def inorder(self):
        resultado = []
        self._inorder_recursivo(self.raiz, resultado)
        return resultado

    def _inorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._inorder_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo.videojuego)
            self._inorder_recursivo(nodo.derecha, resultado)

    def preorder(self):
        resultado = []
        self._preorder_recursivo(self.raiz, resultado)
        return resultado

    def _preorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.videojuego)
            self._preorder_recursivo(nodo.izquierda, resultado)
            self._preorder_recursivo(nodo.derecha, resultado)

    def postorder(self):
        resultado = []
        self._postorder_recursivo(self.raiz, resultado)
        return resultado

    def _postorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._postorder_recursivo(nodo.izquierda, resultado)
            self._postorder_recursivo(nodo.derecha, resultado)
            resultado.append(nodo.videojuego)