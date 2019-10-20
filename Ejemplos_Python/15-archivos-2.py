def app():

    # al usar open('nombre_archivo.extension', 'permiso') la desventaja
    # es que tenemos que cerrear la conexion, para abrir el archivo,
    # leer su contenido y mostrarlo en consola iniciaremos utilizando:

    # with open('nombre_archivo.extension') as archivo, no especificamos
    # una letra por ejemplo w ya que por default los archivo se crean
    # en modo lectura y 'as archivo' es un alias para al momento de usar
    # archivo nos estamos refiriendo a with open('nombre_archivo.extension').

    # Al utilizar with open('nombre_archivo.extension') no es necesario
    # cerrar el archivo
    with open('archivo.txt') as archivo:

        # Iremos iterando cada una de las lines
        for contenido in archivo:

            # el metodo rstrip() elimina los saltos de linea
            print(contenido.rstrip())


app()
