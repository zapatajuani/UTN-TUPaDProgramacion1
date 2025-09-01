"""
Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""


# Variable para cambiar cantidad de numeros facilmente
CANTIDAD_NUMEROS = 10

def ej9():
    # Inicializa suma acumulativa
    suma = 0

    # Solicita la cantidad especificada de numeros
    for _ in range(CANTIDAD_NUMEROS):
        numero = int(input("Ingrese un numero entero: "))
        # Suma cada numero al acumulador
        suma += numero

    # Calcula la media dividiendo suma por cantidad
    media = suma / CANTIDAD_NUMEROS
    print(f"La media de los numeros ingresados es: {media}")


if __name__ == "__main__":
    ej9()
