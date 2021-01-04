# Escribe un programa para ayudar a una empresa que desea asignar sueldos para los cargos de sus trabajadores. La lista es la siguiente:

# Ejecutivo: 90

# Jefe: 100

# Externo: 50

# La variable cargo contiene el nombre del cargo (por ejemplo, "Externo"). Recuerda entregar tu resultado modificando únicamente la variable dinero

def sueldo(cargo):
  dinero = 0
  if (cargo == "Ejecutivo"):
    dinero = dinero + 90
  elif (cargo == "Jefe"):
    dinero = dinero + 100
  elif (cargo == "Externo"):
    dinero = dinero + 50
  return dinero









