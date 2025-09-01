# Importa todas las funciones de los ejercicios
from ej1 import ej1
from ej2 import ej2
from ej3 import ej3
from ej4 import ej4
from ej5 import ej5
from ej6 import ej6
from ej7 import ej7
from ej8 import ej8
from ej9 import ej9
from ej10 import ej10

def mostrar_menu():
    """Muestra el menu de opciones disponibles"""
    print("\n=== ESTRUCTURAS REPETITIVAS ===")
    print("ej1  - Numeros del 0 al 100")
    print("ej2  - Contar digitos de un numero")
    print("ej3  - Suma de numeros en rango")
    print("ej4  - Suma hasta ingresar 0")
    print("ej5  - Juego adivinar numero")
    print("ej6  - Numeros pares decreciente")
    print("ej7  - Suma de 0 a N")
    print("ej8  - Clasificar 100 numeros")
    print("ej9  - Media de 100 numeros")
    print("ej10 - Invertir digitos")
    print("salir - Para terminar el programa")
    print("===============================")

def ejecutar_ejercicio(opcion):
    """Ejecuta el ejercicio segun la opcion seleccionada"""
    # Diccionario que mapea opciones con funciones
    ejercicios = {
        'ej1': ej1,
        'ej2': ej2,
        'ej3': ej3,
        'ej4': ej4,
        'ej5': ej5,
        'ej6': ej6,
        'ej7': ej7,
        'ej8': ej8,
        'ej9': ej9,
        'ej10': ej10
    }
    
    # Verifica si la opcion existe y la ejecuta
    if opcion in ejercicios:
        print(f"\n--- Ejecutando {opcion.upper()} ---")
        ejercicios[opcion]()
        print(f"--- Fin de {opcion.upper()} ---\n")
        return True
    elif opcion == 'salir':
        print("Hasta luego!")
        return False
    else:
        print("Opcion no valida. Intenta de nuevo.")
        return True

if __name__ == "__main__":
    # Bucle principal del programa
    continuar = True
    while continuar:
        # Muestra menu de opciones
        mostrar_menu()
        # Solicita opcion al usuario
        opcion = input("Ingresa tu opcion: ").lower().strip()
        # Ejecuta la opcion seleccionada
        continuar = ejecutar_ejercicio(opcion)
