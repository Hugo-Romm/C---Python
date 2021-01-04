# En esta funciones no buscamos que impriman nada con print, sino que retornen una variable. Por ejemplo, si están pidiendo la suma de dos números, como en la pregunta pasada,
# le devolveremos al que preguntó una variable que contenga el valor de la suma.

# En esta pregunta, hay cuatro variables definidas, pero solo debes retornar una (es decir, en la línea 8 poner algo como return algo, con algo una opción entre var1, var2, var3, var4).
# En esta pregunta debes retornar la multiplicación de los dos parámetros (valores dentro de paréntesis después del nombre de la función) que se pasan a la función. ¿Cuál de las cuatro variables será?

def multiplicacion(a, b):
    var1 = a + b
    var2 = a + var1
    var3 = a * var2
    var4 = a / b

    # Después de esta línea pon algo como return nombre_variable, donde nombre_variable es la variable correcta según lo que pide.
    # Ojo: debe escribirse con la misma indentación (cantidad de espacios al principio de la línea) que las líneas 2 a 5.

    return var3


resultado = multiplicacion(5, 5)
print(resultado)










