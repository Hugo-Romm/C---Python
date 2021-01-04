# Para obtener ciertas estadísticas de un recorrido, se pide realizar un programa que dada una distancia, entregue la velocidad en kilómetros por hora y en metros por segundo.
# Para esto, existen dos variables tiempo y distancia que vienen en segundos y kilómetros respectivamente. Tu programa debe guardar en la variable resultado un string, por ejemplo,
# para el siguiente caso:

# tiempo = 1

# distancia = 0.01

# La variable resultado debería tener lo siguiente:

# "La velocidad es 36.0 km/h o 10.0 m/s"

# Para poder resolver este problema , debes escribir el código que falta en el espacio que lo señala. Asume que ya existen variables con los nombres tiempo y distancia,
# que ya contienen los valores requeridos (no debes pedírselos al usuario), haz los cálculos que necesites, y luego deja el resultado en una variable llamada resultado.





def velocidad(distancia, tiempo):

  velocidad = distancia / tiempo

  a = (float(velocidad) * 3600)

  b = (float(velocidad) * 1000)

  resultado = str(a) +" " "km/h" " " "o" " " + str(b) +" " "m/s"
  print("La velocidad es", str(resultado))

  return resultado

