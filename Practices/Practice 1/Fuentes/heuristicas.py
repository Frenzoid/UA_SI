def uniforme(actual, destino):
    return 0


def manhattan(actual, destino):
    return abs(actual.getFila() - destino.getFila()) + abs(actual.getCol() - destino.getCol())
    

def euclidea(actual, destino):

    dx = abs(actual.getFila() - destino.getFila())
    dy = abs(actual.getCol() - destino.getCol())

    return (dx * dx + dy * dy) ^ (1/2)

def euclidea2(actual, destino):
    dx = abs(actual.getFila() - destino.getFila())
    dy = abs(actual.getCol() - destino.getCol())

    return dx * dx + dy * dy