import json
from modelos.videojuego import Videojuego
from estructuras.avl import ArbolAVL #Tp 4
from estructuras.arbol_general import ArbolGeneral #Tp5
from algoritmos.ranking import top_n #Tp6
from estructuras.grafo import Grafo #Tp7
from algoritmos.bfs import bfs #Tp8
from algoritmos.dfs import dfs #Tp8
from servicios.votos import RegistroVotos, OPINIONES #Votacion
#from estructuras.arbol import ArbolBST # TP3: reemplazado por el AVL en TP4

NIVEL_EDAD = {"E": 0, "E10+": 1, "T": 2, "M": 3, "AO": 4} #Tp8

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

def construir_grafo(catalogo): #Tp7 (funcion nueva)
    grafo = Grafo()
    for juego in catalogo:
        grafo.agregar_vertice(juego)
    for i in range(len(catalogo)):
        for j in range(i + 1, len(catalogo)):
            a, b = catalogo[i], catalogo[j]
            if a.get_genero() == b.get_genero() or a.get_desarrollador() == b.get_desarrollador():
                grafo.agregar_arista(a, b)
    return grafo

def filtrar_por_edad(catalogo, clasificacion):
    return [j for j in catalogo if j.get_clasificacion_esrb() == clasificacion]

def relacionados(grafo, arbol, titulo, recorrido): #Tp8 (funcion nueva)
    origen = arbol.buscar(titulo)
    if origen is None:
        print("No se encontro ese juego")
        return
    # solo se recomiendan juegos igual o menos restrictivos que el original
    tope = NIVEL_EDAD[origen.get_clasificacion_esrb()]
    apto = lambda j: NIVEL_EDAD[j.get_clasificacion_esrb()] <= tope
    resultado = recorrido(grafo, origen, apto)
    if not resultado:
        print("No hay juegos relacionados aptos para esa edad")
    for juego in resultado:
        print(juego)

def mostrar_votos(registro, juego): #Votacion (funcion nueva)
    print(f"{juego.get_titulo()} - ESRB oficial: {juego.get_clasificacion_esrb()}")
    total, cuenta = registro.resumen(juego)
    if total == 0:
        print("Clasificacion de la comunidad: todavia no hay votos")
    else:
        porcentaje = cuenta["acertada"] * 100 // total
        print(f"Clasificacion de la comunidad: {porcentaje}% de acuerdo ({total} votos)")
        print(f"  Acertada: {cuenta['acertada']} - Deberia ser mas alta: {cuenta['mas alta']} - Deberia ser mas baja: {cuenta['mas baja']}")

def iniciar():
    catalogo = cargar_videojuegos()
    arbol = construir_arbol(catalogo)
    jerarquia = construir_jerarquia(catalogo) #Tp5
    grafo = construir_grafo(catalogo) #Tp7
    registro = RegistroVotos() #Votacion

    while True:
        print("\n=== GAMEGUARDIAN ===")
        print("1. Buscar videojuego (Arbol AVL)") #Tp4
        print("2. Listar todos los videojuegos (Inorder)")
        print("3. Filtrar por clasificacion ESRB")
        print("4. Explorar categorias (Arbol general)") #Tp5
        print("5. Top 10 por clasificacion (Heap)") #Tp6
        print("6. Ver juegos conectados a uno (Grafo)") #Tp7
        print("7. Relacionados, mas cercanos primero (BFS)") #Tp8
        print("8. Explorar toda la red de relacionados (DFS)") #Tp8
        print("9. Votar la clasificacion de un juego") #Votacion
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
        elif opcion == "4": #Tp5 (bloque nuevo)
            jerarquia.mostrar_categorias() #cambiad de jerarquias.mostrar
            nombre = input("\nIngrese una categoria para ver sus juegos (ej: E10+, Simulacion): ")
            nodo = jerarquia.buscar_categoria(nombre)
            if nodo is None:
                print("No se encontro esa categoria")
            else:
                for juego in jerarquia.juegos_de(nodo):
                    print(juego)
        elif opcion == "5": #Tp6 (bloque nuevo)
            clasificacion = input("Ingrese clasificacion (E, E10+, T, M): ")
            juegos = filtrar_por_edad(catalogo, clasificacion)
            for puesto, juego in enumerate(top_n(juegos, 10), start=1):
                print(f"{puesto}. {juego}")
        elif opcion == "6": #Tp7 (bloque nuevo)
            titulo = input("Ingrese el titulo: ")
            juego = arbol.buscar(titulo)
            if juego is None:
                print("No se encontro ese juego")
            else:
                vecinos = grafo.adyacentes(juego)
                print(f"{len(vecinos)} juegos conectados:")
                for vecino in vecinos:
                    print(vecino)
        elif opcion == "7": #Tp8 (bloque nuevo)
            relacionados(grafo, arbol, input("Titulo del juego: "), bfs)
        elif opcion == "8": #Tp8 (bloque nuevo)
            relacionados(grafo, arbol, input("Titulo del juego: "), dfs)
        elif opcion == "9": #Votacion (bloque nuevo)
            nickname = input("Ingrese su nombre de usuario: ").strip()
            if not nickname:
                print("Tiene que ingresar un nombre de usuario")
                continue
            juego = arbol.buscar(input("Ingrese el titulo: "))
            if juego is None:
                print("No se encontro ese juego")
                continue
            mostrar_votos(registro, juego)
            if registro.ya_voto(nickname, juego):
                print("Ya votaste por este juego anteriormente.")
                continue
            print("Te parece acertada la clasificacion?")
            print("1) Si  2) Deberia ser mas alta  3) Deberia ser mas baja")
            eleccion = input("Opcion: ")
            if eleccion in OPINIONES:
                registro.votar(nickname, juego, OPINIONES[eleccion])
                print("Gracias, tu voto fue registrado.")
            else:
                print("Opcion invalida, no se registro el voto.")
        elif opcion == "0":
            break