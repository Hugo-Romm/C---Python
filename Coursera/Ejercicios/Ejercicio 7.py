# Escribe un código que calcule el cuadrado de un número si este es impar, o el cubo de un número si este es par. Por ejemplo, para 4 tu programa debe entregar 64, y para 3 debe entregar 9.

def exponenciacion(numero):
  resultado = numero
  if (numero % 2 == 1):
    numero = numero**2
  elif (numero % 2 == 0):
    numero = numero**3
  resultado = numero
  return resultado











