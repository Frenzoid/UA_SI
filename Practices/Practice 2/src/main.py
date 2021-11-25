# Importamos las librerias que necesitaremos
from keras.datasets import mnist
import numpy as np

import utils
from adaboost import adaboost
from funciones_clasificadoras import aplicar_clasificador_fuerte

# Desde la libería de Keras podemos descargar la base datos MNIST.
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Guardamos la base de datos a un fichero
np.savez("mnist",x=x_train,y=y_train)

# Cargamos la base de datos
npzfile = np.load("mnist.npz")
x_train = npzfile['x']
y_train = npzfile['y']



# --- ENTRENAMOS PARA EL NUMERO 0 ---
# Cantidad de imágenes. Si pondemos demasiadas imagenes (+10000), puede que se de el caso en el cual, no hayan tantas imagenes de cierta clase.
N = 10000

# Clase ( tipo imágen en este caso de numero ) sobre el cual entrenar.
clase = 0

# X = Array de N imágenes por 748 slots (imágen aplanada)
# Y = Array de tags relacionados con cada imágen.
# Recibe, N: Numero de imágenes, clase: La clase sobre la cual entrenar, x_train, y_train.
(X, Y) = utils.generar_conjunto_entrenamiento(N, clase, x_train, y_train)

# Cantidad e clasificadores debiles que compondran un clasificador fuerte.
T = 100

# Cantidad de clasificadores debiles a probar para extraer el mejor de ellos.
A = 100

H = adaboost(X, Y, T, A)

# -- PROBAMOS EL CLASIFICADOR FUERTE --
# N = Cantidad de numeros a clasificar.
N = 60000

# Normalizamos las imágenes.
X = utils.normalizar_conjunto(x_train[0:N], 28 * 28)


# Comparamos entre el resultado del clasificador fuerte, y los tags de Y.
ceros_detectados = np.int16(aplicar_clasificador_fuerte(H, X))
ceros_detectados_sumados = np.sum(np.int64(ceros_detectados[:] == 1))

ceros_reales = y_train[0:N]
ceros_reales_sumados = np.sum(np.int64(ceros_reales == clase))


print("Numeros detectados: " + str(ceros_detectados_sumados) + ", Numeros reales: " + str(ceros_reales_sumados))
print(str((ceros_detectados_sumados / ceros_reales_sumados) * 100) + " % de certeza.")

""" print("----------------------") 
print(list(zip(ceros_detectados, ceros_reales)))"""