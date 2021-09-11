from heuristicas import uniforme
from hashtable import HashTable
from nodo import *


def aEstrella(mapa, casilla_origen, casilla_destino, camino, heuristica, limite_iter):

    # Creamos los nodos origen y destino
    nodo_origen = Nodo(None, casilla_origen)
    nodo_destino = Nodo(None, casilla_destino)

    # Inicializamos las listas donde guardaremos los nodos explorados y revisados.
    explorado = set()   # Nodos que se han explorado.
    revisado = set()    # Nodos explorado que se han revisado y comparado.

    # Añadimos el nodo origen.
    explorado.add(nodo_origen)

    # Contador de nodos descubiertos.
    cant_descubierto = 0

    # Hora de la generacion y exploración. Iteramos hasta hallar el nodo destino.
    while explorado:
        print(len(revisado))

        # De los nodos explorados, sacamos el nodo con menor f
        nodo_actual = min(explorado, key=lambda o: o.f)

        # Si hemos encontrado el destino...
        if nodo_actual == nodo_destino:
            nodo_actual_aux = nodo_actual

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
        for casilla_vecina in casillasVecinas(nodo_actual.casilla):

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

            # Si ya hemos explorado el nodo y el nodo actual es mejor que el nodo vecino...
            if nodo_vecino in explorado and nodo_vecino.g > nodo_actual.g + 1:
                # Actualizamos el g y el padre del nodo vecino! ( Se ha encontrado un camino menor para llegar al nodo vecino. )
                nodo_vecino.g = nodo_actual.g + 1
                nodo_vecino.parent = nodo_actual
            else:
                # En caso contrario, calculamos g, h y f, le asignamos el padre (nodo previo con mejor f) y lo guardamos en explorado.
                nodo_vecino.g = nodo_actual.g + 1
                nodo_vecino.h = heuristica(
                    nodo_actual.casilla, nodo_vecino.casilla)
                nodo_vecino.f = nodo_vecino.g + nodo_vecino.h
                nodo_vecino.padre = nodo_actual

                explorado.add(nodo_vecino)
    return -1


# Devolvemos una lista con las casillas vecinas de la casilla actual.
def casillasVecinas(casilla):
    # ↑ = ( 0, 1 )
    # ↗ = ( 1, 1 )
    # → = (-1, 0 )
    # ↘ = ( 1, -1)
    # ↓ = ( 0, -1)
    # ↙ = (-1, -1)
    # ← = ( 1, 0 )
    # ↖ = (-1, 1 )
    # (0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)
    return [casilla + (0, 1), casilla + (0, -1), casilla + (1, 0), casilla + (-1, 0), casilla + (1, 1), casilla + (1, -1), casilla + (-1, 1), casilla + (-1, -1)]
