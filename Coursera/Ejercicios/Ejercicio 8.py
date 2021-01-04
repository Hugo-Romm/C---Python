# Escriba un programa que verifique si un número es primo o no. Por ejemplo, para los número 3, 5, y 13, la variable primo debe ser True, y para 1, 10, y 33, False.

def es_primo(numero):
  primo = True
  x = 1
  div = 0
  while (x <= numero):
    if (a % x == 0):
      div = div + 1
    x = x + 1
  if (div == 2):
    primo = True
    else
    primo = False
  return primo








