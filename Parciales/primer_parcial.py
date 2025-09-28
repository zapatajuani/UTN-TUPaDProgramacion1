import os

titulos: list[str] = []
ejemplares: list[int] = []

LIST_LIMIT = 10

while True:
    # Limpiar la pantalla (funciona en terminales compatibles)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("+------------------------------------+")
    print("|             BIBLIOTECA             |")
    print("+------------------------------------+")
    print("| [1] INGRESAR TITULOS               |")
    print("| [2] INGRESAR EJEMPLARES            |")
    print("| [3] MOSTRAR CATALOGO               |")
    print("| [4] CONSULTAR DISPONIBILIDAD       |")
    print("| [5] LISTAR AGOTADOS                |")
    print("| [6] AGREGAR TITULO NUEVO           |")
    print("| [7] PRESTAMOS / DEVOLUCIONES       |")
    print("| [8] SALIR                          |")
    print("+------------------------------------+")
    print(" OPCION: ", end="")

    opcion = input()

    match opcion:
        # ingresar libros
        case "1":
            os.system('cls' if os.name == 'nt' else 'clear')

            print("Ingrese los libros que desea agregar.")
            print("Liste uno por línea en el.")
            print("Ingrese 'FIN' o nada para terminar.")
            print("Ejemplo de entrada:")
            print("El Señor de los Anillos")
            print("Cien Años de Soledad")
            print("FIN")
            print("-----------------------------------------------------\n")

            titulos_nuevos: list[str] = []
            titulos_repetidos: list[str] = []
            titulos_nuevos_sin_ejemplares: list[str] = []

            while True:
                entrada = input().strip()
                if entrada.upper() == "FIN" or entrada == "":
                    break

                titulo = entrada.strip().title()

                if titulo not in titulos and titulo not in titulos_nuevos:
                    titulos_nuevos.append(titulo)
                else:
                    titulos_repetidos.append(titulo)

            if titulos_repetidos:
                print(
                    "\nLos siguientes títulos ya existen en la lista y no se agregaron:")
                for titulo in titulos_repetidos:
                    print(f"- {titulo}")

            titulos.extend(titulos_nuevos)
            titulos_nuevos_sin_ejemplares.extend(titulos_nuevos)
            ejemplares.extend([0] * len(titulos_nuevos))

            print("\nNuevos títulos agregados exitosamente.")
            input("Presione Enter para continuar...")

            if not titulos_nuevos:
                continue

            print("Ingrese la cantidad de ejemplares para los siguientes títulos:")
            for titulo in titulos_nuevos_sin_ejemplares:
                while True:
                    cantidad = input(
                        f"'{titulo}': ").strip()
                    if cantidad.isdigit() and int(cantidad) >= 0:
                        indice = titulos.index(titulo)
                        ejemplares[indice] = int(cantidad)
                        break
                    else:
                        print(
                            "Entrada inválida. Por favor ingrese un número entero no negativo.")

        # ingresar ejemplares
        case "2":
            if not titulos:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("No hay títulos en la lista. Agregue algunos primero.")
                input("Presione Enter para continuar...")
                continue

            start = 0
            end = LIST_LIMIT

            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                max_len = max(len(titulo) for titulo in titulos)

                cantidad_titulos = len(titulos)

                print(f"Indice | {'Título'.ljust(max_len)} | Ejemplares")
                print("-" * (max_len + 22))

                for i in list(range(cantidad_titulos))[start:end]:
                    index = i
                    titulo = titulos[index]
                    print(
                        f"{str(index + 1).center(6)} | {titulo.ljust(max_len)} | {str(ejemplares[index]).rjust(10)}")

                print("\n[1] ANTERIOR", end=" | ")
                print("[2] SIGUIENTE", end=" | ")
                print("[3] AGREGAR EJEMPLARES", end=" | ")
                print("[4] VOLVER", end=" | OPCION: ")
                opcion = input()
                match opcion:
                    case "1":
                        if start - LIST_LIMIT >= 0:
                            start -= LIST_LIMIT
                            end -= LIST_LIMIT
                    case "2":
                        if start <= cantidad_titulos - LIST_LIMIT:
                            start += LIST_LIMIT
                            end += LIST_LIMIT
                    case "3":
                        indice_agregar = input(
                            "Ingrese el índice del libro al que desea agregar ejemplares: ").strip()

                        if not indice_agregar.isdigit():
                            print(
                                "Entrada inválida. Por favor ingrese un número entero.")
                            input("Presione Enter para continuar...")
                            continue

                        indice_agregar = int(indice_agregar) - 1

                        if 0 <= indice_agregar < len(titulos):
                            cantidad_agregar = input(
                                f"Ingrese la cantidad de ejemplares a agregar para '{titulos[indice_agregar]}': ").strip()

                            if not cantidad_agregar.isdigit():
                                print(
                                    "Entrada inválida. Por favor ingrese un número entero.")
                                input("Presione Enter para continuar...")
                                continue

                            cantidad_agregar = int(cantidad_agregar)

                            if cantidad_agregar > 0:
                                ejemplares[indice_agregar] += cantidad_agregar
                                print("Ejemplares agregados exitosamente.")
                            else:
                                print(
                                    "La cantidad a agregar debe ser mayor que cero.")

                        else:
                            print("Índice inválido.")
                        input("Presione Enter para continuar...")
                    case "4":
                        break
                    case _:
                        pass

        # listar libros
        case "3":

            if not titulos:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("No hay títulos en la lista. Agregue algunos primero.")
                input("Presione Enter para continuar...")
                continue

            start = 0
            end = LIST_LIMIT

            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                max_len = max(len(titulo) for titulo in titulos)

                cantidad_titulos = len(titulos)

                print(f"Indice | {'Título'.ljust(max_len)} | Ejemplares")
                print("-" * (max_len + 22))

                for i in list(range(cantidad_titulos))[start:end]:
                    index = i
                    titulo = titulos[index]
                    print(
                        f"{str(index + 1).center(6)} | {titulo.ljust(max_len)} | {str(ejemplares[index]).rjust(10)}")

                print("\n[1] ANTERIOR", end=" | ")
                print("[2] SIGUIENTE", end=" | ")
                print("[3] VOLVER", end=" | OPCION: ")
                opcion = input()
                match opcion:
                    case "1":
                        if start - LIST_LIMIT >= 0:
                            start -= LIST_LIMIT
                            end -= LIST_LIMIT
                    case "2":
                        if start <= cantidad_titulos - LIST_LIMIT:
                            start += LIST_LIMIT
                            end += LIST_LIMIT
                    case "3":
                        break
                    case _:
                        pass

        # buscar libros
        case "4":
            if not titulos:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("No hay títulos en la lista. Agregue algunos primero.")
                input("Presione Enter para continuar...")
                continue

            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                titulos_encontrados: list[tuple[int, str, int]] = []

                titulo_buscar = input(
                    "Ingrese el título del libro a buscar: ").strip().lower()

                if not titulo_buscar:
                    print("Entrada inválida. Por favor ingrese un título.")
                    input("Presione Enter para continuar...")
                    continue

                for i, titulo in enumerate(titulos):
                    if titulo_buscar.replace(" ", "") in titulo.lower().replace(" ", ""):
                        titulos_encontrados.append((i, titulo, ejemplares[i]))

                os.system('cls' if os.name == 'nt' else 'clear')
                if titulos_encontrados:
                    max_len = max(len(titulo)
                                  for _, titulo, _ in titulos_encontrados)
                    print(f"Indice | {'Título'.ljust(max_len)} | Ejemplares")
                    print("-" * (max_len + 22))
                    for index, titulo, ejemplares_count in titulos_encontrados:
                        print(
                            f"{str(index + 1).ljust(6)} | {titulo.ljust(max_len)} | {str(ejemplares_count).rjust(10)}")
                else:
                    print("No se encontraron títulos que coincidan con la búsqueda.")

                print("\n[1] NUEVA BÚSQUEDA", end=" | ")
                print("[2] VOLVER", end=" | OPCION: ")
                opcion = input()
                match opcion:
                    case "1":
                        continue
                    case "2":
                        break
                    case _:
                        pass

        # listar titulos sin ejemplares
        case "5":
            if not titulos:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("No hay títulos en la lista. Agregue algunos primero.")
                input("Presione Enter para continuar...")
                continue

            os.system('cls' if os.name == 'nt' else 'clear')
            titulos_encontrados: list[tuple[int, str, int]] = []

            for i, cantidad in enumerate(ejemplares):
                if cantidad == 0:
                    titulos_encontrados.append(
                        (i, titulos[i], cantidad))

            os.system('cls' if os.name == 'nt' else 'clear')
            print("Títulos sin ejemplares:\n")
            if titulos_encontrados:
                max_len = max(len(titulo)
                              for _, titulo, _ in titulos_encontrados)
                print(f"Indice | {'Título'.ljust(max_len)} | Ejemplares")
                print("-" * (max_len + 22))
                for index, titulo, ejemplares_count in titulos_encontrados:
                    print(
                        f"{str(index + 1).ljust(6)} | {titulo.ljust(max_len)} | {str(ejemplares_count).rjust(10)}")
            else:
                print("No hay títulos sin ejemplares.")

            input("\nPresione Enter para continuar...")

        # actualizar cantidad
        case "6":
            os.system('cls' if os.name == 'nt' else 'clear')
            nuevo_titulo = input(
                "Ingrese el título del nuevo libro a agregar: ").strip().title()
            
            if not nuevo_titulo:
                print("Entrada inválida. Por favor ingrese un título.")
                input("Presione Enter para continuar...")
                continue

            if nuevo_titulo in titulos:
                print("El título ya existe en la lista.")
                input("Presione Enter para continuar...")
                continue

            nuevo_titulo_ejemplares = input(
                f"Ingrese la cantidad de ejemplares para '{nuevo_titulo}': ").strip()

            if not nuevo_titulo_ejemplares.isdigit():
                print("Entrada inválida. Por favor ingrese un número entero.")
                input("Presione Enter para continuar...")
                continue

            if int(nuevo_titulo_ejemplares) < 0:
                print("La cantidad de ejemplares no puede ser negativa.")
                input("Presione Enter para continuar...")
                continue

            titulos.append(nuevo_titulo)
            ejemplares.append(int(nuevo_titulo_ejemplares))
            print(
                f"Libro '{nuevo_titulo}' con {nuevo_titulo_ejemplares} ejemplares agregado exitosamente.")

        # prestamos/devoluciones
        case "7":
            if not titulos:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("No hay títulos en la lista. Agregue algunos primero.")
                input("Presione Enter para continuar...")
                continue

            start = 0
            end = LIST_LIMIT

            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                max_len = max(len(titulo) for titulo in titulos)

                cantidad_titulos = len(titulos)

                print(f"Indice | {'Título'.ljust(max_len)} | Ejemplares")
                print("-" * (max_len + 22))

                for i in list(range(cantidad_titulos))[start:end]:
                    index = i
                    titulo = titulos[index]
                    print(
                        f"{str(index + 1).ljust(6)} | {titulo.ljust(max_len)} | {str(ejemplares[index]).rjust(10)}")

                print("\n[1] ANTERIOR", end=" | ")
                print("[2] SIGUIENTE", end=" | ")
                print("[3] PRESTAMO", end=" | ")
                print("[4] DEVOLUCION", end=" | ")
                print("[5] VOLVER", end=" | OPCION: ")
                opcion = input()
                match opcion:
                    case "1":
                        if start - LIST_LIMIT >= 0:
                            start -= LIST_LIMIT
                            end -= LIST_LIMIT
                    case "2":
                        if start <= cantidad_titulos - LIST_LIMIT:
                            start += LIST_LIMIT
                            end += LIST_LIMIT

                    case "3":
                        indice_prestamo = input(
                            "Ingrese el índice del libro a prestar: ").strip()

                        if not indice_prestamo.isdigit():
                            print(
                                "Entrada inválida. Por favor ingrese un número entero.")
                            input("Presione Enter para continuar...")
                            continue

                        indice_prestamo = int(indice_prestamo) - 1

                        if 0 <= indice_prestamo < len(titulos):
                            if ejemplares[indice_prestamo] > 0:
                                ejemplares[indice_prestamo] -= 1
                                print(
                                    f"Préstamo realizado. Quedan {ejemplares[indice_prestamo]} ejemplares de '{titulos[indice_prestamo]}'.")
                            else:
                                print(
                                    f"No hay ejemplares disponibles para '{titulos[indice_prestamo]}'.")
                        else:
                            print("Índice inválido.")
                        input("Presione Enter para continuar...")

                    case "4":
                        indice_devolucion = input(
                            "Ingrese el índice del libro a devolver: ").strip()

                        if not indice_devolucion.isdigit():
                            print(
                                "Entrada inválida. Por favor ingrese un número entero.")
                            input("Presione Enter para continuar...")
                            continue

                        indice_devolucion = int(indice_devolucion) - 1

                        if 0 <= indice_devolucion < len(titulos):
                            ejemplares[indice_devolucion] += 1
                            print(
                                f"Devolución realizada. Ahora hay {ejemplares[indice_devolucion]} ejemplares de '{titulos[indice_devolucion]}'.")
                        else:
                            print("Índice inválido.")
                        input("Presione Enter para continuar...")

                    case "5":
                        break
                    case _:
                        pass

        # salir
        case "8":
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        case _:
            pass
