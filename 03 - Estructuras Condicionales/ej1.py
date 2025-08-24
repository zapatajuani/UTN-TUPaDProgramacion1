"""
Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
"""

# El usuario ingresa su edad
edad = int(input("Ingrese su edad: "))

# Verificamos si es mayor de edad
if edad < 0:
    # Manejo de edad negativa
    print("Edad no válida")
elif edad > 18:
    # Si es mayor de 18, mostramos el mensaje
    print("Es mayor de edad")
else:
    # Si no es mayor de 18, mostramos otro mensaje
    print("No es mayor de edad")
