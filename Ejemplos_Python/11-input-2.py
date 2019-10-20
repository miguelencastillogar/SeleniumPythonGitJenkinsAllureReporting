# Formulamos los mandatos que debe cumplir el usuario
pregunta = '\nAgrega un numero y te dire si es par o impar '
pregunta += '(Escribe "Cerrar o cerrar" para salir de la aplicacion) '

# Variable booleana que mantendra el while iterandose
preguntar = True

while preguntar:

    numero = input(pregunta)

    if numero == "Cerrar" or numero == "cerrar":
        preguntar = False
    else:
        numero = int(numero)

        if numero % 2 == 0:
            print(f'El numero {numero} es par')
        else:
            print(f'El numero {numero} es impar')
