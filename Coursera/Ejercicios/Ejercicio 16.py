# Escriba una función que reciba un string como parámetro y retorne el string, pero con cada elemento que estuviese en mayúsculas reemplazado por "$".
# Asuma que el string consistirá solamente de letras.

# Por ejemplo si el string es "Viva la Vida", entonces tu función debe retornar "$iva la $ida".

def reemplazo(string):

    indice = 0

    while indice < len(string):
        letra = string[indice]
        if letra.isupper() == True:
            string = string.replace(letra, '$')
        indice += 1

    return string


print(reemplazo('Viva la Vida'))










