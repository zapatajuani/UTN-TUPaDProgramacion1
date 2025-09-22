# pedir la declaracion logica al usuario
print("Ingrese la declaracion logica (use + para OR, * para AND, ~ para NOT): ")
input_str = input()  # leer la linea ingresada por el usuario
# quitar espacios y pasar a mayusculas para normalizar
declaracion = input_str.replace(" ", "").upper()

SIMBOLOS = ['+', '*', '~', '(', ')']  # simbolos reconocidos en la declaracion
OPERADORES = ['+', '*', '~']  # operadores logicos considerados

variables: list[str] = []  # lista para guardar las variables encontradas
# lista para guardar operadores con su posicion
operadores: list[list[int | str]] = []
open_brackets: list[int] = []  # posiciones de parentesis abiertos
close_brackets: list[int] = []  # posiciones de parentesis cerrados asociadas
# pares [pos_abre, pos_cierra] de parentesis
pair_brackets: list[list[int]] = []

for i, char in enumerate(declaracion):  # recorrer cada caracter con su indice
    if char not in SIMBOLOS and char not in variables:
        # si el caracter no es un simbolo y no esta en variables, agregarlo
        variables.append(char)

    if char in OPERADORES:
        # almacenar la posicion y tipo de operador
        operadores.append([i, char])

    if char == '(' and i not in open_brackets:
        k = i  # comenzar busqueda de cierre desde la posicion del abre
        pos = 0  # variable para guardar la posicion del cierre correspondiente
        while k < len(declaracion):  # recorrer hacia adelante para encontrar cierre sencillo
            if declaracion[k] == '(' and pos != 0:
                break  # si se encuentra otro abre y ya se habia encontrado un cierre, salir

            if declaracion[k] == ')' and k not in close_brackets:
                pos = k  # actualizar la posicion del cierre posible
            k += 1
        open_brackets.append(i)  # guardar la posicion del parentesis abierto
        close_brackets.append(pos)  # guardar la posicion del cierre asociado
        pair_brackets.append([i, pos])  # guardar el par de parentesis

# ordenar las variables en orden descendente para la tabla
variables = sorted(variables, reverse=True)

values = [[0 for _ in range(len(variables))]
          # matriz de combinaciones binarias para las variables
          for _ in range(2 ** len(variables))]

for i in range(len(variables)):  # para cada variable calcular la alternancia de 0/1
    # cuantas veces consecutivas se repite un valor
    repeat = 2 ** (len(variables) - i - 1)
    val = 0  # valor inicial
    count = 0  # contador de repeticiones
    # llenar la columna correspondiente en la matriz de valores
    for j in range(2 ** len(variables)):
        values[j][i] = val
        count += 1
        if count == repeat:
            val = 1 if val == 0 else 0  # alternar el valor entre 0 y 1
            count = 0

# lista de subexpresiones dentro de parentesis y la expresion completa
sub_strings: list[str] = []
for pair in pair_brackets:
    # extraer el contenido entre cada par de parentesis
    sub_strings.append(declaracion[pair[0] + 1: pair[1]])
# agregar la expresion completa al final de las subexpresiones
sub_strings.append(declaracion)

# lista final con cada fila: valores de variables + resultados de subexpresiones
outputs: list[list[int]] = []
for val in values:  # para cada combinacion de valores de variables
    aux: list[int] = []  # lista auxiliar para resultados de subexpresiones
    for s in sub_strings:  # evaluar cada subexpresion
        # convertir simbolos a su equivalente de python
        s = s.replace('~', ' not ')
        s = s.replace('*', ' and ')
        s = s.replace('+', ' or ')
        for i, var in enumerate(variables):
            # reemplazar cada variable por True/False segun la combinacion
            s = s.replace(var, str(bool(val[i])))
        # evaluar la expresion en python y guardar 1 o 0
        aux.append(1 if eval(s) else 0)
    # concatenar los valores de variables con los resultados y agregar a la tabla
    outputs.append(val + aux)

# encabezados de la tabla: variables seguido de subexpresiones
headers = variables + sub_strings

# imprimir la tabla de verdad en consola en formato tabular
print("Tabla de verdad:\n")  # titulo de la tabla
# calcular ancho de cada columna segun encabezados y contenidos
col_widths: list[int] = []
for idx, h in enumerate(headers):
    # ancho maximo entre celdas
    max_cell = max((len(str(row[idx])) for row in outputs), default=0)
    # guardar el ancho necesario para cada columna
    col_widths.append(max(len(h), max_cell))

# encabezado y separador
header_row = " | ".join(h.center(col_widths[i]) for i, h in enumerate(
    headers))  # formar la fila de encabezados centrados
# linea separadora basada en anchos
separator = "-+-".join("-" * col_widths[i] for i in range(len(headers)))
print(header_row)  # imprimir encabezado
print(separator)  # imprimir separador

# filas de la tabla
for row in outputs:
    print(" | ".join(str(cell).center(
        # imprimir cada fila centrando las celdas segun anchos
        col_widths[i]) for i, cell in enumerate(row)))
# fin del codigo
