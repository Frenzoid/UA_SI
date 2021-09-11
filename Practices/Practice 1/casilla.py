class Casilla():
    def __init__(self, f, c):
        self.fila = f
        self.col = c

    def getFila(self):
        return self.fila

    def getCol(self):
        return self.col

    # Sobrecarga del operador igualdad
    def __eq__(self, otraCasilla):
        return self.fila == otraCasilla.getFila() and self.col == otraCasilla.getCol()

    # Sobrecarga del operador + para hacernos la vida mas facil
    def __add__(self, otro):
        if type(otro) is Casilla:
            c = Casilla(self.fila + otro.getFila(),
                        self.col + otro.getFila())
        elif type(otro) is tuple:
            c = Casilla(self.fila + otro[0],
                        self.col + otro[1])
        else:
            raise ValueError(
                'Error en la sobrecarga del operador + en Casilla: Tipo de dato invalido: ' + type(otro).__name__)
        return c

    # Sobrecarga del operador str(Casilla)
    def __str__(self):
        return '(' + str(self.fila) + ', ' + str(self.col) + ')'

    # Devolvemos una lista con las casillas vecinas x8

    def casillasVecinas(self):
        # (0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)
        return [self + (0, -1), self + (0, 1), self + (-1, 0), self + (1, 0), self + (-1, -1), self + (-1, 1), self + (1, -1), self + (1, 1)]

    # Devuelve tupla
    def getTupla(self):
        return (self.fila, self.col)
