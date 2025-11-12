import curses
from typing import Any, Dict, List
from model.model import check_file
from view import (
    main_layout,
    search_layout,
    add_layout,
    update_layout,
    filters_menu,
    menu_estadisticas
)
from utilities import (
    proceso_carga_datos,
    lineas_disponibles,
    paginas,
    calcular_estadisticas,
    reset_esquema_and_values,
    editar_registrar_pais,
    filtrar_paises,
    buscar_pais
)


HEADER_HEIGHT = 3
FOOTER_HEIGHT = 4
MAIN_MENU_HEIGHT_CORRECTION = 4
VALORES_ESQUEMA = ['nombre', 'poblacion', 'superficie', 'continente']
FILTRO_CONTINENTE = ['Todos', 'America del Sur', 'America del Norte',
                     'Europa', 'Asia', 'Africa', 'Oceania']


def main(main_window: curses.window) -> None:
    # --- Configuración inicial de curses ---
    curses.curs_set(0)       # Ocultar el cursor
    main_window.clear()      # Limpiar la pantalla
    main_window.refresh()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE)  # ID 1
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_CYAN)  # ID 2
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)   # ID 3

    # Inicializar historial de pantalla (si es necesario)
    screen = 'main'

    # Número de página actual
    pag_num = 0

    # Pais a buscar
    search_query = ""

    # esquema pais nuevo
    esquema_de_nuevo_pais: Dict[str, str] = {
        'nombre': '',
        'poblacion': '',
        'superficie': '',
        'continente': ''
    }

    # campo actual para agregar pais
    campo_actual = 'nombre'

    # estado de mensajes
    status_msg = ""

    # filters
    mostrar_filtros = False
    filters_obj = {
        'continente': None,
        'rango_poblacion': ('', ''),
        'poblacion_orden': None,
        'rango_superficie': ('', ''),
        'superficie_orden': None
    }
    filter_selector = (0, 0)

    # estadisticas
    mostrar_estadisticas = False

    while True:
        paises = proceso_carga_datos(
            nombre=search_query,
            filters_obj=filters_obj,
        )

        height, width = main_window.getmaxyx()

        total_paginas = paginas(lineas_disponibles(height))

        match screen:
            case 'main':
                main_layout(height, width, pag_num, paises, search_query)
            case 'agregar_pais':
                add_layout(
                    height,
                    width,
                    esquema_de_nuevo_pais,
                    status_msg,
                    campo_actual
                )
            case 'buscar_pais':
                search_layout(height, width, search_query)
            case 'actualizar_pais':
                update_layout(
                    height,
                    width,
                    esquema_de_nuevo_pais,
                    status_msg,
                    campo_actual
                )

        if mostrar_filtros:
            filters_menu(width, height, filters_obj, filter_selector)

        if mostrar_estadisticas:
            estadisticas = calcular_estadisticas(paises)
            menu_estadisticas(width, estadisticas)

        user_input = main_window.getkey()

        match user_input:
            case 'KEY_F(2)':
                if not search_query:
                    screen = 'buscar_pais'
                search_query = ""
            case 'KEY_F(4)':
                screen = 'agregar_pais'
            case 'KEY_F(7)':
                screen = 'actualizar_pais'
            case 'KEY_F(8)':
                mostrar_filtros = not mostrar_filtros
                filter_selector = (0, 0)
            case 'KEY_F(9)':
                mostrar_estadisticas = not mostrar_estadisticas
            case 'KEY_LEFT':
                if not mostrar_filtros and not mostrar_estadisticas:
                    pag_num = max(0, pag_num - 1)
            case 'KEY_RIGHT':
                if not mostrar_filtros and not mostrar_estadisticas:
                    pag_num = min(total_paginas - 1, pag_num + 1)
            case 'KEY_F(10)':
                if screen == 'main':
                    break
                esquema_de_nuevo_pais, status_msg, campo_actual = reset_esquema_and_values()
                screen = 'main'
            case _:
                pass

        if screen == 'buscar_pais':
            screen, search_query = buscar_pais(
                screen, search_query, user_input)

        if screen == 'agregar_pais':
            screen, esquema_de_nuevo_pais, status_msg, campo_actual = editar_registrar_pais(
                screen, user_input, campo_actual, esquema_de_nuevo_pais
            )

        if screen == 'actualizar_pais':
            screen, esquema_de_nuevo_pais, status_msg, campo_actual = editar_registrar_pais(
                screen, user_input, campo_actual, esquema_de_nuevo_pais, edicion=True
            )

        if mostrar_filtros:
            filters_obj, filter_selector = filtrar_paises(
                user_input, filters_obj, filter_selector)

        main_window.clear()
        main_window.refresh()


def start_app():
    # Chequear estadaod de archivo
    check_file('paises.csv')

    # Wrapper para inicializar y restaurar la terminal de forma segura
    curses.wrapper(main)


# --- Ejecutar la aplicación ---
if __name__ == "__main__":
    start_app()
