import os


def imprimir_hola_mundo():
    """imprime 'hola mundo!' por pantalla."""
    print("Hola mundo!")


def saludar_usuario(nombre):
    """recibe un nombre como parametro y devuelve un saludo personalizado."""
    return f"Hola, {nombre}!"


def informacion_personal(nombre, apellido, edad, residencia):
    """recibe nombre, apellido, edad y residencia e imprime un mensaje."""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


def calcular_area_circulo(radio):
    """recibe el radio de un circulo y devuelve su area."""
    return 3.141592 * radio ** 2


def calcular_perimetro_circulo(radio):
    """recibe el radio de un circulo y devuelve su perimetro."""
    return 2 * 3.141592 * radio


def segundos_a_horas(segundos):
    """recibe segundos y devuelve la cantidad equivalente en horas."""
    horas = segundos / 3600
    return horas


def tabla_multiplicar(numero):
    """recibe un numero e imprime su tabla de multiplicar del 1 al 10."""

    if float(numero) - int(numero) != 0:
        print("Por favor, ingresa un número entero para la tabla de multiplicar.")
        return
    
    for i in range(1, 11):
        print(f"{int(numero)} x {i} = {int(numero) * i}")


def operaciones_basicas(a, b):
    """recibe dos numeros (a, b) y devuelve una tupla con la suma, resta, multiplicacion y division."""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido (división por cero)"
    return (suma, resta, multiplicacion, division)


def calcular_imc(peso, altura):
    """recibe peso (kg) y altura (m) y devuelve el indice de masa corporal (imc)."""
    imc = peso / (altura ** 2)
    return imc


def celsius_a_fahrenheit(celsius):
    """recibe grados celsius y los convierte a grados fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def calcular_promedio(a, b, c):
    """recibe tres numeros y devuelve su promedio."""
    promedio = (a + b + c) / 3
    return promedio


def comprobar_numero(valor: str) -> bool:
    """Comprueba si el valor es un número válido (entero o decimal)."""
    if not valor:
        return False

    if valor[0] == '-' and len(valor) > 1:
        valor = valor[1:]

    if '.' in valor and valor.replace('.', '', 1).isdigit():
        return True

    if valor.isdigit():
        return True

    return False


def main():
    """funcion principal que ejecuta el menu interactivo."""
    while True:

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Cual ejercicio quieres ejecutar?")
        print("0. Salir")
        print("1. Imprimir Hola Mundo")
        print("2. Saludar a un usuario")
        print("3. Mostrar información personal")
        print("4. Calcular área y perímetro de un círculo")
        print("5. Convertir segundos a horas")
        print("6. Mostrar tabla de multiplicar")
        print("7. Operaciones básicas")
        print("8. Calcular índice de masa corporal (IMC)")
        print("9. Convertir Celsius a Fahrenheit")
        print("10. Calcular promedio de tres números")
        eleccion = input("\nIngresa el número del ejercicio: ")
        print("\n--------------------------------------------------\n")

        match eleccion:
            case "0":
                break

            case "1":
                imprimir_hola_mundo()

            case "2":
                nombre = input("Ingresa tu nombre: ")
                print(saludar_usuario(nombre))

            case "3":
                nombre = input("Ingresa tu nombre: ")
                apellido = input("Ingresa tu apellido: ")
                edad = input("Ingresa tu edad: ")
                residencia = input("Ingresa tu lugar de residencia: ")

                if not edad.isdigit():
                    print("Por favor, ingresa una edad válida.")
                elif not nombre or not apellido or not residencia:
                    print("Por favor, completa todos los campos.")
                else:
                    informacion_personal(nombre, apellido, edad, residencia)

            case "4":
                radio = input("Ingresa el radio del círculo: ")

                if not comprobar_numero(radio):
                    print("Por favor, ingresa un número válido para el radio.")
                else:
                    radio = float(radio)
                    area = calcular_area_circulo(radio)
                    perimetro = calcular_perimetro_circulo(radio)
                    print(f"El área del círculo es: {area:.2f}")
                    print(f"El perímetro del círculo es: {perimetro:.2f}")

            case "5":
                segundos = input("Ingresa la cantidad de segundos: ")

                if not comprobar_numero(segundos):
                    print("Por favor, ingresa un número válido para los segundos.")
                else:
                    segundos = float(segundos)
                    horas = segundos_a_horas(segundos)
                    print(f"{segundos} segundos son {horas:.2f} horas.")

            case "6":
                numero = input(
                    "Ingresa el número para la tabla de multiplicar: ")

                if not comprobar_numero(numero):
                    print(
                        "Por favor, ingresa un número válido para la tabla de multiplicar.")
                else:
                    numero = float(numero)
                    tabla_multiplicar(numero)

            case "7":
                a = input("Ingresa el primer número: ")
                b = input("Ingresa el segundo número: ")

                if not (comprobar_numero(a) and comprobar_numero(b)):
                    print("Por favor, ingresa números válidos.")
                else:
                    a = float(a)
                    b = float(b)
                    resultados = operaciones_basicas(a, b)
                    print(f"Suma: {resultados[0]}")
                    print(f"Resta: {resultados[1]}")
                    print(f"Multiplicación: {resultados[2]}")
                    print(f"División: {resultados[3]}")

            case "8":
                peso = input("Ingresa tu peso en kilogramos: ")
                altura = input("Ingresa tu altura en metros: ")

                if not (comprobar_numero(peso) and comprobar_numero(altura)):
                    print("Por favor, ingresa números válidos.")
                else:
                    peso = float(peso)
                    altura = float(altura)
                    imc = calcular_imc(peso, altura)
                    print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

            case "9":
                celsius = input("Ingresa la temperatura en Celsius: ")
                if not comprobar_numero(celsius):
                    print("Por favor, ingresa un número válido para la temperatura.")
                else:
                    celsius = float(celsius)
                    fahrenheit = celsius_a_fahrenheit(celsius)
                    print(
                        f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit.")

            case "10":
                a = input("Ingresa el primer número: ")
                b = input("Ingresa el segundo número: ")
                c = input("Ingresa el tercer número: ")

                if not (
                    comprobar_numero(a) and (
                        comprobar_numero(b)) and (
                            comprobar_numero(c))
                ):
                    print("Por favor, ingresa números válidos.")
                else:
                    a = float(a)
                    b = float(b)
                    c = float(c)
                    promedio = calcular_promedio(a, b, c)
                    print(
                        f"El promedio de los tres números es: {promedio:.2f}")

            case _:
                print("Opción no válida.")

        print("\n--------------------------------------------------\n")
        input("Presiona Enter para continuar...")


if __name__ == "__main__":
    main()
