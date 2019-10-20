class Restaurante:

    def __init__(self, nombre, categoria, precio):

        # Por defecto estas variables estan publicas
        # self.nombre = nombre
        # self.categoria = categoria
        # self.precio = precio

        # Para hacerlas PROTECTED unicamente al inicio del nombre
        # del atributo le agregamos un guion bajo
        # self._nombre = nombre
        # self._categoria = categoria
        # self._precio = precio

         # Para hacerlas PRIVATE unicamente al inicio del nombre
        # del atributo le agregamos doble guion bajo
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio

    # Getters

    def get_nombre(self):

        print(self.__nombre)

    def get_categoria(self):

        print(self.__categoria)

    def get_precio(self):

        print(self.__precio)

    # Setters

    def set_nombre(self, nombre):

        self.__nombre = nombre

    def set_categoria(self, categoria):

        self.__categoria = categoria

    def set_precio(self, precio):

        self.__precio = precio

    def mostrar_informacion(self):

        print(
            f'Nombre: {self.__nombre} \nCategoria: {self.__categoria} \nPrecio: {self.__precio}\n')


# Creamos una clase hijo de Restaurante
class Hotel(Restaurante):

    def __init__(self, nombre, categoria, precio):

        # Hacemos referencia a la clase padre
        super().__init__(nombre, categoria, precio)


print('\n')

hotel = Hotel('Cadena de Hoteles Dreams', '5 Estrellas', 250)

hotel.mostrar_informacion()
