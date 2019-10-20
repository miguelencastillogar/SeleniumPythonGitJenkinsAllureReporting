# Python para referirse a arreglo en vez mencionar
# el termino array, pues usa list
lenguajes = ["Python", "Kotlin", "Java", "JavaScript"]

print(lenguajes)

# Los arrays (list) comienzan en la posicion 0
print(lenguajes[0])

# Existen funciones que son especificas de los list.
# Ejemplos:

# Si deseamos ordenar la lista
lenguajes.sort()  # primero se ordenan
print(lenguajes)  # luego se muestran

# Acceder a un elemento dentro de un list
aprendiendo = f"Estoy aprendiendo {lenguajes[3]}"
print(aprendiendo)

# Modificando valores de un list
lenguajes[2] = "PHP"
print(lenguajes)

# Agregar elementos a un list
lenguajes.append("Ruby")
print(lenguajes)

# Eleiminar elemento de un list
del lenguajes[1]
print(lenguajes)

# Eleiminar el ultimo elemento de un list
lenguajes.pop()
print(lenguajes)

# Eleiminar una posicion en especifico de un list con pop()
lenguajes.pop(0)
print(lenguajes)

# Eleiminar por nombre de un list
lenguajes.remove("PHP")
print(lenguajes)
