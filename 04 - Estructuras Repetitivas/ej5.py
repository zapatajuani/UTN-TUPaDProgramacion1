"""
Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
import random


def ej5():
    # Genera numero aleatorio entre 0 y 9
    numero_aleatorio = random.randint(0, 9)
    # Inicializa contador de intentos
    intentos = 0
    # Bandera para controlar si ya adivino
    adivinado = False

    # Continua hasta que adivine el numero
    while not adivinado:
        # Solicita intento al usuario
        intento = int(input("Adivina el numero (entre 0 y 9): "))
        # Incrementa contador de intentos
        intentos += 1
        # Verifica si el intento es correcto
        if intento == numero_aleatorio:
            adivinado = True
            print(f"Felicidades! Adivinaste el numero {numero_aleatorio} en {intentos} intentos.")
        else:
            print("Numero incorrecto. Intenta de nuevo.")


if __name__ == "__main__":
    ej5()
