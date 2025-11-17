import os
import string


NOMBRE_ARCHIVO = "productos.txt"

# --- funciones de validacion ---

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
    elimina espacios y puntuacion al inicio y final del string.
    pone en minusculas por default.
    
    args:
        valor (str): string a limpiar.
        minusculas (bool, optional): convierte a minusculas. defaults to true.
    """
    resultado = valor.strip().strip(string.punctuation)
    if minusculas:
        resultado = resultado.lower()
    return resultado

# --- funciones de los ejercicios ---

def ejecutar_ejercicio_1(nombre_archivo):
    """crea el archivo productos.txt con 3 productos iniciales."""
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write("lapicera,120.50,30\n")
        archivo.write("cuaderno,250.00,15\n")
        archivo.write("regla,80.75,50\n")
    
    print(f"archivo '{nombre_archivo}' creado con exito.")


def ejecutar_ejercicio_2(nombre_archivo):
    """lee productos.txt y los muestra formateados."""
    if not os.path.exists(nombre_archivo):
        print(f"error: el archivo '{nombre_archivo}' no existe.")
        print("por favor, crea el archivo primero (opcion 1).")
        return

    print("--- productos en el archivo ---")
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            
            if not linea_limpia:
                continue 
            
            partes = linea_limpia.split(",")
            
            if len(partes) == 3:
                nombre = partes[0]
                precio_str = partes[1]
                cantidad_str = partes[2]
                
                if es_decimal_valido(precio_str) and es_entero_valido(cantidad_str):
                    precio_float = float(precio_str)
                    print(f"producto: {nombre} | precio: ${precio_float:.2f} | cantidad: {cantidad_str}")
                else:
                    print(f"linea con formato incorrecto (no numerico): {linea_limpia}")
            else:
                 print(f"linea con formato incorrecto (partes): {linea_limpia}")


def ejecutar_ejercicio_3(nombre_archivo):
    """agrega un nuevo producto al final del archivo."""
    if not os.path.exists(nombre_archivo):
        print(f"error: el archivo '{nombre_archivo}' no existe.")
        print("por favor, crea el archivo primero (opcion 1).")
        return

    nombre_input = input("ingresa nombre: ")
    precio_str = input("ingresa precio: ")
    cantidad_str = input("ingresa cantidad: ")

    nombre = format_clean_string(nombre_input, minusculas=True)
    
    if not nombre:
        print("\nnombre invalido. el producto no fue agregado.")
        return
    
    if not es_decimal_valido(precio_str) or not es_entero_valido(cantidad_str):
        print("\nprecio o cantidad invalidos. el producto no fue agregado.")
        return
    
    if float(precio_str) < 0 or int(cantidad_str) < 0:
        print("\nel precio y la cantidad deben ser numeros positivos.")
        return

    linea_nueva = f"{nombre},{float(precio_str):.2f},{int(cantidad_str)}\n"
    
    with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
        archivo.write(linea_nueva)
        
    print(f"\nproducto '{nombre}' agregado correctamente al archivo.")


def ejecutar_ejercicio_4(nombre_archivo, lista_productos):
    """carga el archivo en una lista de diccionarios."""
    if not os.path.exists(nombre_archivo):
        print(f"error: el archivo '{nombre_archivo}' no existe.")
        print("por favor, crea el archivo primero (opcion 1).")
        return

    lista_productos.clear() 
    lineas_con_error = 0

    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            if not linea_limpia:
                continue
            
            partes = linea_limpia.split(",")
            
            if len(partes) == 3 and es_decimal_valido(partes[1]) and es_entero_valido(partes[2]):
                
                nombre_limpio = format_clean_string(partes[0], minusculas=True)
                
                if nombre_limpio:
                    producto = {
                        'nombre': nombre_limpio,
                        'precio': float(partes[1]),
                        'cantidad': int(partes[2])
                    }
                    lista_productos.append(producto)
                else:
                    lineas_con_error += 1
            else:
                lineas_con_error += 1

    print(f"se cargaron {len(lista_productos)} productos en la lista.")
    if lineas_con_error > 0:
        print(f"se ignoraron {lineas_con_error} lineas con formato incorrecto.")


def ejecutar_ejercicio_5(lista_productos):
    """busca un producto por nombre en la lista."""
    if not lista_productos:
        print("la lista de productos esta vacia.")
        print("por favor, carga los productos primero (opcion 4).")
        return

    nombre_input = input("ingresa el nombre del producto a buscar: ")
    nombre_buscado = format_clean_string(nombre_input, minusculas=True)
    
    encontrado = False
    for producto in lista_productos:
        if producto['nombre'] == nombre_buscado:
            print("\n--- producto encontrado ---")
            print(f"  nombre: {producto['nombre']}")
            print(f"  precio: ${producto['precio']:.2f}")
            print(f"  cantidad: {producto['cantidad']}")
            encontrado = True
            break 
            
    if not encontrado:
        print(f"\nproducto '{nombre_buscado}' no encontrado en la lista.")


def ejecutar_ejercicio_6(nombre_archivo, lista_productos):
    """guarda la lista de diccionarios en el archivo."""
    if not lista_productos:
        print("la lista de productos esta vacia. no hay nada que guardar.")
        print("carga los productos primero (opcion 4).")
        return

    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        for producto in lista_productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    
    print(f"se guardaron {len(lista_productos)} productos en '{nombre_archivo}'.")


def main():
    """funcion principal que ejecuta el menu interactivo."""
    
    productos_en_memoria = []

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Menu de opciones:")
        print("0. salir")
        print("1. Crear archivo inicial (3 productos)")
        print("2. Leer y mostrar productos (desde archivo)")
        print("3. Agregar producto (al archivo)")
        print("4. Cargar productos (a lista en memoria)")
        print("5. Buscar producto (en lista en memoria)")
        print("6. Guardar productos (lista a archivo)")
        
        eleccion = input("ingresa el numero de la opcion: ")
        print("\n--------------------------------------------------\n")

        match eleccion:
            case "0":
                break
            case "1":
                ejecutar_ejercicio_1(NOMBRE_ARCHIVO)
            case "2":
                ejecutar_ejercicio_2(NOMBRE_ARCHIVO)
            case "3":
                ejecutar_ejercicio_3(NOMBRE_ARCHIVO)
            case "4":
                ejecutar_ejercicio_4(NOMBRE_ARCHIVO, productos_en_memoria)
            case "5":
                ejecutar_ejercicio_5(productos_en_memoria)
            case "6":
                ejecutar_ejercicio_6(NOMBRE_ARCHIVO, productos_en_memoria)
            case _:
                print("opcion no valida. intenta de nuevo.")

        print("\n--------------------------------------------------\n")
        input("presiona enter para continuar...")


if __name__ == "__main__":
    main()
 