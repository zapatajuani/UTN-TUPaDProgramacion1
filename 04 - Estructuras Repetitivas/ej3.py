"""
Escribe un programa que sume todos los numeros enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
"""

def ej3():
    # Solicita los dos numeros enteros
    numero1 = int(input("Ingrese el primer numero entero: "))
    numero2 = int(input("Ingrese el segundo numero entero: "))

    # Asegura que numero1 sea menor que numero2
    if numero1 > numero2:
        numero1, numero2 = numero2, numero1

    # Inicializa la suma
    suma = 0
    # Suma numeros en el rango excluyendo extremos
    for num in range(numero1 + 1, numero2):
        suma += num

    # Muestra el resultado
    print(f"La suma de los numeros entre {numero1} y {numero2} es: {suma}")

if __name__ == "__main__":
    ej3()
