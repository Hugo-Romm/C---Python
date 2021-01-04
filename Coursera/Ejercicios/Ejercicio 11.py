# Considere que existen los números primos y los números pandigitales. Los números pandigitales son aquellos que contienen todos los dígitos del 0 al 9 al menos una vez,
# como el 1023478695. Escribe una función panprimo que determine si un número n es pandigital y si al mismo tiempo, sus últimos 3 dígitos conforman un número primo,
# retornando True o False según corresponda. Por ejemplo:

# 1) El número 2424643 cumple que sus últimos 3 dígitos conforman un número primo (643), pero no es pandigital por lo tu función que debería retornar False.

# 2) El número 1234567890 cumple que es pandigital, pero sus últimos 3 dígitos no conforman un primo (890), por lo que tu función debería retornar False.

# 3) El número 10123485769 cumple que es pandigital y además el número conformado por sus 3 últimos dígitos (769) es primo, por lo que debería retornar True.

# Tip1: Puedes convertir un entero a una cadena de texto con el método str(numero), y puedes verificar si alguna letra está en el esta cadena de texto haciendo if letra in string: ...

# Tip2: Un número es primo si solo es divisible por 1 y por sí mismo. Para obtener los últimos tres dígitos, puedes obtener el resto del número en su división con 100.

def panprimo(n):
  contador=0
  pan=0
  numerop=n%1000
  primo=False
  pandi=False
  for j in range(2,numerop):
    if numerop % j == 0:
      contador += 1
  for i in range(10):
    if str(pan) in str(n):
      pan += 1
  if contador > 0:
    primo=False
  elif numerop==1:
    primo=False
  else:
    primo=True
  if pan == 10:
    pandi=True
  else:
    pandi=False
  if primo == True and pandi == True:
    return True
  else:
    return False
# escribe tu función aquí, recuerda seguir cuidadosamente
# las instrucciones respecto a argumentos y retorno












