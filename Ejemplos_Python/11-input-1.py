# El Python se utiliza la funcion input() para detener
# la ejecucion del programa hasta que el usuario agrege
# informacion. Tomar en cuenta que las estradas de datos
# siempre vienen en String.

# Captura y muestra de data String por teclado
nombre = input('Cuál es tu nombre: \r\n')
print(f'Hola {nombre}')

# Captura y muestra de data int por teclado
edad = input('Cuál es tu edad? \r\n')
# Convierte edad de tipo String a int
edad = int(edad)

if edad >= 18:
    print('Ya puedes votar')
else:
    print('Aún no puedes votar')

# Mezcla con operadores
numero = input('Introduzca un numero: \r\n')
numero = int(numero)

if numero % 2 == 0:
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')
