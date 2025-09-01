"""
Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""
# Variable para cambiar cantidad de numeros facilmente
CANTIDAD_NUMEROS = 10

def ej8():
    # Inicializa contadores para cada categoria
    pares = impares = positivos = negativos = 0

    # Solicita la cantidad especificada de numeros
    for _ in range(CANTIDAD_NUMEROS):
        numero = int(input("Ingrese un numero entero: "))
        
        # Clasifica el numero como par o impar
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        
        # Clasifica el numero como positivo o negativo
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1

    # Muestra los resultados finales
    print(f"Numeros pares: {pares}")
    print(f"Numeros impares: {impares}")
    print(f"Numeros positivos: {positivos}")
    print(f"Numeros negativos: {negativos}")

if __name__ == "__main__":
    ej8()
