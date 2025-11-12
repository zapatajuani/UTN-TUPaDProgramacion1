import curses

FOOTER_HEIGHT = 4


def main_footer(
    width: int,
    height: int,
    num_pag: int,
    search_query: str = "",
    action_active: bool = False
) -> curses.window:
    """
    Crea y configura la ventana de pie de página principal.
    
    Args:
        width: Ancho de la ventana
        height: Alto de la ventana
        num_pag: Número de página actual
        search_query: Query de búsqueda activa
        action_active: Si hay una acción activa en curso
        
    Returns:
        Ventana de curses configurada para el pie de página
    """
    footer_win = curses.newwin(FOOTER_HEIGHT, width, height - FOOTER_HEIGHT, 0)
    footer_win.bkgd(' ', curses.color_pair(1))  # Poner otro color

    footer_win.addstr(
        1, 2, f"{'F2 Reset  | ' if search_query else 'F2 Buscar | '}")
    footer_win.addstr(1, 14, "F4 Agregar | ")
    footer_win.addstr(1, 27, "F7 Actualizar | ")
    footer_win.addstr(1, 43, "F8 Filtrar | ")
    footer_win.addstr(1, 56, "F9 Reportes | ")
    footer_win.addstr(
        1, 70, f"{'F10 Volver' if action_active else 'F10 Salir'} ")
    footer_win.addstr(2, width - 45, "← Pág anterior | ")
    footer_win.addstr(2, width - 28, "→ Pág siguiente | ")
    footer_win.addstr(2, width - 10, f"Página {num_pag + 1} ")
    footer_win.border()
    return footer_win
