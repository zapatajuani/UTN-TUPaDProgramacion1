"""
Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""

def ej7():
    # Solicita numero entero positivo al usuario
    numero = int(input("Ingrese un numero entero positivo: "))
    # Inicializa suma acumulativa
    suma = 0

    # Suma todos los numeros de 0 al numero ingresado
    for num in range(numero + 1):
        suma += num

    # Muestra el resultado final
    print(f"La suma de los numeros entre 0 y {numero} es: {suma}")  

if __name__ == "__main__":
    ej7()
