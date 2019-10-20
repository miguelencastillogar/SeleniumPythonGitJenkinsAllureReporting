lenguajes = ["Python", "Kotlin", "Java", "JavaScript", "PHP", "Ruby", "GO"]

# Iterador y al igual que las funciones toda
# la logica interna del iterador lo define
# la identacion.
for lenguaje in lenguajes:
    print(f"Estoy aprendiendo {lenguaje}")

# Sera impreso al terminar la iteracion del list
# ya que esta fuera de la identacion del for
print("Se imprime al terminar el for")

# For que escriba numeros, su sintaxis es la siguienete:
# for numero in range(0, 10) en donde 0 es el valor inicial
# y 10 el valor final, tomando en cuenta que la impresion sera
# del 0 al 9, ya que el 10 es el limite
for numero in range(0, 10):
    print(numero)

# El tercer valor que es el 2 significa
# que el valor inicial 0 sera incrementado
# y actualizado de dos en dos por cada iteracion.
# Su impresion sera: 0 2 4 6 8
for numero in range(0, 10, 2):
    print(numero)
