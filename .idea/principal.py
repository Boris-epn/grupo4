class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.vecinos = []
    def agregar_vecino(self, vecino):
        if vecino not in self.vecinos:
            self.vecinos.append(vecino)
print("Bienvenido al proyecto de Estructura de datos y algoritmos")
num_nodos = int(input('Coloque la cantidad de nodos que contiene el grafo: '))

def definir_grafo(num_nodos):
    nodos = []
    for i in range(num_nodos):
        dato = input(f'Coloque el dato que se almacenará en el nodo {i + 1}: ')
        nodo = Nodo(dato)
        num_vecinos = int(input(f'Coloque el número de vecinos que contiene el nodo {i + 1}: '))
        for j in range(num_vecinos):
            vecino_dato = input(f'Coloque el dato almacenado en el vecino {j + 1}: ')
            nodo.agregar_vecino(vecino_dato)
        nodos.append(nodo)
    return nodos
def imprimir_grafo(nodos):
    for nodo in nodos:
        print(f'Nodo {nodo.dato}:')
        for vecino in nodo.vecinos:
            print(f'  Vecino: {vecino}')
nodos = definir_grafo(num_nodos)
imprimir_grafo(nodos)

        
