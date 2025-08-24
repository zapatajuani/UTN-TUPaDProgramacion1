"""
Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”
"""

# El usuario ingresa su nota
nota = float(input("Ingrese su nota: "))

# Verificamos si aprobó o desaprobó
if nota < 0 or nota > 10:
    # Manejo de nota inválida
    print("Nota no válida")
elif nota >= 6:
    # Si la nota es mayor o igual a 6, aprobó
    print("Aprobado")
else:
    # Si la nota es menor a 6, desaprobó
    print("Desaprobado")
