"""
Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""

def ej4():
    # Inicializa suma acumulativa
    suma = 0

    # Bucle infinito hasta que se ingrese 0
    while True:
        # Solicita numero al usuario
        numero = int(input("Ingrese un numero entero (0 para finalizar): "))
        # Si es 0, termina el bucle
        if numero == 0:
            break
        # Suma el numero al acumulador
        suma += numero

    # Muestra el total acumulado
    print(f"La suma total es: {suma}")

if __name__ == "__main__":
    ej4()
