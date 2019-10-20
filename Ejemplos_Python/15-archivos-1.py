def app():

    # Crear el archivo.
    # El metodo open recibe dos argumentos:

    # 1-) rura (en caso de ser diferente al proyecto), nombre y extension.

    # 2-) modo o los permisos, en nuestro caso le pondremos w que significa
    #     permiso de escritura y si este archivo no existe pues lo creara
    archivo = open('archivo.txt', 'w')

    # Escribir en archivo, generaremos numeros en archivo
    for i in range(0, 20):

        archivo.write('Esta en la linea ' + str(i) + '\n')

    # Cerrar el archivo
    archivo.close()


app()
