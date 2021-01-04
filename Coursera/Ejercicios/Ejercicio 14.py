# Escriba una función que reciba un string consistente de unos y ceros y retorne la cantidad de ocurrencias de unos menos la cantidad de ocurrencias de ceros.

# Por ejemplo, si el string es "11000110101", entonces tu función debe retornar 1 (ya que hay 6 unos y 5 ceros)

def ocurrencias(string):
    return string.count("1") - string.count("0")

ocurrencias("11000110101")









