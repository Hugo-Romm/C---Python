print("Bienvenido a ...")
print("""
.__                                                
|  |_________          ____________   ____   ____  
|  |  \_  __ \  ______ \___   /  _ \ /    \_/ __ \ 
|   Y  \  | \/ /_____/  /    (  <_> )   |  \  ___/ 
|___|  /__|            /_____ \____/|___|  /\___  >
     \/                      \/          \/     \/ 
     """)

nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
edad = 2017-agno-1
print()

estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. Cuánto mides? Dímelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))

print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")


#Ahora puedes practicar solicitando mÃ¡s datos al usuario. Solo tienes que usar apropiadamente input() y print()
#1. Escribe 3 solicitudes de datos al usuario, por ejemplo sexo, numero de telefono, ciudad donde vive,
#   pais de nacimiento, direccion, etc. Guarda esos datos en variables del tipo, y finalmente escrÃ­belos en pantalla
#   utilizando print. Puedes agregar todas las lÃ­neas que necesites.

print("Proporcióna datos adicionales obligatorios")
genero = input("¿Cuál es tu genero? ")
print()
print("Genero   ", genero)
print()

numero_cell = str(input("Cuál es tu número de teléfono? "))
print()
print("Mi numero de telefono es = ", numero_cell)
print()

ciudad_vive = input("Cual es tu ciudad? ")
print()
print("Ciudad = ", ciudad_vive)
print("Eso es todo... Gracias!!!")
print()

print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:             ", nombre)
print("Edad:               ", edad, "años")
print("Estatura:           ", estatura_m, "metros y", estatura_cm, "centímetros")
print("Amigos:             ", num_amigos)
print("Genero:             ", genero)
print("Numero de teléfono: ", numero_cell)
print("Ciudad:             ", ciudad_vive)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

#Usaremos una variable bool para indicar si el usuario desea continuar
#utilizando el programa o no
continuar = True

#Este ciclo se mantiene en ejecución hasta que el usuario desee salir
while continuar:

    #Solicitamos opción al usuario
    escribir_mensaje = str(input("¿Deseas escribir un mensaje? (S/N) "))
    if escribir_mensaje == (escribir_mensaje):
        continuar = True
    #Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    if escribir_mensaje == "S" or escribir_mensaje == "s" or escribir_mensaje == "":
        mensaje = input("Vamos a publicar un mensaje. ¿Qué piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")
        print()
        continuar2 = True

    elif escribir_mensaje == "N" or escribir_mensaje == "n":
        continuar = False

while continuar2:
    cambio_nombre = str(input("Desea cambiar su nombre? (S/N) "))
    if cambio_nombre == (cambio_nombre):
        continuar2 = True
    if cambio_nombre == "S" or cambio_nombre == "s" or cambio_nombre == "":
        nombre = str(input("Nuevo nombre: "))
        print("Tu nuevo nombre es: ", nombre)

    elif cambio_nombre == "N" or cambio_nombre == "n":
        continuar2 = False




#Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar Mi Red. ¡Hasta pronto!")
#Ahora puedes escribir mensajes todas las veces que quieras.
#Observa que hemos utilizado un ciclo while que permite repetir la acción de preguntar por un mensajes
#hasta que el usuario escribe algo distino de "S".

#Pero las redes sociales pueden ejecutar más acciones que solamente enviar mensajes.

#Te proponemos los siguientes desafíos:
#1. Este programa termina cada vez que el valor de 'escribir_mensaje' es distinto a "S" o a "s".
#   Modifique el programa para que el programa termine UNICAMENTE cuando se ingresa "N" o "n".
#   En caso que se ingrese algo distinto, debe volver a solicitar una opción al usuario.
#
#2. Modifica este menú para que le permita el usuario realizar más de una acción.
#   Por ejemplo, puedes agregar una acción que permita al usuario modificar su nombre.