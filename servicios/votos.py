import json
import os

OPINIONES = {"1": "acertada", "2": "mas alta", "3": "mas baja"}

class RegistroVotos:
    """Guarda un voto por usuario y por juego. Los votos se guardan en un JSON."""

    def __init__(self, ruta="datos/votos.json"):
        self._ruta = ruta
        self._votos = {}  # titulo -> {nickname: opinion}
        self._cargar()

    def _cargar(self):
        if os.path.exists(self._ruta):
            with open(self._ruta, "r", encoding="utf-8") as archivo:
                self._votos = json.load(archivo)

    def _guardar(self):
        with open(self._ruta, "w", encoding="utf-8") as archivo:
            json.dump(self._votos, archivo, ensure_ascii=False, indent=2)

    def ya_voto(self, nickname, juego):
        return nickname.lower() in self._votos.get(juego.get_titulo(), {})

    def votar(self, nickname, juego, opinion):
        """Registra el voto. Devuelve False si ese usuario ya voto ese juego."""
        if self.ya_voto(nickname, juego):
            return False
        self._votos.setdefault(juego.get_titulo(), {})[nickname.lower()] = opinion
        self._guardar()
        return True

    def resumen(self, juego):
        """Devuelve (total de votos, cantidad por cada opinion)."""
        votos = self._votos.get(juego.get_titulo(), {})
        cuenta = {opinion: 0 for opinion in OPINIONES.values()}
        for opinion in votos.values():
            cuenta[opinion] += 1
        return len(votos), cuenta