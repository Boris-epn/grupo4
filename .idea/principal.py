from collections import deque


class Nodo:
    def __init__(self, dato=None, identificador=1):
        self.dato = dato
        self.vecinos = []
        self.identificador = identificador

    def agregar_vecino(self, vecino):
        if vecino not in self.vecinos:
            self.vecinos.append(vecino)


nodos = {}

def BFS(nodoinicio, nodofin):
    camino = []
    if nodoinicio not in [nodo.dato for nodo in nodos.values()] or nodofin not in [nodo.dato for nodo in nodos.values()]:
        print('Coloque nodos válidos')
        return None
    por_inspeccionar = deque([nodoinicio])
    padres = {nodoinicio: None}
    visitados = set([nodoinicio])
    while por_inspeccionar:
        nodo_actual = por_inspeccionar.popleft()
        if nodo_actual == nodofin:
            while nodo_actual is not None:
                camino.append(nodo_actual)
                nodo_actual = padres[nodo_actual]
            return camino[::-1]
        nodo_obj = next(nodo for nodo in nodos.values() if nodo.dato == nodo_actual)
        for vecino in nodo_obj.vecinos:
            if vecino.dato not in visitados:
                visitados.add(vecino.dato)
                padres[vecino.dato] = nodo_actual
                por_inspeccionar.append(vecino.dato)
    print("No se encontró un camino entre los nodos especificados.")
    return camino
def dfs(nodo_actual, nodo_destino, visitados, camino_actual, camino_mas_profundo):
    visitados.add(nodo_actual.identificador)
    camino_actual.append(nodo_actual.identificador)
    if nodo_actual.identificador == nodo_destino.identificador:
        if len(camino_actual) > len(camino_mas_profundo[0]):
            camino_mas_profundo[0] = list(camino_actual)
    else:
        for vecino in nodo_actual.vecinos:
            if vecino.identificador not in visitados:
                dfs(vecino, nodo_destino, visitados, camino_actual, camino_mas_profundo)
    visitados.remove(nodo_actual.identificador)
    camino_actual.pop()
def camino_mas_profundo_dfs(nodo_inicio, nodo_destino):
    visitados = set()
    camino_mas_profundo = [[]]
    dfs(nodo_inicio, nodo_destino, visitados, [], camino_mas_profundo)
    return camino_mas_profundo[0]
def solicitar_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")
def definir_grafo():
    datos = set()
    identificador_actual = 1
    while True:
        print("\nMenú de opciones:")
        print("1. Ingresar un nuevo nodo, o editar un nodo existente")
        print("2. Borrar un nodo")
        print("3. Editar un nodo")
        print("4. Mostrar el diccionario de grafo")
        print("5. Utilizar BFS")
        print("6. Utilizar DFS")
        print("7. Salir")
        opcion = solicitar_entero("Seleccione una opción: ")
        if opcion == 1:
            dato = input(f'Coloque el dato que se almacenará en el nodo {identificador_actual}: ')
            if dato not in datos:
                nodo = Nodo(dato, identificador_actual)
                nodos[identificador_actual] = nodo
                datos.add(dato)
                identificador_actual += 1
                num_vecinos = solicitar_entero(
                    f'Coloque el número de vecinos que contiene el nodo {nodo.identificador}: ')
                for _ in range(num_vecinos):
                    vecino_dato = input(f'Coloque el dato almacenado en el vecino: ')
                    vecino = next((n for n in nodos.values() if n.dato == vecino_dato), None)
                    if vecino is None:
                        vecino = Nodo(vecino_dato, identificador_actual)
                        nodos[identificador_actual] = vecino
                        datos.add(vecino_dato)
                        identificador_actual += 1
                    nodo.agregar_vecino(vecino)
            else:
                print("El dato ya existe")
                opcion = input("¿Desea colocar vecinos al nodo existente? (y/n): ")
                if opcion == 'y':
                    nodo = next(n for n in nodos.values() if n.dato == dato)
                    num_vecinos = solicitar_entero(
                        f'Coloque el número de vecinos que contiene el nodo {nodo.identificador}: ')
                    for _ in range(num_vecinos):
                        vecino_dato = input(f'Coloque el dato almacenado en el vecino: ')
                        vecino = next((n for n in nodos.values() if n.dato == vecino_dato), None)
                        if vecino is None:
                            vecino = Nodo(vecino_dato, identificador_actual)
                            nodos[identificador_actual] = vecino
                            datos.add(vecino_dato)
                            identificador_actual += 1
                        nodo.agregar_vecino(vecino)
        elif opcion == 2:
            nodo_id = solicitar_entero("Ingrese el identificador del nodo que desea borrar: ")
            if nodo_id in nodos:
                for nodo in nodos.values():
                    nodo.vecinos = [v for v in nodo.vecinos if v.identificador != nodo_id]
                del nodos[nodo_id]
                print(f"Nodo {nodo_id} borrado.")
            else:
                print("El nodo no existe.")
        elif opcion == 3:
            nodo_id = solicitar_entero("Ingrese el identificador del nodo que desea editar: ")
            if nodo_id in nodos:
                nuevo_dato = input("Ingrese el nuevo dato para el nodo: ")
                if nuevo_dato not in datos:
                    datos.remove(nodos[nodo_id].dato)
                    nodos[nodo_id].dato = nuevo_dato
                    datos.add(nuevo_dato)
                    print(f"Nodo {nodo_id} actualizado con el nuevo dato '{nuevo_dato}'.")
                else:
                    print("El dato ya existe. Intente con otro.")
            else:
                print("El nodo no existe.")
        elif opcion == 4:
            grafo = construir_diccionario_grafo(nodos)
            imprimir_diccionario_grafo(grafo)
        elif opcion == 5:
            nodo_inicio = input('Coloque el contenido del nodo de inicio: ')
            nodo_fin = input('Coloque el contenido del nodo de fin: ')
            camino = BFS(nodo_inicio, nodo_fin)
            print(f"Camino BFS: {camino}")
        elif opcion == 6:
            nodo_inicio_dato = input('Coloque el nodo de inicio: ')
            nodo_fin_dato = input('Coloque el contenido del nodo de fin: ')
            nodo_inicio = next((n for n in nodos.values() if n.dato == nodo_inicio_dato), None)
            nodo_fin = next((n for n in nodos.values() if n.dato == nodo_fin_dato), None)
            if nodo_inicio and nodo_fin:
                camino = camino_mas_profundo_dfs(nodo_inicio, nodo_fin)
                print(f"Camino más profundo DFS: {camino}")
            else:
                print("Nodos de inicio o fin no encontrados.")
        elif opcion == 7:
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
def construir_diccionario_grafo(nodos):
    return {nodo.identificador: {'nombre': nodo.dato, 'vecinos': [vecino.identificador for vecino in nodo.vecinos]} for
            nodo in nodos.values()}
def imprimir_diccionario_grafo(grafo):
    print("\nDiccionario del grafo:")
    print(grafo)

# Ejecución principal
print("Bienvenido al proyecto de Estructura de Datos y Algoritmos")
definir_grafo()

