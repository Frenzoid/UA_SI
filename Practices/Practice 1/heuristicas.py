def uniforme():
    return 0


def manhattan(casilla1, casilla2):
    return abs(casilla1.getFila() - casilla2.getFila()) + abs(casilla1.getCol() - casilla2.getCol())
