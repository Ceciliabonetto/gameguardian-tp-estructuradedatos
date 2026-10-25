import json
from modelos.videojuego import Videojuego
from estructuras.avl import ArbolAVL #Tp 4
from estructuras.arbol_general import ArbolGeneral #Tp5
from algoritmos.ranking import top_n #Tp6
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

def construir_jerarquia(catalogo): #Tp5 (funcion nueva)
    jerarquia = ArbolGeneral("Videojuegos")
    for juego in catalogo:
        jerarquia.insertar_juego(juego)
    return jerarquia

def filtrar_por_edad(catalogo, clasificacion):
    return [j for j in catalogo if j.get_clasificacion_esrb() == clasificacion]

def iniciar():
    catalogo = cargar_videojuegos()
    arbol = construir_arbol(catalogo)
    jerarquia = construir_jerarquia(catalogo) #Tp5

    while True:
        print("\n=== GAMEGUARDIAN ===")
        print("1. Buscar videojuego (Arbol AVL)") #Tp4
        print("2. Listar todos los videojuegos (Inorder)")
        print("3. Filtrar por clasificacion ESRB")
        print("4. Explorar categorias (Arbol general)") #Tp5
        print("5. Top 10 por clasificacion (Heap)") #Tp6
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
        elif opcion == "4": #Tp5 
            jerarquia.mostrar_categorias() #cambiad de jerarquias.mostrar
            nombre = input("\nIngrese una categoria para ver sus juegos (ej: E10+, Simulacion): ")
            nodo = jerarquia.buscar_categoria(nombre)
            if nodo is None:
                print("No se encontro esa categoria")
            else:
                for juego in jerarquia.juegos_de(nodo):
                    print(juego)
        elif opcion == "5": #Tp6 
            clasificacion = input("Ingrese clasificacion (E, E10+, T, M): ")
            juegos = filtrar_por_edad(catalogo, clasificacion)
            for puesto, juego in enumerate(top_n(juegos, 10), start=1):
                print(f"{puesto}. {juego}")
        elif opcion == "0":
            break