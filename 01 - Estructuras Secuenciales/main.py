print("----------------------- EJERCICIO 1 -------------------------")
print("Hola Mundo!")

print("----------------------- EJERCICIO 2 -------------------------")
nombre = input("Como te llamas? ")
print(f"Hola, {nombre}!")

print("----------------------- EJERCICIO 3 -------------------------")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

print("----------------------- EJERCICIO 4 -------------------------")
radio = float(input("Ingrese el radio del circulo: "))
area = 3.14159 * radio**2
print(f"El area del circulo es: {area}")

print("----------------------- EJERCICIO 5 -------------------------")
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas")

print("----------------------- EJERCICIO 6 -------------------------")
numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

print("----------------------- EJERCICIO 7 -------------------------")
num1 = int(input("Ingrese el primer numero entero distinto de 0: "))
num2 = int(input("Ingrese el segundo numero entero distinto de 0: "))
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicacion: {num1 * num2}")
print(f"Division: {num1 / num2}")

print("----------------------- EJERCICIO 8 -------------------------")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Su indice de masa corporal es: {imc}")

print("----------------------- EJERCICIO 9 -------------------------")
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print(f"{celsius}C equivalen a {fahrenheit}F")

print("----------------------- EJERCICIO 10 -------------------------")
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres numeros es: {promedio}")