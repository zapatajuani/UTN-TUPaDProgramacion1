"""
Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas.
"""

# Se imprimen las instrucciones
print("Ingrese su nombre y elija una opción:")
print("1: Nombre en mayúsculas")
print("2: Nombre en minúsculas")
print("3: Nombre con la primera letra mayúscula")

# El usuario ingresa su nombre
nombre = input("Ingrese su nombre: ")
# El usuario elige una opción
opcion = input("Ingrese 1, 2 o 3 según la opción deseada: ")

# Verificamos la opción elegida y transformamos el nombre en consecuencia
if opcion == '1':
    # Opción 1: Convertir a mayúsculas
    nombre_transformado = nombre.upper()
elif opcion == '2':
    # Opción 2: Convertir a minúsculas
    nombre_transformado = nombre.lower()
elif opcion == '3':
    # Opción 3: Convertir a título (primera letra mayúscula)
    nombre_transformado = nombre.title()
else:
    # Opción inválida
    nombre_transformado = "Opción no válida"

# Imprimimos el resultado
print("Resultado:", nombre_transformado)
