# Creando un diccionario (objeto) simple

cancion = {
    # llave : valor (Para agregar mas valores los separamos por comas)
    'artista': 'Metallica',
    'cancion': 'Enter Sandman',
    'lanzamiento': 1992,
    'likes': 3000
}

# Imprimir todos los valores
print(cancion)

# Acceder a los elementos del diccionario
print(cancion['artista'])
print(cancion['lanzamiento'])

# Mezclar con un string y tomando en cuenta que si procedemos
# de esta manera: print(f'Estoy escuchando {cancion['artista']}')
# obtendremos un error y siendo la unica solucion asignar el
# valor del diccionario (objeto) a una variable y luego
# mezclarla con un String.
artista = cancion['artista']

print(f'Estoy escuchando a {artista}')

# Imprimir todos los valores antes de agregar nuevo valor
print(cancion)

# Agregar nuevos elementos
# debido a que la nueva propiedad no existe, pues automaticamente la grega
cancion['palylist'] = 'Heavy Metal'

# Imprimir todos los valores despues de agregar nuevo valor
print(cancion)

# Imprimir todos los valores antes de modificacion
print(cancion)

# Agregar nuevos elementos
# debido a que la propiedad existe, pues modifica su valor
cancion['cancion'] = 'Seek & Destroy'

# Imprimir todos los valores despues de modificacion
print(cancion)

# Imprimir todos los valores antes de eliminar propiedad
print(cancion)

# Agregar nuevos elementos
# debido a que la propiedad existe, pues modifica su valor
del cancion['lanzamiento']

# Imprimir todos los valores despues de eliminar propiedad
print(cancion)
