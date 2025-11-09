import curses
from curses.textpad import Textbox, rectangle
import time
from typing import Dict, List
from model import cargar_paises, cantidad_de_paises, buscar_pais_por_nombre, agregar_pais

HEADER_HEIGHT = 3
FOOTER_HEIGHT = 4
MAIN_MENU_HEIGHT_CORRECTION = 4
VALORES_ESQUEMA = ['nombre', 'poblacion', 'superficie', 'continente']

#############################################################
# Utilidades
#############################################################


def reset_esquema_and_values() -> tuple[Dict[str, str], str, str]:
    return {
        'nombre': '',
        'poblacion': '',
        'superficie': '',
        'continente': ''
    }, "", VALORES_ESQUEMA[0]


def nuevo_pais(
    screen: str,
    user_input: str,
    campo_actual: str,
    esquema: Dict[str, str]
) -> tuple[str, Dict[str, str], str, str]:
    status_msg = ""

    # --- CAMBIO 1: Lógica de entrada de datos por tipo de campo ---
    if len(user_input) == 1 and user_input.isprintable():
        if campo_actual in ['poblacion', 'superficie']:
            if user_input.isdigit():
                esquema[campo_actual] += user_input
            else:
                status_msg = "Error: Este campo solo acepta números."
        elif campo_actual in ['nombre', 'continente']:
            if user_input.isalpha() or user_input.isspace():
                esquema[campo_actual] += user_input
            else:
                status_msg = "Error: Este campo solo acepta letras y espacios."

    elif user_input == "KEY_BACKSPACE":
        if len(esquema[campo_actual]) == 0 and VALORES_ESQUEMA.index(campo_actual) > 0:
            # Si el campo está vacío, ir al campo anterior
            indice_campo = VALORES_ESQUEMA.index(campo_actual)
            campo_actual = VALORES_ESQUEMA[indice_campo - 1]
        else:
            # Borrar el último carácter del campo actual
            esquema[campo_actual] = esquema[campo_actual][:-1]

    # --- CAMBIO 2: Lógica de Navegación (Enter) ---
    # Se quitó 'and esquema[campo_actual]' para permitir navegar.
    elif user_input == '\n':
        indice_campo = VALORES_ESQUEMA.index(campo_actual)

        if indice_campo < len(VALORES_ESQUEMA) - 1:
            # Navegar al siguiente campo
            campo_actual = VALORES_ESQUEMA[indice_campo + 1]
        else:
            # Es el último campo, intentar SUBMIT (enviar)
            # --- VALIDACIÓN (como pide la consigna) ---
            if not all(esquema.values()):  # Revisa si algún valor es ""
                status_msg = "Error: No se permiten campos vacíos."
            else:
                res = agregar_pais(esquema)
                if res[0]:
                    # Éxito: limpiar formulario y volver al main
                    esquema = {key: '' for key in VALORES_ESQUEMA}
                    # Resetear al primer campo
                    campo_actual = VALORES_ESQUEMA[0]
                    screen = 'main'
                else:
                    status_msg = f"Error al agregar país: {res[1]}"

    return screen, esquema, status_msg, campo_actual


def proceso_carga_datos(
    nombre: str,
) -> List[Dict[str, str]] | tuple[bool, str]:
    paises = cargar_paises('paises.csv')

    if nombre:
        paises = buscar_pais_por_nombre(nombre, paises)
        if paises[0] is None:
            return False, str(paises[1])

    return paises


def buscar_pais(
    screen: str,
    search_query: str,
    user_input: str
) -> tuple[str, str]:

    if user_input.isalpha():
        search_query += user_input

    elif user_input == "KEY_BACKSPACE" and search_query:
        search_query = search_query[:-1]

    elif user_input == '\n' and search_query:
        # Aquí se procesaría la búsqueda
        screen = 'main'

    return screen, search_query


def lineas_disponibles(height: int) -> int:
    return height - (HEADER_HEIGHT + FOOTER_HEIGHT) - MAIN_MENU_HEIGHT_CORRECTION


def paginas(lineas_disponibles: int) -> int:
    total_paises = cantidad_de_paises('paises.csv')

    total_paginas = (total_paises // lineas_disponibles)

    if total_paises % lineas_disponibles != 0:
        total_paginas += 1

    return total_paginas

############################################################
# Componentes de la interfaz de usuario
############################################################


def main_header(width: int) -> curses.window:
    header_win = curses.newwin(HEADER_HEIGHT, width, 0, 0)
    header_win.bkgd(' ', curses.color_pair(1))  # Poner color de fondo
    header_win.addstr(1, 2, "TPI PROGRAMACIÓN 1 - GESTIÓN DE PAÍSES")
    header_win.addstr(1, width - 12, time.strftime("%d/%m/%Y"))
    header_win.border()  # Dibujar un borde
    return header_win


def main_footer(
    width: int,
    height: int,
    num_pag: int,
    action_active: bool = False
) -> curses.window:
    footer_win = curses.newwin(FOOTER_HEIGHT, width, height - FOOTER_HEIGHT, 0)
    footer_win.bkgd(' ', curses.color_pair(1))  # Poner otro color

    footer_win.addstr(1, 2, "F2 Buscar | ")
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


def main_menu(
    width: int,
    height: int,
    pag_num: int,
    lineas_disponibles: int,
    paises: List[Dict[str, str]] | tuple[bool, str]
) -> curses.window:
    # Altura disponible para el menú principal
    main_height = height - (
        HEADER_HEIGHT + FOOTER_HEIGHT)

    # Paginación
    total_paginas = paginas(lineas_disponibles)

    # Asegurar que pag_num esté dentro de los límites
    pag_num = max(0, min(pag_num, total_paginas - 1))

    menu_win = curses.newwin(main_height, width, HEADER_HEIGHT, 0)
    menu_win.bkgd(' ', curses.color_pair(2))  # Poner color de fondo
    menu_win.border()

    # Tmaño columnas proporcionado a width
    column_widths = {
        'nombre': int(width * 0.28),
        'continente': int(width * 0.28),
        'poblacion': int(width * 0.28),
        'superficie': int(width * 0.16)
    }

    # si paises es un error, mostrar mensaje
    if isinstance(paises, tuple) and not paises[0]:
        menu_win.addstr(
            main_height // 2,
            (width // 2) - len(paises[1]) // 2,
            str(paises[1])
        )
        return menu_win

    # si no es una lista, retornar el menú vacío
    if not isinstance(paises, list):
        return menu_win

    menu_win.addstr(1, 2, "Pais")
    menu_win.addstr(1, column_widths['nombre'] + 2, "Continente")
    menu_win.addstr(
        1, column_widths['nombre'] + column_widths['continente'] + 2, "Población")
    menu_win.addstr(
        1, column_widths['nombre'] + column_widths['continente'] + column_widths['poblacion'] + 2, "Superficie [km²]")
    menu_win.hline(2, 1, curses.ACS_HLINE, menu_win.getmaxyx()[1] - 2)

    # Mostrar algunos países
    for i, pais in enumerate(paises[pag_num * lineas_disponibles:(pag_num + 1) * lineas_disponibles]):
        poblacion = f"{int(pais['poblacion']):,}".replace(',', '.')
        superficie = f"{int(pais['superficie']):,}".replace(',', '.')

        menu_win.addstr(i + 3, 2, pais['nombre'])
        menu_win.addstr(i + 3, column_widths['nombre'] + 2, pais['continente'])
        menu_win.addstr(
            i + 3, column_widths['nombre'] + column_widths['continente'] + 2, poblacion)
        menu_win.addstr(
            i + 3, column_widths['nombre'] + column_widths['continente'] + column_widths['poblacion'] + 2, superficie)

    return menu_win


def search_menu(
    width: int,
    height: int,
    query: str = ""
) -> curses.window:
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


def add_menu(
    width: int,
    height: int,
    nuevo_pais: Dict[str, str],
    status_msg: str,
    campo_actual: str
) -> curses.window:
    add_height = height - (HEADER_HEIGHT + FOOTER_HEIGHT)

    add_win = curses.newwin(add_height, width, HEADER_HEIGHT, 0)
    add_win.bkgd(' ', curses.color_pair(2))  # Poner color de fondo
    add_win.border()

    add_win.addstr(1, 2, "Agregar un nuevo país: ")
    add_win.addstr(
        3, 2, "Nombre:",
        curses.A_UNDERLINE if campo_actual == 'nombre' else 0
    )
    add_win.addstr(
        4, 2, "Población:",
        curses.A_UNDERLINE if campo_actual == 'poblacion' else 0
    )
    add_win.addstr(
        5, 2, "Superficie [km²]:",
        curses.A_UNDERLINE if campo_actual == 'superficie' else 0
    )
    add_win.addstr(
        6, 2, "Continente:",
        curses.A_UNDERLINE if campo_actual == 'continente' else 0
    )

    if nuevo_pais.get('nombre') is not None:
        add_win.addstr(3, 20, str(nuevo_pais.get('nombre', '')),)
    if nuevo_pais.get('poblacion') is not None:
        add_win.addstr(4, 20, str(nuevo_pais.get('poblacion', '')),)
    if nuevo_pais.get('superficie') is not None:
        add_win.addstr(5, 20, str(nuevo_pais.get('superficie', '')),)
    if nuevo_pais.get('continente') is not None:
        add_win.addstr(6, 20, str(nuevo_pais.get('continente', '')),)

    rectangle(add_win, 2, 1, 7, width - 2)

    add_win.addstr(
        8, 2, "Presione Enter para avanzar entre campos y enviar el formulario.")

    if status_msg:
        add_win.addstr(10, 2, status_msg, curses.color_pair(3))

    return add_win

############################################################
# Layout de la aplicación
############################################################


def main_layout(
    height: int, width: int, pag_num: int, paises: List[Dict[str, str]] | tuple[bool, str]
) -> tuple[curses.window, curses.window, curses.window]:
    header_layout = main_header(width)
    footer_layout = main_footer(width, height, pag_num)

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


def search_layout(
    height: int, width: int, query: str = ""
) -> tuple[curses.window, curses.window, curses.window]:
    header_layout = main_header(width)
    footer_layout = main_footer(width, height, 0, action_active=True)
    search_layout = search_menu(width, height, query)

    header_layout.refresh()
    search_layout.refresh()
    footer_layout.refresh()

    return header_layout, search_layout, footer_layout


def add_layout(
    height: int,
    width: int,
    nuevo_pais: Dict[str, str],
    status_msg: str,
    campo_actual: str
) -> tuple[curses.window, curses.window, curses.window]:
    header_layout = main_header(width)
    footer_layout = main_footer(width, height, 0, action_active=True)
    add_layout = add_menu(width, height, nuevo_pais, status_msg, campo_actual)
    header_layout.refresh()
    add_layout.refresh()
    footer_layout.refresh()

    return header_layout, add_layout, footer_layout


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

    while True:
        paises = proceso_carga_datos(
            nombre=search_query
        )

        height, width = main_window.getmaxyx()

        total_paginas = paginas(lineas_disponibles(height))

        match screen:
            case 'main':
                main_layout(height, width, pag_num, paises)
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
                pass

        user_input = main_window.getkey()

        match user_input:
            case 'KEY_F(2)':
                search_query = ""
                screen = 'buscar_pais'
            case 'KEY_F(4)':
                screen = 'agregar_pais'
            case 'KEY_F(7)':
                screen = 'actualizar_pais'
            case 'KEY_LEFT':
                pag_num = max(0, pag_num - 1)
            case 'KEY_RIGHT':
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
            screen, esquema_de_nuevo_pais, status_msg, campo_actual = nuevo_pais(
                screen, user_input, campo_actual, esquema_de_nuevo_pais
            )

        if screen == 'actualizar_pais':
            # Aquí se manejaría la lógica para actualizar un país
            pass

        main_window.clear()
        main_window.refresh()


############################################################
# Funciones de prueba
#############################################################

def start_app():
    # Wrapper para inicializar y restaurar la terminal de forma segura
    curses.wrapper(main)


def test_key_input():
    def key_test(stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Presiona cualquier tecla (Ctrl+Q para salir):")
        stdscr.refresh()
        while True:
            key = stdscr.getkey()
            stdscr.clear()
            stdscr.addstr(0, 0, f"Tecla presionada: {key} (Ctrl+Q para salir)")
            stdscr.refresh()
            if key == 17:  # Ctrl+Q
                break

    curses.wrapper(key_test)


# --- Ejecutar la aplicación ---
if __name__ == "__main__":
    start_app()
    # test_key_input()
