import os
import random
import string

# -------------------------------------------


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
    Elimina espacios y puntuacion al inicio y final del string. 
    Pone en minusculas por default.
    
    Args:
        valor (str): string a limpiar.
        minusculas (bool, optional): convierte a minusculas. Defaults to True.
    """
    resultado = valor.strip().strip(string.punctuation)
    if minusculas:
        resultado = resultado.lower()
    return resultado

def correct_hour_format(hour: str) -> bool:
    """verifica que la hora este en formato HH:MM y sea valida."""
    if len(hour) != 5 or hour[2] != ':':
        return False
    hh, mm = hour.split(':')
    if not (hh.isdigit() and mm.isdigit()):
        return False
    hh_int = int(hh)
    mm_int = int(mm)
    return 0 <= hh_int < 24 and 0 <= mm_int < 60

# -------------------------------------------


def ejecutar_ejercicio_1(frutas_dict):
    """anade frutas al diccionario de precios."""
    print(f"Diccionario actual: {frutas_dict}")
    frutas_dict['Naranja'] = 1200
    frutas_dict['Manzana'] = 3500
    frutas_dict['Pera'] = 2300
    print(f"Diccionario actualizado: {frutas_dict}")


def ejecutar_ejercicio_2(frutas_dict):
    """actualiza precios de frutas existentes."""
    print(f"Diccionario actual: {frutas_dict}")
    frutas_dict['Banana'] = 1330
    frutas_dict['Manzana'] = 1700
    frutas_dict['Melon'] = 2800
    print(f"Diccionario actualizado: {frutas_dict}")


def ejecutar_ejercicio_3(frutas_dict):
    """crea una lista solo con las claves (frutas)."""
    frutas = list(frutas_dict.keys())
    print(f"Lista de frutas: {frutas}")


def ejecutar_ejercicio_4():
    """gestiona una agenda de numeros telefonicos."""
    agenda = {}
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Que desea hacer?")
        print("1. Añadir contacto")
        print("2. Buscar contacto")
        print("3. Salir")
        opcion = input("Ingrese el numero de la opcion: ")
        print("\n--------------------------------------------------\n")

        match opcion:
            case "1":
                nombre = input("Ingrese el nombre del contacto: ")
                numero = input("Ingrese el numero de telefono: ")

                if not nombre or not numero:
                    print("Nombre y numero no pueden estar vacios.")

                elif not es_entero_valido(numero):
                    print("Numero invalido. Debe ser un numero entero.")

                elif len(agenda.keys()) >= 5:
                    print("Agenda llena. No se pueden anadir mas contactos.")

                elif format_clean_string(nombre) in agenda:
                    agenda[format_clean_string(nombre)] = numero
                    print(f"Contacto {nombre} actualizado.")
                
                else:
                    agenda[format_clean_string(nombre)] = numero
                    print(f"Contacto {format_clean_string(nombre).title()} añadido.")
            case "2":
                nombre = input("Ingrese el nombre del contacto a buscar: ")
                if not nombre:
                    print("Ingrese un nombre valido.")
                elif format_clean_string(nombre) in agenda:
                    print(f"Numero de {format_clean_string(nombre).title()}: {agenda[format_clean_string(nombre)]}")
                else:
                    print(f"Contacto {format_clean_string(nombre).title()} no encontrado.")
            case "3":
                break
            case _:
                print("Opcion no valida. Intente de nuevo.")

        print("\n--------------------------------------------------\n")
        input("Presiona Enter para continuar...")


def ejecutar_ejercicio_5():
    """analiza una frase, muestra unicas y recuento."""
    frase = input("Ingrese una frase: ")

    if not frase:
        print("Frase vacia. No se puede analizar.")
        return

    palabras = [format_clean_string(palabra) for palabra in frase.split()]
    palabras_unicas = set(palabras)
    cantidad_palabras = {}
    for palabra in palabras:
        if palabra in cantidad_palabras:
            cantidad_palabras[palabra] += 1
        else:
            cantidad_palabras[palabra] = 1

    print(f"Palabras unicas: {palabras_unicas}")
    print(f"Recuento de palabras: {cantidad_palabras}")


def ejecutar_ejercicio_6():
    """gestiona alumnos y el promedio de sus notas."""
    alumnos_dict = {}
    i = 0
    while i < 3:
        alumno = input("Ingrese el nombre del alumno: ")
        if not alumno:
            print("El nombre del alumno no puede estar vacio.")
            continue
        if format_clean_string(alumno) in alumnos_dict:
            print("El alumno ya existe. Ingrese otro nombre.")
            continue
        if any(char.isdigit() for char in alumno):
            print("El nombre del alumno no puede contener numeros.")
            continue

        notas = []
        while True:
            nota = input(
                f"Ingrese la nota {len(notas) + 1} del alumno (0-10): ")
            if not es_decimal_valido(nota):
                print("Nota invalida. Debe ser un numero decimal.")
                continue
            nota_float = float(nota)
            if nota_float < 0 or nota_float > 10:
                print("Nota fuera de rango. Debe estar entre 0 y 10.")
                continue

            notas.append(nota_float)
            if len(notas) == 3:
                break

        alumnos_dict[format_clean_string(alumno).title()] = tuple(notas)
        i += 1

    for alumno, notas in alumnos_dict.items():
        promedio = sum(notas) / len(notas)
        print(f"Alumno: {alumno}, Notas: {notas}, Promedio: {promedio:.2f}")


def ejecutar_ejercicio_7():
    """muestra operaciones con sets de parciales."""
    UNIVERSO_ALUMNOS = 10
    parcial_1 = {random.randint(1, 10) for _ in range(0, UNIVERSO_ALUMNOS)}
    parcial_2 = {random.randint(1, 10) for _ in range(0, UNIVERSO_ALUMNOS)}

    print(f"Cantidad total de alumnos: {UNIVERSO_ALUMNOS}")
    print(f"Alumnos que aprobaron parcial 1: {parcial_1}")
    print(f"Alumnos que aprobaron parcial 2: {parcial_2}")
    print(f"Alumnos que aprobaron ambos parciales: {parcial_1.intersection(parcial_2)}")
    print(f"Alumnos que aprobaron solo uno de los parciales: {parcial_1.symmetric_difference(parcial_2)}")
    print(f"Alumnos que aprobaron al menos un parcial: {parcial_1.union(parcial_2)}")


def ejecutar_ejercicio_8():
    """gestiona el stock de productos."""
    stock = {
        'manzana': 50,
        'banana': 30,
        'naranja': 40
    }

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Que desea hacer?")
        print("1. Ver stock")
        print("2. Añadir stock")
        print("3. Añadir producto")
        print("4. Salir")
        opcion = input("Ingrese el numero de la opcion: ")
        print("\n--------------------------------------------------\n")

        match opcion:
            case "1":
                print(f"Stock actual: {stock}")
            case "2":
                producto = input("Ingrese el nombre del producto: ")
                cantidad = input("Ingrese la cantidad a añadir: ")
                if format_clean_string(producto) not in stock:
                    print("Producto no existe en el stock.")  
                elif not es_entero_valido(cantidad) or int(cantidad) <= 0:
                    print("Cantidad invalida. Debe ser un entero positivo.")
                else:
                    stock[format_clean_string(producto)] += int(cantidad)
                    print(f"Stock actualizado: {stock}")
            case "3":
                producto = input("Ingrese el nombre del nuevo producto: ")
                cantidad = input("Ingrese la cantidad inicial: ")
                if not producto:
                    print("El nombre del producto no puede estar vacio.")
                elif format_clean_string(producto) in stock:
                    print("El producto ya existe en el stock.")
                elif not es_entero_valido(cantidad) or int(cantidad) < 0:
                    print("Cantidad invalida. Debe ser un entero no negativo.")
                else:   
                    stock[format_clean_string(producto)] = int(cantidad)
                    print(f"Producto {format_clean_string(producto)} añadido al stock.")
            case "4":
                break
            case _:
                print("Opcion no valida. Intente de nuevo.")

        print("\n--------------------------------------------------\n")
        input("Presiona Enter para continuar...")


def ejecutar_ejercicio_9():
    """consulta la agenda por dia y hora."""
    agenda: dict[tuple[str, str], str] = {}
    DIAS = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Que desea hacer?")
        print("1. Anadir evento")
        print("2. Consultar evento")
        print("3. Salir")
        opcion = input("Ingrese el numero de la opcion: ")
        print("\n--------------------------------------------------\n")

        match opcion:
            case "1":
                dia = input("Ingrese el dia del evento (e.g., Lunes): ")
                hora = input("Ingrese la hora del evento (e.g., 14:00): ")
                descripcion = input("Ingrese la descripcion del evento: ")

                if not dia or not hora or not descripcion:
                    print("Dia, hora y descripcion no pueden estar vacios.")
                elif format_clean_string(dia) not in DIAS:
                    print("Dia invalido. Ingrese un dia de la semana valido.")
                elif not correct_hour_format(hora):
                    print("Formato de hora invalido. Use HH:MM en formato 24 horas.")
                elif (format_clean_string(dia), hora) in agenda:
                    print(f"Ya existe un evento programado para {format_clean_string(dia).title()} a las {hora}.")
                else:
                    agenda[(format_clean_string(dia), hora)] = descripcion
                    print(f"Evento anadido para {format_clean_string(dia).title()} a las {hora}.")

            case "2":
                dia = input("Ingrese el dia del evento a consultar: ")
                hora = input("Ingrese la hora del evento a consultar: ")

                if format_clean_string(dia) == "":
                    print("Dia no puede estar vacio.")

                elif format_clean_string(dia) not in DIAS:
                    print("Dia invalido. Ingrese un dia de la semana valido.")

                elif hora and not correct_hour_format(hora):
                    print("Formato de hora invalido. Use HH:MM en formato 24 horas.")
                
                elif format_clean_string(dia) in [d[0] for d in agenda.keys()]:
                    eventos_dia = {h: desc for (d, h), desc in agenda.items() if d == format_clean_string(dia)}
                    if eventos_dia:
                        print(f"Eventos para {dia.title()}:")
                        for h, desc in eventos_dia.items():
                            print(f" - A las {h}: {desc}")
                    else:
                        print(f"No hay eventos programados para {dia.title()}.")

                elif (format_clean_string(dia), hora) in agenda:
                    print(f"Evento en {dia.title()} a las {hora}: {agenda[(format_clean_string(dia), hora)]}")
                else:
                    print(f"No hay eventos programados para {dia.title()} a las {hora}.")
            
            case "3":
                break
            case _:
                print("Opcion no valida. Intente de nuevo.")

        print("\n--------------------------------------------------\n")
        input("Presiona Enter para continuar...")


def ejecutar_ejercicio_10():
    """invierte un diccionario de paises y capitales."""
    paises_capitales = {}

    while True:
        pais = input("Ingrese el nombre del pais (o deje vacio para terminar): ")
        if not pais:
            break
        capital = input(f"Ingrese la capital de {pais}: ")
        if not capital:
            print("La capital no puede estar vacia.")
            continue
        paises_capitales[format_clean_string(pais).title()] = format_clean_string(capital).title()

    print()
    print("Diccionario original (Paises y Capitales): {")
    for pais, capital in paises_capitales.items():
        print(f"'{pais}': '{capital}'")
    print("}")

    capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

    print()
    print("Diccionario invertido (Capitales y Paises): {")
    for capital, pais in capitales_paises.items():
        print(f"'{capital}': '{pais}'")
    print("}")


# -------------------------------------------


def main():
    """funcion principal que ejecuta el menu interactivo."""

    precios_frutas = {
        'Banana': 1200,
        'Anana': 2500,
        'Melon': 3000,
        'Uva': 1450
    }

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Cual ejercicio quieres ejecutar?")
        print("0. Salir")
        print("1. Anadir frutas al diccionario")
        print("2. Actualizar precios de frutas")
        print("3. Crear lista de frutas")
        print("4. Agenda de numeros telefonicos")
        print("5. Analizador de frases")
        print("6. Promedio de alumnos")
        print("7. Operaciones con sets (parciales)")
        print("8. Gestion de stock")
        print("9. Consultar agenda de eventos")
        print("10. Invertir diccionario (paises y capitales)")

        eleccion = input("Ingresa el numero del ejercicio: ")
        print("\n--------------------------------------------------\n")

        match eleccion:
            case "0":
                break
            case "1":
                ejecutar_ejercicio_1(precios_frutas)
            case "2":
                ejecutar_ejercicio_2(precios_frutas)
            case "3":
                ejecutar_ejercicio_3(precios_frutas)
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
            case "9":
                ejecutar_ejercicio_9()
            case "10":
                ejecutar_ejercicio_10()
            case _:
                print("Opcion no valida. Intenta de nuevo.")

        print("\n--------------------------------------------------\n")
        input("Presiona Enter para continuar...")


if __name__ == "__main__":
    main()
