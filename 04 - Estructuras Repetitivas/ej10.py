"""
Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""


def ej10():
    # Solicita numero como string para poder invertirlo
    numero = input("Ingrese un numero entero: ")
    # Inicializa string para almacenar numero invertido
    numero_invertido = ""
    # Recorre el string en orden inverso
    for digito in numero[::-1]:
        # Concatena cada digito al resultado
        numero_invertido = numero_invertido + digito
    # Muestra el numero invertido
    print(f"El numero invertido es: {numero_invertido}")


if __name__ == "__main__":
    ej10()
