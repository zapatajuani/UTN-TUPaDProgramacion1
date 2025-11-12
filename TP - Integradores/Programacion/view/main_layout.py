import curses
from typing import List, Dict
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from .main_header import main_header
from .main_footer import main_footer
from .main_menu import main_menu
from utilities.lineas_disponibles import lineas_disponibles


def main_layout(
    height: int,
    width: int,
    pag_num: int,
    paises: List[Dict[str, str]] | tuple[bool, str],
    search_query: str
) -> tuple[curses.window, curses.window, curses.window]:
    """
    Crea el layout completo de la pantalla principal.
    
    Args:
        height: Alto de la ventana
        width: Ancho de la ventana
        pag_num: Número de página actual
        paises: Lista de países o tupla de error
        search_query: Query de búsqueda actual
        
    Returns:
        Tupla con las ventanas de encabezado, menú principal y pie de página
    """
    header_layout = main_header(width)
    footer_layout = main_footer(width, height, pag_num, search_query)

    main_layout = main_menu(
        width,
        height,
        pag_num,
        lineas_disponibles(height),
        paises
    )

    header_layout.refresh()
    main_layout.refresh()
    footer_layout.refresh()

    return header_layout, main_layout, footer_layout
