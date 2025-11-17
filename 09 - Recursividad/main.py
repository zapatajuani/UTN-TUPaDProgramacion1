import os
import string

# --- funciones de validacion ---


def es_entero_valido(valor: str) -> bool:
    """
    comprueba si el string es un numero entero valido (positivo o negativo).
    no acepta decimales.
    """
    if not valor:
        return False
    if valor[0] == '-':
        valor = valor[1:]
        if not valor:
            return False
    return valor.isdigit()


def es_decimal_valido(valor: str) -> bool:
    """
    comprueba si el string es un numero decimal o entero valido
    (positivo o negativo).
    """
    if not valor:
        return False
    if valor[0] == '-':
        valor = valor[1:]
        if not valor:
            return False
    return valor.replace('.', '', 1).isdigit()


def format_clean_string(valor: str, minusculas: bool = True) -> str:
    """
    elimina espacios y puntuacion al inicio y final del string.
    pone en minusculas por default.
    """
    resultado = valor.strip().strip(string.punctuation)
    if minusculas:
        resultado = resultado.lower()
    return resultado

# --- funciones recursivas ---


def factorial(n: int) -> int:
    """calcula el factorial de n recursivamente."""
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """calcula el n-esimo numero de fibonacci recursivamente."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def potencia(base: float, exponente: int) -> float:
    """calcula la potencia recursivamente."""
    if exponente == 0:
        return 1
    if exponente < 0:
        return 1 / potencia(base, -exponente)
    return base * potencia(base, exponente - 1)

def decimal_a_binario(n: int) -> str:
    """convierte un numero decimal a binario recursivamente."""
    n = int(n)
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)

def es_palindromo(palabra: str) -> bool:
    """comprueba si una palabra es palindromo recursivamente."""
    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    return False


def suma_digitos(n: int) -> int:
    """suma los digitos de un numero recursivamente."""
    n = abs(int(n))
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)


def contar_bloques(n: int) -> int:
    """cuenta los bloques de una piramide recursivamente."""
    n = int(n)
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

def contar_digito(numero: int, digito: int) -> int:
    """cuenta cuantas veces aparece un digito en un numero."""
    numero = abs(int(numero))
    digito = abs(int(digito))

    if numero < 10:
        return 1 if numero == digito else 0
    return (1 if (numero % 10) == digito else 0) + contar_digito(numero // 10, digito)

# --- funciones de ejecucion (menu) ---


def ejecutar_ejercicio_1():
    """pide un numero y muestra factoriales hasta ese numero."""
    num_str = input("ingresa un numero entero positivo: ")

    if not es_entero_valido(num_str) or int(num_str) < 0:
        print("entrada invalida. debe ser un numero entero positivo.")
        return

    n = int(num_str)
    if n == 0:
        print("el factorial de 0 es 1")
        return

    print(f"calculando factoriales de 1 a {n}:")
    for i in range(1, n + 1):
        print(f"  factorial de {i} es: {factorial(i)}")


def ejecutar_ejercicio_2():
    """pide un numero y muestra la serie de fibonacci."""
    num_str = input("ingresa hasta que posicion de fibonacci mostrar: ")

    if not es_entero_valido(num_str) or int(num_str) < 0:
        print("entrada invalida. debe ser un numero entero positivo.")
        return

    n = int(num_str)
    print(f"serie de fibonacci hasta la posicion {n}:")
    for i in range(n + 1):
        print(f"  fib({i}) = {fibonacci(i)}")


def ejecutar_ejercicio_3():
    """pide base y exponente y calcula la potencia."""
    base_str = input("ingresa el numero base (puede ser decimal): ")
    exp_str = input("ingresa el exponente (entero): ")

    if not es_decimal_valido(base_str) or not es_entero_valido(exp_str):
        print("datos invalidos. la base debe ser un numero y el exponente un entero.")
        return

    base = float(base_str)
    exponente = int(exp_str)
    resultado = potencia(base, exponente)
    print(f"{base} elevado a {exponente} es: {resultado}")


def ejecutar_ejercicio_4():
    """pide un numero decimal y lo convierte a binario."""
    num_str = input("ingresa un numero entero positivo: ")

    if not es_entero_valido(num_str) or int(num_str) < 0:
        print("entrada invalida. debe ser un numero entero positivo.")
        return

    n = int(num_str)
    resultado = decimal_a_binario(n)
    print(f"el numero {n} en binario es: {resultado}")


def ejecutar_ejercicio_5():
    """pide una palabra y comprueba si es palindromo."""
    palabra_input = input("ingresa una palabra (sin espacios ni acentos): ")

    palabra = format_clean_string(palabra_input, minusculas=True)

    if not palabra:
        print("entrada invalida.")
        return

    if es_palindromo(palabra):
        print(f"'{palabra}' si es un palindromo.")
    else:
        print(f"'{palabra}' no es un palindromo.")


def ejecutar_ejercicio_6():
    """pide un numero y suma sus digitos."""
    num_str = input("ingresa un numero entero positivo: ")

    if not es_entero_valido(num_str):
        print("entrada invalida.")
        return

    n = int(num_str)
    resultado = suma_digitos(n)
    print(f"la suma de los digitos de {n} es: {resultado}")


def ejecutar_ejercicio_7():
    """pide numero de bloques base y calcula el total."""
    num_str = input("ingresa el numero de bloques de la base (n > 0): ")

    if not es_entero_valido(num_str) or int(num_str) <= 0:
        print("entrada invalida. debe ser un entero positivo.")
        return

    n = int(num_str)
    resultado = contar_bloques(n)
    print(f"una piramide con base {n} tiene un total de {resultado} bloques.")


def ejecutar_ejercicio_8():
    """pide un numero y un digito, y cuenta apariciones."""
    num_str = input("ingresa un numero entero positivo: ")
    dig_str = input("ingresa el digito a buscar (0-9): ")

    if not es_entero_valido(num_str) or (
        not es_entero_valido(dig_str)) or (
            len(dig_str) != 1):
        print("datos invalidos. ingresa un numero y un solo digito.")
        return

    numero = int(num_str)
    digito = int(dig_str)
    resultado = contar_digito(numero, digito)
    print(
        f"el digito {digito} aparece {resultado} veces en el numero {numero}.")


def main():
    """funcion principal que ejecuta el menu interactivo."""

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Menu de opciones - tp recursividad")
        print("0. salir")
        print("1. Factoriales de 1 a n")
        print("2. Serie de fibonacci")
        print("3. Potencia recursiva")
        print("4. Decimal a binario")
        print("5. Es palindromo")
        print("6. Suma de digitos")
        print("7. Bloques de la piramide")
        print("8. Contar digito en numero")

        eleccion = input("ingresa el numero de la opcion: ")
        print("\n--------------------------------------------------\n")

        match eleccion:
            case "0":
                break
            case "1":
                ejecutar_ejercicio_1()
            case "2":
                ejecutar_ejercicio_2()
            case "3":
                ejecutar_ejercicio_3()
            case "4":
                ejecutar_ejercicio_4()
            case "5":
                ejecutar_ejercicio_5()
            case "6":
                ejecutar_ejercicio_6()
            case "7":
                ejecutar_ejercicio_7()
            case "8":
                ejecutar_ejercicio_8()
            case _:
                print("opcion no valida. intenta de nuevo.")

        print("\n--------------------------------------------------\n")
        input("presiona enter para continuar...")


if __name__ == "__main__":
    main()
