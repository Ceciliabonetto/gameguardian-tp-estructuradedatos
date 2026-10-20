class NodoGeneral:
    def __init__(self, nombre, videojuego=None):
        self.nombre = nombre
        self.videojuego = videojuego  # solo las hojas (juegos) lo tienen
        self.hijos = []

    def obtener_hijo(self, nombre):
        for hijo in self.hijos:
            if hijo.nombre == nombre:
                return hijo
        return None


class ArbolGeneral:
    """Jerarquia: Raiz -> clasificacion ESRB -> genero -> videojuego."""

    def __init__(self, nombre_raiz):
        self.raiz = NodoGeneral(nombre_raiz)

    def insertar_juego(self, videojuego):
        nodo_edad = self._obtener_o_crear(self.raiz, videojuego.get_clasificacion_esrb())
        nodo_genero = self._obtener_o_crear(nodo_edad, videojuego.get_genero())
        nodo_genero.hijos.append(NodoGeneral(videojuego.get_titulo(), videojuego))

    def _obtener_o_crear(self, padre, nombre):
        hijo = padre.obtener_hijo(nombre)
        if hijo is None:
            hijo = NodoGeneral(nombre)
            padre.hijos.append(hijo)
        return hijo

    def buscar_categoria(self, nombre):
        return self._buscar(self.raiz, nombre.lower())

    def _buscar(self, nodo, nombre):
        # solo categorias: los juegos tienen videojuego, las categorias no
        if nodo.videojuego is None and nodo.nombre.lower() == nombre:
            return nodo
        for hijo in nodo.hijos:
            encontrado = self._buscar(hijo, nombre)
            if encontrado is not None:
                return encontrado
        return None

    def juegos_de(self, nodo):
        """Todos los videojuegos que cuelgan de un nodo (recorrido en profundidad)."""
        if nodo.videojuego is not None:
            return [nodo.videojuego]
        resultado = []
        for hijo in nodo.hijos:
            resultado.extend(self.juegos_de(hijo))
        return resultado

        def mostrar(self):
                self._mostrar(self.raiz, 0)

    def _mostrar(self, nodo, nivel):
        # recorrido en preorden: primero el nodo, despues sus hijos
        print("  " * nivel + "- " + nodo.nombre)
        for hijo in nodo.hijos:
            self._mostrar(hijo, nivel + 1)

    def mostrar_categorias(self):
        """Muestra solo las categorias, sin los videojuegos (las hojas)."""
        self._mostrar_categorias(self.raiz, 0)

    def _mostrar_categorias(self, nodo, nivel):
        if nodo.videojuego is not None:
            return  # es un juego (hoja): no se muestra
        print("  " * nivel + "- " + nodo.nombre)
        for hijo in nodo.hijos:
            self._mostrar_categorias(hijo, nivel + 1)