import curses
from typing import Dict
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from .main_header import main_header
from .main_footer import main_footer
from .update_menu import update_menu


def update_layout(
    height: int,
    width: int,
    nuevo_pais: Dict[str, str],
    status_msg: str,
    campo_actual: str
) -> tuple[curses.window, curses.window, curses.window]:
    """
    Crea el layout completo de la pantalla para actualizar países.
    
    Args:
        height: Alto de la ventana
        width: Ancho de la ventana
        nuevo_pais: Diccionario con datos del país a actualizar
        status_msg: Mensaje de estado a mostrar
        campo_actual: Campo actualmente seleccionado
        
    Returns:
        Tupla con las ventanas de encabezado, menú de actualizar y pie de página
    """
    header_layout = main_header(width)
    footer_layout = main_footer(width, height, 0, action_active=True)
    update_layout = update_menu(
        width, height, nuevo_pais, status_msg, campo_actual)

    header_layout.refresh()
    update_layout.refresh()
    footer_layout.refresh()

    return header_layout, update_layout, footer_layout
