class Restaurante:

    # Constructor
    def __init__(self, nombre, categoria, precio):

        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self):

        print(
            f'Nombre: {self.nombre} \nCategoria {self.categoria} \nPrecio: {self.precio}\n')


print('\n')

restaurante = Restaurante('Pizzeria Mexico', 'Comida Italiana', 50)
restaurante.mostrar_informacion()

restaurante2 = Restaurante('Meson de Daisy', 'Comida Dominicana', 20)
restaurante2.mostrar_informacion()
