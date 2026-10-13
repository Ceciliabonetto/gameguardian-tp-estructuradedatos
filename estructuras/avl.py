#TP 4:
class NodoAVL:
    def __init__(self, videojuego):
        self.videojuego = videojuego
        self.izquierda = None
        self.derecha = None
        self.altura = 1


class ArbolAVL:
    """Arbol binario de busqueda auto-balanceado, ordenado por titulo."""

    def __init__(self):
        self.raiz = None

    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def _balance(self, nodo):
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha)

    def _actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))

    def _rotar_derecha(self, y):
        x = y.izquierda
        t2 = x.derecha
        x.derecha = y
        y.izquierda = t2
        self._actualizar_altura(y)
        self._actualizar_altura(x)
        return x

    def _rotar_izquierda(self, x):
        y = x.derecha
        t2 = y.izquierda
        y.izquierda = x
        x.derecha = t2
        self._actualizar_altura(x)
        self._actualizar_altura(y)
        return y

    def insertar(self, videojuego):
        self.raiz = self._insertar(self.raiz, videojuego)

    def _insertar(self, nodo, videojuego):
        if nodo is None:
            return NodoAVL(videojuego)

        titulo = videojuego.get_titulo().lower()

        if titulo < nodo.videojuego.get_titulo().lower():
            nodo.izquierda = self._insertar(nodo.izquierda, videojuego)
        else:
            nodo.derecha = self._insertar(nodo.derecha, videojuego)

        self._actualizar_altura(nodo)
        balance = self._balance(nodo)

        # Caso izquierda-izquierda
        if balance > 1 and titulo < nodo.izquierda.videojuego.get_titulo().lower():
            return self._rotar_derecha(nodo)

        # Caso derecha-derecha
        if balance < -1 and titulo >= nodo.derecha.videojuego.get_titulo().lower():
            return self._rotar_izquierda(nodo)

        # Caso izquierda-derecha
        if balance > 1 and titulo >= nodo.izquierda.videojuego.get_titulo().lower():
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)

        # Caso derecha-izquierda
        if balance < -1 and titulo < nodo.derecha.videojuego.get_titulo().lower():
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo

    def buscar(self, titulo):
        nodo = self.raiz
        titulo = titulo.lower()
        while nodo is not None:
            actual = nodo.videojuego.get_titulo().lower()
            if titulo == actual:
                return nodo.videojuego
            nodo = nodo.izquierda if titulo < actual else nodo.derecha
        return None

    def inorder(self):
        resultado = []
        self._inorder(self.raiz, resultado)
        return resultado

    def _inorder(self, nodo, resultado):
        if nodo is not None:
            self._inorder(nodo.izquierda, resultado)
            resultado.append(nodo.videojuego)
            self._inorder(nodo.derecha, resultado)

    def altura(self):
        return self._altura(self.raiz)