import curses
from typing import Any, Dict

HEADER_HEIGHT = 3


def menu_estadisticas(
    width: int,
    estadisticas: Dict[str, Any] | bool,
) -> None:
    """
    Crea y muestra el menú de estadísticas.
    
    Args:
        width: Ancho de la ventana
        estadisticas: Diccionario con estadísticas calculadas o False si hay error
    """
    info = curses.newwin(
        23,
        int(width * 0.9),
        HEADER_HEIGHT + 3,
        int(width * 0.05)
    )
    info.bkgd(' ', curses.color_pair(1))
    info.border()

    if not estadisticas:
        info.addstr(
            1,
            2,
            "No se pudieron calcular las estadísticas debido a un error o falta de datos.",
            curses.color_pair(3)
        )
        info.refresh()
        return

    if isinstance(estadisticas, dict):
        info.addstr(1, 2, "Estadísticas", curses.A_BOLD | curses.A_UNDERLINE)

        info.addstr(3, 2, "Continente")
        info.addstr(3, 22, "Cantidad de Países")
        info.addstr(3, 50, "Promedio Población")
        info.addstr(3, 75, "Promedio Superficie [km²]")
        info.hline(4, 1, curses.ACS_HLINE, info.getmaxyx()[1] - 2)

        fila = 5
        for key, stats in estadisticas.items():
            if key in [
                'pais_mayor_poblacion',
                'pais_menor_poblacion',
                'pais_mayor_superficie',
                'pais_menor_superficie'
            ]:
                continue

            continente_display = key.replace(
                '_', ' ').title() if key != 'total' else 'Total'
            info.addstr(fila, 2, continente_display)
            info.addstr(fila, 22, str(stats['cant_paises']))
            info.addstr(fila, 50, f"{stats['prom_poblacion']:.2f}")
            info.addstr(fila, 75, f"{stats['prom_superficie']:.2f}")
            fila += 1
        info.hline(fila, 1, curses.ACS_HLINE, info.getmaxyx()[1] - 2)

        info.addstr(
            fila + 2, 2,
            f"Pais con mayor población: {estadisticas['pais_mayor_poblacion']['nombre']}"
        )

        info.addstr(
            fila + 3, 2,
            f"Pais con menor población: {estadisticas['pais_menor_poblacion']['nombre']}"
        )

        info.addstr(
            fila + 5, 2,
            f"Pais con mayor superficie: {estadisticas['pais_mayor_superficie']['nombre']}"
        )

        info.addstr(
            fila + 6, 2,
            f"Pais con menor superficie: {estadisticas['pais_menor_superficie']['nombre']}"
        )

        info.addstr(
            21, 2,
            "Presione F9 para cerrar el reporte de estadísticas."
        )

    info.refresh()
