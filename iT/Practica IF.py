print("Programa de evaluacion de notas de alumnos")
print()
nota_alumno = input("Introduce la nota" )

def evaluacion(nota):
    valoracion = "aprobado"
    if nota<5:
        valoracion = "suspenso"
    return valoracion

print(evaluacion(int(nota_alumno)))

#-----------------------------------




