import csv
from typing import List, Dict

# Utilidades


def cantidad_de_paises(path: str) -> int:
    with open(path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return sum(1 for _ in reader)


def validar_pais(pais: Dict[str, str], registro_nuevo: bool = True) -> tuple[bool, str]:

    paises = cargar_paises('paises.csv')
    for existente in paises:
        if existente['nombre'].lower() == pais['nombre'].lower() and registro_nuevo:
            return False, "El país ya existe en la base de datos."

    if pais['nombre'] is None or not pais['nombre'].replace(" ", "").isalpha():
        return False, "El país debe tener un nombre válido."
    if pais['poblacion'] is None or not pais['poblacion'].isalnum():
        return False, "El país debe tener una población válida."
    if pais['superficie'] is None or not pais['superficie'].isalnum():
        return False, "El país debe tener una superficie válida."
    if pais['continente'] is None or not pais['continente'].replace(" ", "").isalpha():
        return False, "El país debe tener un continente válido."
    return True, "País válido."

# Funciones responsables de manejar los datos de los países en CSV


def cargar_paises(file_path: str) -> List[Dict[str, str]]:
    paises = []
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            paises.append(row)
    return paises


def agregar_pais(nuevo_pais: Dict[str, str]) -> tuple[bool, str]:
    es_valido, mensaje = validar_pais(nuevo_pais)
    if not es_valido:
        return False, mensaje

    for key, value in nuevo_pais.items():
        nuevo_pais[key] = value.strip().title()

    # Agregar el país a la base de datos CSV
    with open('paises.csv', mode='a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['nombre', 'poblacion', 'superficie', 'continente']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(nuevo_pais)

    return True, "País agregado exitosamente."


def actualizar_pais(datos_actualizados: Dict[str, str]) -> tuple[bool, str]:
    es_valido, mensaje = validar_pais(datos_actualizados, registro_nuevo=False)
    if not es_valido:
        return False, mensaje

    paises = cargar_paises('paises.csv')
    for i, pais in enumerate(paises):
        if pais['nombre'].lower() == datos_actualizados['nombre'].lower():
            paises[i] = datos_actualizados
            break
    else:
        return False, "País no encontrado."

    with open('paises.csv', mode='w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['nombre', 'poblacion', 'superficie', 'continente']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(paises)

    return True, "País actualizado exitosamente."

# Funciones para filtro y busqueda de datos cargados


def buscar_pais_por_nombre(
    nombre: str,
    paises: List[Dict[str, str]]
) -> List[Dict[str, str]] | tuple[None, str]:
    if not nombre.isalpha():
        return None, "El nombre del país debe ser válido."

    if not paises:
        return None, "No hay países cargados para buscar."

    paises_validos = []

    for pais in paises:
        if nombre.lower() in pais['nombre'].lower():
            paises_validos.append(pais)

    if not paises_validos:
        return None, "País no encontrado."

    return paises_validos


def filtrar_por_continente(
    paises: List[Dict[str, str]], continente: str
) -> List[Dict[str, str]]:
    return [pais for pais in paises if pais['continente'].lower() == continente.lower()]


def filtrar_por_rango_poblacion(
    paises: List[Dict[str, str]], min_poblacion: int, max_poblacion: int
) -> List[Dict[str, str]]:
    resultado = []
    for pais in paises:
        poblacion = int(pais['poblacion'])
        if min_poblacion <= poblacion <= max_poblacion:
            resultado.append(pais)

    return resultado


def filtrar_por_rango_superficie(
    paises: List[Dict[str, str]], min_superficie: int, max_superficie: int
) -> List[Dict[str, str]]:
    resultado = []
    for pais in paises:
        superficie = int(pais['superficie'])
        if min_superficie <= superficie <= max_superficie:
            resultado.append(pais)

    return resultado


if __name__ == "__main__":
    pass
