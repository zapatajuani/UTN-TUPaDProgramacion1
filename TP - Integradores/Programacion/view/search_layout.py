import curses
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from .main_header import main_header
from .main_footer import main_footer
from .search_menu import search_menu


def search_layout(
    height: int, width: int, query: str = ""
) -> tuple[curses.window, curses.window, curses.window]:
    """
    Crea el layout completo de la pantalla de búsqueda.
    
    Args:
        height: Alto de la ventana
        width: Ancho de la ventana
        query: Query de búsqueda actual
        
    Returns:
        Tupla con las ventanas de encabezado, menú de búsqueda y pie de página
    """
    header_layout = main_header(width)
    footer_layout = main_footer(width, height, 0, action_active=True)
    search_layout = search_menu(width, height, query)

    header_layout.refresh()
    search_layout.refresh()
    footer_layout.refresh()

    return header_layout, search_layout, footer_layout
