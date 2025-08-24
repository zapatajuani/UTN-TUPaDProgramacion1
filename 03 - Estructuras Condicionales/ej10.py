"""
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano.
"""

# El usuario ingresa el hemisferio, mes y día
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

# Verificamos la estación según el hemisferio, mes y día
if hemisferio != 'N' and hemisferio != 'S':
    # Manejo de hemisferio inválido
    print("Hemisferio no válido")
elif mes < 1 or mes > 12 or dia < 1 or dia > 31:
    # Manejo de fecha inválida
    print("Fecha no válida")
else:
    if hemisferio == 'N':
        # Hemisferio Norte
        if (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20):
            estacion = "Invierno"
        elif (mes > 3 and mes <= 5) or ((mes == 3 and dia >= 21) or (mes == 6 and dia <= 20)):
            estacion = "Primavera"
        elif (mes > 6 and mes <= 8) or ((mes == 6 and dia >= 21) or (mes == 9 and dia <= 20)):
            estacion = "Verano"
        else:
            estacion = "Otoño"
    else:
        # Hemisferio Sur
        if (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20):
            estacion = "Verano"
        elif (mes > 3 and mes <= 5) or ((mes == 3 and dia >= 21) or (mes == 6 and dia <= 20)):
            estacion = "Otoño"
        elif (mes > 6 and mes <= 8) or ((mes == 6 and dia >= 21) or (mes == 9 and dia <= 20)):
            estacion = "Invierno"
        else:
            estacion = "Primavera"

    # Imprimimos la estación
    print("Estación:", estacion)
