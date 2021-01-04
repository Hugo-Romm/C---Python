# Escriba una función que reciba dos strings como parámetros y retorne un nuevo string que consista del primero, pero con el segundo string intercalado entre cada letra del primero.

# Por ejemplo si los strings son "paz" y "so", entonces tu función debe retornar "psoasozso"

def intercalar(string_a, string_b):
    i = 0
    cadena = ""
    while (i < len(string_a)):
        cadena += string_a[i] + string_b

        i = i + 1
    return cadena


variable = intercalar("paz", "so")
print(variable)












