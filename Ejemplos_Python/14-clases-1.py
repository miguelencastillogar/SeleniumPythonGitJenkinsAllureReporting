class Restaurante:

    # El parámetro self se refiere al objeto instanciado de esa clase sobre el cual se está invocando dicho método.
    # Es decir, el objeto que usaste para llamar al método (en tu ejemplo persona1 y persona2).

    # Python, dentro de los métodos definidos de una clase, establece que el primer parámetro definido en un método
    # recibirá el objeto con el cual se invoca dicho método. Este parámetro (que se suele llamar self aunque se puede
    # usar cualquier nombre de variable [ver comentarios]) es usado dentro de la implementación del método para modificar
    # el contenido o atributos de dicho objeto como desees.

    # Por lo tanto, es una condición necesaria que todos los métodos de una clase que puedan ser llamados a través
    # de un objeto tengan al menos un parámetro, el cual se asignará automáticamente al objeto usado en la invocación.

    # Aunque en la definición del método, self es el primer parámetro, a la hora de llamar a dicho método no hace falta
    # pasarle el propio objeto como primer parámetro explícitamente ya que Python lo hace de manera implícita sin necesidad
    # de hacerlo manualmente. Es decir, el primer parámetro self del método se asigna automáticamente al propio objeto
    # y el resto de parámetros a los argumentos con que llames al método.

    # En el caso del método __init__(), el parámetro self se refiere al objeto recién instanciado de la clase
    # que quieres obtener al crear dicho objeto con Nombre_Clase().

    # self es el equivalente al this de otros lenguajes (aunque self no es palabra reservada como this [ver comentarios]),
    # con la diferencia de que en otros lenguajes no hace falta definir los métodos con un parámetro this, mientras que
    # en Python sí es necesario.

    # En conclusion self es una manera de referirse al mismo objeto que estamos ejecutando

    def agregar_restaurante(self, nombre):

        # Atributo
        self.nombre = nombre

    def mostrar_informacion(self):

        print(f'Nombre: {self.nombre}')


# Instanciar la clase
restaurante = Restaurante()
restaurante.agregar_restaurante('Pizzeria Mexico')
restaurante.mostrar_informacion()

# Otro Instanciamiento de la misma clase, pero esta vez
# es un objeto con informacion diferente
restaurante2 = Restaurante()
restaurante2.agregar_restaurante('Pizzarelli')
restaurante2.mostrar_informacion()

# Mostrar la informacion acciendo directamente
print(f'Nombre Restaurante: {restaurante.nombre}')
print(f'Nombre Restaurante: {restaurante2.nombre}')
