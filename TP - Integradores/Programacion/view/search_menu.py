import curses
from curses.textpad import rectangle

HEADER_HEIGHT = 3
FOOTER_HEIGHT = 4


def search_menu(
    width: int,
    height: int,
    query: str = ""
) -> curses.window:
    """
    Crea y configura el menú de búsqueda de países.
    
    Args:
        width: Ancho de la ventana
        height: Alto de la ventana
        query: Query de búsqueda actual
        
    Returns:
        Ventana de curses configurada para búsqueda
    """
    # Aquí se implementaría el menú de búsqueda
    search_height = height - (HEADER_HEIGHT + FOOTER_HEIGHT)

    search_win = curses.newwin(search_height, width, HEADER_HEIGHT, 0)
    search_win.bkgd(' ', curses.color_pair(2))  # Poner color de fondo
    search_win.border()

    search_win.addstr(1, 2, "Ingrese el nombre del país a buscar: ")
    search_win.addstr(3, 2, "Nombre del país: ")
    search_win.addstr(3, 20, query)
    rectangle(search_win, 2, 1, 4, width - 2)

    return search_win
