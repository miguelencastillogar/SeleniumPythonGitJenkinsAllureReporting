# Lo qe esta en la definicion de la funcion es un parametro
def informacion(nombre, puesto):
    # Esta sentencia dara error: print("Soy {nombre}"),
    # deberia ser: print(f"Soy {nombre}") y es debido a que
    # al mezclar String con variables se debe
    # agregar la palabra f al inicio de la cadena
    # y fuera de las comillas.
    print(f"Soy {nombre} y soy {puesto}")

# esta funcion tienen parametros por default
# y el parametro que tiene el valor por default
# es puesto = "Desconocido" y esto permite que
# al llamar la funcion pueda ser con un solo
# parametro, ejemplo: informacion2("Jairis Rosario").
# en caso de llamar la funcion con sus dos
# argumentos pues se sobreecribira el parametro
# con el argumento enviado por parametro, ejemplo


def informacion2(nombre, puesto="Desconocido"):
    print(f"Soy {nombre} y soy {puesto}")


# Lo qe esta en la llamada de la funcion es un argumento
informacion("Miguel Castillo", "Desarrollador de Aplicaciones")
informacion("Juan Caso", "Consultor")
informacion("Jairis Rosario", "Consultor")

# Parametros por default
informacion2("Jairis Rosario")
informacion2("Angel Angeles", "Consultor Junior")
