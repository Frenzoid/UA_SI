from nodo import *


def aEstrella(mapa, casilla_origen, casilla_destino, camino):

    # Creamos los nodos origen y destino
    nodo_origen = Nodo(None, casilla_origen)
    nodo_destino = Nodo(None, casilla_destino)

    # Inicializamos las listas donde guardaremos los nodos explorados y revisados.
    explorado = []
    revisado = []

    # Añadimos el nodo origen.
    explorado.append(nodo_origen)

    # Hora de la generacion y exploración. Iteramos hasta hallar el nodo destino.
    while len(explorado) > 0:

        # Obtenemos el nodo actual
        nodo_actual = explorado[0]
        indice_actual = 0

        # Verificamos si el nodo actual es más costoso que alguno de la lista, si lo es, lo reemplazamos.
        #  Creo que asi filtramos bifurcaciones con diferentes costes.
        for i, nodo in enumerate(explorado):
            if nodo.f < nodo_actual.f:
                nodo_actual = nodo
                indice_actual = i

        # Sacamos el nodo actual, y lo guardamos en la lista de revisados.
        explorado.pop(indice_actual)
        revisado.append(nodo_actual)

        # Si encontramos el destino...
        if nodo_actual == nodo_destino:
            nodo_actual_aux = nodo_actual

            # Guardamos en la lista "camino" el nodo actual y sus padres hasta el origen.
            while nodo_actual_aux is not None:
                print("2")
                # Le damos un valor diferente al camino para que se dibuje.
                casilla_actual = nodo_actual_aux.casilla
                camino[casilla_actual.getFila()][casilla_actual.getCol()] = "X "

                # Guardamos el nodo padre para iterar sobre el padre.
                nodo_actual_aux = nodo_actual_aux.padre

            # Damos la vuelta a la lista, y devolvemos el coste.
            camino[::-1]
            return nodo_actual.f

        # Creamos hijos
        hijos = []

        # Revisamos las casillas de los alrededores.
        for casilla_vecina in nodo_actual.casilla.casillasVecinas():
            print("3")

            # Nos aseguramos de que la casilla vecina no es una pared
            if mapa.getCelda(casilla_vecina.getFila(), casilla_vecina.getCol()) != 0:
                print("4")
                continue

            # Evitamos que una casilla vecina escanee a otra casilla vecina y provoque un bucle.
            for n in hijos:
                if n.casilla == casilla_vecina:
                    continue

            # TODO revisar si la casilla está dentro del mapa, si no, continue.

            # Creamos un nuevo nodo de la casilla vecina, usando el nodo actual como padre
            nuevo_nodo = Nodo(nodo_actual, casilla_vecina)

            # Añadimos el nodo a los hijos.
            hijos.append(nuevo_nodo)

        # Iteramos sobre los hijos, exploramos.
        for nodo_hijo in hijos:
            print("5")
            # Si el hijo ya ha sido revisado, pasamos de su cara.
            if nodo_hijo.revisado:
                continue

            # Calculamos f, g y h
            nodo_hijo.h = 0

            nodo_hijo.g = nodo_actual.g + 1
            nodo_hijo.f = nodo_hijo.g + nodo_hijo.h

            # (Caso en el cual un nodo ya ha explorado el nodo vecino) Si el hijo ya esta en la lista de explorados, pasamos de su cara.
            for nodo_explorado in explorado:
                if nodo_hijo.g > nodo_explorado.g and nodo_hijo.explorado:
                    continue

            # Añadimos el nodo hijo a la lista de explorados
            nodo_hijo.explorado = True
            explorado.append(nodo_hijo)

    return -1

#            print(len(explorado))
#            if len(explorado) > 0:
#                print(str(explorado[-1].casilla))
