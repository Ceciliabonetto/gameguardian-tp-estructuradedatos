class Videojuego:
    def __init__(self, titulo, genero, desarrollador, clasificacion_esrb):
        self._titulo = titulo
        self._genero = genero
        self._desarrollador = desarrollador
        self._clasificacion_esrb = clasificacion_esrb

    def get_titulo(self):
        return self._titulo

    def get_genero(self):
        return self._genero

    def get_clasificacion_esrb(self):
        return self._clasificacion_esrb

    @classmethod
    def desde_dict(cls, datos):
        return cls(datos["titulo"], datos["genero"], datos["desarrollador"], datos["clasificacion_esrb"])

    def __str__(self):
        return f"{self._titulo} - ESRB {self._clasificacion_esrb} - {self._genero}"