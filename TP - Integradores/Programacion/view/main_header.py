import curses
import time

HEADER_HEIGHT = 3


def main_header(width: int) -> curses.window:
    """
    Crea y configura la ventana de encabezado principal.
    
    Args:
        width: Ancho de la ventana
        
    Returns:
        Ventana de curses configurada para el encabezado
    """
    header_win = curses.newwin(HEADER_HEIGHT, width, 0, 0)
    header_win.bkgd(' ', curses.color_pair(1))  # Poner color de fondo
    header_win.addstr(1, 2, "TPI PROGRAMACIÓN 1 - GESTIÓN DE PAÍSES")
    header_win.addstr(1, width - 12, time.strftime("%d/%m/%Y"))
    header_win.border()  # Dibujar un borde
    return header_win
