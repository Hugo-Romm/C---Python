milista=["Maria", 5 ,True, 78.35]

milista.extend(["Sandra", "Ana", "Lucia"])

milista.remove("Ana")

milista.pop()

print(milista[:])

print(milista.index("Sandra"))

print("Pepe" in milista)

#--------------------------------------------

milista2=["Pedro", "Diego", "Agustin"]

milista3=milista2+milista

print(milista3[:])

#---------------------------------------------
milista4=["el uno", "el dos", "el tres"] * 5

print(milista4[:])
