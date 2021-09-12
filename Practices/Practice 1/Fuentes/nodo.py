from casilla import *
from mapa import *


class Nodo():
    def __init__(self, padre=None, casilla=None):
        self.padre = padre
        self.casilla = casilla

        # Distancia desde el inicio
        self.g = 0

        # Distancia hasta el final
        self.h = 0

        # Distancia total ( suma de amabs )
        self.f = 0

    # Sobrecarga operador ==.
    def __eq__(self, otroNodo):
        return self.casilla == otroNodo.casilla

    # Para poder guardarlo en un set, debe tener un hash.
    def __hash__(self):
        return self.casilla.__hash__()