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
print("Bienvenido al proyecto de Estructura de datos y algoritmos")
num_nodos = solicitar_entero('Coloque la cantidad de nodos que contiene el grafo: ')
def definir_grafo(num_nodos):
    nodos = []
    datos = []
    i = 0
    while i < num_nodos:
        dato = input(f'Coloque el dato que se almacenará en el nodo {i + 1}: ')
        if dato not in datos:
            nodo = Nodo(dato,i+1)
            num_vecinos = solicitar_entero(f'Coloque el número de vecinos que contiene el nodo {i + 1}: ')
            for j in range(num_vecinos):
                vecino_dato = input(f'Coloque el dato almacenado en el vecino {j + 1}: ')
                nodo.agregar_vecino(vecino_dato)
            nodos.append(nodo)
            i += 1
        else:
            print('Por favor, coloque un nodo no repetido.')
        datos.append(dato)
    return nodos
def imprimir_grafo(nodos):
    for nodo in nodos:
        print(f'Nodo {nodo.dato}:',f'{nodo.identificador}')
        for vecino in nodo.vecinos:
            print(f'  Vecino: {vecino}')



        
