# Revisar si una condicion es mayor a
balance = 0

if balance > 0:
    print("Puedes pagar")
else:
    print("No tienes saldo")

likes = 200
if likes == 200:
    print("Excelente, 200 likes")
else:
    print("No tienes 200 likes")

# if con text
lenguaje = "Python"
if lenguaje == "Python":
    print("Excelente desicion")

# la sentencia != se expresa de la siguiente forma:
if not lenguaje == "PHP":
    print(f"Excelente desicion, sabes {lenguaje}")

# Evaluar un boolean
usuario_autenticado = True

if usuario_autenticado == True:
    print("Acceso al sistema")
else:
    print("Debes iniciar sesion")

# Es lo mismo que el if anterior
if usuario_autenticado:
    print("Acceso al sistema")
else:
    print("Debes iniciar sesion")

# evaluar un elemento de una lista
lenguajes = ["Python", "Kotlin", "Java", "JavaScript", "PHP", "Ruby", "GO"]

if "PHP" in lenguajes:
    print("PHP si existe")
else:
    print("PHP no existe")

# if anidado
usuario_autenticado = False
usuario_admin = False

if usuario_autenticado:
    if usuario_admin:
        print("ACCESO TOTAL")
    else:
        print("Acceso al sistema")
else:
    print("Debes iniciar sesion")
