"""
Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
"""
def ej1():
    # Recorre numeros del 0 al 100 usando range(101)
    for numero in range(101):
        # Imprime cada numero seguido de un espacio
        print(numero, end=" ")
    # Agrega salto de linea al final
    print()

if __name__ == "__main__":
    ej1()
