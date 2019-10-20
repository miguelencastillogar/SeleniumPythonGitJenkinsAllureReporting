# Diferencias entre un metodo y una funcion

nombre = "miguel"


def mostrar_nombre(nombre):
    print(f"Hola {nombre}")


# Esto es una funcion: nombre_funcion(parametro)
# o nombre_funcion()
mostrar_nombre(nombre)

# Esto es un metodo: nombre_variable.nombre_funcion(parametro)
# o nombre_variable.nombre_funcion()
print(nombre.upper())
print(nombre.title())
