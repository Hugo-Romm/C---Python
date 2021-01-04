# Considerando que las variables pueden almacenar cualquier tipo de dato, en este ejercicio se utilizaran variables de tipo booleanas.
# En computación un operador muy conocido es el operador lógico XOR (exclusive OR), el que dadas dos expresiones a y b booleanas,
# entrega verdadero únicamente si una de ellas es verdadera, y falso en cualquier otro caso.

# Por ejemplo si se tiene

# resultado = True XOR False

# en resultado estará almacenado el valor True, en cambio si se tiene

# resultado = True XOR True o resultado = False XOR False

# en resultado estará almacenado el valor False.

# La tabla de verdad para todos los valores posibles de a y b, es la siguiente:

# a	    b	    a XOR b
# True	True	False
# True	False	True
# False	True	True
# False	False	False
# Así, utilizando los conocimientos de booleanos adquiridos en el curso, y los conocimientos de operadores lógicos, modifica el código de más abajo,
# para que en la variable xor quede almacenado el valor de hacer XOR entre las variables a y b.

# Para poder resolver este problema , debes escribir el código que falta en el espacio que lo señala. Asume que ya existen variables con los nombres a y b,
# que ya contienen los valores requeridos (no debes pedírselos al usuario), haz los cálculos que necesites, y luego deja el resultado en una variable llamada xor.

def xor(a, b):
  xor = False
  xor = (a or b) and not (a and b)
  return xor









