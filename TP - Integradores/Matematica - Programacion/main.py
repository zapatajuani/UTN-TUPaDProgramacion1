# pedir la declaracion logica al usuario
print("====================== GENERADOR DE TABLAS DE VERDAD =======================")
print("Ingrese AND, OR, NOT, XOR, NAND, NOR como operadores logicos para visualizar")
print("los esquemas de las tablas de verdad correspondientes.")
print("Ingrese la declaracion logica (use + para OR, * para AND, ~ para NOT): ")
print("Ejemplo: A * (B + ~C)\n")

# puertas logicas reconocidas
PUERTAS_LOGICAS = ['AND', 'OR', 'NOT', 'XOR', 'NAND', 'NOR']

# valores booleanos posibles
booleanos = [0, 1]

# simbolos reconocidos en la declaracion
SIMBOLOS = ['+', '*', '~', '(', ')']

# operadores logicos considerados
OPERADORES = ['+', '*', '~']

# variables
VARIABLES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
             "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

while True:
    # leer la linea ingresada por el usuario
    input_str = input()

    # si la entrada es una puerta logica, mostrar su tabla de verdad
    if input_str.upper() in PUERTAS_LOGICAS:
        if input_str.lower() == "and":
            print("\nTABLA DE VERDAD AND")
            print("P | Q | P and Q")
            print("---------------")
            for p in booleanos:
                for q in booleanos:
                    print(f"{p} | {q} | {str(p and q).center(7)}")
            print()

        elif input_str.lower() == "or":
            print("\nTABLA DE VERDAD OR")
            print("P | Q | P or Q")
            print("--------------")
            for p in booleanos:
                for q in booleanos:
                    print(f"{p} | {q} | {str(p or q).center(6)}")
            print()

        elif input_str.lower() == "not":
            print("\nTABLA DE VERDAD NOT")
            print("P | not P ")
            print("----------")
            for p in booleanos:
                print(f"{p} | {str(int(not p)).center(6)}")
            print()

        elif input_str.lower() == "xor":
            print("\nTABLA DE VERDAD XOR")
            print("P | Q | P xor Q")
            print("---------------")
            for p in booleanos:
                for q in booleanos:
                    print(f"{p} | {q} | {str(p ^ q).center(7)}")
            print()

        elif input_str.lower() == "nand":
            print("\nTABLA DE VERDAD NAND")
            print("P | Q | P nand Q")
            print("----------------")
            for p in booleanos:
                for q in booleanos:
                    print(f"{p} | {q} | {str(int(not (p and q))).center(8)}")
            print()

        elif input_str.lower() == "nor":
            print("\nTABLA DE VERDAD NOR")
            print("P | Q | P nor Q")
            print("---------------")
            for p in booleanos:
                for q in booleanos:
                    print(f"{p} | {q} | {int(not (p or q))}")
            print()

    # si la entrada no es una puerta logica, salir del bucle para procesar la expresion
    elif input_str.strip() == "" or not all(c not in SIMBOLOS + VARIABLES for c in input_str):
        break


# quitar espacios y pasar a mayusculas para normalizar
declaracion = input_str.replace(" ", "").upper()

# lista para guardar las variables encontradas
variables: list[str] = []

# lista para guardar operadores con su posicion
operadores: list[list[int | str]] = []

# posiciones de parentesis abiertos
open_brackets: list[int] = []

# posiciones de parentesis cerrados asociadas
close_brackets: list[int] = []

# pares [pos_abre, pos_cierra] de parentesis
pair_brackets: list[list[int]] = []

# recorrer cada caracter con su indice
for i, char in enumerate(declaracion):
    if char not in SIMBOLOS and char not in variables:
        # si el caracter no es un simbolo y no esta en variables, agregarlo
        variables.append(char)

    if char in OPERADORES:
        # almacenar la posicion y tipo de operador
        operadores.append([i, char])

    if char == '(' and i not in open_brackets:
        # comenzar busqueda de cierre desde la posicion del abierto
        k = i

        # variable para guardar la posicion del cierre correspondiente
        pos = 0

        # recorrer hacia adelante para encontrar cierre sencillo
        while k < len(declaracion):

            # si se encuentra otro abierto y ya se habia encontrado un cierre, salir
            if declaracion[k] == '(' and pos != 0:
                break

            # si se encuentra un cierre y no se habia encontrado antes, guardar la posicion
            if declaracion[k] == ')' and k not in close_brackets:
                pos = k
            k += 1

        # guardar la posicion del parentesis abierto
        open_brackets.append(i)

        # guardar la posicion del cierre asociado
        close_brackets.append(pos)

        # guardar el par de parentesis
        pair_brackets.append([i, pos])

# ordenar las variables en orden descendente para la tabla
variables = sorted(variables, reverse=True)

# matriz de combinaciones binarias para las variables
values = [[0 for _ in range(len(variables))]
          for _ in range(2 ** len(variables))]

# para cada variable calcular la alternancia de 0/1
for i in range(len(variables)):
    # cuantas veces consecutivas se repite un valor
    repeat = 2 ** (len(variables) - i - 1)

    # valor inicial
    val = 0

    # contador de repeticiones
    count = 0

    # llenar la columna correspondiente en la matriz de valores
    for j in range(2 ** len(variables)):
        values[j][i] = val
        count += 1
        if count == repeat:
            # alternar el valor entre 0 y 1
            val = 1 if val == 0 else 0
            count = 0

# lista de subexpresiones dentro de parentesis y la expresion completa
sub_strings: list[str] = []

# extraer el contenido entre cada par de parentesis
for pair in pair_brackets:
    sub_strings.append(declaracion[pair[0] + 1: pair[1]])

# agregar la expresion completa al final de las subexpresiones
sub_strings.append(declaracion)

# lista final con cada fila: valores de variables + resultados de subexpresiones
outputs: list[list[int]] = []

# para cada combinacion de valores de variables
for val in values:
    # lista auxiliar para resultados de subexpresiones
    aux: list[int] = []

    # evaluar cada subexpresion
    for s in sub_strings:
        # convertir simbolos a su equivalente de python
        s = s.replace('~', ' not ')
        s = s.replace('*', ' and ')
        s = s.replace('+', ' or ')

        # reemplazar cada variable por True/False segun la combinacion
        for i, var in enumerate(variables):
            s = s.replace(var, str(bool(val[i])))

        # evaluar la expresion en python y guardar 1 o 0
        aux.append(1 if eval(s) else 0)

    # concatenar los valores de variables con los resultados y agregar a la tabla
    outputs.append(val + aux)

# encabezados de la tabla: variables seguido de subexpresiones
headers = variables + sub_strings

# imprimir la tabla de verdad en consola en formato tabular

# titulo de la tabla
print("Tabla de verdad:\n")

# calcular ancho de cada columna segun encabezados y contenidos
col_widths: list[int] = []
for idx, h in enumerate(headers):
    # ancho maximo entre celdas
    max_cell = max((len(str(row[idx])) for row in outputs), default=0)
    # guardar el ancho necesario para cada columna
    col_widths.append(max(len(h), max_cell))

# encabezado y separador
# formar la fila de encabezados centrados
header_row = " | ".join(h.center(col_widths[i]) for i, h in enumerate(
    headers))

# linea separadora basada en anchos
separator = "-+-".join("-" * col_widths[i] for i in range(len(headers)))

# imprimir encabezado
print(header_row)

# imprimir separador
print(separator)

# filas de la tabla
for row in outputs:
    print(" | ".join(str(cell).center(
        # imprimir cada fila centrando las celdas segun anchos
        col_widths[i]) for i, cell in enumerate(row)))
# fin del codigo
