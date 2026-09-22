import random
import time
from modelos.videojuego import Videojuego
from algoritmos.busqueda import buscar_secuencial, buscar_binaria

GENEROS = ["Accion", "RPG", "Shooter", "Simulacion", "Aventura", "Deportes"]
CLASIFICACIONES = ["E", "E10+", "T", "M"]

def generar_catalogo_falso(cantidad):
    """Genera 'cantidad' videojuegos con titulos unicos, para pruebas de rendimiento."""
    catalogo = []
    for i in range(cantidad):
        titulo = f"Juego{i:05d}"
        genero = random.choice(GENEROS)
        desarrollador = f"Estudio{random.randint(1, 50)}"
        clasificacion = random.choice(CLASIFICACIONES)
        catalogo.append(Videojuego(titulo, genero, desarrollador, clasificacion))
    return catalogo


def medir_tiempo(funcion_busqueda, catalogo, titulo_buscado):
    inicio = time.perf_counter()
    funcion_busqueda(catalogo, titulo_buscado)
    fin = time.perf_counter()
    return (fin - inicio) * 1000


def ejecutar_experimento():
    tamanios = [100, 1000, 10000]
    print(f"{'N elementos':<15}{'Secuencial (ms)':<20}{'Binaria (ms)':<15}")
    print("-" * 50)

    for n in tamanios:
        catalogo = generar_catalogo_falso(n)
        catalogo_ordenado = sorted(catalogo, key=lambda j: j.get_titulo().lower())

        titulo_buscado = f"Juego{n-1:05d}"

        tiempo_secuencial = medir_tiempo(buscar_secuencial, catalogo, titulo_buscado)
        tiempo_binaria = medir_tiempo(buscar_binaria, catalogo_ordenado, titulo_buscado)

        print(f"{n:<15}{tiempo_secuencial:<20.4f}{tiempo_binaria:<15.4f}")


if __name__ == "__main__":
    ejecutar_experimento()