from heuristicas import uniforme
from hashtable import HashTable
from nodo import *


def aEstrella(mapa, casilla_origen, casilla_destino, camino, heuristica):

    # Creamos los nodos origen y destino
    nodo_origen = Nodo(None, casilla_origen)
    nodo_destino = Nodo(None, casilla_destino)

    # Inicializamos las listas donde guardaremos los nodos explorados y revisados.
    explorado = set()   # Nodos que se han explorado.
    revisado = set()    # Nodos explorado que se han revisado y comparado.

    # Añadimos el nodo origen.
    explorado.add(nodo_origen)

    # Hora de la generacion y exploración. Iteramos hasta hallar el nodo destino.
    while explorado:

        # De los nodos explorados, sacamos el nodo con menor f
        nodo_actual = min(explorado, key=lambda o: o.f)

        # Si hemos encontrado el destino...
        if nodo_actual == nodo_destino:
            # Guardamos f
            f = nodo_actual.f

            # Reconstruimos el camino
            while nodo_actual:
                casilla_actual = nodo_actual.casilla
                camino[casilla_actual.getFila()][casilla_actual.getCol()] = "X "

                # Si ha sido el ultimo nodo en procesar, devolvemos f, en caso contrario, continuamos.
                if not nodo_actual.padre:
                    return f
                else:
                    nodo_actual = nodo_actual.padre

        # Hemos revisado el nodo con menor F, lo sacamos de los explorados, y lo guardamos en revisados.
        explorado.remove(nodo_actual)
        revisado.add(nodo_actual)

        # Revisamos las casillas de los alrededores.
        for casilla_vecina in casillasVecinas(nodo_actual):

            # Creamos un nuevo nodo vecino de la casilla vecina, usando el nodo actual como padre
            nodo_vecino = Nodo(nodo_actual, casilla_vecina)

            # Revisamos si ya lo tenemos dentro del set de revisados ( usando el hash. O(1) - O(N)!!! VIVAN LAS HASHTABLES!!! )
            if nodo_vecino in revisado:
                continue

            # Nos aseguramos de que la casilla vecina no es una pared
            if mapa.getCelda(casilla_vecina.getFila(), casilla_vecina.getCol()) != 0:
                continue

            # Revisamos si la celda está fuera del mapa
            if not mapa.dentroMapa(casilla_vecina.getFila(), casilla_vecina.getCol()):
                continue

            # Si el nodo no ha sido explorado, los calculamos y añadimos
            if nodo_vecino not in explorado:

                nodo_vecino.g += nodo_actual.g + \
                    cMovimiento(nodo_actual, nodo_vecino)
                nodo_vecino.h = heuristica(
                    nodo_actual.casilla, nodo_vecino.casilla)
                nodo_vecino.f = nodo_vecino.g + nodo_vecino.h
                nodo_vecino.padre = nodo_actual

                explorado.add(nodo_vecino)

            # Si ya hemos explorado el nodo y el nodo actual es mejor que el nodo vecino...
            for nodo_explorado in explorado:
                if nodo_explorado == nodo_vecino and nodo_explorado.g > nodo_actual.g + cMovimiento(nodo_explorado, nodo_actual):

                    # Actualizamos el g y el padre del nodo vecino! ( Se ha encontrado un camino menor para llegar al nodo vecino. )
                    nodo_explorado.g += nodo_actual.g + \
                        cMovimiento(nodo_explorado, nodo_actual)
                    nodo_explorado.padre = nodo_actual
                break

            """ Version 1.

            # Si ya hemos explorado el nodo y el nodo actual es mejor que el nodo vecino...
            if nodo_vecino in explorado and nodo_vecino.g > nodo_actual.g + cMovimiento(nodo_actual, nodo_vecino):
                # Actualizamos el g y el padre del nodo vecino! ( Se ha encontrado un camino menor para llegar al nodo vecino. )
                nodo_vecino.g = nodo_actual.g + \
                    cMovimiento(nodo_actual, nodo_vecino)
                nodo_vecino.parent = nodo_actual
            else:
                # En caso contrario, calculamos g, h y f, le asignamos el padre (nodo previo con mejor f) y lo guardamos en explorado.
                nodo_vecino.g = nodo_actual.g + \
                    cMovimiento(nodo_actual, nodo_vecino)
                nodo_vecino.h = heuristica(
                    nodo_actual.casilla, nodo_vecino.casilla)
                nodo_vecino.f = nodo_vecino.g + nodo_vecino.h
                nodo_vecino.padre = nodo_actual

                explorado.add(nodo_vecino)
            """
    return -1


# Devolvemos una lista con las casillas vecinas de la casilla actual.
def casillasVecinas(nodo):
    casilla = nodo.casilla
    # ↑ = ( 0, 1 )
    # ↓ = ( 0, -1)
    # → = (-1, 0 )
    # ← = ( 1, 0 )
    # ↗ = ( 1, 1 )
    # ↘ = ( 1, -1)
    # ↖ = (-1, 1 )
    # ↙ = (-1, -1)
    # (0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)
    return [casilla + Casilla(0, 1), casilla + Casilla(0, -1), casilla + Casilla(1, 0), casilla + Casilla(-1, 0),
            casilla + Casilla(1, 1), casilla + Casilla(1, -1), casilla + Casilla(-1, 1), casilla + Casilla(-1, -1)]


# devolvemos el coste del movimiento
def cMovimiento(n1, n2):
    diagonales = set({Casilla(1, 1), Casilla(1, -1),
                     Casilla(-1, -1), Casilla(-1, 1)})

    if ((n1.casilla - n2.casilla) in diagonales):
        return 1.5

    return 1
