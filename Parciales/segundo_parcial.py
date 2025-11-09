import csv
import os
import math
import shutil
import time
from datetime import datetime

NOMBRE_ARCHIVO = "catalogo.csv"
LIST_LIMIT = 10


def mensaje_de_bienvenida():
    """muestra un saludo inicial al usuario basado en la hora."""
    hora_actual: int = datetime.now().hour

    if 6 <= hora_actual < 12:
        print("Buenos dias!", end=" ", flush=True)
    elif 12 <= hora_actual < 18:
        print("Buenas tardes!", end=" ", flush=True)
    else:
        print("Buenas noches!", end=" ", flush=True)

    print("Bienvenido al sistema de gestion de libros", end="", flush=True)
    time.sleep(1)

    tiempo_carga = 3

    for _ in range(tiempo_carga):
        print(".", end="", flush=True)
        time.sleep(0.8)
    print("\nListo para comenzar!")
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")


def mensaje_de_salida():
    """muestra un saludo de despedida al usuario."""
    print("\nSaliendo del programa", end="", flush=True)

    tiempo_carga = 3

    for _ in range(tiempo_carga):
        print(".", end="", flush=True)
        time.sleep(0.8)
    print("\nHasta luego!")
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")


def main_display(h: int, w: int) -> None:
    """imprime el menu principal de opciones adaptado al ancho de la consola."""
    print("+" + "-" * (w-2) + "+")
    print("|" + "BIBLIOTECA ESCOLAR UTN".center(w-2) + "|")
    print("+" + "-" * (w-2) + "+")

    menu = [
        "INGRESAR TITULOS           [1]",
        "INGRESAR EJEMPLARES        [2]",
        "MOSTRAR CATALOGO           [3]",
        "CONSULTAR DISPONIBILIDAD   [4]",
        "LISTAR AGOTADOS            [5]",
        "AGREGAR TITULO             [6]",
        "ACTUALIZAR EJEMPLARES      [7]",
        "SALIR                      [8]",
    ]

    for item in menu:
        print("| " + item, end=f"{' ' * (w - len(item) - 4)} |\n")

    print("+" + "-" * (w-2) + "+")


def print_header(titulo: str, w: int):
    """limpia la pantalla e imprime un encabezado estandar."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("+" + "-" * (w-2) + "+")
    print("|" + titulo.center(w-2) + "|")
    print("+" + "-" * (w-2) + "+")


def normalizar_titulo(titulo):
    """limpia y estandariza un titulo (quita espacios, pasa a minusculas)."""
    return titulo.strip().lower()


def validar_cantidad_input(mensaje_prompt):
    """fuerza al usuario a ingresar un numero entero positivo o cero."""
    while True:
        valor = input(mensaje_prompt).strip()
        if valor.isdigit():
            cantidad = int(valor)
            if cantidad >= 0:
                return cantidad
            else:
                print("Error: La cantidad no puede ser negativa.")
        else:
            print("Error: Debe ingresar un numero entero valido (>= 0).")


def buscar_libro(catalogo, titulo_buscado):
    """busca un libro por titulo exacto (ignora mayusculas/espacios)."""
    titulo_normalizado_buscado = normalizar_titulo(titulo_buscado)
    for libro in catalogo:
        titulo_en_catalogo = normalizar_titulo(libro["TITULO"])
        if titulo_en_catalogo == titulo_normalizado_buscado:
            return libro
    return None


def cargar_catalogo(nombre_archivo):
    """lee el csv y lo carga en memoria como lista de diccionarios."""
    catalogo = []
    if not os.path.exists(nombre_archivo):
        print("No se encontro 'catalogo.csv'. Iniciando con catalogo vacio.")
        time.sleep(1)
        return catalogo

    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            if "TITULO" in fila and "CANTIDAD" in fila:
                if fila["CANTIDAD"].isdigit():
                    cantidad_int = int(fila["CANTIDAD"])
                else:
                    cantidad_int = 0
                catalogo.append(
                    {"TITULO": fila["TITULO"], "CANTIDAD": cantidad_int})
            else:
                print(
                    f"Advertencia: Fila ignorada por formato incorrecto: {fila}")

    print(f"Catalogo cargado desde '{nombre_archivo}'.")
    time.sleep(1)
    return catalogo


def guardar_catalogo(catalogo, nombre_archivo):
    """guarda la lista de diccionarios (catalogo) en el archivo csv."""
    fieldnames = ["TITULO", "CANTIDAD"]
    with open(nombre_archivo, mode='w', encoding='utf-8', newline='') as archivo:
        escritor_csv = csv.DictWriter(archivo, fieldnames=fieldnames)
        escritor_csv.writeheader()
        escritor_csv.writerows(catalogo)


def opcion_1_ingresar_multiples(catalogo, w: int):
    """logica para la opcion 1: agregar multiples libros."""
    print_header("1. Ingresar Titulos Multiples", w)
    print("Ingrese los libros. Ingrese 'FIN' o nada para terminar.\n")

    libros_agregados = 0
    while True:
        titulo_input = input("TITULO (o 'FIN' para parar): ")
        titulo_check = titulo_input.strip()

        if titulo_check.upper() == "FIN" or titulo_check == "":
            break

        titulo = titulo_input.strip().title()

        if not titulo:
            print("Error: El titulo no puede estar vacio.")
            continue

        libro_existente = buscar_libro(catalogo, titulo)
        if libro_existente:
            print(f"Error: El libro '{titulo}' ya existe. No se agregara.")
            continue

        cantidad = validar_cantidad_input(f"CANTIDAD para '{titulo}' (>=0): ")

        nuevo_libro = {"TITULO": titulo, "CANTIDAD": cantidad}
        catalogo.append(nuevo_libro)
        print(f"Libro '{titulo}' agregado con exito!")
        libros_agregados += 1
        print("+" + "-" * (w-2) + "+")

    if libros_agregados > 0:
        print(f"\nResumen: Se agregaron {libros_agregados} libros nuevos.")
    else:
        print("\nNo se agregaron libros nuevos.")

    input("\nPresione Enter para continuar...")
    return catalogo, (libros_agregados > 0)


def _mostrar_lista_paginada(catalogo, w: int, titulo_header: str, start: int, end: int) -> bool:
    """funcion interna para mostrar cualquier lista de forma paginada y dinamica."""
    if not catalogo:
        print_header(titulo_header, w)
        print("No hay titulos en la lista. Agregue algunos primero.")
        print("+" + "-" * (w-2) + "+")
        input("\nPresione Enter para continuar...")
        return False

    cantidad_titulos = len(catalogo)
    max_paginas = math.ceil(cantidad_titulos / LIST_LIMIT)

    print_header(titulo_header, w)

    espacio_fijo = 25
    if w < espacio_fijo + 10:
        max_len_titulo = 10
    else:
        max_len_titulo = w - espacio_fijo

    libros_a_mostrar = []
    for i in range(start, min(end, cantidad_titulos)):
        libro = catalogo[i]
        titulo_truncado = (libro['TITULO'][:max_len_titulo - 3] + '...') if len(
            libro['TITULO']) > max_len_titulo else libro['TITULO']
        libros_a_mostrar.append((i, titulo_truncado, str(libro['CANTIDAD'])))

    header = f"| {'INDICE':^6} | {'CANTIDAD':^8} | {'TITULO'.ljust(max_len_titulo)} |"
    print(header)
    print("+" + "-" * (w-2) + "+")

    for i, titulo_trunc, cantidad in libros_a_mostrar:
        row = f"| {str(i + 1):^6} | {cantidad:^8} | {titulo_trunc.ljust(max_len_titulo)} |"
        print(row)

    print("+" + "-" * (w-2) + "+")

    pagina_actual = (start // LIST_LIMIT) + 1
    print(f"|--- Pagina {pagina_actual} de {max_paginas} ---".ljust(w-2) + "|")
    print("+" + "-" * (w-2) + "+")

    return True


def opcion_2_ingresar_ejemplares(catalogo, w: int):
    """logica para la opcion 2: sumar ejemplares a un libro existente."""
    catalogo_modificado = False

    start = 0
    end = LIST_LIMIT
    cantidad_titulos = len(catalogo)

    while True:
        mostro_algo = _mostrar_lista_paginada(
            catalogo, w, "2. Ingresar Ejemplares", start, end)

        if not mostro_algo:
            return catalogo, False

        print("[1] ANTERIOR | [2] SIGUIENTE | [3] AGREGAR EJEMPLARES | [4] VOLVER |")
        opcion = input("OPCION: ").strip()

        match opcion:
            case "1":
                if start - LIST_LIMIT >= 0:
                    start -= LIST_LIMIT
                    end -= LIST_LIMIT
            case "2":
                if end < cantidad_titulos:
                    start += LIST_LIMIT
                    end += LIST_LIMIT
            case "3":
                idx_str = input("Ingrese el indice del libro (1-N): ").strip()
                if idx_str.isdigit():
                    idx_real = int(idx_str) - 1
                    if 0 <= idx_real < cantidad_titulos:
                        libro_a_modificar = catalogo[idx_real]
                        print(
                            f"Libro seleccionado: '{libro_a_modificar['TITULO']}'")
                        cantidad_a_sumar = validar_cantidad_input(
                            "Cuantos ejemplares desea sumar? ")

                        if cantidad_a_sumar > 0:
                            libro_a_modificar["CANTIDAD"] += cantidad_a_sumar
                            print(
                                f"Stock actualizado. Nuevo stock: {libro_a_modificar['CANTIDAD']}")
                            catalogo_modificado = True
                        else:
                            print("No se realizaron cambios (cantidad 0).")
                    else:
                        print("Indice invalido.")
                else:
                    print("Entrada invalida. Ingrese un numero.")
                input("\nPresione Enter para continuar...")
            case "4":
                return catalogo, catalogo_modificado
            case _:
                pass


def opcion_3_mostrar_catalogo(catalogo, w: int):
    """logica para la opcion 3: listar todos los libros con paginacion."""
    start = 0
    end = LIST_LIMIT
    cantidad_titulos = len(catalogo)

    while True:
        mostro_algo = _mostrar_lista_paginada(
            catalogo, w, "3. Mostrar Catalogo", start, end)

        if not mostro_algo:
            return

        print("[1] ANTERIOR | [2] SIGUIENTE | [3] VOLVER |")
        opcion = input("OPCION: ").strip()

        match opcion:
            case "1":
                if start - LIST_LIMIT >= 0:
                    start -= LIST_LIMIT
                    end -= LIST_LIMIT
            case "2":
                if end < cantidad_titulos:
                    start += LIST_LIMIT
                    end += LIST_LIMIT
            case "3":
                break
            case _:
                pass


def opcion_4_consultar_disponibilidad(catalogo, w: int):
    """logica para la opcion 4: buscar libros por coincidencia parcial."""
    while True:
        print_header("4. Consultar Disponibilidad (Busqueda Aproximada)", w)
        if not catalogo:
            print("No hay titulos en la lista. Agregue algunos primero.")
            print("+" + "-" * (w-2) + "+")
            input("\nPresione Enter para continuar...")
            return

        titulo_buscado = input("Ingrese parte del TITULO a buscar: ").strip()

        if not titulo_buscado:
            print("Entrada invalida. No ingreso un termino de busqueda.")
        else:
            titulo_buscar_norm = titulo_buscado.lower().replace(" ", "")

            titulos_encontrados = []
            for i, libro in enumerate(catalogo):
                titulo_catalogo_norm = libro["TITULO"].lower().replace(" ", "")

                if titulo_buscar_norm in titulo_catalogo_norm:
                    titulos_encontrados.append((i, libro))

            if titulos_encontrados:
                print(
                    f"\n--- Se encontraron {len(titulos_encontrados)} resultado(s) ---")

                espacio_fijo = 25
                max_len_titulo = w - \
                    espacio_fijo if w > (espacio_fijo + 10) else 10

                header = f"| {'INDICE':^6} | {'CANTIDAD':^8} | {'TITULO'.ljust(max_len_titulo)} |"
                print(header)
                print("+" + "-" * (w-2) + "+")

                for idx, libro in titulos_encontrados:
                    titulo_truncado = (libro['TITULO'][:max_len_titulo - 3] + '...') if len(
                        libro['TITULO']) > max_len_titulo else libro['TITULO']
                    row = f"| {str(idx + 1):^6} | {str(libro['CANTIDAD']):^8} | {titulo_truncado.ljust(max_len_titulo)} |"
                    print(row)

                print("+" + "-" * (w-2) + "+")
            else:
                print(
                    f"\nNo se encontro ningun libro que contenga '{titulo_buscado}'.")

        print("\n[1] NUEVA BUSQUEDA | [2] VOLVER |")
        opcion_menu = input("OPCION: ").strip()
        match opcion_menu:
            case "1":
                continue
            case "2":
                break
            case _:
                pass


def opcion_5_listar_agotados(catalogo, w: int):
    """logica para la opcion 5: mostrar solo libros con cantidad cero."""
    print_header("5. Libros Agotados (Stock 0)", w)

    libros_agotados = []
    for i, libro in enumerate(catalogo):
        if libro["CANTIDAD"] == 0:
            libros_agotados.append((i, libro))

    if not libros_agotados:
        print("No hay libros agotados en este momento.")
    else:
        espacio_fijo = 25
        max_len_titulo = w - espacio_fijo if w > (espacio_fijo + 10) else 10

        header = f"| {'INDICE':^6} | {'CANTIDAD':^8} | {'TITULO'.ljust(max_len_titulo)} |"
        print(header)
        print("+" + "-" * (w-2) + "+")

        for idx, libro in libros_agotados:
            titulo_truncado = (libro['TITULO'][:max_len_titulo - 3] + '...') if len(
                libro['TITULO']) > max_len_titulo else libro['TITULO']
            row = f"| {str(idx + 1):^6} | {str(libro['CANTIDAD']):^8} | {titulo_truncado.ljust(max_len_titulo)} |"
            print(row)

    print("+" + "-" * (w-2) + "+")
    input("\nPresione Enter para continuar...")


def opcion_6_agregar_titulo(catalogo, w: int):
    """logica para la opcion 6: agregar un unico libro nuevo."""
    print_header("6. Agregar Nuevo Titulo (Individual)", w)

    titulo_input = input("Ingrese el TITULO: ")
    titulo = titulo_input.strip().title()

    if not titulo:
        print("Error: El titulo no puede estar vacio.")
        input("\nPresione Enter para continuar...")
        return catalogo, False

    libro_existente = buscar_libro(catalogo, titulo)
    if libro_existente:
        print("Error: Ya existe un libro con ese titulo.")
        input("\nPresione Enter para continuar...")
        return catalogo, False

    cantidad = validar_cantidad_input("Ingrese la cantidad inicial (>=0): ")

    nuevo_libro = {"TITULO": titulo, "CANTIDAD": cantidad}
    catalogo.append(nuevo_libro)
    print(f"Libro '{titulo}' con {cantidad} ejemplares agregado con exito!")

    print("+" + "-" * (w-2) + "+")
    input("\nPresione Enter para continuar...")
    return catalogo, True


def opcion_7_actualizar_ejemplares(catalogo, w: int):
    """logica para la opcion 7: realizar prestamos (restar) y devoluciones (sumar)."""
    catalogo_modificado = False

    start = 0
    end = LIST_LIMIT
    cantidad_titulos = len(catalogo)

    while True:
        mostro_algo = _mostrar_lista_paginada(
            catalogo, w, "7. Prestamos / Devoluciones", start, end)

        if not mostro_algo:
            return catalogo, False

        print(
            "[1] ANTERIOR | [2] SIGUIENTE | [3] PRESTAMO | [4] DEVOLUCION | [5] VOLVER |")
        opcion = input("OPCION: ").strip()

        match opcion:
            case "1":
                if start - LIST_LIMIT >= 0:
                    start -= LIST_LIMIT
                    end -= LIST_LIMIT
            case "2":
                if end < cantidad_titulos:
                    start += LIST_LIMIT
                    end += LIST_LIMIT

            case "3":
                idx_str = input(
                    "Ingrese el indice del libro a PRESTAR (1-N): ").strip()
                if idx_str.isdigit():
                    idx_real = int(idx_str) - 1
                    if 0 <= idx_real < cantidad_titulos:
                        libro_a_modificar = catalogo[idx_real]

                        if libro_a_modificar["CANTIDAD"] > 0:
                            libro_a_modificar["CANTIDAD"] -= 1
                            print(
                                f"Prestamo registrado. Nuevo stock: {libro_a_modificar['CANTIDAD']}")
                            catalogo_modificado = True
                        else:
                            print(
                                "Operacion rechazada: No hay ejemplares disponibles (Stock 0).")
                    else:
                        print("Indice invalido.")
                else:
                    print("Entrada invalida.")
                input("\nPresione Enter para continuar...")

            case "4":
                idx_str = input(
                    "Ingrese el indice del libro a DEVOLVER (1-N): ").strip()
                if idx_str.isdigit():
                    idx_real = int(idx_str) - 1
                    if 0 <= idx_real < cantidad_titulos:
                        libro_a_modificar = catalogo[idx_real]

                        libro_a_modificar["CANTIDAD"] += 1
                        print(
                            f"Devolucion registrada. Nuevo stock: {libro_a_modificar['CANTIDAD']}")
                        catalogo_modificado = True
                    else:
                        print("Indice invalido.")
                else:
                    print("Entrada invalida.")
                input("\nPresione Enter para continuar...")

            case "5":
                return catalogo, catalogo_modificado
            case _:
                pass


def main():
    """funcion principal que ejecuta el bucle del programa."""
    os.system("cls" if os.name == "nt" else "clear")
    mensaje_de_bienvenida()

    catalogo = cargar_catalogo(NOMBRE_ARCHIVO)

    while True:
        size = shutil.get_terminal_size()
        ancho = size.columns
        alto = size.lines

        os.system("cls" if os.name == "nt" else "clear")

        main_display(h=alto, w=ancho)

        eleccion_del_usuario = input("\nSeleccione una opcion: ").strip()

        catalogo_modificado = False

        match eleccion_del_usuario:
            case "1":
                catalogo, catalogo_modificado = opcion_1_ingresar_multiples(
                    catalogo, ancho)
            case "2":
                catalogo, catalogo_modificado = opcion_2_ingresar_ejemplares(
                    catalogo, ancho)
            case "3":
                opcion_3_mostrar_catalogo(catalogo, ancho)
            case "4":
                opcion_4_consultar_disponibilidad(catalogo, ancho)
            case "5":
                opcion_5_listar_agotados(catalogo, ancho)
            case "6":
                catalogo, catalogo_modificado = opcion_6_agregar_titulo(
                    catalogo, ancho)
            case "7":
                catalogo, catalogo_modificado = opcion_7_actualizar_ejemplares(
                    catalogo, ancho)
            case "8":
                mensaje_de_salida()
                break
            case _:
                print("Opcion no valida. Intente nuevamente.")
                input("\nPresione Enter para continuar...")

        if catalogo_modificado:
            guardar_catalogo(catalogo, NOMBRE_ARCHIVO)
            print(
                f"\n** Cambios guardados exitosamente en '{NOMBRE_ARCHIVO}'! **")
            time.sleep(1.5)


if __name__ == "__main__":
    main()
