"""
Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
    ● Niño/a: menor de 12 años.
    ● Adolescente: mayor o igual que 12 años y menor que 18 años.
    ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
    ● Adulto/a: mayor o igual que 30 años.
"""

# El usuario ingresa su edad
edad = int(input("Ingrese su edad: "))

# Verificamos a qué categoría pertenece
if edad < 0:
    # Manejo de edad negativa
    print("Edad no válida")
elif edad < 12:
    # Si es menor de 12, es niño/a
    print("Niño/a")
elif edad < 18:
    # Si es mayor o igual a 12 y menor de 18, es adolescente
    print("Adolescente")
elif edad < 30:
    # Si es mayor o igual a 18 y menor de 30, es adulto/a joven
    print("Adulto/a joven")
else:
    # Si es mayor o igual a 30, es adulto/a
    print("Adulto/a")
