"""
Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
"""
def ej2():
    # Inicializa contador de digitos
    digitos = 0
    # Solicita numero al usuario como string
    numero = input("Ingrese un numero entero: ")

    # Recorre cada caracter del string
    for char in numero:
        # Verifica si el caracter es un digito
        if char.isdigit():
            # Incrementa contador
            digitos += 1
    
    # Muestra resultado final
    print(f"El numero tiene {digitos} digitos.")

if __name__ == "__main__":
    ej2()
