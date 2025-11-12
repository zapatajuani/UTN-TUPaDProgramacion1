import curses
from typing import List, Dict
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utilities.paginas import paginas

HEADER_HEIGHT = 3
FOOTER_HEIGHT = 4


def main_menu(
    width: int,
    height: int,
    pag_num: int,
    lineas_disponibles: int,
    paises: List[Dict[str, str]] | tuple[bool, str]
) -> curses.window:
    """
    Crea y configura el menú principal con la lista de países.
    
    Args:
        width: Ancho de la ventana
        height: Alto de la ventana
        pag_num: Número de página actual
        lineas_disponibles: Líneas disponibles para mostrar países
        paises: Lista de países o tupla de error
        
    Returns:
        Ventana de curses configurada para el menú principal
    """
    # Altura disponible para el menú principal
    main_height = height - (
        HEADER_HEIGHT + FOOTER_HEIGHT)

    # Paginación
    total_paginas = paginas(lineas_disponibles)

    # Asegurar que pag_num esté dentro de los límites
    pag_num = max(0, min(pag_num, total_paginas - 1))

    menu_win = curses.newwin(main_height, width, HEADER_HEIGHT, 0)
    menu_win.bkgd(' ', curses.color_pair(2))  # Poner color de fondo
    menu_win.border()

    # Tmaño columnas proporcionado a width
    column_widths = {
        'nombre': int(width * 0.28),
        'continente': int(width * 0.28),
        'poblacion': int(width * 0.28),
        'superficie': int(width * 0.16)
    }

    # si paises es un error, mostrar mensaje
    if isinstance(paises, tuple) and not paises[0]:
        menu_win.addstr(
            main_height // 2,
            (width // 2) - len(paises[1]) // 2,
            str(paises[1])
        )
        return menu_win

    # si no es una lista, retornar el menú vacío
    if not isinstance(paises, list):
        return menu_win

    menu_win.addstr(1, 2, "Pais")
    menu_win.addstr(1, column_widths['nombre'] + 2, "Continente")
    menu_win.addstr(
        1, column_widths['nombre'] + column_widths['continente'] + 2, "Población")
    menu_win.addstr(
        1, column_widths['nombre'] + column_widths['continente'] + column_widths['poblacion'] + 2, "Superficie [km²]")
    menu_win.hline(2, 1, curses.ACS_HLINE, menu_win.getmaxyx()[1] - 2)

    # Mostrar algunos países
    for i, pais in enumerate(paises[pag_num * lineas_disponibles:(pag_num + 1) * lineas_disponibles]):
        poblacion = f"{int(pais['poblacion']):,}".replace(',', '.')
        superficie = f"{int(pais['superficie']):,}".replace(',', '.')

        menu_win.addstr(i + 3, 2, pais['nombre'])
        menu_win.addstr(i + 3, column_widths['nombre'] + 2, pais['continente'])
        menu_win.addstr(
            i + 3, column_widths['nombre'] + column_widths['continente'] + 2, poblacion)
        menu_win.addstr(
            i + 3, column_widths['nombre'] + column_widths['continente'] + column_widths['poblacion'] + 2, superficie)

    return menu_win
