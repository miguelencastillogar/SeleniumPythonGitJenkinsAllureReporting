# Creamos esta variable fuera de la funcion principal
# ya que la utilizaremos en varias funciones
playlist = {}  # Diccionario vacio
playlist['canciones'] = []  # lista vacia

# Cuando creamos una aplicacion mas real, lo ideal
# es tener una funcion principal. Siempre es buena
# idea que tengamos una funcion principal que mande
# a llamas las demas funciones siendo esta la que
# arranque nuestra aplicacion y de hecho asi es que
# lo lograremos en Python.

# Nuentra funcion principal:


def app():

    # Salto de linea
    print('\n')

    # Variable booleana
    agregar_playlist = True

    while agregar_playlist:

        nombre_playlist = input('¿Cómo deseas nombrar la playlist? ')

        # En caso de la variable tener informacion
        if nombre_playlist:

            # Agregamos un nombre a la playlist
            playlist['nombre'] = nombre_playlist

            # Ya tenemos playlist
            agregar_playlist = False

            # Agregamos las canciones al playlist
            agregar_canciones()


def agregar_canciones():

    # Nombre del playlist
    nombre_playlist = playlist['nombre']

    # Pregunta para el usuario
    pregunta = f'Agrega canciones para la playlist {nombre_playlist} '
    pregunta += '(Escribe "X" para dejar de agregar canciones): '

    # Variable booleana para controlar la iteracion del while
    agregar_cancion = True

    while agregar_cancion:

        cancion = input(pregunta)

        if cancion == 'x' or cancion == 'X':

            agregar_cancion = False

            mostrar_resumen()

        elif cancion == "":

            print('Dejaste el campo vacio.')

        else:

            playlist.get('canciones').append(cancion)
            # Es lo mismo: playlist['canciones'].append(cancion)


def mostrar_resumen():

    nombre_playlist = playlist['nombre']
    print(f'\nNombre del playlist: {nombre_playlist}')
    print('\nLista de Canciones:\n')

    for cancion in playlist['canciones']:
        print(f'- {cancion}')


app()

# Salto de linea
print('\n')
