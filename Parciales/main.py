print("=== GENERADOR DE TABLAS DE VERDAD ===")
print("Opciones: and | or | not | xor | nand | nor")

booleanos = [0, 1]

while True:
    try:
        op = input("Elige un operador lógico: ").lower()

        if op not in ["and", "or", "not", "xor", "nand", "nor"]:
            raise ValueError("Operador inválido")

        # Si llega acá, es porque la opción es válida → salimos del bucle
        break

    except ValueError as e:
        print(f"Error: {e}. Intenta de nuevo.\n")

# Ahora mostramos la tabla según el operador elegido
if op == "and":
    print("\nTABLA DE VERDAD AND")
    print("P\tQ\tP and Q")
    for p in booleanos:
        for q in booleanos:
            print(f"{p}\t{q}\t{p and q}")

elif op == "or":
    print("\nTABLA DE VERDAD OR")
    print("P\tQ\tP or Q")
    for p in booleanos:
        for q in booleanos:
            print(f"{p}\t{q}\t{p or q}")

elif op == "not":
    print("\nTABLA DE VERDAD NOT")
    print("P\t¬P")
    for p in booleanos:
        print(f"{p}\t{int(not p)}")

elif op == "xor":
    print("\nTABLA DE VERDAD XOR")
    print("P\tQ\tP xor Q")
    for p in booleanos:
        for q in booleanos:
            print(f"{p}\t{q}\t{p ^ q}")

elif op == "nand":
    print("\nTABLA DE VERDAD NAND")
    print("P\tQ\tP nand Q")
    for p in booleanos:
        for q in booleanos:
            print(f"{p}\t{q}\t{int(not (p and q))}")

elif op == "nor":
    print("\nTABLA DE VERDAD NOR")
    print("P\tQ\tP nor Q")
    for p in booleanos:
        for q in booleanos:
            print(f"{p}\t{q}\t{int(not (p or q))}")
