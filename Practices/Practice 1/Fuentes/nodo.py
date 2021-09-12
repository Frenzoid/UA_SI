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
    def __eq__(self, otro):
        return self.casilla == otro.casilla

    # Para poder identificarlo por la casilla, y evitar tener 2 instancias del mismo nodo con las mismas coordenadas.
    def __hash__(self):
        return self.casilla.__hash__()
