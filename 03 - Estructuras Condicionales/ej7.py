"""
Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.
"""

# El usuario ingresa una frase o palabra
frase = input("Ingrese una frase o palabra: ")

letra_final = frase[-1].lower()

# Verificamos si la frase termina con una vocal
if letra_final == 'a' or letra_final == 'e' or letra_final == 'i' or letra_final == 'o' or letra_final == 'u':
    # Si termina con vocal, añadimos un signo de exclamación
    frase += '!'

# Imprimimos el resultado
print(frase)
