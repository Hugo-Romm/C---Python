midiccionario = {"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}
midiccionario["Italia"]="Lisboa"
print(midiccionario)
midiccionario["Italia"]="Roma"
print(midiccionario)
del midiccionario["Reino Unido"]
print(midiccionario)
print()
#-------------------------------------------------------------------------------------------------------
midiccionario1 = {"Alemania":"Berlin", "Francia": 3, "España": 4}
print(midiccionario1)
print()
mitupla = ["España", "Francia", "Reino Unido", "Alemania"]
midiccionario1 = {mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Londres", mitupla[3]:"Berlín"}
print(midiccionario1["Francia"])
print()
midiccionario1 = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario1.keys())
print(midiccionario1.values())
print(len(midiccionario1))
print(midiccionario1["anillos"])



