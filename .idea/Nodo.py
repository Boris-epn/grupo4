class Nodo:
    def __init_(self, dato=None):
        self.dato = dato
        self.vecinos=[]

    def agreggar_vecino(self,vecino):
        if vecino not in self.vecinos:
            self.vecinos.append(vecino )

