import matplotlib.pyplot as plt
import numpy as np

# El conjunto de entrenamiento para una clase ( tipo de imágen ) debe ser: 50% imágenes de la clase, y 50% imágenes que no son de la clase.
def generar_conjunto_entrenamiento(N, clase, x_train, y_train):

    # N: Total de imágenes del conjunto de entrenamiento, debe ser para para partir 50% / 50%
    if(N % 2 != 0):
        raise Exception("N no es Par")

    # Mitad de la clase, Mitad no clase.
    N = int(N/2)

    # Creamos una máscara para todo el conjunto de entrenamiento
    mask = y_train == clase

    # Partimos en 2 el dataset, los elementos que son de la clase, y los que no lo son.
    arr_clase = x_train[mask]
    arr_noClase = x_train[~mask]

    # Concatenamos dichos arrays, y creamos un array de 1 y -1 por cada array.
    X = np.concatenate((arr_clase[0:N], arr_noClase[0:N]))
    X = normalizar_conjunto(X, 28 * 28)

    Y = np.concatenate((np.ones(N), np.ones(N) * -1))

    return (X, Y)

def normalizar_conjunto(X, dim_imagen):
    return X.reshape(len(X), dim_imagen)


def plot_arrays(X, Y, title, xlabel, ylabel):
    plt.title(title)
    plt.plot(X, Y, "bo")
    plt.xlabel(ylabel)
    plt.ylabel(xlabel)
    plt.show()

def mostrar_imagen(imagen):
    plt.figure()
    plt.imshow(imagen)
    plt.show()