# Elvi Mihai Sabau Sabau

class Casilla():
    """Slot class, used to store coordinates as tuples on the map"""
    def __init__(self, f, c):
        self.fila = f
        self.col = c

    def getFila(self):
        return self.fila

    def getCol(self):
        return self.col

    # Sobrecarga del operador igualdad
    def __eq__(self, otro):
        if type(otro) is Casilla:
            return self.fila == otro.getFila() and self.col == otro.getCol()
        elif type(otro) is tuple:
            return self.fila == otro[0] and self.col == otro[1]
        else:
            raise ValueError(
                'Error on the Casilla == overload. Data type invalid:' + type(otro).__name__)

    # Sobrecarga del operador + para hacernos la vida mas facil
    def __add__(self, otro):
        if type(otro) is Casilla:
            c = Casilla(self.fila + otro.getFila(),
                        self.col + otro.getCol())
        else:
            raise ValueError(
                'Error on the Casilla + overload. Data type invalid:' + type(otro).__name__)
        return c

    # Sobrecarga del operador - para hacernos la vida mas facil
    def __sub__(self, otro):
        if type(otro) is Casilla:
            c = Casilla(self.fila - otro.getFila(),
                        self.col - otro.getCol())
        else:
            raise ValueError(
                'Error on the Casilla - overload. Data type invalid:' + type(otro).__name__)
        return c

    # Sobrecarga del operador str(Casilla)
    def __str__(self):
        return '(' + str(self.fila) + ', ' + str(self.col) + ')'

    # Un hash unico basado en sus coordenadas.
    def __hash__(self):
        return hash(self.getTupla())

    # Devuelve tupla
    def getTupla(self):
        """Returns a tuple version of the Slot class (Casilla)"""
        return (self.fila, self.col)
