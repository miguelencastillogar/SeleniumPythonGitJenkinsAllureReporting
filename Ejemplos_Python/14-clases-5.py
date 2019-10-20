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

        return self.__nombre

    def get_categoria(self):

        return self.__categoria

    def get_precio(self):

        return self.__precio

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


# Polimorfismo es la habilidad de tener diferentes comportamientos
# basado en que subclase se esta utilizando, relacionado muy
# estrechamente con herencia.
class Hotel(Restaurante):

    def __init__(self, nombre, categoria, precio, alberca):

        # Hacemos referencia a la clase padre
        super().__init__(nombre, categoria, precio)

        # Aqui se aplica el polimorfismo, ya que este atributo
        # unicamente existe y se utiliza al momento de utilizar
        # la clase Hotel
        self.__alberca = alberca

    # Agregamos un metodo que solo existe en el Hotel
    # Aqui se aplica el polimorfismo, ya que este comportamiento
    # unicamente existe y se utiliza al momento de utilizar
    # la subclase Hotel
    def get_alberca(self):

        return self.__alberca

    def set_alberca(self, alberca):

        self.__alberca = alberca

    # Reescribir un metodo (debe llamarse igual)
    def mostrar_informacion(self):

        # Se puede utilizar tanto self o super para hacer referencia a la clase padre:
        # super().get_nombre() o self.get_nombre()
        # super().get_categoria() o self.get_categoria()
        # super().get_precio() o self.get_precio()
        print(
            f'Nombre: {super().get_nombre()} \nCategoria: {self.get_categoria()} \nPrecio: {self.get_precio()} \nAlberca: {self.__alberca}\n')


print('\n')

hotel = Hotel('Cadena de Hoteles Dreams', '5 Estrellas', 250, 'Si')
hotel.mostrar_informacion()
