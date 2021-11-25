import random
import numpy as np

# Dimensión con la que vamos a trabajar. En nuestro caso 28*28
def generar_clasificador_debil(dim_imagen):
  ht = np.zeros(3)
  ht[0] = np.random.randint(0, dim_imagen)        # Num. Pixel
  ht[1] = random.randint(0, 255)               # Valor Umbral Grises
  ht[2] = np.sign(np.random.rand(1) * 2-1)     # Decisión
  return ht;

def aplicar_clasificador_debil(ht, X):

  # Por cada imágen de X, comprobamos si el pixel de dicha imágen tiene un valor mayor que el clasificador
  #   si no lo es, en vez de descartarlo, le podemos dar la vuelta, y reusarlo.
  if(ht[2] == 1):
    mascara_resultados = X[:, int(ht[0])] > ht[1]
  else: 
    mascara_resultados = X[:, int(ht[0])] <= ht[1]

  # Usamos int para pasar de true y false a 1 y 0
  resultados = np.int16(mascara_resultados)
  
  # Pasamos de 0 a -1
  resultados[np.where(resultados == 0)] = -1

  return resultados

def obtener_error(resultados, Y, D):

  # Usamos int para pasar de true y false a 1 y 0
  errv = np.int64(resultados != Y)
  sumerr = np.double(np.sum(errv * D))
  
  return [sumerr, errv]

def aplicar_clasificador_fuerte(H, X):  
  certeza = []

  # Por cada clasificador debil ht del cojunto de fuertes h, lo aplicamos a todas las imágnes de X, y vemos si nos dice
  for [ht, alpha] in H:

    # POR CADA IMAGEN SE PASA TODAS LAS ht
    resultados = aplicar_clasificador_debil(ht, X)

    if (len(certeza) == 0):
      certeza = alpha * resultados
    else:
      certeza = certeza + (alpha * resultados)

  f = np.sign(certeza)
  return f