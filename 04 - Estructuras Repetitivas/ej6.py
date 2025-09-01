"""
Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
"""

def ej6():
    # Recorre numeros de 100 a 0 en orden decreciente
    for numero in range(100, -1, -1):
        # Verifica si el numero es par
        if numero % 2 == 0:
            # Imprime el numero par seguido de espacio
            print(numero, end=" ")
    # Agrega salto de linea al final
    print()

if __name__ == "__main__":
    ej6()
