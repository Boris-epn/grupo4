class Nodo:
    def __init__(self, dato=None, identificador=1):
        self.dato = dato
        self.vecinos = []
        self.identificador = identificador

    def agregar_vecino(self, vecino):
        if vecino not in self.vecinos:
            self.vecinos.append(vecino)

def solicitar_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")

def definir_grafo():
    nodos = {}
    datos = set()  # Para evitar nombres duplicados
    identificador_actual = 1  # Contador de IDs para asignar secuencialmente
    while True:
        print("\nMenú de opciones:")
        print("1. Ingresar un nuevo nodo")
        print("2. Borrar un nodo")
        print("3. Editar un nodo")
        print("4. Mostrar el diccionario de grafo")

        print("5. Salir")
        opcion = solicitar_entero("Seleccione una opción: ")

        if opcion == 1:  # Ingresar nuevo nodo
            dato = input(f'Coloque el dato que se almacenará en el nodo {identificador_actual}: ')
            if dato not in datos:
                nodo = Nodo(dato, identificador_actual)
                nodos[identificador_actual] = nodo
                datos.add(dato)
                identificador_actual += 1

                num_vecinos = solicitar_entero(f'Coloque el número de vecinos que contiene el nodo {nodo.identificador}: ')
                for _ in range(num_vecinos):
                    vecino_dato = input(f'Coloque el dato almacenado en el vecino: ')
                    vecino = next((n for n in nodos.values() if n.dato == vecino_dato), None)
                    if vecino is None:
                        vecino = Nodo(vecino_dato, identificador_actual)
                        nodos[identificador_actual] = vecino
                        identificador_actual += 1
                    nodo.agregar_vecino(vecino)
            else:
                print("El dato ya existe. Intente con otro.")

        elif opcion == 2:  # Borrar nodo
            nodo_id = solicitar_entero("Ingrese el identificador del nodo que desea borrar: ")
            if nodo_id in nodos:
                # Remover el nodo y su referencia en los vecinos
                for nodo in nodos.values():
                    nodo.vecinos = [v for v in nodo.vecinos if v.identificador != nodo_id]
                del nodos[nodo_id]
                print(f"Nodo {nodo_id} borrado.")
            else:
                print("El nodo no existe.")

        elif opcion == 3:  # Editar nodo
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

        elif opcion == 4:  # Mostrar diccionario
            grafo = construir_diccionario_grafo(nodos)
            imprimir_diccionario_grafo(grafo)

        elif opcion == 5:  # Salir
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

def construir_diccionario_grafo(nodos):
    grafo = {}
    for identificador, nodo in nodos.items():
        grafo[identificador] = {
            'nombre': nodo.dato,
            'vecinos': [vecino.identificador for vecino in nodo.vecinos]
        }
    return grafo

def imprimir_diccionario_grafo(grafo):
    print("\nDiccionario del grafo:")
    print(grafo)

# Ejecución principal
print("Bienvenido al proyecto de Estructura de Datos y Algoritmos")
definir_grafo()
