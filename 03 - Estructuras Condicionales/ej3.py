"""
Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar.
"""

# El usuario ingresa un número
numero = int(input("Ingrese un número: "))

# Verificamos si el número es par
if numero % 2 == 0:
    # Si es par, mostramos el mensaje correspondiente
    print("Ha ingresado un número par")
else:
    # Si no es par, mostramos otro mensaje
    print("Por favor, ingrese un número par")
