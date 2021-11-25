import numpy as np

import funciones_clasificadoras as cd
import utils

def adaboost(X, Y, T, A):

  # Vector de error, se actualiza por cada clasificador debil, inicialmente uniforme
  D = np.ones(len(X), dtype=np.double) / len(X)

  # Datos para la gráfica.
  pixel = []
  error = []
  
  # Array donde guardaremos tuplas de [mejor_clasificador, confianza] = [ht, alpha]
  H = []

  for t in range(T):
    
    # Menor suma de errores del clasificador debil y su array de errores.
    menor_sumerr = np.inf
    menor_errv = []

    # Mejor clasificador debil ( de A pruebas aleatorias, el que menor error tiene )
    mejor_ht = None

    # Probamos A clasificadores debiles, y nos quedamos con el mejor de todos.
    for k in range(A):

      ht = cd.generar_clasificador_debil(28 * 28)
      resultados_entrenamiento = cd.aplicar_clasificador_debil(ht, X)
      [sumerr, errv] = cd.obtener_error(resultados_entrenamiento, Y, D)
      
      if(sumerr < menor_sumerr):
        mejor_ht = ht
        menor_sumerr = sumerr
        menor_errv = errv

      """if(menor_sumerr > 0.3):
        A = A + 1"""

    # Calculamos la confianza.
    if(menor_sumerr == 0.0):
      alpha = 0.0
    else:
      alpha = np.double(0.5 * np.log2((1.0 - menor_sumerr) / menor_sumerr))

    # Arrays de clasificadores y sus confianzas.
    H.append([mejor_ht, alpha])

    # Normalizamos D.
    # print((alpha, menor_sumerr, np.sum(D)))
    Z = np.sum(D)
    exp = np.double(np.exp(-alpha * -np.double(menor_errv)))
    D = np.double(D * exp / Z)

    # Datos para gráfica.
    pixel.append(mejor_ht[0])
    error.append(menor_sumerr)

  # Un plot chulo de los mejores debiles
  utils.plot_arrays(error, pixel, "Error de cada Clasificador por Pixel", "Grado de Error - 1: 100% error, 0: Perfecto.", "Numero de Pixel.")

  """print("Clasificadores de T:")
  print(H)"""

  return H