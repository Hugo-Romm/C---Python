print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

agno = int(input("Para preparar tu perfil, dime en quÃ© aÃ±o naciste. "))
edad = 2017-agno-1
print()

estatura = float(input("CuÃ©ntame mÃ¡s de ti, para agregarlo a tu perfil. Â¿CuÃ¡nto mides? DÃ­melo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

num_amigos = int(input("Muy bien. Finalmente, cuÃ©ntame cuantos amigos tienes. "))

print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "aÃ±os")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centÃ­metros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la informaciÃ³n. Esperamos que disfrutes con Mi Red")
print()

mensaje = input("Ahora vamos a publicar tu primer mensaje. Â¿QuÃ© piensas hoy? ")
print()
print("--------------------------------------------------")
print(nombre, "dice:", mensaje)
print("--------------------------------------------------")
