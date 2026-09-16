import json
from modelos.videojuego import Videojuego

def cargar_videojuegos():
    with open("datos/videojuegos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    return [Videojuego.desde_dict(d) for d in datos]

def buscar(catalogo, titulo):
    for juego in catalogo:
        if juego.get_titulo().lower() == titulo.lower():
            return juego
    return None

def listar(catalogo):
    for juego in catalogo:
        print(juego)

def filtrar_por_edad(catalogo, clasificacion):
    return [j for j in catalogo if j.get_clasificacion_esrb() == clasificacion]

def iniciar():
    catalogo = cargar_videojuegos()
    while True:
        print("\n=== GAMEGUARDIAN ===")
        print("1. Buscar videojuego")
        print("2. Listar todos")
        print("3. Filtrar por clasificacion ESRB")
        print("0. Salir")
        opcion = input("Elija una opcion: ")

        if opcion == "1":
            titulo = input("Ingrese el titulo: ")
            resultado = buscar(catalogo, titulo)
            print(resultado if resultado else "No se encontro ese juego")
        elif opcion == "2":
            listar(catalogo)
        elif opcion == "3":
            clasificacion = input("Ingrese clasificacion (E, E10+, T, M): ")
            for j in filtrar_por_edad(catalogo, clasificacion):
                print(j)
        elif opcion == "0":
            break