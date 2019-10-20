# Iniciar un diccionario vacio
jugador = {}
# Mostramos el diccionario vacio
print(jugador)

# Agregamos una propiedad y valor al diccionario vacio,
# no olvidemos que si es una propiedad que no existe
# la agrega automaticamente al diccionarios
jugador['nombre'] = 'Miguel Castillo'
jugador['puntaje'] = 0

# Mostramos el diccionario luego de agregar propiedades y valores
print(jugador)

# Modificamos el valor de una propiedad existente,
# no olvidemos que si existe la propiedad, automaticamnte
# de modificara su valor
jugador['puntaje'] = 100

# Mostramos el diccionario luego de modificar
# propiedades y valores
print(jugador)

# Acceder a u valor que no existe de una nueva forma
# debido a que este valor no existe nos imprime None
print(jugador.get('consola'))

# De esta forma si el valor no existe, pues presentara
# el mensaje que definimos
print(jugador.get('consola', 'No existe este valor en el diccionario'))


# Iterar en el diccionario
for llave, valor in jugador.items():
    print(f'{llave} : {valor}')

# Eliminar llaves y valores
del jugador['nombre']
del jugador['puntaje']

# Mostramos el diccionario luego de eliminar
# las llaves y valores
print(jugador)
