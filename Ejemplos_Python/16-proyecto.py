# Libreria que tiene una gran cantidad
# de funciones para manejar archivos
import os

# las constantes en Python se escriben en mayuscula
CARPETA = 'contactos/'  # Carpeta de contactos
EXTENSION = '.txt'  # Extension de archivos


# Clase Contacto
class Contacto:

    def __init__(self, nombre, telefono, categoria):

        self.__nombre = nombre
        self.__telefono = telefono
        self.__categoria = categoria

    # Getters

    def get_nombre(self):

        return self.__nombre

    def get_telefono(self):

        return self.__telefono

    def get__categoria(self):

        return self.__categoria

    # Setters

    def set_nombre(self, nombre):

        self.__nombre = nombre

    def set_telefono(self, telefono):

        self.__telefono = telefono

    def set__categoria(self, categoria):

        self.__categoria = categoria


def app():

    try:
        # Creacion de los directorios
        crear_directorio()

        # Muestra el menu de opciones
        mostrar_menu()

        # Preguntar al usuario la accion a realizar
        preguntar = True

        while preguntar:

            opcion = input('\nSelecciones una Opción: ')
            opcion = int(opcion)

            if opcion == 1:
                agregar_contacto()
                preguntar = False

            elif opcion == 2:
                editar_contacto()
                preguntar = False

            elif opcion == 3:
                mostrar_contactos()
                preguntar = False

            elif opcion == 4:
                buscar_contacto()
                preguntar = False

            elif opcion == 5:
                eliminar_contacto()
                preguntar = False

            else:
                print('\nOpción no válida, intente de nuevo.')

    except Exception as e:

        print('\n' + e.__str__())
        print('\n¡¡¡Gracias por utilizarnos!!!\n')


def eliminar_contacto():

    print('\nEliminar Contacto\n')

    nombre_contacto = input(
        'Introduzca el nombre del contacto que desea eliminar: ')

    # Revisar si el archivo ya existe, lo logramos mediante os.path.isfile(ruta_nombre.estension).
    existe = existe_contacto(nombre_contacto)

    if existe:

        os.remove(CARPETA + nombre_contacto + EXTENSION)

        existe = existe_contacto(nombre_contacto)

        if not existe:

            print('\n¡¡¡Contacto eliminado correctamente!!!\n')

        else:

            print('\n¡¡¡Contacto no eliminado correctamente!!!\n')

    else:

        print(f'\nEl contacto {nombre_contacto} no existe.')

    app()


def buscar_contacto():

    print('\nBuscar Contacto\n')

    nombre_contacto = input(
        'Introduzca el nombre del contacto que desea buscar: ')

    # Revisar si el archivo ya existe, lo logramos mediante os.path.isfile(ruta_nombre.estension).
    existe = existe_contacto(nombre_contacto)

    if existe:

        print('\n')

        # En este caso usamos la letra 'w' para especificar el modo
        # de escritura, ya que por default se crea en modo lectura,
        # y el 'with open' lo utilizamos para que abra y cierre el
        # archivo automaticamente.
        with open(CARPETA + nombre_contacto + EXTENSION) as archivo:

            for contenido in archivo:

                print(contenido.rstrip())

        print('\n¡¡¡Contacto consultado correctamente!!!\n')

    else:

        print(f'\nEl contacto {nombre_contacto} no existe.')

    app()


def mostrar_contactos():

    print('\nMostrar Contactos\n')

    # el metodo os.listdir nos permite listar los archivos de un directorio
    archivos = os.listdir(CARPETA)

    # Agregue unicamente los archivos que finalizan con txt
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    # Iteramos la lista de archivos con extension .txt
    for archivo in archivos_txt:

        # Leemos el archivo
        with open(CARPETA + archivo) as contacto:

            # Iteramos el contenido del archivo
            for contenido in contacto:

                # Imprimimos la informacion del archivo
                print(contenido.rstrip())

            print('\n')

    app()


def editar_contacto():

    print('\nEditar Contacto\n')

    nombre_contacto_anterior = input(
        'Introduzca el nombre del contacto que desea editar: ')

    # Revisar si el archivo ya existe, lo logramos mediante os.path.isfile(ruta_nombre.estension).
    existe = existe_contacto(nombre_contacto_anterior)

    if existe:

        # En este caso usamos la letra 'w' para especificar el modo
        # de escritura, ya que por default se crea en modo lectura,
        # y el 'with open' lo utilizamos para que abra y cierre el
        # archivo automaticamente.
        with open(CARPETA + nombre_contacto_anterior + EXTENSION, 'w') as archivo:

            # Capturamos el nuevo nombre del contacto
            nombre_contacto_nuevo = input(
                '\nIntroduzca el nuevo nombre del contacto que desea editar: ')
            # Capturamos el nuevo telefono del contacto
            telefono_contacto = input(
                'Introduzca el nuevo télefono del contacto: ')
            # Capturamos la nuevo categoria del contacto
            categoria_contacto = input(
                'Introduzca la nueva categoría del contacto: ')

            # Instanciamos la clase
            contacto = Contacto(
                nombre_contacto_nuevo, telefono_contacto, categoria_contacto)

            # Escribimos en el archivo
            archivo.write('Nombre: ' + contacto.get_nombre() + '\n')
            archivo.write('Telefono: ' + contacto.get_telefono() + '\n')
            archivo.write('Categoria: ' + contacto.get__categoria())

        # Renombrar el archivo y lo hacemos mediante
        # os.rename(rutaVieja_nombreViejo.estension, rutanueva_nombrenuevo.estension)
        os.rename(CARPETA + nombre_contacto_anterior + EXTENSION,
                  CARPETA + nombre_contacto_nuevo + EXTENSION)
        print(
            f'\n¡¡¡Contacto {nombre_contacto_anterior} editado correctamente por {nombre_contacto_nuevo}!!!\n')

    else:

        print(f'\n¡¡¡El Contacto {nombre_contacto_anterior} no existe!!!\n')

    app()


def agregar_contacto():

    print('\nAgregar Contacto\n')

    nombre_contacto = input('Introduzca el nombre del contacto: ')

    # Revisar si el archivo ya existe, lo logramos mediante os.path.isfile(ruta_nombre.estension).
    existe = existe_contacto(nombre_contacto)

    if not existe:

        # En este caso usamos la letra 'w' para especificar el modo
        # de escritura, ya que por default se crea en modo lectura,
        # y el 'with open' lo utilizamos para que abra y cierre el
        # archivo automaticamente.
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            # Capturamos el telefono del contacto
            telefono_contacto = input('Introduzca el télefono del contacto: ')
            # Capturamos la categoria del contacto
            categoria_contacto = input(
                'Introduzca la categoría del contacto: ')

            # Instanciamos la clase
            contacto = Contacto(
                nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribimos en el archivo
            archivo.write('Nombre: ' + contacto.get_nombre() + '\n')
            archivo.write('Telefono: ' + contacto.get_telefono() + '\n')
            archivo.write('Categoria: ' + contacto.get__categoria())

        print('\n¡¡¡Contacto agregado correctamente!!!\n')

    else:

        print(f'\nEl contacto {nombre_contacto} ya existe.')

    app()


def mostrar_menu():

    print('\nSeleccione del Menú lo que desea hacer\n')
    print('1-) Agregar Nuevo Contacto')
    print('2-) Editar contacto')
    print('3-) Mostrar Contactos')
    print('4-) Buscar contacto')
    print('5-) Eliminar contacto')


def crear_directorio():

    # Para revisar si una carpeta existe o no
    # es con os.path.exists.

    # Si la carpeta contactos no existe, pues la creamos
    if not os.path.exists(CARPETA):

        # Crea directorio
        os.makedirs(CARPETA)


def existe_contacto(nombre):

    return os.path.isfile(CARPETA + nombre + EXTENSION)


app()

print('\n')
