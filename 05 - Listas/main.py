import random
import os


def ej1():
    """
    Crear una lista con las notas de 10 estudiantes.
        • Mostrar la lista completa.
        • Calcular y mostrar el promedio.
        • Indicar la nota más alta y la más baja.
    """

    notas = [
        3, 5, 6, 8, 2, 5, 8, 9, 2, 6
    ]

    for i, nota in enumerate(notas):
        print(f"Nota {i+1}: {nota}")

    print(f"Promedio de notas: {sum(notas) / len(notas)}")
    print(f"Notas mas alta: {max(notas)}")
    print(f"Nota mas baja: {min(notas)}")


def ej2():
    """
    Pedir al usuario que cargue 5 productos en una lista.
        • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
        • Preguntar al usuario qué producto desea eliminar y actualizar la lista.
    """

    productos: list[str] = []

    while len(productos) < 5:
        producto = input("Ingrese un producto a su canasta: ")
        productos.append(producto)

    productos = sorted(productos)

    for prod in productos:
        print(f"Producto {productos.index(prod)+1}: {prod}")

    while True:
        remove = input("Ingrese que producto quiere eliminar: ")
        if remove in productos:
            productos.remove(remove)
            break
        else:
            print("El producto no existe en la lista")

    for prod in productos:
        print(f"Producto {productos.index(prod)+1}: {prod}")


def ej3():
    """
    Generar una lista con 15 números enteros al azar entre 1 y 100.
        • Crear una lista con los pares y otra con los impares.
        • Mostrar cuántos números tiene cada lista
    """
    numeros: list[int] = []
    while len(numeros) < 15:
        numeros.append(random.randint(1, 100))

    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]

    print(f"Lista original: {numeros}")

    print(f"Total numeros pares:   {len(pares)}")
    print(f"Total numeros impares: {len(impares)}")


def ej4():
    """
    Dada una lista con valores repetidos:

        datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

        • Crear una nueva lista sin elementos repetidos.
        • Mostrar el resultado.
    """
    datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

    filtrado = [datos[i]
                for i in range(len(datos)) if datos[i] not in (datos[0:i] + datos[i+1:])]

    print(f"Array filtrado: {filtrado}")


def ej5():
    """
    Crear una lista con los nombres de 8 estudiantes presentes en clase.
        • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
        • Mostrar la lista final actualizada
    """

    estudiantes = [
        "Ana", "Luis", "Carlos", "Marta",
        "Sofía", "Jorge", "Lucía", "Diego"
    ]

    while True:
        action = input(
            "Que accion desea realiar?\n[1] - Agregar\n[2] - Eliminar\n")

        if action == "1":
            nombre = input("Ingrese el nombre: ")
            estudiantes.append(nombre)
            break

        if action == "2":
            nombre = input("Ingrese el nombre: ")
            if nombre in estudiantes:
                estudiantes.remove(nombre)
                break

            print("El nombre no existe en la lista")

    print("Lista final: ")
    for nombre in estudiantes:
        print(nombre)


def ej6():
    """
    Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
    último pasa a ser el primero).
    """

    numeros = [1, 2, 3, 4, 5, 6, 7]

    print("Lista orginal: ")
    print(numeros)

    last_number = numeros.pop()
    numeros.insert(0, last_number)

    print("Lista rotada: ")
    print(numeros)


def ej7():
    """
    Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
        • Calcular el promedio de las mínimas y el de las máximas.
        • Mostrar en qué día se registró la mayor amplitud térmica.
    """

    temperaturas = [
        [random.randint(10, 20), random.randint(21, 30)] for _ in range(7)
    ]

    dias = [
        "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"
    ]

    promedio_minimas = sum(t_min for t_min, _ in temperaturas) / 7
    promedio_maximas = sum(t_max for _, t_max in temperaturas) / 7
    amplitud_termica = [t_max - t_min for t_min, t_max in temperaturas]

    dia_mayor_amplitud = temperaturas[amplitud_termica.index(
        max(amplitud_termica))]

    for i in range(7):
        print(10*"-" + f" {dias[i]} " + (21-len(dias[i]))*"-")
        if temperaturas[i] == dia_mayor_amplitud:
            print(">>> Dia de mayor amplitud termica <<<")
        print(f"Temperatura minima: {temperaturas[i][0]}")
        print(f"Temperatura maxima: {temperaturas[i][1]}")
        print(f"Amplitud termica:  {amplitud_termica[i]}")

    print(10*"-" + " Promedios " + 10*"-")
    print(f"Promedio temperaturas minimas: {promedio_minimas:.2f}")
    print(f"Promedio temperaturas maximas: {promedio_maximas:.2f}")


def ej8():
    """
    Crear una matriz con las notas de 5 estudiantes en 3 materias.
        • Mostrar el promedio de cada estudiante.
        • Mostrar el promedio de cada materia.
    """

    materias = ["Matematicas", "Historia", "Ciencias"]
    num_estudiantes = 25

    notas_materias = [
        [random.randint(1, 10) for _ in range(len(materias))] for _ in range(num_estudiantes)
    ]

    promedio_estudiantes = [sum(notas)/len(notas) for notas in notas_materias]
    promedio_materia = [sum(nota[i] for nota in notas_materias)/num_estudiantes
                        for i in range(len(materias))]

    for i in range(num_estudiantes):
        print(f"Estudiante {i+1}: ")
        for j in range(len(materias)):
            print(f"{materias[j]}: {notas_materias[i][j]}", end=" | ")
        print(f"Promedio: {promedio_estudiantes[i]:.2f}")
        print(20*"-")

    for i in range(len(materias)):
        print(f"Promedio de {materias[i]}: {promedio_materia[i]:.2f}")


def ej9():
    """
    Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
        • Inicializarlo con guiones "-" representando casillas vacías.
        • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
    """

    tablero = [
        ["-" for _ in range(3)] for _ in range(3)
    ]

    player = "X"
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:

        print("\n    0   1   2  ")
        print("  |-----------|")
        for i in range(3):
            print(
                f"{i} | {tablero[i][0]} | {tablero[i][1]} | {tablero[i][2]} |")
        print("  |-----------|\n")

        count = 0
        for row in tablero:
            count += row.count("-")

        if count == 0:
            print("Se completo el tablero")
            break

        print("'exit' en algun valor para salir")
        col = input("Jugador " + player + " ingrese la columna: ")
        row = input("Jugador " + player + " ingrese la fila: ")

        if col == "exit" or row == "exit":
            break

        if col in ["0", "1", "2"] and row in ["0", "1", "2"]:
            if tablero[int(row)][int(col)] == "-":
                tablero[int(row)][int(col)] = player

                if player == "X":
                    player = "O"
                else:
                    player = "X"

                os.system('cls' if os.name == 'nt' else 'clear')
                continue

            print("Posicion ocupada")
        else:
            print("Dato incorrecto")

        input("\nEnter para continuar")

        os.system('cls' if os.name == 'nt' else 'clear')


def ej10():
    """
    Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
        • Mostrar el total vendido por cada producto.
        • Mostrar el día con mayores ventas totales.
        • Indicar cuál fue el producto más vendido en la semana.
    """

    productos = ["Producto A", "Producto B", "Producto C", "Producto D"]
    dias = ["Lunes", "Martes", "Miercoles",
            "Jueves", "Viernes", "Sabado", "Domingo"]

    ventas = [
        [random.randint(1, 20) for _ in range(len(dias))] for _ in range(len(productos))
    ]

    total_por_producto = [sum(venta) for venta in ventas]
    total_por_dia = [sum(ventas[i][j] for i in range(len(productos)))
                     for j in range(len(dias))]

    dia_mayores_ventas = dias[total_por_dia.index(max(total_por_dia))]
    producto_mas_vendido = productos[total_por_producto.index(
        max(total_por_producto))]

    for i in range(len(productos)):
        print(f"{productos[i]} - Total vendido: {total_por_producto[i]}")

    print(20*"-")
    print(f"Dia con mayores ventas totales: {dia_mayores_ventas}")
    print(f"Producto más vendido en la semana: {producto_mas_vendido}")


if __name__ == "__main__":
    funciones = [
        ej1, ej2, ej3, ej4, ej5,
        ej6, ej7, ej8, ej9, ej10
    ]

    print("Ejercicios de práctica")
    for i, funcion in enumerate(funciones, 1):
        print(f"\n -------- Ej{i} -------- \n")
        funcion()
        input("\nPrecione Enter para continuar")
        os.system('cls' if os.name == 'nt' else 'clear')
