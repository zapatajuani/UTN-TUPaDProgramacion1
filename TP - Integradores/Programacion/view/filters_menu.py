import curses
from typing import Any, Dict

HEADER_HEIGHT = 3
FILTRO_CONTINENTE = ['Todos', 'America del Sur', 'America del Norte',
                     'Europa', 'Asia', 'Africa', 'Oceania']


def filters_menu(
    width: int,
    height: int,
    filters_obj: Dict[str, Any],
    filter_selector: tuple[int, int]
) -> None:
    """
    Crea y muestra el menú de filtros interactivo.
    
    Args:
        width: Ancho de la ventana
        height: Alto de la ventana
        filters_obj: Objeto con filtros actuales
        filter_selector: Posición actual del selector
    """
    filters = curses.newwin(
        30,
        int(width * 0.8),
        HEADER_HEIGHT + 3,
        int(width * 0.1)
    )
    filters.bkgd(' ', curses.color_pair(1))
    filters.border()

    filters.addstr(1, 2, "Filtros", curses.A_BOLD | curses.A_UNDERLINE)
    # Filtro Continente
    filters.addstr(3, 2, "Continente",
                   curses.A_UNDERLINE if filter_selector[0] == 0 else 0)

    filters.addstr(3, 13, f"{(int(width * 0.8)-15) * '-'}")

    for idx, continente in enumerate(FILTRO_CONTINENTE):
        estilo = curses.A_REVERSE if filter_selector[1] == idx else 0
        filtros_seleccionados = filters_obj['continente']
        if filtros_seleccionados == continente or (filtros_seleccionados is None and continente == 'Todos'):
            estilo |= curses.A_BOLD

        row = 5 + (idx // 4)
        col = 4 + (20 * (idx % 4))

        filters.addstr(row, col, continente, estilo)

    # Filtro Rango Población
    filters.addstr(8, 2, "Filtro Población")
    filters.addstr(8, 19, f"{(int(width * 0.8)-21) * '-'}")

    filters.addstr(10, 4, f"Min: {filters_obj['rango_poblacion'][0] or 'N/A'}",
                   curses.A_UNDERLINE if filter_selector[0] == 1 else 0)
    filters.addstr(11, 4, f"Max: {filters_obj['rango_poblacion'][1] or 'N/A'}",
                   curses.A_UNDERLINE if filter_selector[0] == 2 else 0)

    filters.addstr(13, 4, "Ordenar Mayor a menor",
                   curses.A_UNDERLINE if filter_selector[0] == 3 else 0)
    filters.addstr(
        13, 26, f"{'[X]' if filters_obj['poblacion_orden'] == 'desc' else '[ ]'}")

    filters.addstr(15, 4, "Ordenar Menor a mayor",
                   curses.A_UNDERLINE if filter_selector[0] == 4 else 0)
    filters.addstr(
        15, 26, f"{'[X]' if filters_obj['poblacion_orden'] == 'asc' else '[ ]'}")

    # Filtro Rango Superficie
    filters.addstr(17, 2, "Rango Superficie")
    filters.addstr(17, 19, f"{(int(width * 0.8)-21) * '-'}")

    filters.addstr(19, 4, f"Min: {filters_obj['rango_superficie'][0] or 'N/A'}",
                   curses.A_UNDERLINE if filter_selector[0] == 5 else 0)
    filters.addstr(20, 4, f"Max: {filters_obj['rango_superficie'][1] or 'N/A'}",
                   curses.A_UNDERLINE if filter_selector[0] == 6 else 0)

    filters.addstr(22, 4, "Ordenar Mayor a menor",
                   curses.A_UNDERLINE if filter_selector[0] == 7 else 0)
    filters.addstr(
        22, 26, f"{'[X]' if filters_obj['superficie_orden'] == 'desc' else '[ ]'}")

    filters.addstr(24, 4, "Ordenar Menor a mayor",
                   curses.A_UNDERLINE if filter_selector[0] == 8 else 0)
    filters.addstr(
        24, 26, f"{'[X]' if filters_obj['superficie_orden'] == 'asc' else '[ ]'}")

    filters.addstr(
        27, 2, "Presione F8 para cerrar los filtros. Enter para aplicar o intercalar.")

    filters.refresh()
