import json
from modelos.videojuego import Videojuego
from estructuras.avl import ArbolAVL #Tp 4
#from estructuras.arbol import ArbolBST

def cargar_videojuegos():
    with open("datos/videojuegos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    return [Videojuego.desde_dict(d) for d in datos]

def construir_arbol(catalogo):
    arbol = ArbolAVL() #Tp 4
    for juego in catalogo:
        arbol.insertar(juego)
    return arbol

def filtrar_por_edad(catalogo, clasificacion):
    return [j for j in catalogo if j.get_clasificacion_esrb() == clasificacion]

def iniciar():
    catalogo = cargar_videojuegos()
    arbol = construir_arbol(catalogo)

    while True:
        print("\n=== GAMEGUARDIAN ===")
        print("1. Buscar videojuego (Arbol AVL)") #Tp4
        print("2. Listar todos los videojuegos (Inorder)")
        print("3. Filtrar por clasificacion ESRB")
        print("0. Salir")
        opcion = input("Elija una opcion: ")

        if opcion == "1":
            titulo = input("Ingrese el titulo: ")
            resultado = arbol.buscar(titulo)
            print(resultado if resultado else "No se encontro ese juego")
        elif opcion == "2":
            for juego in arbol.inorder():
                print(juego)
        elif opcion == "3":
            clasificacion = input("Ingrese clasificacion (E, E10+, T, M): ")
            for j in filtrar_por_edad(catalogo, clasificacion):
                print(j)
        elif opcion == "0":
            break