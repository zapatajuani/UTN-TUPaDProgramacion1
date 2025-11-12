import curses
from typing import Dict
from curses.textpad import rectangle

HEADER_HEIGHT = 3
FOOTER_HEIGHT = 4


def update_menu(
    width: int,
    height: int,
    nuevo_pais: Dict[str, str],
    status_msg: str,
    campo_actual: str
) -> curses.window:
    """
    Crea y configura el menú para actualizar un país existente.
    
    Args:
        width: Ancho de la ventana
        height: Alto de la ventana
        nuevo_pais: Diccionario con datos del país a actualizar
        status_msg: Mensaje de estado a mostrar
        campo_actual: Campo actualmente seleccionado
        
    Returns:
        Ventana de curses configurada para actualizar país
    """
    update_height = height - (HEADER_HEIGHT + FOOTER_HEIGHT)

    update_win = curses.newwin(update_height, width, HEADER_HEIGHT, 0)
    update_win.bkgd(' ', curses.color_pair(2))  # Poner color de fondo
    update_win.border()

    update_win.addstr(1, 2, "Actualizar un país existente: ")
    update_win.addstr(
        3, 2, "Nombre:",
        curses.A_UNDERLINE if campo_actual == 'nombre' else 0
    )
    update_win.addstr(
        4, 2, "Población:",
        curses.A_UNDERLINE if campo_actual == 'poblacion' else 0
    )
    update_win.addstr(
        5, 2, "Superficie [km²]:",
        curses.A_UNDERLINE if campo_actual == 'superficie' else 0
    )
    update_win.addstr(
        6, 2, "Continente:",
        curses.A_UNDERLINE if campo_actual == 'continente' else 0
    )

    if nuevo_pais.get('nombre') is not None:
        update_win.addstr(3, 20, str(nuevo_pais.get('nombre', '')),)
    if nuevo_pais.get('poblacion') is not None:
        update_win.addstr(4, 20, str(nuevo_pais.get('poblacion', '')),)
    if nuevo_pais.get('superficie') is not None:
        update_win.addstr(5, 20, str(nuevo_pais.get('superficie', '')),)
    if nuevo_pais.get('continente') is not None:
        update_win.addstr(6, 20, str(nuevo_pais.get('continente', '')),)

    rectangle(update_win, 2, 1, 7, width - 2)

    update_win.addstr(
        8, 2, "Presione Enter para avanzar entre campos y enviar el formulario.")

    if status_msg:
        update_win.addstr(10, 2, status_msg, curses.color_pair(3))

    return update_win
