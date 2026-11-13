import unittest

from estructuras.avl import ArbolAVL


class JuegoFalso:
    """Juego minimo para probar el arbol: solo necesita get_titulo()."""

    def __init__(self, titulo):
        self._titulo = titulo

    def get_titulo(self):
        return self._titulo


def armar_arbol(titulos):
    arbol = ArbolAVL()
    for titulo in titulos:
        arbol.insertar(JuegoFalso(titulo))
    return arbol


class TestArbolAVL(unittest.TestCase):

    def test_buscar_encuentra_un_juego_existente(self):
        arbol = armar_arbol(["Minecraft", "Fortnite", "Celeste"])
        juego = arbol.buscar("Fortnite")
        self.assertIsNotNone(juego)
        self.assertEqual(juego.get_titulo(), "Fortnite")

    def test_buscar_ignora_mayusculas(self):
        arbol = armar_arbol(["Minecraft", "Fortnite"])
        self.assertIsNotNone(arbol.buscar("minecraft"))

    def test_buscar_devuelve_none_si_no_existe(self):
        arbol = armar_arbol(["Minecraft", "Fortnite"])
        self.assertIsNone(arbol.buscar("Tetris"))

    def test_inorder_devuelve_los_titulos_ordenados(self):
        arbol = armar_arbol(["Zelda", "Celeste", "Minecraft", "Among Us", "Hades"])
        titulos = [j.get_titulo() for j in arbol.inorder()]
        self.assertEqual(titulos, ["Among Us", "Celeste", "Hades", "Minecraft", "Zelda"])

    def test_rotacion_derecha_derecha(self):
        # A, B, C ordenados: sin balanceo seria una escalera de altura 3.
        arbol = armar_arbol(["A", "B", "C"])
        self.assertEqual(arbol.raiz.videojuego.get_titulo(), "B")
        self.assertEqual(arbol.altura(), 2)

    def test_datos_ordenados_mantienen_altura_logaritmica(self):
        # 1000 titulos ya ordenados: un BST comun tendria altura 1000.
        titulos = [f"juego{i:04d}" for i in range(1000)]
        arbol = armar_arbol(titulos)
        self.assertLessEqual(arbol.altura(), 11)


if __name__ == "__main__":
    unittest.main()